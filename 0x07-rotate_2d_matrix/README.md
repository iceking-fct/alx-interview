# Overview #

## Background Context ##
Rotating a 2D matrix 90 degrees clockwise is a common interview challenge.  It's relatively simple to implement in Python and while it seems like an abstract concept, its application is useful in various areas of software development which include:
- Image Rotation: Rotating an image by 90 degrees is a common operation in image editing, photo manipulation, or preprocessing for computer vision.
- Game Development: Used to rotate sprites, textures, or game maps in 2D games.
- Canvas Manipulation: In GUI applications, it is often necessary to rotate elements for alignment or styling.
- Chart Orientation: Rotating heatmaps, tables, or grid-based plots for better visualization.
- Text Alignment: Reorienting labels or titles in a graphical representation.
- Tetris: Rotating blocks is a fundamental mechanic in games like Tetris, where shapes are rotated 90 degrees to fit into spaces.
- And many other instances where a grid roatation is a needed.

So now knowing that it's useful and applicable, sit back, relax and reminisce on how you can apply this technique in the future. Cheers and Happy Coding!

## Reference Materials ##
The following can be used for referencing these areas, curated for optimized understanding:


## Folder Details ###
- **Date Created:** Wed Nov. 20 2024 5:47pm
- **Author:** [MIRACLE AMAJAMA](https.//github.com/iceking-fct).
- **Project Timeline:**
- **Released:** Mon Nov 18 2024 - 6am.
  - **1st Deadline** Fri Nov. 22 2024 - 6am.
  - **Duration:** 96hrs (4 days)
  - **Completed:** Thu Nov 21 2024 - 5:80am.


## Files  ###
*This is a high-level view of files in this directory and a short description of what they contain. Each file is task based and a full description of each task, requirement and constraints can be found in each file. The tasks are designed to test understanding of these concepts above....* **enjoy!**

| **SN** | File                         | Description                                         |
|----|----------------------------------------------------|---------------------------------------|
| 1. | [0-rotate_2d_matrix.py](https://github.com/iceking-fct/alx-interview/tree/main/0x07-rotate_2d_matrix/0-rotate_2d_matrix.py) | A script that rotates a 2D array 90deg clockwise. |


0x07. Rotate 2D Matrix
Algorithm
Python
 Weight: 1
 Project over - took place from Nov 18, 2024 6:00 AM to Nov 22, 2024 6:00 AM
 An auto review will be launched at the deadline
In a nutshell…
Auto QA review: 0.0/11 mandatory
Altogether:  0.0%
Mandatory: 0.0%
Optional: no optional tasks
For the “0. Rotate 2D Matrix” project, you are tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts and resources that you need to grasp in order to successfully complete this project.

Concepts Needed:
Matrix Representation in Python:

Understanding how 2D matrices are represented using lists of lists in Python.
Accessing and modifying elements in a 2D matrix.
In-place Operations:

Performing operations on data without creating a copy of the data structure.
The importance of minimizing space complexity by modifying the matrix in place.
Matrix Transposition:

Understanding the concept of transposing a matrix (swapping rows and columns).
Implementing matrix transposition as a step in the rotation process.
Reversing Rows in a Matrix:

Manipulating rows of a matrix by reversing their order as part of the rotation process.
Nested Loops:

Using nested loops to iterate through 2D data structures like matrices.
Modifying elements within nested loops to achieve the desired rotation.
Resources:
Python Official Documentation:

Data Structures (list comprehensions, nested list comprehension)
More on Lists
GeeksforGeeks Articles:

Inplace rotate square matrix by 90 degrees
Transpose a matrix in Single line in Python
TutorialsPoint:

Python Lists for basics of list manipulation in Python.
By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving their problem-solving and algorithmic thinking skills in Python.

Additional Resources
Mock Technical Interview
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.8.0)
You are not allowed to import any module
All modules and functions must be documented
All your files must be executable
Tasks
0. Rotate 2D Matrix
mandatory
Score: 0.0% (Checks completed: 0.0%)
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
Repo:

GitHub repository: alx-interview
Directory: 0x07-rotate_2d_matrix
File: 0-rotate_2d_matrix.py
