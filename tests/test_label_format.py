import os
import pandas as pd
import pathlib
import requests

from github import Github
from json_tricks import loads, load
from urllib.parse import urlparse
from warnings import warn


def get_secrets(local_secrets_path=None):
    if local_secrets_path is None:
        local_secrets_path = os.path.join("local_secrets", "secrets.json")
    if os.path.isfile(local_secrets_path):
        with open(local_secrets_path, "r") as json_file:
            secrets = load(json_file)
    else:
        secrets = os.environ
    return secrets


def github_authentication(secrets=os.environ):
    access_token = secrets["ACCESS_TOKEN_GITHUB"]
    return Github(access_token)


def test_label_format(label_dir, taxonomy_terms=None):
    
    label_info_df_path = pathlib.Path(label_dir, "label_info.csv")
    label_info_df = pd.read_csv(label_info_df_path)
    files_ignore_for_now = ["[freesoundID]_label.txt", "full_taxonomy_labels.txt"]
    label_files = [f for f in label_info_df["label_file"].values if f not in files_ignore_for_now]
    label_file_paths = [pathlib.Path(label_dir, f) for f in label_files]
    
    for p in label_file_paths:
        check_label_name_format(p, taxonomy_terms=taxonomy_terms)

def check_label_name_format(p, taxonomy_terms=None):
    anno_df = pd.read_table(p, header=None)
    label_names = anno_df.iloc[:,2]
    for label_name in label_names:
        assert label_name.split("-")[0] in ["C1", "C2"], str(p) + ": The part of the label before `-` should be C1 or C2, not " + label_name.split("-")[0]    
        if taxonomy_terms is not None:
            assert label_name.split("-")[1] in taxonomy_terms, str(p) + ": The part of the label after `-` should be in the taxonomy terms: " + label_name.split("-")[1]

if __name__ == "__main__":
    
    repo_is_public = True
    check_older_taxonomy_urls = False
    
    package_dir = pathlib.Path(__file__).parent.parent.absolute()
    label_dir = pathlib.Path(package_dir, "labels")
    
    if repo_is_public:
        public_taxonomy_url = "https://raw.githubusercontent.com/miso-sound/miso-sound-taxonomy/main/terms/taxonomy_for_annotations.json"
        decoded_content = requests.get(public_taxonomy_url).text
    else:
        local_secrets_path = pathlib.Path(package_dir, "local_secrets", "secrets.json")
        secrets = get_secrets(local_secrets_path=local_secrets_path)
        g = github_authentication(secrets=secrets)
        repo = g.get_repo("miso-sound/miso-sound-taxonomy")
        decoded_content = repo.get_contents("terms/taxonomy_for_annotations.json").decoded_content.decode()
    newest_taxonomy = loads(decoded_content)
   
    label_info_df_path = pathlib.Path(label_dir, "label_info.csv")
    label_info_df = pd.read_csv(label_info_df_path)
    files_ignore_for_now = ["[freesoundID]_label.txt", "full_taxonomy_labels.txt"]
    label_files = [f for f in label_info_df["label_file"].values if f not in files_ignore_for_now]
    label_info_recs = label_info_df.to_dict("records")
    
    taxonomy_terms = list(newest_taxonomy.keys())
    test_label_format(label_dir=label_dir, taxonomy_terms=taxonomy_terms)
    
    if check_older_taxonomy_urls:
        for rec in label_info_recs:
            if rec["label_file"] in label_files:
                parsed_url = urlparse(rec["taxonomy"])
                repo_path = parsed_url[2].split("/blob/")[0][1:]
                repo = g.get_repo(repo_path)
                sha = parsed_url[2].split("/blob/")[1].split("/")[0]
                path_to_content_file = parsed_url[2].split("/blob/")[1].split(sha + "/")[1]
                decoded_content = repo.get_contents(path_to_content_file, ref=sha).decoded_content.decode()
                try:
                    taxonomy_version = loads(decoded_content)
                except:
                    warn(rec["taxonomy"] + " is not in a valid JSON format. Please update the taxonomy file in the label_info spreadsheet.")
