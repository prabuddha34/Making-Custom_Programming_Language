# PraxLang

> A small interpreted programming language built from scratch in Python.

**PraxLang** is a personal programming language project created to explore how programming languages work internally — from lexical analysis and parsing to AST construction, symbol tables, scopes, and interpretation.

The project is intentionally built from the ground up without relying on parser generators or existing language runtimes.

PraxLang uses its own syntax, lexer, parser, AST nodes, interpreter, error system, REPL, and `.pra` source-file format.

---

## ✨ Features

### Core language

- Integer and floating-point numbers
- Variables
- Arithmetic expressions
- Operator precedence
- Unary `+` and `-`
- Exponentiation with `^`
- Cube operation
- Square root
- Absolute value
- Even / odd checking

### Variables

Variables use the `V` keyword:

```prax
V x = 10
V y = 20

x + y
```

---

## 🔀 Control Flow

PraxLang supports conditional statements:

```prax
IF x > 10 THEN
    PRINT x
END
```

Multiple branches are supported:

```prax
IF x > 10 THEN
    PRINT x
ELIF x == 10 THEN
    PRINT 10
ELSE
    PRINT 0
END
```

### `FOR` loops

```prax
FOR i = 1 TO 5 THEN
    PRINT i
END
```

### `WHILE` loops

```prax
V x = 1

WHILE x <= 5 THEN
    PRINT x
    V x = x + 1
END
```

Multiline blocks are terminated using `END`.

---

## 📦 Lists

PraxLang supports list creation:

```prax
V numbers = [10, 20, 30, 40]
```

and indexing:

```prax
PRINT numbers[0]
PRINT numbers[2]
```

Lists are represented internally by the interpreter and can be accessed through index expressions.

---

## 🧩 Functions

PraxLang supports function definitions, arguments, function calls, and local scopes.

Example:

```prax
Function add(a, b) -> a + b
```

Functions can then be called using:

```prax
add(10, 20)
```

Functions receive their own symbol table while retaining access to their surrounding environment.

---

## 🔢 Operators

### Arithmetic

| Operator | Description |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `^` | Exponentiation |

### Comparison

| Operator | Description |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

### Logical

| Operator | Description |
|---|---|
| `AND` | Logical AND |
| `OR` | Logical OR |
| `NOT` | Logical NOT |

Boolean results are represented internally as `1` and `0`.

---

## 🧮 Built-in Operations

PraxLang currently includes several built-in operations:

```prax
sqrt 25
abs -10
even_check 10
odd_check 7
```

The language also supports exponentiation:

```prax
2 ^ 5
```

and cube operations:

```prax
3 cube
```

---

## 🏗️ How PraxLang Works

PraxLang follows a traditional interpreter pipeline:

```text
             PraxLang Source
                    │
                    ▼
                ┌───────┐
                │ Lexer │
                └───┬───┘
                    │
                    ▼
                 Tokens
                    │
                    ▼
                ┌────────┐
                │ Parser │
                └───┬────┘
                    │
                    ▼
                  AST
                    │
                    ▼
              ┌────────────┐
              │ Interpreter│
              └─────┬──────┘
                    │
                    ▼
                 Result
```

### Lexer

The lexer reads raw PraxLang source code and converts it into tokens.

For example:

```prax
V x = 10 + 5
```

becomes a sequence containing tokens representing:

```text
KEYWORD(V)
IDENTIFIER(x)
=
INT(10)
+
INT(5)
```

The lexer also tracks line and column information for errors.

### Parser

The parser consumes the tokens and constructs an **Abstract Syntax Tree (AST)**.

For example:

```prax
2 + 3 * 4
```

is represented structurally so that multiplication is evaluated before addition.

### AST

PraxLang uses dedicated node classes for different language constructs, including nodes for:

- Numbers
- Variables
- Variable assignments
- Binary operations
- Unary operations
- Lists
- Indexing
- Functions
- Function calls
- `IF`
- `FOR`
- `WHILE`
- `PRINT`
- Multiple statements

### Interpreter

The interpreter walks the AST and evaluates each node.

A visitor-style architecture is used:

```text
AST Node
   │
   ▼
visit(Node)
   │
   ├── visitNumberNodes()
   ├── visitBinOp()
   ├── visitIfNode()
   ├── visitForNode()
   ├── visitWhileNode()
   ├── visitListNode()
   ├── visitCallNode()
   └── ...
```

