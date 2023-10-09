import extension as extension
import pandas as pd
import polars as pl
import bs4
from bs4 import BeautifulSoup


def create_df(key_dict: dict, library: str):
    try:
        if library == 'pd':
            # Create a new DataFrame from the provided dictionary using pandas
            df = pd.DataFrame().from_dict(key_dict)
            return df  # Return the created DataFrame
        elif library == 'pl':
            df = pl.DataFrame(key_dict)
            return df  # Return the created DataFrame

    except Exception as e:
        # Handle exceptions and print an error message if one occurs
        print(f"An error occurred while creating the DataFrame: {e}")
        return None  # Return None in case of an error


def save_df(df: pd.core.frame.DataFrame | pl.dataframe.frame.DataFrame, ext_type: str, path: str):
    if isinstance(df, pl.dataframe.frame.DataFrame):
        df = df.to_pandas()

    # Define a mapping of file extensions to corresponding DataFrame export functions.
    extension_mapping = {
        'csv': df.to_csv,  # Map 'csv' extension to DataFrame's to_csv method.
        'xlsx': df.to_excel,  # Map 'xlsx' extension to DataFrame's to_excel method.
        'parquet': df.to_parquet  # Map 'parquet' extension to DataFrame's to_parquet method.
    }

    try:
        # Save the DataFrame to the specified path
        extension_mapping[ext_type](path, index=False)

    except Exception as e:
        # Handle exceptions and print an error message if one occurs
        print(f"An error occurred while saving the DataFrame: {e}")


def display_df(df: pd.core.frame.DataFrame | pl.dataframe.frame.DataFrame, contents: int):
    if isinstance(df, pl.dataframe.frame.DataFrame):
        df = df.to_pandas()

    try:
        # Display the DataFrame with better readability
        print(df.head(contents).to_string())

    except Exception as e:
        # Handle exceptions and print an error message if one occurs
        print(f"An error occurred while loading the DataFrame: {e}")


def load_df(ext_type: str, library: str, path: str, d_type: extension = False):
    # Define a dictionary that maps file extensions to corresponding read functions
    extension_mapping = {
        'csv': {
            'pd': pd.read_csv,
            'pl': pl.read_csv
        },
        'xlsx': {
            'pd': pd.read_excel,
            'pl': pl.read_excel
        },
        'parquet': {
            'pd': pd.read_parquet,
            'pl': pl.read_parquet
        }
    }

    if d_type:
        # If a d_type is specified, use it when reading the file
        return extension_mapping[ext_type][library](path, dtype=d_type)
    else:
        # If no d_type is specified, read the file without it
        return extension_mapping[ext_type][library](path)

