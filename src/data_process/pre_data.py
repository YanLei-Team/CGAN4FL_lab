import csv
import re

import chardet
import numpy as np
import pandas as pd
import os
import globalvar as gl
import config

path = gl.get_value('path')
path_raw = gl.get_value('path_raw')
def main():
    nums = np.array(os.listdir(path))
    for file_name in nums:
        df = pd.read_csv(path + str(file_name) + "/matrix.csv", index_col=0)
        df.to_csv(path + str(file_name) + "/matrix.csv", index=False)
        tag = df['error']
        df = df.drop(['error'], axis=1, inplace=False)
        df.replace(",", " ")
        df.to_csv(path + str(file_name) + "/matrix.txt", index=False, sep=' ', header=0)
        tag.to_csv(path + str(file_name) + "/error.txt", index=False, header=0)
def pre_raw():
    nums = np.array(os.listdir(path_raw))
    for file_name in nums:
        line_list = []
        file_path = path_raw + str(file_name) + '/gzoltars/Chart/' + str(file_name) + "/spectra"
        with open(file_path, 'r') as f:  #
            lines = f.readlines()
            for line in lines:
                left, right = line.split("#")
                line_list.append(re.findall('\d+', right)[0])
        line_list.append('error')

        data = []
        path = path_raw + str(file_name) + '/gzoltars/Chart/' + str(file_name) + "/matrix"
        with open(path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip("\n")
                line = line.split()
                if line[-1] == '+':
                    line[-1] = '0'
                if line[-1] == '-':
                    line[-1] = '1'
                data.append(line)
        test = pd.DataFrame(columns=line_list, data=data)
        test.to_csv(path_raw + str(file_name) + '/gzoltars/Chart/' + str(file_name) + "/matrix.csv", index=0)

if __name__ == '__main__':
    main()
    pre_raw()
