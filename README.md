# HybridDog — Python OOP Practice

A simple Python program demonstrating **Object-Oriented Programming (OOP)** concepts such as **inheritance, multiple inheritance, constructors, and `super()`**.

## 📌 Description

This project creates a `HybridDog` class that inherits from both the `dog` and `pet` classes.

The program takes the dog's **name, colour, owner, and age** as input and displays the information using a `show()` method.

## 🧠 OOP Concepts Used

### 1. Inheritance

The `dog` and `cat` classes inherit from the `animal` class.

```python
class dog(animal):
```

This allows them to use the `colour` attribute defined in `animal`.

### 2. `super()`

The `dog` and `cat` classes use `super()` to call the constructor of the parent `animal` class.

```python
super().__init__(c)
```

### 3. Multiple Inheritance

`HybridDog` inherits from both `dog` and `pet`.

```python
class HybridDog(dog, pet):
```

Therefore, a `HybridDog` object can have properties from both classes.

### 4. Constructors

Each class has its own `__init__()` method for initializing object attributes.

### 5. Method Definition

The `show()` method displays the information stored in the `HybridDog` object.

## 📂 Class Structure

```text
animal
  ├── dog
  │     └── HybridDog
  │
  └── cat

pet
  └── HybridDog
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python main.py
```

You will be asked to enter:

```text
Enter dog name:
Enter dog colour:
Enter owner name:
Enter dog age:
```

### Example

```text
Enter dog name: Bruno
Enter dog colour: Brown
Enter owner name: Fareeha
Enter dog age: 3

Name: Bruno
Color: Brown
Owner: Fareeha
Age: 3
```

## 🎯 Purpose

This project is mainly for practicing Python OOP concepts, especially **multiple inheritance and constructor initialization**.



