import pandas as pd

DIM_FILE = "../data/DimTables.xlsx"
INTERNET_FILE = "../data/FactInternetSales.xlsx"
RESELLER_FILE = "../data/FactResellerSales.xlsx"

dim_tables = pd.read_excel(
    DIM_FILE,
    sheet_name=None
)
for sheet_name, df in dim_tables.items():
    print(f"Dimension Table: {sheet_name}")
    print("Columns:")
    print(df.columns.tolist())
    print(f"\nRows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

fact_internet = pd.read_excel(INTERNET_FILE)
print("FactInternetSales")
print("Columns:")
print(fact_internet.columns.tolist())
print(f"\nRows: {fact_internet.shape[0]}")
print(f"Columns: {fact_internet.shape[1]}")

fact_reseller = pd.read_excel(RESELLER_FILE)
print("FactResellerSales")
print("Columns:")
print(fact_reseller.columns.tolist())
print(f"\nRows: {fact_reseller.shape[0]}")
print(f"Columns: {fact_reseller.shape[1]}")
