import numpy as np

def calculate(list):
    if len(list) != 9:
        #Exception
        raise ValueError("List must contain nine numbers.")
  
    #Values for matrix
    ls_matrix = np.array(list)
    
    mean_rows = [ls_matrix[[0,1,2]].mean(), ls_matrix[[3,4,5]].mean(), ls_matrix[[6,7,8]].mean()]
    mean_columns = [ls_matrix[[0,3,6]].mean(), ls_matrix[[1,4,7]].mean(), ls_matrix[[2,5,8]].mean()]

    var_rows = [ls_matrix[[0,1,2]].var(), ls_matrix[[3,4,5]].var(), ls_matrix[[6,7,8]].var()]
    var_columns = [ls_matrix[[0,3,6]].var(), ls_matrix[[1,4,7]].var(), ls_matrix[[2,5,8]].var()]

    std_rows = [ls_matrix[[0,1,2]].std(), ls_matrix[[3,4,5]].std(), ls_matrix[[6,7,8]].std()]
    std_columns = [ls_matrix[[0,3,6]].std(), ls_matrix[[1,4,7]].std(), ls_matrix[[2,5,8]].std()]

    max_rows = [ls_matrix[[0,1,2]].max(), ls_matrix[[3,4,5]].max(), ls_matrix[[6,7,8]].max()]
    max_columns = [ls_matrix[[0,3,6]].max(), ls_matrix[[1,4,7]].max(), ls_matrix[[2,5,8]].max()]

    min_rows = [ls_matrix[[0,1,2]].min(), ls_matrix[[3,4,5]].min(), ls_matrix[[6,7,8]].min()]
    min_columns = [ls_matrix[[0,3,6]].min(), ls_matrix[[1,4,7]].min(), ls_matrix[[2,5,8]].min()]

    sum_rows = [ls_matrix[[0,1,2]].sum(), ls_matrix[[3,4,5]].sum(), ls_matrix[[6,7,8]].sum()]
    sum_columns = [ls_matrix[[0,3,6]].sum(), ls_matrix[[1,4,7]].sum(), ls_matrix[[2,5,8]].sum()]

    #Dictionary
    calculations = {'mean': [mean_columns, mean_rows, ls_matrix.mean()], 
                    'variance': [var_columns, var_rows, ls_matrix.var()], 
                    'standard deviation': [std_columns, std_rows, ls_matrix.std()], 
                    'max': [max_columns, max_rows, ls_matrix.max()], 
                    'min': [min_columns, min_rows, ls_matrix.min()], 
                    'sum': [sum_columns, sum_rows, ls_matrix.sum()] } 

    return  calculations