# Football Match Predictor

This project is a football match predictor using logistic regression. It predicts the outcome of a football match (home team win, draw, or away team win).

[Visit Football Match Predictor](https://pavanshelke-football-match-prediction.onrender.com)


## Data Source

The dataset used in this project was sourced from [Football-Data.co.uk](http://football-data.co.uk/data.php). It provides comprehensive football match statistics.

## Model Performance

I have performed Logistic Regression and Random Rorest Classification on the dataset with Logistic Regression giving the highest accuracy of 60.00%
## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Run the Streamlit app: `streamlit run ui.py`

## Usage

1. Open the Streamlit app in your web browser.
2. Enter the home team and away team in the provided input boxes.
3. Click the "Predict" button to see the predicted match result.

## Files

- `event.csv`: Contains match data.
- `lr.pkl`: Binary file of the trained logistic regression model.
- `predict_code.ipynb`: Jupyter Notebook for model training and exploration.
- `ui.py`: Streamlit UI file for user interaction.
- `requirements.txt`: File containing project dependencies.

## Dependencies

- scikit-learn
- pandas
- streamlit

