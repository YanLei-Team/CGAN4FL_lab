import globalvar as gl
from pathlib import Path

gl._init()

lab_root = Path(__file__).parent.parent

data_path = lab_root / "data"
raw_data_path = data_path / "raw"
rank_data_path = data_path / "rank"

gl.set_value('path', str(raw_data_path / "Chart"))
gl.set_value('path_raw', str(raw_data_path / "Chart"))
gl.set_value('save_r_path', str(rank_data_path / "Chart"))
