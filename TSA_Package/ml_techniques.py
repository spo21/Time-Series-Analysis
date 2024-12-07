from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np


def linear_regression(train, test):
    model = LinearRegression()
    correct = 0

    train = train.copy()
    train['Target'] = train['Close'].shift(-1)  # Next day's closing price
    train = train.dropna()  # Drop rows with NaN values (due to shifting)

    for i in range(len(test)):
        # Fit the model using the training data
        model.fit(train[['Open', 'Close', 'High', 'Low', 'Volume']], train['Target'])

        # Predict the target for the current test row
        current_row = test.iloc[i:i+1]  # Select the current row as a DataFrame
        prediction = model.predict(current_row[['Open', 'Close', 'High', 'Low', 'Volume']])
        actual = current_row['Close'].values[0]

        # Check prediction
        if prediction[0] > actual:
            correct += 1

        # Add the current test row to the training set for incremental learning
        new_row = current_row.copy()
        new_row['Target'] = current_row['Close'].values[0]  # Assign actual target
        train = pd.concat([train, new_row])

    accuracy = correct / len(test) if len(test) > 0 else 0
    return accuracy
