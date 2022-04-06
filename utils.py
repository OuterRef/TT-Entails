from typing import List
from BuildSentences import LogicalExpression, buildSentences

def extractSymbols(sentence: LogicalExpression) -> List[str]:
    result = []
    if sentence.symbol is not None:
        if sentence.symbol not in result:
            result.append(sentence.symbol)
    else:
        for child in sentence.children:
            result.extend(extractSymbols(child))
    return result

def PL_True(sentence: LogicalExpression, model: dict) -> bool:
    if sentence.symbol is not None:
        return model[sentence.symbol]
    elif sentence.connective == "and":
        for child in sentence.children:
            if not PL_True(child, model):
                return False
        return True
    elif sentence.connective == "or":
        for child in sentence.children:
            if PL_True(child, model):
                return True
        return False
    elif sentence.connective == "not":
        return not PL_True(sentence.children[0], model)
    elif sentence.connective == "if":
        left = sentence.children[0]
        right = sentence.children[1]
        if PL_True(left, model) and not PL_True(right, model):
            return False
        else:
            return True
    elif sentence.connective == "iff":
        left = sentence.children[0]
        right = sentence.children[1]
        if PL_True(left, model) == PL_True(right, model):
            return True
        else:
            return False
    else:
        raise NameError ("Invalid connective!")

def extendModel(symbol: str, boolean: bool, model: dict) -> dict:
    model[symbol] = boolean
    return model

def TT_Entails(KB: LogicalExpression, alpha: LogicalExpression) -> bool:
    symbol1 = extractSymbols(KB)
    symbol2 = extractSymbols(alpha)
    for item in symbol2:
        if item not in symbol1:
            symbol1.append(item)
    return TT_CheckAll(KB, alpha, symbol1, {})

def TT_CheckAll(KB: LogicalExpression, alpha: LogicalExpression, symbols: List[str], model: dict) -> bool:
    if symbols == []:
        if PL_True(KB, model):
            return PL_True(alpha, model)
        else:
            return True
    else:
        p = symbols.pop()
        return (TT_CheckAll(KB, alpha, symbols, extendModel(p, True, model)) 
                and 
                TT_CheckAll(KB, alpha, symbols, extendModel(p, False, model))
        )




