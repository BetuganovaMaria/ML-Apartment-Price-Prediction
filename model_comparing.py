from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
import numpy as np


def compare_models(x_train, y_train):
    models = [LinearRegression(),
              DecisionTreeRegressor(),
              RandomForestRegressor(),
              GradientBoostingRegressor(),
              CatBoostRegressor(verbose=False),
              XGBRegressor(objective='reg:squarederror'),
              ]
    model_names = ['LinearRegression',
                   'DecisionTreeRegressor',
                   'RandomForestRegressor',
                   'GradientBoostingRegressor',
                   'CatBoostRegressor',
                   'XGBRegressor'
                   ]
    for i in range(len(models)):
        model = models[i]
        model_name = model_names[i]
        rmse = np.mean(np.sqrt(-cross_val_score(model, x_train, y_train.values.ravel(), cv=5, scoring="neg_mean_squared_error")))
        print(f"MSE: {model_name}  {round(rmse, 4)}")

    # result:
    # >> MSE: LinearRegression  36492.6932
    # >> MSE: DecisionTreeRegressor  43780.7469
    # >> MSE: RandomForestRegressor  31252.2144
    # >> MSE: GradientBoostingRegressor  31285.3437
    # >> MSE: CatBoostRegressor  30275.6273
    # >> MSE: MSE: XGBRegressor  31789.3788

    # CatBoostRegressor is the best model


def print_feature_importances(column_keys, model):
    print('Feature importances:')
    feature_importances = model.feature_importances_
    for i in range(len(feature_importances)):
        print('\t', round(feature_importances[i], 3), column_keys[i])
