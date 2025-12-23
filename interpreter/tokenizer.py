# Akuma Tokenizer

import re
from re import Pattern
from collections import namedtuple

Token = namedtuple("Token", ["type", "value"])

TOKEN_SPEC = [
    ("NUMBER",   r"\d+"),
    ("STRING",   r'"[^"]*"'),
    ("BOOLEAN",  r"\b(true|false)\b"),
    ("KEYWORD",  r"\b(import|from|var|fc|return|value)\b"),
    ("PROPERTY", r"\b(Type|Constant|InChange)\b"),
    ("TYPE",     r"\b(Integer|String|Boolean)\b"),
    ("SKIP",     r"[ \t\n]+"),
    ("COMMENT",  r"//.*|/\*[\s\S]*?\*/"),
    ("LPAREN",   r"\("),
    ("RPAREN",   r"\)"),
    ("LBRACE",   r"\{"),
    ("RBRACE",   r"\}"),
    ("EQUAL",    r"="),
    ("PLUS",     r"\+"),
    ("MINUS",    r"-"),
    ("EXP",      r"\*\*"),
    ("MUL",      r"\*"),
    ("DIV",      r"/"),
    ("MOD",      r"%"),
    ("DOT",      r"\."),
    ("COMMA",    r","),
    ("SEMICOLON",r";"),
    ("COLON",    r":"),
    ("IDENT",    r"[A-Za-z_][A-Za-z0-9_]*"),
]

def tokenizer(code) -> list[Token]:
    tokens: list[Token] = []
    idx = 0
    line = 1
    
    compiled_tokens = [re.compile(token_regex) for _, token_regex in TOKEN_SPEC]
    
    while idx < len(code):
        if code[idx] == "\n":
            line += 1
        
        match = None
        for i, token_regex in enumerate(compiled_tokens):
            match = token_regex.match(code, idx)
            
            if match:
                text = match.group()
                if TOKEN_SPEC[i][0] not in ("SKIP", "COMMENT"):
                    tokens.append(Token(TOKEN_SPEC[i][0], text))
                idx = match.end()
                break
        if not match:
            raise Exception("Unexpected character on line " + str(line) + " : " + code[idx])
    return tokens

if __name__ == "__main__":
    code = """var a { Type: Integer, InChange: { value * 5 } } = 10;
    @
    """
    tokens = tokenizer(code)
    for token in tokens:
        print(token)
