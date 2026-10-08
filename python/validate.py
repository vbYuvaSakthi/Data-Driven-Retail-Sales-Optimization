import pandas as pd


dim_customer = pd.read_csv(
    "../data/cleaned/DimCustomer.csv"
)

dim_employee = pd.read_csv(
    "../data/cleaned/DimEmployee.csv"
)

dim_geography = pd.read_csv(
    "../data/cleaned/DimGeography.csv"
)

dim_product = pd.read_csv(
    "../data/cleaned/DimProduct.csv"
)

dim_reseller = pd.read_csv(
    "../data/cleaned/DimReseller.csv"
)

dim_territory = pd.read_csv(
    "../data/cleaned/DimSalesTerritory.csv"
)

fact_internet = pd.read_csv(
    "../data/cleaned/FactInternetSales.csv"
)

fact_reseller = pd.read_csv(
    "../data/cleaned/FactResellerSales.csv"
)


print("\nNULL VALUE CHECK")

tables = {
    "DimCustomer": dim_customer,
    "DimEmployee": dim_employee,
    "DimGeography": dim_geography,
    "DimProduct": dim_product,
    "DimReseller": dim_reseller,
    "DimSalesTerritory": dim_territory,
    "FactInternetSales": fact_internet,
    "FactResellerSales": fact_reseller
}
for table_name, df in tables.items():
    print(f"\n{table_name}")
    null_count = df.isnull().sum().sum()
    print("Total Null Values:", null_count)

print("\nDUPLICATE CHECK")

for table_name, df in tables.items():

    print(
        table_name,
        "Duplicate Rows:",
        df.duplicated().sum()
    )

print("\nPRIMARY KEY VALIDATION")

pk_checks = {
    "DimCustomer": (dim_customer, "CustomerKey"),
    "DimEmployee": (dim_employee, "EmployeeKey"),
    "DimGeography": (dim_geography, "GeographyKey"),
    "DimProduct": (dim_product, "ProductKey"),
    "DimReseller": (dim_reseller, "ResellerKey"),
    "DimSalesTerritory": (
        dim_territory,
        "SalesTerritoryKey"
    )
}

for table_name, (df, pk) in pk_checks.items():

    duplicate_keys = df[pk].duplicated().sum()

    print(
        f"{table_name} ({pk}) Duplicate Keys:",
        duplicate_keys
    )

print("\nFOREIGN KEY VALIDATION")

# ProductKey

invalid_product_internet = \
    ~fact_internet["ProductKey"].isin(
        dim_product["ProductKey"]
    )

print(
    "Invalid ProductKeys in FactInternetSales:",
    invalid_product_internet.sum()
)

invalid_product_reseller = \
    ~fact_reseller["ProductKey"].isin(
        dim_product["ProductKey"]
    )

print(
    "Invalid ProductKeys in FactResellerSales:",
    invalid_product_reseller.sum()
)

# CustomerKey

invalid_customer = \
    ~fact_internet["CustomerKey"].isin(
        dim_customer["CustomerKey"]
    )

print(
    "Invalid CustomerKeys:",
    invalid_customer.sum()
)

# ResellerKey

invalid_reseller = \
    ~fact_reseller["ResellerKey"].isin(
        dim_reseller["ResellerKey"]
    )

print(
    "Invalid ResellerKeys:",
    invalid_reseller.sum()
)

# SalesTerritoryKey

invalid_territory_internet = \
    ~fact_internet["SalesTerritoryKey"].isin(
        dim_territory["SalesTerritoryKey"]
    )

print(
    "Invalid Territory Keys (Internet):",
    invalid_territory_internet.sum()
)

invalid_territory_reseller = \
    ~fact_reseller["SalesTerritoryKey"].isin(
        dim_territory["SalesTerritoryKey"]
    )

print(
    "Invalid Territory Keys (Reseller):",
    invalid_territory_reseller.sum()
)

print("\nAll Validation Checks Completed")
