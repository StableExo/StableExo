import os
# It seems the `kaggle` package is the standard for datasets, while `kagglehub` is more for models.
# I'll use the `kaggle` library. It might have been installed as a dependency of kagglehub.
# If not, the error will tell me.

print("Attempting to download dataset from Kaggle...")

try:
    from kaggle.api.kaggle_api_extended import KaggleApi

    # Instantiate the API
    api = KaggleApi()

    # This will look for the kaggle.json file in ~/.kaggle/ or environment variables
    api.authenticate()

    dataset = 'ankurzing/sentiment-analysis-for-financial-news'
    download_path = 'data/raw/nlp'

    print(f"Downloading dataset '{dataset}' to '{download_path}'...")

    api.dataset_download_files(dataset, path=download_path, unzip=True)

    print("Dataset downloaded and unzipped successfully.")

    # Verify by listing the files in the directory
    downloaded_files = os.listdir(download_path)
    print(f"Files in '{download_path}': {downloaded_files}")
    if not downloaded_files:
        print("Warning: The download directory is empty.")

except Exception as e:
    print(f"An error occurred during the download process: {e}")
    print("\nThis is likely because the Kaggle API requires authentication.")
    print("To fix this, a `kaggle.json` API token file must be present at `~/.kaggle/kaggle.json`.")
    print("Since I cannot handle API keys myself, I am blocked on this step.")
    print("Please provide an alternative public URL for the dataset, or another way to access the data.")
