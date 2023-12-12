import os
import pandas as pd
from data_process import data_merge, testcase_aug
from calculate_suspiciousness import rank
from calculate_suspiciousness import contrast_l
from data_process.data_undersampling.undersampling import UndersamplingData
from read_data.Defects4JDataLoader import Defects4JDataLoader
from paths import Paths


class Pipeline:
    def __init__(self, project_dir, program, bug_id):
        self.project_dir = project_dir
        self.program = program
        self.bug_id = bug_id
        self.dataloader = self._choose_dataloader_obj()
        self.column_raw = self._choose_dataloader_obj().column_raw

    def run(self):
        self._run_task()
        return self.df, self.column_raw

    def _dynamic_choose(self, loader):
        self.dataset_dir = self.project_dir
        data_obj = loader(self.dataset_dir, self.program, self.bug_id)
        data_obj.load()
        return data_obj

    def _choose_dataloader_obj(self):
        return self._dynamic_choose(Defects4JDataLoader)

    def _run_task(self):
        self.data_obj = UndersamplingData(self.dataloader)
        self.df = self.data_obj.process()


def undersam(program, version, methods):
    project_dir = Paths.DatasetRoot
    version_dir = Paths.get_version_dir("d4j", program, version)
    pl = Pipeline(project_dir, program, version)
    df, column_raw = pl.run()
    column_raw.append('error')
    df.columns = column_raw
    under_sam_file_path = version_dir / "under_sam.csv"
    df.to_csv(under_sam_file_path, index=0)
    data = pd.read_csv(under_sam_file_path, index_col=0)
    for method in methods:
        rank_temporary = f"rank_{method}1.csv"
        rank_final_method = f"rank_{method}.csv"
        rank.rank(data, method, version_dir / rank_temporary)
        contrast_l.contrast_line(
            version_dir / rank_temporary,
            version_dir / rank_final_method,
            version_dir / "bugline.csv"
        )


def cal(program, version, methods):
    version_dir = Paths.get_version_dir("d4j", program, version)
    testcase_aug.main(program, version)
    data_merge.d_merge(version_dir)
    data = pd.read_csv(version_dir / "matrix.csv", index_col=0)
    for method in methods:
        rank_temporary = f"rank_{method}1.csv"
        rank_final_method = f"rank_{method}.csv"
        rank.rank(data, method, version_dir / rank_temporary)
        contrast_l.contrast_line(
            version_dir / rank_temporary,
            version_dir / rank_final_method,
            version_dir / "bugline.csv",
        )


def main():
    program = "Chart"
    program_data_path = Paths.get_program_data_dir("d4j", program)
    versions = os.listdir(program_data_path)
    methods = [
        'ochiai',
        'dstar',
        'barinel',
        'MLP',
        'CNN',
        'RNN',
    ]
    for version in versions:
        print(f"Processing buggy-version {version}")
        undersam(program, version, methods)
        cal(program, version, methods)


if __name__ == '__main__':
    main()
