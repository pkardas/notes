[go back](https://github.com/pkardas/learning)

# Abbreviations

[TOC]

## SOLID

### SRP - Single Responsibility Principle

A class should have only one reason to change, so in order to reduce reasons for modifications - one class should have one responsibility. It is a bad practise to create classes doing everything.

Why is it so important that class have only one reason to change? If class have more than one responsibility they become coupled and this might led to surprising consequences like one change breaks another functionality.

You can avoid these problems by asking a simple question before you  make any changes: What is the responsibility of your  class / component / micro-service? If your answer includes the word “and”, you’re most likely breaking the single responsibility principle.

### OCP - Open-Closed Principle

Classes, modules, functions, etc. should be open to extension but closed to modification. 

Code should be extensible and adaptable to new requirements. In other words, we should be able to add new system functionality without having to modify the existing code. We should add functionality only by writing new code.

If we want to add a new thing to the application and we have to modify the "old", existing code to achieve this, it is quite likely that it was not written in the best way. Ideally, new behaviors are simply added.

### LSP - Liskov Substitution Principle

This rule deals with the correct use of inheritance and states that wherever we pass an object of a base class, we should be able to pass an object of a class inheriting from that class.

Example of violation:

```python
class A:
  def foo() -> str:
    return "foo"
  
class B(A):
  def foo(bar: str) -> str:
    return f"foo {bar}"
```

B is not taking the same arguments, meaning A and B are cot compatible. A can not be used instead of B, and B can not be used instead of A.

### ISP - Interface Segregation Principle

Clients should not be forced to depend upon interfaces that they do not use. ISP splits interfaces that are very large into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them. 

### DIP - Dependency Inversion Principle

High-level modules, which provide complex logic, should be easily reusable and unaffected by changes in low-level modules, which provide  utility features. To achieve that, you need to introduce an abstraction that decouples the high-level and low-level modules from each other.

## DRY

## KISS

## ACID

## BASE 

## NF 

### 1NF

### 2NF

### 3NF

