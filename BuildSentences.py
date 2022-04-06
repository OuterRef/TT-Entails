import re
from typing import List

PRIORITY_DICT = {
    "#"  : 0,
    "("  : 1,
    "if" : 2,
    "iff": 2,
    "or" : 3,
    "and": 4,
    "not": 5,
    ")"  : 6
}

class LogicalExpression(object):
    def __init__(self, content: str) -> None:
        super(LogicalExpression, self).__init__()
        if content in PRIORITY_DICT:
            self.connective = content
            self.symbol = None
        else:
            self.symbol = content
            self.connective = None
        self.children: List[LogicalExpression] = []
        self.parent: LogicalExpression = None

    def appendChild(self, child) -> None:
        child: LogicalExpression = child
        self.children.append(child)
        child.parent = self

def readLinesFromTxt(file: str) -> list:
    in_file = open(file)
    lines = in_file.readlines()
    new_lines = []
    for line in lines:
        if line != "\n":
            if line[-1] == '\n':
                line = line[:-1]
            new_lines.append(line)
    in_file.close()
    return new_lines

def line2Tokens(line: str) -> list:
    # "(" and ")" are independent tokens
    tokens = re.split('([ ()])', line)
    tokens = [token for token in tokens if token != '' and token != ' ']
    return tokens

def toRPN(tokens: list) -> list:
    op = ["#"]  # S1
    var = []    # S2
    for token in tokens:
        if token in PRIORITY_DICT:  # it is an operand
            if token == "(":
                # push 
                op.append(token)
            elif token == ")":
                # pop till (
                while op[-1] != "(":
                    var.append(op.pop(-1))
                op.pop(-1)  # pop "("
            elif PRIORITY_DICT[token] > PRIORITY_DICT[op[-1]]:
                # push
                op.append(token)
            else:
                # pop till smaller than token
                while PRIORITY_DICT[op[-1]] >= PRIORITY_DICT[token]:
                    var.append(op.pop(-1))
                op.append(token)
        else:
            var.append(token)
    while len(op) > 1:
        var.append(op.pop(-1))
    assert op == ["#"]
    return var

def RPN2Tree(var: list) -> LogicalExpression:
    def theOperation(op_node: LogicalExpression, children: List[LogicalExpression]) -> LogicalExpression:
        assert op_node.symbol is None
        assert op_node.connective is not None
        for child in children:
            op_node.appendChild(child)
        return op_node
    var = [LogicalExpression(node) for node in var]
    result: list[LogicalExpression] = []
    for node in var:
        if node.symbol is not None:  # a leaf node
            # push
            result.append(node)
        else:                        # an operand
            # do "the operation"
            if node.connective == "not":
                result.append(theOperation(node, [result.pop(-1)]))
            else:
                result.append(theOperation(node, [result.pop(-1), result.pop(-1)]))
    return result[0]

def buildSentences(file: str) -> LogicalExpression:
    h_node = LogicalExpression("and")
    lines = readLinesFromTxt(file)
    for line in lines:
        tokens = line2Tokens(line)
        var = toRPN(tokens)
        result = RPN2Tree(var)
        h_node.appendChild(result)
    return h_node

