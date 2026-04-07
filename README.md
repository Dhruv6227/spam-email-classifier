# Spam Email Classifier

## Overview
This project is a machine learning web application built with Streamlit that classifies an email as either "Spam" or "Not Spam" based on its text content. It takes an input message and utilizes a pre-trained machine learning model along with a text vectorizer (both serialized using `pickle`) to quickly evaluate and predict whether the text is spam.

## Project Structure
- `app.py`: The main Streamlit web application script. It contains the user interface and processing logic for generating predictions.
- `model.ipynb`: A Jupyter Notebook that details the data exploration, preprocessing, and model training steps. This notebook is also responsible for generating the `.pkl` files.
- `spam.csv`: The dataset used to train the machine learning model.
- `model/`: A folder containing the exported artifacts needed to run predictions:
  - `model.pkl`: The trained machine learning model.
  - `vectorizer.pkl`: The text vectorizer used to transform text input into feature vectors.
- `requirements.txt`: The list of Python library dependencies.

## Key Dependencies
- `pandas`
- `numpy`
- `scikit-learn`
- `streamlit`
- `pickle-mixin`

## Getting Started

### Prerequisites
Make sure you have Python installed on your operating system.

### Installation
1. Clone this repository or download the project files.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the specific library versions using:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
1. With dependencies installed, type the following command to launch the app:
   ```bash
   streamlit run app.py
   ```
2. The Streamlit web interface should open automatically in your default internet browser (usually at `http://localhost:8501`).
3. Enter the content of the email or message into the designated text area and click **Predict** to view the classification result.
