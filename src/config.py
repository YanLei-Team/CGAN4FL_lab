import globalvar as gl
from paths import Paths

gl._init()

gl.set_value('path', str(Paths.get_program_data_dir("d4j", "Chart")))
gl.set_value('path_raw', str(Paths.get_program_data_dir("d4j", "Chart")))
gl.set_value('save_r_path', str(Paths.get_program_rank_dir("d4j", "Chart")))
