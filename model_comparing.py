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
    print('MSE:')
    for i in range(len(models)):
        model = models[i]
        model_name = model_names[i]
        rmse = np.mean(np.sqrt(-cross_val_score(model, x_train, y_train.values.ravel(),
                                                cv=5, scoring="neg_mean_squared_error")))
        print('\t', model_name, round(rmse, 4))

    # result:
    # >> LinearRegression  36492.6932
    # >> DecisionTreeRegressor  43780.7469
    # >> RandomForestRegressor  31252.2144
    # >> GradientBoostingRegressor  31285.3437
    # >> CatBoostRegressor  30275.6273
    # >> XGBRegressor  31789.3788

    # CatBoostRegressor is the best model


def print_feature_importances(column_keys, model):
    print('Feature importances:')
    feature_importances = model.feature_importances_
    for i in range(len(feature_importances)):
        print('\t', round(feature_importances[i], 3), column_keys[i])

    # result:
    # >> 1.832 LandContour
    # >> 3.826 GarageYrBlt
    # >> 4.336 FullBath
    # >> 9.033 BsmtFinSF1
    # >> 6.325 TotRmsAbvGrd
    # >> 2.576 ExterQual
    # >> 4.266 OpenPorchSF
    # >> 0.071 Heating
    # >> 0.341 Condition2
    # >> 21.776 OverallQual
    # >> 7.641 GarageCars
    # >> 4.928 KitchenQual
    # >> 0.749 KitchenAbvGr
    # >> 8.67 2ndFlrSF
    # >> 1.161 CentralAir
    # >> 2.605 BsmtQual
    # >> 14.639 TotalBsmtSF
    # >> 5.223 Fireplaces
