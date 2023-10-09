import python_utils.common_utils as cu

import polars as pl
import pandas as pd


class PolarsDF:
    def __init__(self):
        # Storage directories
        self.csv_path = "../datasets/scraped_data.csv"
        self.xlsx_path = "../datasets/scraped_data.xlsx"
        self.parquet_path = "../datasets/scraped_data.parquet"

    def polars_df(self):
        df_test = cu.create_df({'col_1': [1, 2, 4, 6]}, 'pl')
        print(df_test)

        # Load data from a CSV file and assign it to 'df_csv'
        df_csv = cu.load_df('csv', 'pl', self.csv_path)

        # Save 'df_csv' as an Excel file
        cu.save_df(df_csv, 'xlsx', self.xlsx_path)

        # Load data from the Excel file and assign it to 'df_xlsx'
        df_xlsx = cu.load_df('xlsx', 'pl', self.xlsx_path)

        # Save 'df_xlsx' as a Parquet file
        cu.save_df(df_xlsx, 'parquet', self.parquet_path)

        # Load data from the Parquet file and assign it to 'df_parquet'
        df_parquet = cu.load_df('parquet', 'pl', self.parquet_path)

        # Display the first 5 rows of 'df_parquet'
        cu.display_df(df_parquet, 5)


if __name__ == "__main__":
    main = PolarsDF()
    main.polars_df()
