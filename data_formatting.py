from constants import *
from corr_operations import check_corr_emptiness, check_corr_coefficients
from pandas import read_csv

# train.csv
# test_with_results.csv


def format_file(filename):
    dataset = read_csv(f'data/{filename}')

    dataset = format_data_types(dataset)

    corr_coefficients = dataset.corr()
    check_corr_emptiness(corr_coefficients)
    check_corr_coefficients(corr_coefficients)

    corr_fields = [GR_LIV_AREA_KEY, FIRST_FLR_SF_KEY]  # for deleting one of two dependent values
    new_dataset = dataset.drop(corr_fields, axis=1)

    create_formatted_file(new_dataset, f'formatted_{filename}')


def format_data_types(df):
    # filling empty fields
    for column in [LAND_CONTOUR_KEY, GARAGE_YR_BLT_KEY, FULL_BATH_KEY, TOT_RMS_ABV_GRD_KEY,
                   EXTER_QUAL_KEY, HEATING_KEY, CONDITION_2_KEY, GARAGE_CARS_KEY, KITCHEN_ABV_GR_KEY,
                   OVERALL_QUAL_KEY, KITCHEN_QUAL_KEY, CENTRAL_AIR_KEY, BSMT_QUAL_KEY, FIREPLACES_KEY]:
        df.loc[:, column] = df[column].fillna(df[column].mode()[0])

    for column in [FIRST_FLR_SF_KEY, BSMT_FIN_SF_1_KEY, OPEN_PORCH_SF_KEY,
                   GR_LIV_AREA_KEY, SECOND_FLR_SF_KEY, TOTAL_BSMT_SF_KEY]:
        df.loc[:, column] = df[column].fillna(df[column].mean())

    # data types processing
    df.loc[:, LAND_CONTOUR_KEY] = df[LAND_CONTOUR_KEY].map(LAND_CONTOUR_TYPES)
    df.loc[:, EXTER_QUAL_KEY] = df[EXTER_QUAL_KEY].map(EXTER_QUAL_TYPES)
    df.loc[:, HEATING_KEY] = df[HEATING_KEY].map(HEATING_TYPES)
    df.loc[:, CONDITION_2_KEY] = df[CONDITION_2_KEY].map(CONDITION_2_TYPES)
    df.loc[:, KITCHEN_QUAL_KEY] = df[KITCHEN_QUAL_KEY].map(KITCHEN_QUAL_TYPES)
    df.loc[:, CENTRAL_AIR_KEY] = df[CENTRAL_AIR_KEY].map(CENTRAL_AIR_TYPES)
    df.loc[:, BSMT_QUAL_KEY] = df[BSMT_QUAL_KEY].map(BSMT_QUAL_TYPES)

    return df


def create_formatted_file(df, filename):
    df.to_csv(f'formatted_data/{filename}', index=False, encoding='utf-8')


def create_result_file(df):
    df.to_csv(f'result/result.csv', index=False, encoding='utf-8')