---

## 🧠 Symbol Tables and Scope

PraxLang has its own `SymbolTable` implementation.

Symbol tables store variables and support parent scopes:

```text
Global Symbol Table
        │
        ├── x
        ├── y
        │
        └── Function Scope
                │
                ├── a
                └── b
```

Function calls create a fresh local symbol table while maintaining access to the surrounding environment.

This allows PraxLang to experiment with lexical/environment-based scope rather than simply storing every variable globally.

---

## ⚠️ Error Handling

PraxLang has separate error types for different stages of execution:

```text
Illegal Character
Invalid Syntax
Run Time Error
```

Errors include source locations:

```text
Invalid Syntax: Missing END (Line 4, Column 12)
```

This makes syntax and runtime problems easier to locate while experimenting with the language.

---

## 💻 Running PraxLang

### Requirements

- Python 3
- No external parser/runtime required

Clone the repository and enter the project directory.

Then start the REPL:

```bash
python praxlang.py
```

You should see:

```text
PraxLang >>>
```

Example:

```text
PraxLang >>> 10 + 20
[RESULT] 30
```

---

## 📄 Running a `.pra` File

PraxLang source files use the:

```text
.pra
```

extension.

Example file:

```text
hello.pra
```

```prax
V result = 1

FOR i = 1 TO 5 THEN
    V result = result * i
    PRINT result
END
```

Run it with:

```bash
python praxlang.py hello.pra
```

---

## 🛠️ Project Structure

The project is currently intentionally compact while the language is being developed.

```text
PraxLang/
│
├── praxlang.py
├── *.pra
├── README.md
└── ...
```

The main implementation currently contains the major components of the language:

```text
Tokens
   ↓
Lexer
   ↓
AST Nodes
   ↓
Parser
   ↓
Symbol Table
   ↓
Interpreter
   ↓
REPL / File Runner
```

---

## 📚 Language Design

PraxLang is not intended to imitate an existing language exactly.

The syntax is deliberately experimental.

For example, variable declarations use:

```prax
V x = 10
```

rather than traditional declarations such as:

```text
var x = 10
```

The project is primarily an exploration of:

- Language design
- Lexing
- Parsing
- AST construction
- Interpreters
- Runtime environments
- Scope
- Error handling
- Control flow

---

## 🚧 Current Limitations

PraxLang is still a small experimental language.

It currently does **not** aim to provide the feature set or performance of production languages such as C++, Java, Python, Rust, or Go.

Some areas are still limited, including:

- Type system
- Standard library
- String literal support
- More advanced data structures
- More complete function semantics
- Advanced runtime features
- Optimisation
- Bytecode generation
- Native compilation
- Tooling / IDE integration
- Package management

These limitations are intentional at this stage of development.

The goal is to understand the fundamentals before attempting more advanced language infrastructure.

---

## 🗺️ Possible Future Development

Potential future directions include:

- String literals
- More complete list operations
- `BREAK`
- `CONTINUE`
- Return statements
- Better function semantics
- User-defined data structures
- Better type checking
- Standard library
- Improved error messages
- Modules
- Bytecode VM
- Compiler backend
- Native executable generation
- Syntax highlighting
- Language Server Protocol support

---

## 🎯 Why This Project Exists

PraxLang started as an experiment in understanding what actually happens between source code and execution.

Instead of only learning programming languages as a user, this project explores the machinery behind them:

```text
Source Code
    ↓
Lexing
    ↓
Tokens
    ↓
Parsing
    ↓
AST
    ↓
Interpretation
    ↓
Execution
```

Building each part manually provides a practical way to understand concepts that are normally hidden behind compilers and interpreters.

---

## 📌 Project Status

**Status: Experimental / Educational**

PraxLang is currently a working interpreted language with its own:

- Lexer
- Parser
- AST
- Interpreter
- Symbol tables
- Functions
- Control flow
- Lists
- Error handling
- REPL
- `.pra` source files

The language is considered a learning project rather than a production programming language.

---

## 👤 Author

**Prabuddha Pal**

Built as a personal exploration of programming language implementation, interpreters, and language design.

---

## 📜 License

This project is intended as an educational and experimental programming-language project.
