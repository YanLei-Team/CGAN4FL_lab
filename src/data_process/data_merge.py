import pandas as pd


def d_merge(version_dir):
    first = pd.read_csv(version_dir / "matrix.csv")
    second = pd.read_csv(version_dir / "matrix_gen.csv")
    big_df = pd.merge(first, second, how='outer')
    big_df.to_csv(version_dir / "matrix_merge.csv", index=False)


if __name__ == "__main__":
    d_merge()
