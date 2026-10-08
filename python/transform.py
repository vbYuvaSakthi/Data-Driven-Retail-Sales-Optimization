import pandas as pd

dim_tables = pd.read_excel(
    "../data/DimTables.xlsx",
    sheet_name=None
)

fact_internet = pd.read_excel(
    "../data/FactInternetSales.xlsx"
)

fact_reseller = pd.read_excel(
    "../data/FactResellerSales.xlsx"
)

for sheet_name, df in dim_tables.items():

    print(f"\nTransforming {sheet_name}...")

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)
    # Clean column names
    df.columns = df.columns.str.strip()
    # Handle missing values
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(0)

    # Convert date columns if present
    date_columns = [
        "BirthDate",
        "HireDate",
        "FirstPurchaseDate"
    ]
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )
    # Age and AgeGroup for Customer table
    if sheet_name == "DimCustomer":
        current_year = pd.Timestamp.now().year
        df["Age"] = (
            current_year
            - df["BirthDate"].dt.year
        )
        # Fill missing age values
        df["Age"] = df["Age"].fillna(0)
        bins = [0, 25, 35, 45, 50, 150]
        labels = [
            "18-25",
            "26-35",
            "36-45",
            "46-50",
            "50+"
        ]

        df["AgeGroup"] = pd.cut(
            df["Age"],
            bins=bins,
            labels=labels
        )

        # Replace remaining null AgeGroups
        df["AgeGroup"] = df["AgeGroup"].astype(str)
        df["AgeGroup"] = df["AgeGroup"].replace("nan", "Unknown")

    dim_tables[sheet_name] = df

print("\nTransforming FactInternetSales...")

fact_internet.drop_duplicates(inplace=True)

# Convert dates

for col in ["OrderDate", "DueDate", "ShipDate"]:

    fact_internet[col] = pd.to_datetime(
        fact_internet[col],
        errors="coerce"
    )

if "CarrierTrackingNumber" in fact_internet.columns:
    fact_internet.drop(
        columns=["CarrierTrackingNumber"],
        inplace=True
)

# business measures
fact_internet["Profit"] = (
    fact_internet["SalesAmount"]
    - fact_internet["TotalProductCost"]
)

print("\nTransforming FactResellerSales...")

fact_reseller.drop_duplicates(inplace=True)

# Remove bad records with null keys
fact_reseller.dropna(
    subset=[
        "ProductKey",
        "ResellerKey",
        "EmployeeKey",
        "SalesTerritoryKey",
        "OrderDate"
    ],
    inplace=True
)

# Convert dates

for col in ["OrderDate", "DueDate", "ShipDate"]:

    fact_reseller[col] = pd.to_datetime(
        fact_reseller[col],
        errors="coerce"
    )

# Replace missing tracking numbers

fact_reseller["CarrierTrackingNumber"] = (
    fact_reseller["CarrierTrackingNumber"]
    .fillna("Not Available")
)

# Create business measures

fact_reseller["Profit"] = (
    fact_reseller["SalesAmount"]
    - fact_reseller["TotalProductCost"]
)

product_keys = set(
    dim_tables["DimProduct"]["ProductKey"]
)

reseller_keys = set(
    dim_tables["DimReseller"]["ResellerKey"]
)

territory_keys = set(
    dim_tables["DimSalesTerritory"]["SalesTerritoryKey"]
)

fact_reseller = fact_reseller[
    fact_reseller["ProductKey"].isin(product_keys)
]

fact_reseller = fact_reseller[
    fact_reseller["ResellerKey"].isin(reseller_keys)
]

fact_reseller = fact_reseller[
    fact_reseller["SalesTerritoryKey"].isin(
        territory_keys
    )
]


for sheet_name, df in dim_tables.items():

    output_file = f"../data/cleaned/{sheet_name}.csv"

    df.to_csv(
        output_file,
        index=False
    )

    print(f"Saved: {output_file}")

fact_internet.to_csv(
    "../data/cleaned/FactInternetSales.csv",
    index=False
)
fact_reseller.to_csv(
    "../data/cleaned/FactResellerSales.csv",
    index=False
)
print("\nTransformation Completed Successfully")

print("\nRow Counts After Cleaning")

for sheet_name, df in dim_tables.items():
    print(f"{sheet_name}: {len(df)}")

print(f"FactInternetSales: {len(fact_internet)}")
print(f"FactResellerSales: {len(fact_reseller)}")