from constants import (LAND_CONTOUR_TYPES, EXTER_QUAL_TYPES, HEATING_TYPES,
                       CONDITION_2_TYPES, KITCHEN_QUAL_TYPES,
                       CENTRAL_AIR_TYPES, BSMT_QUAL_TYPES)
from pandas import read_csv

train_file = read_csv('data/train.csv')
train_data = train_file.values.tolist()

