import os
import gdown

URLS = {
    "tokyo_xs": "https://drive.google.com/file/d/15QB3VNKj93027UAQWv7pzFQO1JDCdZj2/view?usp=share_link",
    "sf_xs": "https://drive.google.com/file/d/1tQqEyt3go3vMh4fj_LZrRcahoTbzzH-y/view?usp=share_link",
    "gsv_xs": "https://drive.google.com/file/d/1q7usSe9_5xV5zTfN-1In4DlmF5ReyU_A/view?usp=share_link",
    "svox": "https://drive.google.com/file/d/16iuk8voW65GaywNUQlWAbDt6HZzAJ_t9/view?usp=drive_link"
}

ZIP_DIR = "data_zip"
os.makedirs(ZIP_DIR, exist_ok=True)

for dataset_name, url in URLS.items():
    zip_filepath = os.path.join(ZIP_DIR, f"{dataset_name}.zip")

    if os.path.exists(zip_filepath):
        print(f"{dataset_name}.zip already exists, skipping.")
        continue

    print(f"Downloading {dataset_name}...")
    gdown.download(url, zip_filepath, fuzzy=True, quiet=False)
    print(f"Downloaded {dataset_name} to {zip_filepath}")