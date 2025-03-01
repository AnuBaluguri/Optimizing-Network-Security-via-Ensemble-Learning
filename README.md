# Optimizing Network Security via Ensemble Learning

This repository contains the code and data accompanying the research paper *"Optimizing Network Security via Ensemble Learning: A Nexus with Intrusion Detection"* by Anu Baluguri et al. The study presents a robust framework for network intrusion detection using a stacked ensemble technique to enhance detection accuracy and robustness.

## Repository Contents

- **Code.ipynb**: A Jupyter Notebook implementing the stacked ensemble intrusion detection system (IDS).
- **NID_data.xlsx**: The dataset used for training and evaluating the IDS.
- **JIS_Final_Paper__Optimizing_Network_Security_via_Ensemble_Learning.pdf**: The final version of the research paper detailing the methodology and findings.

## Overview of the Approach

The proposed IDS framework employs a stacked ensemble method, integrating multiple base machine learning models to capture diverse patterns in network traffic. The base models include:

- Multi-Layer Perceptron (MLP)
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Decision Trees

The predictions from these base models are combined and fed into a meta-model implemented using Logistic Regression, which synthesizes the information to make final predictions about the nature of the network traffic. This ensemble approach aims to improve detection robustness and accuracy by leveraging the strengths of each individual model.

## Getting Started

To explore and utilize the code provided in this repository:

### 1. Clone the Repository
```bash
git clone https://github.com/AnuBaluguri/Optimizing-Network-Security-via-Ensemble-Learning.git
```

### 2. Install Dependencies
Ensure you have the necessary Python libraries installed. You can install the required packages manually using:
```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```
*Note: The above packages are commonly used in machine learning projects. Please refer to the imports in `Code.ipynb` and install any additional dependencies as needed.*

### 3. Open the Jupyter Notebook
Launch Jupyter Notebook and open `Code.ipynb` to review and run the code. This notebook includes data preprocessing steps, model training, and evaluation procedures.

### 4. Dataset
The `NID_data.xlsx` file contains the dataset used for training and testing. Ensure this file is in the same directory as the notebook or adjust the file path accordingly within the notebook.

## Citation
If you utilize this code or dataset in your research, please cite the original paper:

```bibtex
@article{baluguri-2024,
	author = {Baluguri, Anu and Pasumarthy, Vasudha and Roy, Indranil and Gupta, Bidyut and Rahimi, Nick},
	journal = {Journal of Information Security},
	month = {1},
	number = {04},
	pages = {545--556},
	title = {{Optimizing Network Security via Ensemble Learning: A Nexus with Intrusion Detection}},
	volume = {15},
	year = {2024},
	doi = {10.4236/jis.2024.154030},
	url = {https://www.scirp.org/journal/paperinformation?paperid=136719},
}
```

For any questions or further information, please contact the repository owner or refer to the original publication.
