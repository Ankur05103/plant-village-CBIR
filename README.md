
# Plant Village CBIR

## Overview

Plant Village CBIR (Content-Based Image Retrieval) retrieves plant images based on their features. This repository includes tools for extracting features from plant images and querying the dataset to find similar images.

## Plant Village Dataset

The Plant Village dataset is a large collection of plant images used for training and evaluating models for plant disease classification. It contains images of healthy and diseased plant leaves, covering various species and diseases.

## Files and Directories

- `CustomFeatures.h5`: Stores custom features of the plant images.
- `extraction.ipynb`: Jupyter notebook for feature extraction.
- `extraction_backup.py`: Script for feature extraction.
- `query.ipynb`: Jupyter notebook for querying the dataset.
- `requirements.txt`: Lists the dependencies required for the project.

## Installation

To get started, clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/Ankur05103/plant-village-CBIR.git
cd plant-village-CBIR
pip install -r requirements.txt
```

## Usage

**Feature Extraction**: 

1. Open `extraction.ipynb`.
2. Extract features from your plant images.
3. Save them to `CustomFeatures.h5`.

**Querying**: 

1. Open `query.ipynb`.
2. Load the saved features.
3. Perform queries to find similar plant images.

