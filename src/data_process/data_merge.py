
import pandas as pd
import globalvar as gl
import config

path = gl.get_value('path')
def d_merge(file_name):
    first = pd.read_csv(path + str(file_name) + "/matrix.csv")
    second =pd.read_csv(path + str(file_name) + "/matrix_gen.csv")
    big_df = pd.merge(first, second, how='outer')
    big_df.to_csv(path + str(file_name) + "/matrix_merge.csv",index=False)
if __name__ == "__main__":
    d_merge()