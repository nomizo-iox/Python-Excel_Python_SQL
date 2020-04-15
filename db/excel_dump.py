from db.db_connection import *
import pymysql
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt

import pandas.io.sql
import xlrd


def excel__db_dump():
    # Create connection and Cursor objects
    cnx = pymysql.Connect(host=host, user=user, password=password, port=port, db=db)
    cursor = cnx.cursor()

    # Read Data
    data = pd.read_excel('superstore.xls')

    # Rename Columns
    data = data.rename(columns={'Row ID': 'Row_ID', 'Order ID': 'Order_ID', 'Order Date': 'Order_Date',
                                'Ship Date': 'Ship_Date', 'Ship Mode': 'Ship_Mode', 'Customer ID': 'Customer_ID',
                                'Customer Name': 'Customer_Name', 'Segment': 'Segment_Code', 'Country': 'Country_Name',
                                'City': 'City_Name', 'State': 'State_Name', 'Postal Code': 'Postal_Code',
                                'Region': 'Region_Name', 'Product ID': 'Product_ID', 'Category': 'Category_Name',
                                'Sub-Category': 'Sub_Category_Name', 'Product Name': 'Product_Name', 'Sales': 'Sale_No',
                                'Quantity': 'Quantity_No', 'Discount': 'Discount_No', 'Profit': 'Profit_No'})
    # Export
    data.to_excel('superstore_data.xls', index=False)

    # Open the workbook & define the worksheet
    book = xlrd.open_workbook('superstore_data.xls')
    sheet = book.sheet_by_name('Orders')

    query1 = """
    CREATE TABLE superstore (
    Row_ID INT AUTO_INCREMENT PRIMARY KEY, 
    Order_ID VARCHAR(100), 
    Order_Date DATE, 
    Ship_Date DATE,
    Ship_Mode VARCHAR(100), 
    Customer_ID VARCHAR(100), 
    Customer_Name VARCHAR(100), 
    Segment_Code VARCHAR(50), 
    Country_Name VARCHAR(100),
    City_Name VARCHAR(100), 
    State_Name VARCHAR(50), 
    Postal_Code INT,
    Region_Name VARCHAR(50), 
    Product_ID VARCHAR(100), 
    Category_Name VARCHAR(50), 
    Sub_Category_Name VARCHAR(50), 
    Product_Name VARCHAR(255), 
    Sale_No DECIMAL, 
    Quantity_No INT,
    Discount_No FLOAT, 
    Profit_No DECIMAL)
    """

    query2 = """
    INSERT INTO superstore (
    Row_ID, 
    Order_ID, 
    Order_Date,
    Ship_Date, 
    Ship_Mode,  
    Customer_ID, 
    Customer_Name, 
    Segment_Code, 
    Country_Name ,
    City_Name , 
    State_Name, 
    Postal_Code,
    Region_Name, 
    Product_ID, 
    Category_Name, 
    Sub_Category_Name, 
    Product_Name, 
    Sale_No, 
    Quantity_No,
    Discount_No, 
    Profit_No
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:
        cursor.execute(query1)
        cnx.commit()
    except pymysql.ProgrammingError:
        pass

    cursor.execute("SELECT count(*) FROM superstore")
    before_import = cursor.fetchone()

    for r in range(1, sheet.nrows):
        
