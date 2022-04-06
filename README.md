# TT Entails

## Brief

- See if KB (knowledge base) entails $\alpha$, i.e. can $\alpha$ be deduced from known evidence (observation and rules)

## Syntax

- One BNF sentence in one line, end with "\n".

- Use blank(s) to seperate different tokens.

## Variables

- Big letter + numbers recommended.

- Reserved variables: 'True', 'False' as well as all the operands.

## Usage

- Input KB in KB.txt, and $\alpha$ in alpha.txt in accordance with required syntax

- run `python ./main.py` (Python version: 3.10.0)

- The result is a bool, telling you whether KB entails $\alpha$ or not

## Operands

| Operand | priority |
| :-----: | :------: |
|   ()    |    0     |
|   not   |    1     |
|   and   |    2     |
|   or    |    3     |
|   iff   |    4     |
|   if    |    4     |

## Example

KB.txt

```
B11 iff (P12 or P21)
B21 iff (P11 or P22 or P31)
not B11
B21
```

alpha.txt

```
P31 or P22
```

Result: True

## Features

- Multiple blanks (tabs) and empty lines allowed.

## Credits

- [TT-ENTAILS: Inference by Enumeration in Propositional Logic](http://vlm1.uta.edu/~athitsos/courses/cse4308_fall2016/lectures/03a_tt_entails.pdf)

