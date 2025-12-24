# Grammar Of Akuma

## Akuma Grammar v0.1

### Lexical

---

```EBNF
letter = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

integer = digit { digit } ;

symbol = "[" | "]" | "{" | "}" | "(" | ")" | "<" | ">"
| "'" | '"' | "=" | "|" | "." | "," | ";" | "-"
| "+" | "*" | "?" | "_" ;

arithmetic_operator = "+" | "-" | "*" | "/" | "%" | "**" ;

string = '"' { string_char } '"' ;
string_char = letter | digit | symbol | " " ;

boolean = "true" | "false" ;

type = "Integer" | "String" | "Boolean" ;

keyword = "import" | "from" | "var" | "fc" | "return" ;

line_comment = "//" { any_char_except_newline } ;

block_comment = "/*" { string_char } "*/" ;

identifier = letter { letter | digit | "_" } ;
```

### Variable Declaration

```EBNF
var_decl =
    "var"
    identifier
    var_property_block
    "="
    expression
    ";" ;

var_property_block =
    "{"
        [ var_property { "," var_property } ]
    "}" ;

var_property =
    "Type" ":" type
    | "Constant"
    | inchange_property
    | import_property ;

inchange_property =
    "InChange"
    ":"
    "{"
        expression
        [ "AffectsInitValue" ":" boolean ]
    "}" ;
```

### Variable Change

```EBNF
var_change =
    identifier
    "="
    expression
    ";" ;
```

### Expression

```EBNF
expression =
    additive_expression ;

additive_expression =
    multiplicative_expression
    { ("+" | "-") multiplicative_expression } ;

multiplicative_expression =
    primary_expression
    { ("*" | "/" | "%" | "**") primary_expression } ;

primary_expression =
    integer
    | string
    | boolean
    | identifier
    | function_call
    | "(" expression ")" ;

function_call =
    identifier
    "."
    "call"
    property_block ;
```

TODO: Add unary operatör.

### Importing

```EBNF
import_decl =
    ("import" | "from")
    string
    import_property_block
    ";" ;

import_property_block =
    "{" [ import_property { "," import_property } ] "}" ;

import_property =
    "Import" ":" "[" string { "," string } "]" ;
```
