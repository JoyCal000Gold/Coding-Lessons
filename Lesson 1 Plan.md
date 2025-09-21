# Lesson Plan: Programming Concepts & Analytics Web App

Built with Quarto (R Markdown) + Python + C++/Rust Extensions

**Lesson Objectives:**
Build a strong conceptual foundation by classifying programming languages and understanding their core design goals and use cases. So, before jumping into syntax, it helps students understand why languages exist, their strengths and weaknesses, and which to pick for different tasks.

### Learning Goals
- Learn conditional statements (if/else)
- Understand data types (strings, integers, booleans)
- Implement a for loop for navigation (e.g., buttons to switch between sections/pages)
- Compare language paradigms and execution models through direct usage
- Use built-in functions for input/output and data manipulation
- See how R Markdown integrates with Python, C++, and Rust code chunks

## Webpage One (Homepage): Password Protection

**Objective:**  
Teach basic programming concepts such as functions, data types, variables, and operators.

### What to Cover

- Start with a password prompt using a simple if/else statement.
- The user must input a password to access the next page or section.

---

## Webpage: Data

**Objectives:**
- Composite Data Types (Core): JSON (Python) to data.frame (R) conversion
- Advanced Data Concepts (Study Ahead): Cross-language data serialization
- Memory Fundamentals (Study Ahead): How data moves between language runtimes

### WHaat to Cover
- Working with APIs and static datasets.
- Modifying and filtering data.
- Introduction to Python user interface systems.
- Use Python's API libraries while processing data in R
- Show how to pass data between R and Python chunks in Quarto

---

## Webpage: Analytics

** Objectives:**
- Leverage R's statistical computing strengths for analysis
- Demonstrate language-specific optimization for different tasks
- Memory Management (Study Ahead): How Quarto manages multi-language memory


#### What to Cover
- Python regression analysis.
- R regression analysis.
- Visualizations with R graphs and Python graphics.

---

## Webpage: Reports

** Objectives:**
Demonstrate advanced Quarto features for multi-language documents
Show complete workflow from data acquisition to final report
Preview advanced concepts available in each language ecosystem

#### What to Cover
- Reporting with R Markdown, PDF, HTML output.
- Using R and Quarto for interactive and static reports.

### Resources for Further Learning

