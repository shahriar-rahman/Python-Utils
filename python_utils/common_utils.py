import pandas as pd
import bs4
from bs4 import BeautifulSoup


class GenericUtils:
    def __init__(self):
        pass

    @staticmethod
    def create_df(key_dict: dict):
        try:
            # Create a new DataFrame from the provided dictionary using pandas
            df = pd.DataFrame().from_dict(key_dict)
            return df  # Return the created DataFrame

        except Exception as e:
            # Handle exceptions and print an error message if one occurs
            print(f"An error occurred while creating the DataFrame: {e}")
            return None  # Return None in case of an error

    @staticmethod
    def save_df(df: pd.core.frame.DataFrame, path: str):
        try:
            # Save the DataFrame to the specified path
            df.to_csv(path, index=False)

        except Exception as e:
            # Handle exceptions and print an error message if one occurs
            print(f"An error occurred while saving the DataFrame: {e}")

    @staticmethod
    def display_df(df: pd.core.frame.DataFrame, contents: int):
        try:
            # Display the DataFrame with better redability
            print(df.head(contents).to_string())

        except Exception as e:
            # Handle exceptions and print an error message if one occurs
            print(f"An error occurred while loading the DataFrame: {e}")


if __name__ == "__main__":
    main = GenericUtils()
