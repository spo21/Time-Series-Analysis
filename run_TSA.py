from TSA_Package import get_data, analyse_data, data_split, linear_regression

Apple = get_data()  

train, test = data_split(Apple)

### Problem: How accurately can you predict the next days increase or decrease in stock value
### Take 80% of the data and calculate a rolling next day prediction of up or down, verify against the 20% test data and output a prediction accuracy

# Try linear regression
lr_prediction_accuracy = linear_regression(train, test)
print(lr_prediction_accuracy)