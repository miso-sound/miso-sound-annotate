import pathlib
import os
import pandas as pd
import re

if __name__ == "__main__":
    
    code_paths = {}
    code_paths["repo_name"] = "miso-sound-annotate"
    
    code_paths["repo_path"] = os.getcwd()
    base_dir = os.path.basename(code_paths["repo_path"])
    while base_dir != code_paths["repo_name"]:
        code_paths["repo_path"] = os.path.dirname(
            os.path.abspath(code_paths["repo_path"]))
        base_dir = os.path.basename(code_paths["repo_path"])
    
    package_dir = code_paths["repo_path"]
    
    label_dir = pathlib.Path(package_dir, "labels")
    label_file_paths = list(pathlib.Path(label_dir).glob("*.txt"))
    
    all_records = []
    for p in label_file_paths:
        anno_df = pd.read_table(p, header=None)
        label_names = anno_df.iloc[:,2]
        anno_df.columns = ["Start", "Stop", "Label"]
        anno_df["Duration"] = anno_df["Stop"] - anno_df["Start"]
        anno_df["File"] = pathlib.Path(p).stem.split("_labels")[0]
        anno_df["Salience"] = [label.split("C")[1].split("-")[0] for label in anno_df["Label"].values]
        anno_df["Label"] = [label.split("-")[1] for label in anno_df["Label"].values]
        records = anno_df.to_dict("records")
        all_records.extend(records)
        
    label_timing_df = pd.DataFrame(all_records)
    
    summary_dfs = []
    summary_dfs.append(
        label_timing_df.groupby(["Label"])
        .sum()
        .loc[:, ["Duration"]]
        .rename(columns={"Duration": "Total duration"})
    )
    summary_dfs.append(
        label_timing_df.groupby(["Label"])
        .mean()
        .loc[:, ["Duration"]]
        .rename(columns={"Duration": "Mean duration"})
    )
    summary_dfs.append(
        label_timing_df.groupby(["Label"])
        .count()
        .loc[:, ["Duration"]]
        .rename(columns={"Duration": "Count of label instances"})
    )
    summary_dfs.append(
        label_timing_df.drop_duplicates(subset=["Label", "File"])
        .groupby(["Label"])
        .count()
        .loc[:, ["Duration"]]
        .rename(columns={"Duration": "Count of files with label"})
    )
    summary_df = pd.concat(summary_dfs, axis=1).sort_values(by=["Count of files with label"], ascending=False)
    summary_table = summary_df.reset_index().to_markdown()
    
    with open(pathlib.Path(package_dir,"README.md")) as f:
        old_readme = f.read()
    
    start_str ="start_sync_summary_table"
    stop_str = "stop_sync_summary_table"
    end_comment_str = "\n-->\n"
    start_comment_str = "\n<!---\n"
    result = re.findall(r"" + start_str + "(.*?)" + stop_str, old_readme, re.DOTALL|re.MULTILINE)[0]
    old_replace_content = start_str + result + stop_str
    new_replace_content = start_str + end_comment_str + summary_table + start_comment_str + stop_str
    new_readme = old_readme.replace(old_replace_content, new_replace_content)
    
    with open(pathlib.Path(package_dir,"README.md"), "w") as f:
        f.write(new_readme)