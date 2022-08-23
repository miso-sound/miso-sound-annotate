import numpy as np
import pandas as pd
import pathlib

def test_label_format():
    package_dir = pathlib.Path(__file__).parent.parent.absolute()
    label_dir = pathlib.Path(package_dir, "labels")
    label_info_df_path = pathlib.Path(label_dir, "label_info.csv")
    label_info_df = pd.read_csv(label_info_df_path)
    files_ignore_for_now = ["[freesoundID]_label.txt", "full_taxonomy_labels.txt"]
    label_files = [f for f in label_info_df["label_file"].values if f not in files_ignore_for_now]
    label_file_paths = [pathlib.Path(label_dir, f) for f in label_files]
    
    for p in label_file_paths:
        anno_df = pd.read_table(p, header=None)
        label_names = anno_df.iloc[:,2]
        [check_label_name_format(name) for name in label_names]

def check_label_name_format(label_name):
    assert label_name.split("-")[0] in ["C1", "C2"], label_name + ": The part of the label before `-` should be C1 or C2, not " + label_name.split("-")[0]    

if __name__ == "__main__":
    out = test_label_format()