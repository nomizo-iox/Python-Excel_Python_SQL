import pandas as pd


def excel_loader():
    xl = pd.read_data('superstore.xls', sheet_name='Orders')
    print(xl)


if __name__ == '__main__':
    excel_loader()
