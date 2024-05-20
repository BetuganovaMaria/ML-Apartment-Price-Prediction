from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
import numpy as np


def compare_models(x_train, y_train):
    models = [LinearRegression(),
              DecisionTreeRegressor(),
              RandomForestRegressor(),
              GradientBoostingRegressor()
              ]

    for model in models:
        rmse = np.mean(np.sqrt(-cross_val_score(model, x_train, y_train.values.ravel(), cv=5, scoring="neg_mean_squared_error")))
        print(f"MSE: {str(model)}  {round(rmse, 4)}")

    # result:
    # >> MSE: LinearRegression()  36492.6932
    # >> MSE: DecisionTreeRegressor()  42279.3253
    # >> MSE: RandomForestRegressor()  31161.1689
    # >> MSE: GradientBoostingRegressor()  30960.1191

    # GradientBoostingRegressor() is the best model


def print_feature_importances(column_keys, model):
    print('Feature importances:')
    feature_importances = model.feature_importances_
    for i in range(len(feature_importances)):
        print('\t', round(feature_importances[i], 3), column_keys[i])
