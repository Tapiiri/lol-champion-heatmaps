import sqlite3
import pandas as pd

def load_and_combine_tlol_db(db_paths):
    """
    Load TLoL databases combine them into a single list.

    Args:
        db_paths (list): List of strings, where each string is a path to a TLoL DB.

    Returns:
        list: Combined list of centerpoints from all database files.
    """

    combined_data = []

    # Iterate over the file paths
    for game_path in db_paths:
        con = sqlite3.connect(game_path)
        champs_sql = pd.read_sql_query("SELECT * FROM champs", con)
        champs_df  = pd.DataFrame(champs_sql)
        champs_df  = champs_df.drop(labels=["game_id"], axis=1)
        champs_df  = champs_df[champs_df["time"] > 5.0]
        champs_df = champs_df.drop_duplicates(subset=["time", "name"])

        game_id = game_path.split("\\")[-1].split(".")[0]
        champs_df["game_id"] = game_id
        combined_data.append(champs_df)
        con.close()
        
    return pd.concat(combined_data)


