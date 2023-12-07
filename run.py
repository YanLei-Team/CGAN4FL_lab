import os
import numpy as np
import pandas as pd
from data_process import data_merge, testcase_aug

from calculate_suspiciousness import rank
from calculate_suspiciousness import contrast_l
import globalvar as gl
from data_process.data_undersampling.undersampling import UndersamplingData
from read_data.Defects4JDataLoader import Defects4JDataLoader
file_name = gl.get_value('file_name')
path = gl.get_value('path')
path_raw = gl.get_value('path_raw')

class Pipeline:
    def __init__(self, project_dir,program,bug_id):
        self.project_dir = project_dir
        self.program = program
        self.bug_id = bug_id
        self.dataloader = self._choose_dataloader_obj()
        self.column_raw = self._choose_dataloader_obj().column_raw
    def run(self):
        self._run_task()
        return self.df,self.column_raw
    def _dynamic_choose(self, loader):
        self.dataset_dir =self.project_dir
        data_obj = loader(self.dataset_dir, self.program, self.bug_id)
        data_obj.load()
        return data_obj

    def _choose_dataloader_obj(self):
        return self._dynamic_choose(Defects4JDataLoader)
    def _run_task(self):
        self.data_obj = UndersamplingData(self.dataloader)
        self.df=self.data_obj.process()
def undersam():
    file_name_list = np.array(os.listdir(path))
    for file_name in file_name_list:
        project_dir = '/home/Documents/'
        program = 'Chart'
        pl = Pipeline(project_dir,program,file_name)
        df,column_raw = pl.run()
        column_raw.append('error')
        df.columns=column_raw
        df.to_csv(project_dir+"d4j/data/"+program+"/"+str(file_name)+"/gzoltars/"+program+"/"+str(file_name)+"/under_sam.csv",index=0)
        data = pd.read_csv(path_raw + str(file_name) + '/gzoltars/Chart/' + str(file_name) + "/under_sam.csv", index_col=0)
        rank_temporary1 = 'rank_ochiai1.csv'
        rank_temporary2 = 'rank_dstar1.csv'
        rank_temporary3 = 'rank_barinel1.csv'
        rank_temporary4 = 'rank_MLP1.csv'
        rank_temporary5 = 'rank_CNN1.csv'
        rank_temporary6 = 'rank_RNN1.csv'

        method1 = 'ochiai'
        method2 = 'dstar'
        method3 = 'barinel'
        method4 = 'MLP'
        method5 = 'CNN'
        method6 = 'RNN'
        rank_final_method1 = 'rank_ochiai.csv'
        rank_final_method2 = 'rank_dstar.csv'
        rank_final_method3 = 'rank_barinel.csv'
        rank_final_method4 = 'rank_MLP.csv'
        rank_final_method5 = 'rank_CNN.csv'
        rank_final_method6 = 'rank_RNN.csv'
        rank.rank(data, method1, file_name, rank_temporary1)
        rank.rank(data, method2, file_name, rank_temporary2)
        rank.rank(data, method3, file_name, rank_temporary3)
        rank.rank(data, method4, file_name, rank_temporary4)
        rank.rank(data, method5, file_name, rank_temporary5)
        rank.rank(data, method6, file_name, rank_temporary6)
        contrast_l.contrast_line(file_name, rank_temporary1, rank_final_method1)
        contrast_l.contrast_line(file_name, rank_temporary2, rank_final_method2)
        contrast_l.contrast_line(file_name, rank_temporary3, rank_final_method3)
        contrast_l.contrast_line(file_name, rank_temporary4, rank_final_method4)
        contrast_l.contrast_line(file_name, rank_temporary6, rank_final_method6)
        contrast_l.contrast_line(file_name, rank_temporary5, rank_final_method5)
def cal():
    file_name_list = np.array(os.listdir(path))
    for file_name in file_name_list:
        testcase_aug.main(file_name)
        data_merge.d_merge(file_name)
        data = pd.read_csv(path_raw + str(file_name) + "/matrix.csv", index_col=0) 
        rank_temporary1 = 'rank_ochiai1.csv'
        rank_temporary2 = 'rank_dstar1.csv'
        rank_temporary3 = 'rank_barinel1.csv'
        rank_temporary4 = 'rank_MLP1.csv'
        rank_temporary5 = 'rank_CNN1.csv'
        rank_temporary6 = 'rank_RNN1.csv'

        method1 = 'ochiai'
        method2 = 'dstar'
        method3 = 'barinel'
        method4 = 'MLP'
        method5 = 'CNN'
        method6 = 'RNN'
        rank_final_method1 = 'rank_ochiai.csv'
        rank_final_method2 = 'rank_dstar.csv'
        rank_final_method3 = 'rank_barinel.csv'
        rank_final_method4 = 'rank_MLP.csv'
        rank_final_method5 = 'rank_CNN.csv'
        rank_final_method6 = 'rank_RNN.csv'
        rank.rank(data, method1, file_name, rank_temporary1)
        rank.rank(data, method2, file_name, rank_temporary2)
        rank.rank(data, method3, file_name, rank_temporary3)
        rank.rank(data, method4, file_name, rank_temporary4)
        rank.rank(data, method5, file_name, rank_temporary5)
        rank.rank(data, method6, file_name, rank_temporary6)
        contrast_l.contrast_line(file_name, rank_temporary1, rank_final_method1)
        contrast_l.contrast_line(file_name, rank_temporary2, rank_final_method2)
        contrast_l.contrast_line(file_name, rank_temporary3, rank_final_method3)
        contrast_l.contrast_line(file_name, rank_temporary4, rank_final_method4)
        contrast_l.contrast_line(file_name, rank_temporary6, rank_final_method6)
        contrast_l.contrast_line(file_name, rank_temporary5, rank_final_method5)

if __name__ == '__main__':
   undersam()
   cal()
