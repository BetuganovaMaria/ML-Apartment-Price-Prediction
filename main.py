from data_formatting import *
from model_comparing import compare_models, print_feature_importances
from constants import SALE_PRICE_KEY, ID_KEY
from catboost import CatBoostRegressor
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv, DataFrame
from sklearn.model_selection import cross_val_score


# format files
format_file('train.csv')
format_file('test_with_results.csv')

train_dataset = read_csv('formatted_data/formatted_train.csv')
test_dataset = read_csv('formatted_data/formatted_test_with_results.csv')
column_keys = train_dataset.columns.tolist()

y_train = train_dataset[[SALE_PRICE_KEY]]
x_train = train_dataset.drop([SALE_PRICE_KEY], axis=1)

y_test = test_dataset[[SALE_PRICE_KEY]]
x_test = test_dataset.drop([SALE_PRICE_KEY, ID_KEY], axis=1)

# compare to choose the best
compare_models(x_train, y_train)

# choose the best model
model = CatBoostRegressor(verbose=False)
model = model.fit(x_train, y_train.values.ravel())

y_pred = model.predict(x_test)
mse = np.mean(np.sqrt(-cross_val_score(model, x_test, y_test.values.ravel(), cv=5, scoring="neg_mean_squared_error")))
print(f'MSE CatBoostRegressor: {mse}')  # mse = 12302.83934392931

# to see which parameters affect the most
print_feature_importances(column_keys, model)

# creating file with result predicted data
result_dataset = DataFrame({ID_KEY: test_dataset[[ID_KEY]].values.ravel(),
                            SALE_PRICE_KEY: y_pred})
create_result_file(result_dataset)

# graph for comparing
plt.figure()
plt.scatter(test_dataset[[ID_KEY]].values.ravel(), y_test, s=7, label="y_test")
plt.scatter(test_dataset[[ID_KEY]].values.ravel(), y_pred, s=7, label="y_pred")
plt.legend()
plt.show()
