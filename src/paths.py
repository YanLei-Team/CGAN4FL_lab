from pathlib import Path


class Paths:
    LabRoot = Path(__file__).parent.parent

    DatasetRoot = LabRoot / "data"

    @classmethod
    def get_dataset_dir(cls, dataset_name: str):
        return cls.DatasetRoot / dataset_name

    @classmethod
    def get_program_data_dir(cls, dataset_name: str, program_name: str):
        return cls.DatasetRoot / dataset_name / "data" / program_name

    @classmethod
    def get_program_rank_dir(cls, dataset_name: str, program_name: str):
        return cls.DatasetRoot / dataset_name / "rank" / program_name

    @classmethod
    def get_version_dir(cls, dataset_name: str, program_name: str, version_name: str):
        return cls.DatasetRoot / dataset_name / "data" / program_name / version_name / "gzoltars" / program_name / version_name
