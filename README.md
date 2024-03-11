# L-system

Lindenmayer Systems, or L-systems, are a mathematical formalism introduced by biologist Aristid Lindenmayer in 1968 to describe the growth processes of plant development. They have since found applications in computer graphics, art, and linguistics. This repository provides a simple implementation in Python.

## Usage

Define an L-system. The example below [represents a binary tree](https://www.youtube.com/watch?v=puwhf-404Xc). 

```python
system = LSystem({
    'X': 'XX',
    'Y': 'X[-Y][+Y]',
})
```

Grow the system for some number of steps.

```python
system.grow('Y', steps=3)  # Returns 'XX[-X[-Y][+Y]][+X[-Y][+Y]]'
```
