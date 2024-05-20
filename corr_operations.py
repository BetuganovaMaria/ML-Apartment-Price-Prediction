MAX_ACCEPTABLE_CORR = 0.8


def check_corr_emptiness(corr_coefficients):
    field_drop = [i for i in corr_coefficients if corr_coefficients[i].isnull().drop_duplicates().values[0]]
    print(field_drop)
    # result
    # >> []


def check_corr_coefficients(corr_coefficients):
    for column in corr_coefficients:
        for row in corr_coefficients.index[corr_coefficients[column] > MAX_ACCEPTABLE_CORR]:
            if column != row:
                print(column, " -> ", row, ": r^2 = ",
                      corr_coefficients[column][corr_coefficients.index == row].values[0])
    # result
    # >> 1stFlrSF  ->  TotalBsmtSF : r^2 =  0.8195299750050338
    # >> TotRmsAbvGrd  ->  GrLivArea : r^2 =  0.8254893743088426
    # >> GrLivArea  ->  TotRmsAbvGrd : r^2 =  0.8254893743088426
    # >> TotalBsmtSF  ->  1stFlrSF : r^2 =  0.8195299750050338
