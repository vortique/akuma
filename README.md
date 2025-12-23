# 😈 Akuma

A property-based programming language.

## Features

- Everything have a property.
- Everything can be a property.

> I don't know anything more than this (for now).

## Syntax (Only thoughts, no actions)

### Comment example

**The syntax of a comment is**:

`// <TitleForComment> <PropertyOfComment> <ValueOfComment>`

---

```akuma
/* About File { IsDocument: false, Title: "About File" }

Written by: Vortique
Date: 2025-12-23

*/

/* About The Comment { IsDocument: true, Title: "About The Comment" }

{
    IsDocument: true, // Whether the comment is a document (Optional). If it is, a document page will be created for it.
    Title: "About The Comment" // The title of the comment. If IsDocument is false, this will be the comment, otherwise it will be the title of the document and it'll be required.
} = The properties of the comment.

*/

```

### Variable example

**The syntax of a variable initialization is**:

`var <VariableName> { <PropertyOfVariable>: <ValueOfProperty>, ... } = <InitialValueOfVariable>`

**The syntax of a variable change is**:

`<VariableName> { <PropertyOfVariable>: <ValueOfProperty>, ... } = <NewValueOfVariable>`

---

```akuma

/* About File { IsDocument: false, Title: "About File" }

Written by: Vortique
Date: 2025-12-23

*/

import "akuma.default";

var var1 { Type: Integer, InChange: { value * 5, AffectsInitValue: false } } = 10;

/* About The Example { IsDocument: true, Title: "About The Example" }

var = A keyword for variable initilization.

var1 = The name of the variable.

{
    Type: Integer, // The type of the variable (Required).
    InChange:
    {
        value * 5, // The value of the variable when it changes (Optional).
        AffectsInitValue: false // Whether the initial value is affected by the InChange (Optional).
    }
} = The properties of the variable.

10 = The initial value of the variable.
*/

```

### Function example

**The syntax of a function definition is**:

`fc <FunctionName> { <PropertyOfFunction>: <ValueOfProperty>, ... } => { <FunctionBody> }`

**The syntax of a function call is**:

`<FunctionName>.call { <PropertyOfFunction>: <ValueOfProperty>, ... }`

---

```akuma

// Function definition

fc sum { ReturnType: Integer, Parameters: { param1: { Type: Integer }, param2: { Type: Integer } } } => {
    return param1 + param2;
}

/* About The Function { IsDocument: true, Title: "About The Function" }

fc = A keyword for function definition.

sum = The name of the function.

{
    ReturnType: Integer, // The return type of the function (Required).
    Parameters: { param1: { Type: Integer }, param2: { Type: Integer } } // The parameters of the function (Optional).
} = The properties of the function.

*/

// Function call

sum.call { param1: 10, param2: 20 };

/* About The Function Call { IsDocument: true, Title: "About The Function Call" }

sum = The name of the function.

{
    param1: 10, // The value of the parameter (Required).
    param2: 20 // The value of the parameter (Required).
} = The properties of the function call.

*/

```

### Default functions and importing libraries example

```akuma

/* About File { IsDocument: false, Title: "About File" }

Written by: Vortique
Date: 2025-12-23

*/

import "akuma.default";
from "akuma.io" { Import: ["echo"] }

var myValue { Type: Integer } = 10;
var myOtherValue { Type: Integer };

myOtherValue = sum.call { param1: myValue, param2: 5 };

echo.call { valueToPrint: myOtherValue }; // Output will be 15.

/* About importing { IsDocument: true, Title: "About importing" }

import "akuma.default"; // Importing the "default" library (Required, If not added, all code is a plain text).
from "akuma.io" { Import: ["echo"] } // Importing the "echo" function from the "io" library (Optional). The array in the Import property is the list of anything to import.

*/

```

## Examples

You can find more examples in the [examples](examples) directory.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