#### Websites
- [Real Python](https://realpython.com/)
- [Python Official Documentation](https://docs.python.org/3/)
- [R for Data Science](https://r4ds.hadley.nz/)
- [Shiny by RStudio](https://shiny.posit.co/)
- [Quarto Documentation](https://quarto.org/docs/)

#### YouTube Channels & Playlists
- [Corey Schafer - Python Programming](https://www.youtube.com/user/schafer5)
- [Data School - Python & Data Science](https://www.youtube.com/c/DataSchool)
- [StatQuest with Josh Starmer (R & Statistics)](https://www.youtube.com/c/joshstarmer)
- [R Programming 101](https://www.youtube.com/playlist?list=PLqzoL9-eJTNBDdKgJgJzaQcY6OXmsXAHU)

#### Books
- _Python Crash Course_ by Eric Matthes
- _Automate the Boring Stuff with Python_ by Al Sweigart
- _R for Data Science_ by Hadley Wickham & Garrett Grolemund
- _Hands-On Programming with R_ by Garrett Grolemund
#### Notes
# Programming Concepts Taxonomy - Basic Lesson Scope
*Core concepts for beginners, with advanced topics for further study*

## I. Foundational Elements

### A. Data Types
1. **Primitive Types** *(Core Lesson)*
   a. Numeric
      i. Integer
      ii. Floating Point
   b. Textual
      i. String
   c. Logical
      i. Boolean

2. **Composite Types** *(Core Lesson)*
   a. Collections
      i. Arrays/Lists
      ii. Dictionaries/Maps

3. **Advanced Data Concepts** *(Study Ahead)*
   a. Numeric Precision
      i. Fixed vs Floating Point
      ii. Overflow/Underflow
   b. Memory Representation
      i. Binary Encoding
      ii. Character Encoding (ASCII, UTF-8)
   c. Structured Data
      i. Tuples
      ii. Sets
      iii. Custom Types/Structs

### B. Variables & Memory
1. **Variable Operations** *(Core Lesson)*
   a. Declaration
   b. Assignment

2. **Scope Management** *(Core Lesson)*
   a. Global
   b. Local

3. **Memory Fundamentals** *(Study Ahead)*
   a. Stack vs Heap
   b. Variable Lifetime
   c. Memory Addresses
   d. Pointers vs References
   e. Memory Allocation/Deallocation

## II. Expressions & Operations

### A. Operators
1. **Comparison Operators** *(Core Lesson)*
   a. Equality Operators
      i. Equal (==)
      ii. Not Equal (!=)
   b. Relational Operators
      i. Less Than (<)
      ii. Greater Than (>)
      iii. Less Than or Equal (<=)
      iv. Greater Than or Equal (>=)

2. **Logical Operators** *(Core Lesson)*
   a. Boolean Logic
      i. Logical AND (&&/and)
      ii. Logical OR (||/or)
      iii. Logical NOT (!/not)

3. **Assignment Operators** *(Core Lesson)*
   a. Simple Assignment (=)

4. **Advanced Operators** *(Study Ahead)*
   a. Arithmetic Operators
      i. Basic Math (+, -, *, /)
      ii. Modulus (%)
      iii. Increment/Decrement (++, --)
   b. Bitwise Operators
      i. AND (&)
      ii. OR (|)
      iii. XOR (^)
      iv. Shift (<<, >>)
   c. Compound Assignment
      i. Add-assign (+=)
      ii. Subtract-assign (-=)
   d. Memory Operators
      i. Address-of (&)
      ii. Dereference (*)
      iii. Member Access (., ->)

### B. Expression Types
1. **Primary Expressions** *(Core Lesson)*
   a. Variables
   b. Literals
   c. User Input

2. **Boolean Expressions** *(Core Lesson)*
   a. Comparison Results
   b. Logical Combinations

3. **Advanced Expression Concepts** *(Study Ahead)*
   a. Operator Precedence
   b. Type Coercion/Casting
   c. Short-circuit Evaluation
   d. Side Effects

## III. Control Structures

### A. Conditional Control
1. **Basic Conditionals** *(Core Lesson)*
   a. If Statements
   b. If-Else Statements
   c. Else-If Chains

2. **Advanced Conditionals** *(Study Ahead)*
   a. Switch/Case Statements
   b. Pattern Matching
   c. Guard Clauses

### B. Iterative Control
1. **Entry-controlled Loops** *(Core Lesson)*
   a. For Loops
      i. Range-based Iteration
      ii. Collection Iteration

2. **Advanced Loop Concepts** *(Study Ahead)*
   a. While Loops
   b. Do-While Loops
   c. Nested Loops
   d. Loop Control
      i. Break Statements
      ii. Continue Statements
   e. Iterator Patterns

## IV. Functions & Procedures

### A. Function Usage
1. **Built-in Functions** *(Core Lesson)*
   a. Input Functions
   b. Output Functions
   c. Type Conversion Functions
   d. Collection Functions

### B. Function Calls
1. **Basic Function Calls** *(Core Lesson)*
   a. Functions with Parameters
   b. Functions with Return Values

### C. Advanced Function Concepts *(Study Ahead)*
1. **Function Definition**
   a. Custom Functions
   b. Parameters and Arguments
   c. Return Values
   d. Local vs Global Variables

2. **Function Types**
   a. Pure vs Impure Functions
   b. Recursive Functions
   c. Higher-order Functions

3. **Advanced Features**
   a. Default Parameters
   b. Variable Arguments
   c. Lambda/Anonymous Functions
   d. Function Overloading

## V. Language Implementation

### A. Execution Models
1. **Interpreted Languages**
   a. Python - Interactive Development
   b. R - Statistical Computing

2. **Compiled Languages**
   a. C++ - Systems Programming
   b. Rust - Memory Safety

### B. Memory Management *(Study Ahead)*
1. **Automatic Memory Management**
   a. Garbage Collection (Python, Java)
   b. Reference Counting

2. **Manual Memory Management**
   a. malloc/free (C++)
   b. new/delete (C++)

3. **Modern Memory Safety**
   a. Ownership System (Rust)
   b. Borrowing and Lifetimes (Rust)
   c. RAII (C++/Rust)
### C. Language Design Goals *(Core Lesson)*
   a. Readability
   b. Simplicity
   c. General Purpose

2. **R**
   a. Statistical Analysis
   b. Data Visualization
   c. Research-Oriented

3. **C++**
   a. Performance
   b. System Control
   c. Resource Management

4. **Rust**
   a. Memory Safety
   b. Performance
   c. Concurrency

### E. Use Cases by Language *(Core Lesson)*
1. **Python**
   a. Web Development
   b. Data Science
   c. Automation
   d. APIs

2. **R**
   a. Statistical Analysis
   b. Data Visualization
   c. Research Reports
   d. Time Series Analysis

## VI. Programming Paradigms

### A. Imperative Programming
1. **Procedural Programming** *(Core Lesson)*
   a. Step-by-step Instructions
   b. Sequential Execution
   c. Function Calls

2. **Advanced Imperative Concepts** *(Study Ahead)*
   a. Object-Oriented Programming
      i. Classes and Objects
      ii. Encapsulation
      iii. Inheritance
      iv. Polymorphism
   b. Structured Programming
      i. Control Flow Management
      ii. Modular Design

### B. Language-Specific Paradigms *(Core Lesson)*
1. **Python**
   a. Multi-paradigm
   b. Object-oriented Capable
   c. Functional Features

2. **R**
   a. Statistical Computing
   b. Vectorized Operations
   c. Functional Programming

3. **C++**
   a. Multi-paradigm
   b. Object-oriented
   c. Generic Programming

4. **Rust**
   a. Systems Programming
   b. Functional Features
   c. Memory Safety Focus

### C. Advanced Programming Paradigms *(Study Ahead)*
1. **Functional Programming**
   a. Pure Functions
   b. Immutability
   c. Higher-order Functions
   d. Recursion

2. **Concurrent Programming**
   a. Multi-threading
   b. Async/Await Patterns
   c. Message Passing
   d. Shared Memory Models

3. **Generic Programming**
   a. Templates (C++)
   b. Generics (Rust)
   c. Type Parameters
