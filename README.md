# PraxLang 🚀

> A minimal, dynamically typed, interpreted programming language built entirely from scratch in Python, without external parser generators or third-party runtimes.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Project Status](https://img.shields.io/badge/status-experimental%20%2F%20educational-orange.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**PraxLang** is an experimental programming language built from the ground up to explore how programming languages work internally.

The project implements its own **lexer, parser, AST, symbol tables, scope handling, and tree-walking interpreter** without relying on external parser generators or third-party language runtimes.

---

## 📸 Overview & Architecture

PraxLang follows a traditional **tree-walking interpreter pipeline**.

Source code is read, tokenized by the lexer, parsed into an Abstract Syntax Tree (AST), and then evaluated by the interpreter.

```text
┌────────────────────────┐
│     PraxLang Source    │
│         (.pra)         │
└───────────┬────────────┘
            │
            ▼
     ┌─────────────┐
     │    Lexer    │
     └──────┬──────┘
            │ Tokens
            ▼
     ┌─────────────┐
     │    Parser   │
     └──────┬──────┘
            │ AST
            ▼
     ┌─────────────┐
     │ Interpreter │◄──────────┐
     └──────┬──────┘           │
            │              Symbol Tables
            ▼              & Environments
     ┌─────────────┐           │
     │  Execution  │───────────┘
     │   / Result  │
     └─────────────┘
```

### Pipeline

```text
Source Code
    ↓
Lexical Analysis
    ↓
Parsing
    ↓
AST Construction
    ↓
Scope Resolution
    ↓
Tree-Walking Interpretation
    ↓
Program Output
```

---

## ✨ Features

### 🧱 Built From First Principles

- Custom lexer
- Custom parser
- Custom AST representation
- Custom tree-walking interpreter
- No external parser generators such as PLY, ANTLR, or Lark
- No third-party language runtime

### 🔤 Custom Syntax

PraxLang uses its own syntax and keywords, including:

- `V` for variable declarations
- `IF`, `ELIF`, `ELSE`, `END`
- `FOR`, `TO`
- `WHILE`
- `THEN`
- `PRINT`
- `FUNCTION`

### 📦 Core Data Types

PraxLang currently supports:

- Integers
- Floating-point numbers
- Lists

### 🌳 Abstract Syntax Tree

Expressions and statements are converted into AST nodes before execution, separating parsing from interpretation.

### 🧠 Symbol Tables & Scope

PraxLang maintains symbol tables and nested environments for variable storage and scope management.

Function calls create their own execution environments for handling parameters and local variables.

### 🔁 Control Flow

Supported control-flow constructs include:

- `IF`
- `ELIF`
- `ELSE`
- `FOR`
- `WHILE`

### 🧩 Functions

PraxLang supports user-defined functions with parameters and function calls.

Example:

```praxlang
FUNCTION multiply(a, b) -> a * b

PRINT multiply(6, 7)
```

### 🧮 Built-in Operations

PraxLang provides several built-in mathematical operations:

- `sqrt`
- `abs`
- `even_check`
- `odd_check`
- `cube`
- Exponentiation using `^`

### ⚠️ Error Handling

PraxLang provides dedicated error types for different stages of execution:

- **Illegal Character Error** — invalid characters during lexical analysis
- **Invalid Syntax Error** — invalid program structure
- **Runtime Error** — errors occurring during execution

Errors include useful **line and column information** to make debugging easier.

---

# 🔤 Syntax Guide

## Variables

Variables are declared using the `V` keyword.

```praxlang
V x = 10
V y = 20.5
V numbers = [1, 2, 3, 4]

PRINT x + y
PRINT numbers[0]
```

---

## Conditional Statements

```praxlang
V score = 85

IF score >= 90 THEN
    PRINT 1
ELIF score >= 70 THEN
    PRINT 2
ELSE
    PRINT 0
END
```

---

## FOR Loops

```praxlang
FOR i = 1 TO 5 THEN
    PRINT i
END
```

---

## WHILE Loops

```praxlang
V counter = 0

WHILE counter < 3 THEN
    PRINT counter
    V counter = counter + 1
END
```

---

## Functions

Functions can accept parameters and return the value of their expression.

```praxlang
FUNCTION multiply(a, b) -> a * b

PRINT multiply(6, 7)
```

Output:

```text
42
```

---

## 🔢 Operators & Built-in Operations

| Category | Supported Operations |
|---|---|
| Arithmetic | `+`, `-`, `*`, `/`, `^` |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| Logical | `AND`, `OR`, `NOT` |
| Mathematical | `sqrt`, `abs`, `cube` |
| Checks | `even_check`, `odd_check` |

Logical expressions internally evaluate to `1` or `0`.

---

# 🛠️ Project Structure

```text
PraxLang/
│
├── praxlang.py          # Main interpreter pipeline
│                        # Lexer, Parser, AST & Interpreter
│
├── examples/
│   └── hello.pra        # Example PraxLang programs
│
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

---

# 🚀 Getting Started

## Prerequisites

Make sure you have **Python 3.8 or newer** installed.

Check your Python version:

```bash
python --version
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/prabuddha34/Making-Custom_Programming_Language.git
cd Making-Custom_Programming_Language
```

---

## Run the Interactive REPL

Start PraxLang in interactive mode:

```bash
python praxlang.py
```

Example:

```text
PraxLang >>> V x = 10
PraxLang >>> x * 3
[RESULT] 30
```

---

## Run a PraxLang Script

You can execute `.pra` source files directly:

```bash
python praxlang.py examples/hello.pra
```

Example:

```text
[OUTPUT] Hello from PraxLang!
```

---

# 🛣️ Roadmap & Limitations

PraxLang is primarily an educational project and is still experimental.

Potential future improvements include:

- [ ] String literals and string manipulation
- [ ] Explicit `RETURN` statements
- [ ] `BREAK` and `CONTINUE`
- [ ] User-defined data structures
- [ ] HashMap / dictionary support
- [ ] More complete standard-library functionality
- [ ] Static type-checking pass over the AST
- [ ] Bytecode compiler
- [ ] Virtual Machine (VM)
- [ ] Language Server Protocol (LSP)
- [ ] Editor syntax highlighting
- [ ] Improved module/import system
- [ ] Better runtime diagnostics

---

# 🎯 Why PraxLang?

PraxLang started as an experiment to understand what happens between writing code and actually executing it.

Instead of relying on existing language infrastructure, the project explores the process directly:

```text
Characters
    ↓
Tokens
    ↓
Syntax
    ↓
AST
    ↓
Environment
    ↓
Interpretation
    ↓
Output
```

Building these components from scratch provides a practical understanding of concepts such as:

- Lexical analysis
- Parsing
- Abstract Syntax Trees
- Expression evaluation
- Scope and environments
- Symbol tables
- Function calls
- Runtime errors
- Interpreter architecture

---

# 👤 Author

**Prabuddha Pal**

- GitHub: [@prabuddha34](https://github.com/prabuddha34)

---

# 📜 License

PraxLang is distributed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.
