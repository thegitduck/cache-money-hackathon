from sqlite3 import connect
from helpers import get_proj_dir

DB = connect(f"{get_proj_dir()}/database.db")