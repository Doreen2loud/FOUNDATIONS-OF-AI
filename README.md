# AI and ML 
## Task 1

This project uses a neural network to recognize handwritten digits (0–9) using the MNIST dataset.

### Dataset
The model uses the MNIST dataset, which contains:

 1. 60,000 training images
 2. 10,000 test images
 3. Images are 28×28 pixels in grayscale


### Objective

To build and train a neural network that can accurately classify handwritten digits based on image input.

### Technologies Used
 1. Python
 2. TensorFlow / Keras
 3. NumPy
 4. Matplotlib

### How to Run

1. Clone the repository
2. Install dependencies
3. Run the training script


```bash
pip install -r requirements.txt
python mnist_Task1.py
```

## Task 2a
### Purpose

 This program solves the Map Colouring problem for Australia using Constraint Satisfaction Problem (CSP) approach with backtracking algorithm.

 ### Rules
1. All the 6 regions of Austarlia should be coloured.
2. The coloured used should either be of the 3:Red,Blue or Green.
3. Adjacent regions should not share the same colour.


### How it works
1. Defines all 6 Australian regions
2. Defines which regions share borders
3. Tries colours one by one using backtracking
4. Verifies no two neighbours share same colour
5. Displays the final solution

### How to run

```bash
python task2a_MapColouring.py
```