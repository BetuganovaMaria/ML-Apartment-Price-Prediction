# ML Apartment Price Prediction

Model for sale price predicting.

## Libraries

- catboost
- matplotlib
- numpy
- pandas
- sklearn
- xgboost

## Data for prediction
### Data

Data description: ```data_description.txt```.

Test and train data: ```test.csv```, ```train.csv```.

Test results: ```sample_submission.csv```.

Test data & results: ```test_with_results.csv```.

### Formatted data

Formatted test data & results and train data: 
```formatted_test_with_results.csv```, ```formatted_train.csv```

### Result

Predicted result sale price: ```result.csv```

## Program files

### main.py

- formatting data for using model;
- choosing the best model (```CatBoostRegressor```) by comparing them;
- predicting data and comparing them;
- creating result file;
- showing graph for comparing test and predicted data.

### constants.py

Constants for keys & maps for data formatting. 
It's description can be found in ```data_description.txt```.

### data_formatting.py

```def format_data_types(df)```
- filling empty fields;
- replacing not number values using maps.

```def format_file(filename)```
- formatting data types;
- deleting columns in depend on correlation coefficients.

```def create_formatted_file(df, filename)```
- create formatted file in **formatted_data** directory.

```def create_result_file(df)```
- create file with results in **result** directory.

### corr_operations.py

```def check_corr_emptiness(corr_coefficients)```
- check correlation coefficients for emptiness and in case of emptiness add if for deleting.

```def check_corr_coefficients(corr_coefficients)```
- find dependent values and add them for deleting.

### model_comparing.py

```def compare_models(x_train, y_train)```
- compare models for choosing the best option by mean squared error comparing.

```def print_feature_importances(column_keys, model)```
- print feature importances for current model.
