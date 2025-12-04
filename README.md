# 🧬 Genetic Traits Simulator (PA2 Biology Lab)

This project is a Python-based simulation for a Biology Laboratory, developed for the **Programació i Algorismia 2 (PA2)** course. It models genetic experiments to study the relationship between chromosome pairs and physical traits within a genealogical tree.

## 📋 Project Overview
The application analyzes how genetic traits are distributed across a family structure. It processes "experiments" consisting of individuals with genealogical relationships and chromosome data (bitstrings). The core functionality includes:
* **Genealogy Mapping:** reconstructing family trees from preorder traversal input.
* **Genetics Analysis:** calculating the specific gene combinations (intersections) responsible for observed traits.
* **Trait Distribution:** visualizing which members of a lineage manifest a specific trait using inorder traversal.

## 🚀 Tech Stack
* **Language:** Python 3
* **Dependencies:** `pytokr` (for efficient input tokenization).

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| **`interficie.py`** | **Entry point**. Reads commands from standard input (stdin) and orchestrates the experiment flow. |
| **`conj_individus.py`** | Manages the collection of individuals and the private `__Arbre` class for genealogical relationships. |
| **`conj_trets.py`** | Maintains the dictionary of traits and calculates the intersection of chromosome pairs for each trait. |
| **`individu.py`** | Represents a single individual, linking their chromosome pair to their set of observed traits. |
| **`parell_cromosomes.py`** | Handles the bitstring logic for chromosome pairs and intersection operations. |

## ⚙️ Installation & Usage

1.  **Install Requirements**
    You need the `pytokr` library to parse the input format.
    ```bash
    pip install pytokr
    ```

2.  **Run the Simulation**
    The program reads commands from **standard input**. You should pipe a text file containing the experiment data.
    ```bash
    python interficie.py < input_data.txt
    ```

### Input Format Summary
The input expects a sequence of commands handled by `interficie.py`:
* `experiment <n> <m>`: Starts a new experiment with `n` individuals and chromosomes of length `m`. Followed by the tree structure (preorder) and chromosome data.
* `afegir_tret <name> <id>`: Associates a trait with an individual and updates the genetic intersection.
* `consulta_tret <name>`: Displays the gene combination and individuals with the trait.
* `distribucio_tret <name>`: Prints the inorder traversal of the affected subtree.
* `fi`: Exits the program.

## 👤 Authors
Created by **Nil Macià Codera** and **Joan Bennassar Martín** (UPC - FIB, 2022-2023).
