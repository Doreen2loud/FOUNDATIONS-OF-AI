# FOUNDATIONS OF AI

## Registrations Details

NAME: DOREEN MULEE
REG/NO: CIT-223-070/2024
UNIT NAME: FOUNDATIONS OF AI
UNIT CODE: CCS 2226
COURSE: COMPUTER SCIENCE

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


## Task 2b


### Purpose 
To colour all 17 Nairobi Sub-Counties using the LEAST possible number of colours with no two 
adjacent sub-counties sharing the same colour.




### Sub-Counties
1. Westlands
2. Dagoretti North
3. Dagoretti South
4. Langata
5. Kibra
6. Roysambu
7. Kasarani
8. Ruaraka
9. Embakasi South
10. Embakasi North
11. Embakasi Central
12. Embakasi East
13. Embakasi West
14. Makadara
15. Kamukunji
16. Starehe
17. Mathare


### Rules
- No two neighbouring sub-counties can share the same colour
- Must use the minimum number of colours possible



### How it works
1. Defines all 17 Nairobi sub-counties
2. Defines border relationships referenced from Nairobi County map
3. Starts by trying 3 colours
4. Increases number of colours if solution not found
5. Uses backtracking algorithm to assign colours
6. Verifies all constraints are satisfied
7. Displays minimum colours needed and full solution



### Result
- Minimum colours needed: 4
- All 17 sub-counties successfully coloured
- No two neighbouring sub-counties share same colour
- All constraints satisfied 



### How to run
```bash
python task2b_NairobiClouring.py
```


