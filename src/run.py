import os
import numpy as np
import pandas as pd
from data_process import data_merge, testcase_aug
from calculate_suspiciousness import rank
from calculate_suspiciousness import contrast_l
import globalvar as gl
from data_process.data_undersampling.undersampling import UndersamplingData
from read_data.Defects4JDataLoader import Defects4JDataLoader
from paths import Paths

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
        project_dir = Paths.DatasetRoot
        program = 'Chart'
        version_dir = Paths.get_version_dir("d4j", program, file_name)
        pl = Pipeline(project_dir,program,file_name)
        df,column_raw = pl.run()
        column_raw.append('error')
        df.columns=column_raw
        under_sam_file_path = version_dir / "under_sam.csv"
        df.to_csv(under_sam_file_path, index=0)
        data = pd.read_csv(under_sam_file_path, index_col=0)
        rank_temporaries = [
            'rank_ochiai1.csv',
            'rank_dstar1.csv',
            'rank_barinel1.csv',
            'rank_MLP1.csv',
            'rank_CNN1.csv',
            'rank_RNN1.csv',
        ]
        methods = [
            'ochiai',
            'dstar',
            'barinel',
            'MLP',
            'CNN',
            'RNN',
        ]
        rank_final_methods = [
            'rank_ochiai.csv',
            'rank_dstar.csv',
            'rank_barinel.csv',
            'rank_MLP.csv',
            'rank_CNN.csv',
            'rank_RNN.csv',
        ]
        for i in range(6):
            rank.rank(data, methods[i], version_dir / rank_temporaries[i])
            contrast_l.contrast_line(
                version_dir / rank_temporaries[i],
                version_dir / rank_final_methods[i],
                version_dir / "bugline.csv"
            )


def cal():
    file_name_list = np.array(os.listdir(path))
    for file_name in file_name_list:
        version_dir = Paths.get_version_dir("d4j", "Chart", file_name)
        testcase_aug.main(file_name)
        data_merge.d_merge(file_name)
        data = pd.read_csv(version_dir / "matrix.csv", index_col=0)
        rank_temporaries = [
            'rank_ochiai1.csv',
            'rank_dstar1.csv',
            'rank_barinel1.csv',
            'rank_MLP1.csv',
            'rank_CNN1.csv',
            'rank_RNN1.csv',
        ]
        methods = [
            'ochiai',
            'dstar',
            'barinel',
            'MLP',
            'CNN',
            'RNN',
        ]
        rank_final_methods = [
            'rank_ochiai.csv',
            'rank_dstar.csv',
            'rank_barinel.csv',
            'rank_MLP.csv',
            'rank_CNN.csv',
            'rank_RNN.csv',
        ]
        for i in range(6):
            rank.rank(data, methods[i], version_dir / rank_temporaries[i])
            contrast_l.contrast_line(
                version_dir / rank_temporaries[i],
                version_dir / rank_final_methods[i],
                version_dir / "bugline.csv",
            )

if __name__ == '__main__':
   undersam()
   cal()
