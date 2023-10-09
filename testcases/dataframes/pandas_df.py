import python_utils.common_utils as cu


class PandasDF:
    def __init__(self):
        # Storage directories
        self.csv_path = "../datasets/scraped_data.csv"
        self.xlsx_path = "../datasets/scraped_data.xlsx"
        self.parquet_path = "../datasets/scraped_data.parquet"

    def pandas_df(self):
        # Load data from a CSV file and assign it to 'df_csv'
        df_csv = cu.load_df('csv', self.csv_path)

        # Save 'df_csv' as an Excel file
        cu.save_df(df_csv, 'xlsx', self.xlsx_path)

        # Load data from the Excel file and assign it to 'df_xlsx'
        df_xlsx = cu.load_df('xlsx', self.xlsx_path)

        # Save 'df_xlsx' as a Parquet file
        cu.save_df(df_xlsx, 'parquet', self.parquet_path)

        # Load data from the Parquet file and assign it to 'df_parquet'
        df_parquet = cu.load_df('parquet', self.parquet_path)

        # Display the first 5 rows of 'df_parquet'
        cu.display_df(df_parquet, 5)


if __name__ == "__main__":
    main = PandasDF()
    main.pandas_df()
