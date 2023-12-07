import os
import numpy as np
import pandas as pd
import globalvar as gl
import config
path = gl.get_value('path')
path_raw = gl.get_value('path_raw')
method = gl.get_value('method')
def contrast_line(file_name,rank_temporary,rank_final_method):
    if os.path.getsize(path + str(file_name)  + '/'+rank_temporary) > 0:
        df1 = pd.read_csv(path+str(file_name) +'/bugline.csv',names=['line'])
        df2 = pd.read_csv(path + str(file_name)  + '/'+rank_temporary,index_col=None,header=0)
        list1 = df1['line'].tolist()
        array1 = np.array(df2)
        list2 = array1.tolist()
        list3 = []
        for j in range(len(list2)):
            for i in range(len(list1)):
                if list1[i]==list2[j][2]:
                    list3.append(list2[j])
        names = ['rank', 'rate', 'line']
        test = pd.DataFrame(columns=names,data=list3)
        test.to_csv(path + str(file_name) + '/'+rank_final_method,index=0)
        df = pd.read_csv(path + str(file_name) + '/' + rank_final_method, index_col=None)
        cols = ['rate']
        df = pd.merge(
            df.groupby('line', as_index=False)[cols].max(),
            df,
            how='left'
        ).drop_duplicates(subset=['line','rate'], keep='first')
        df=df[['rank','rate','line']]
        df.to_csv(path + str(file_name) + '/' + rank_final_method, index=0)
if __name__ == "__main__":
    contrast_line()
