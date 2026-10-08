#fact internet
CREATE TABLE FactInternetSales (
    ProductKey INT,
    CustomerKey INT,
    SalesTerritoryKey INT,
    SalesOrderNumber VARCHAR(50),
    SalesOrderLineNumber INT,
    DiscountAmount DECIMAL(15,2),
    TotalProductCost DECIMAL(15,2),
    SalesAmount DECIMAL(15,2),
    Freight DECIMAL(15,2),
    OrderDate DATE,
    DueDate DATE,
    ShipDate DATE,
    Profit DECIMAL(15,2)
);

#fact reseller
CREATE TABLE FactResellerSales (
    ProductKey INT,
    ResellerKey INT,
    EmployeeKey INT,
    SalesTerritoryKey INT,
    SalesOrderNumber VARCHAR(50),
    SalesOrderLineNumber INT,
    DiscountAmount DECIMAL(15,2),
    TotalProductCost DECIMAL(15,2),
    SalesAmount DECIMAL(15,2),
    Freight DECIMAL(15,2),
    CarrierTrackingNumber VARCHAR(100),
    OrderDate DATE,
    DueDate DATE,
    ShipDate DATE,
    Profit DECIMAL(15,2)
);



