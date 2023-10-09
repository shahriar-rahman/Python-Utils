import python_utils.common_utils as cu


class PandasDF:
    def __init__(self):
        self.csv_path = "../datasets/scraped_data.csv"
        self.xlsx_path = "../datasets/scraped_data.xlsx"

    def pandas_df(self):
        df_csv = cu.load_df('csv', self.csv_path)
        cu.display_df(df_csv, 5)
        cu.save_df(df_csv, 'xlsx', self.xlsx_path)

        df_xlsx = cu.load_df('xlsx', self.xlsx_path)
        cu.display_df(df_xlsx, 5)
        cu.save_df(df_xlsx, 'csv', self.csv_path)


if __name__ == "__main__":
    main = PandasDF()
    main.pandas_df()
