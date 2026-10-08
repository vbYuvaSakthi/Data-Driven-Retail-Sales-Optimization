#dim customer
CREATE TABLE DimCustomer (
    CustomerKey INT PRIMARY KEY,
    GeographyKey INT,
    CustomerName VARCHAR(100),
    BirthDate DATE,
    MaritalStatus VARCHAR(20),
    Gender VARCHAR(20),
    EmailAddress VARCHAR(100),
    YearlyIncome DECIMAL(12,2),
    Education VARCHAR(50),
    Occupation VARCHAR(50),
    HouseOwnerFlag VARCHAR(10),
    Address VARCHAR(255),
    FirstPurchaseDate DATE,
    Age INT,
    AgeGroup VARCHAR(20)
);

#dim employee
CREATE TABLE DimEmployee (
    EmployeeKey INT PRIMARY KEY,
    ParentEmployeeKey INT,
    SalesTerritoryKey INT,
    EmployeeName VARCHAR(100),
    Title VARCHAR(100),
    EmailAddress VARCHAR(100),
    DepartmentName VARCHAR(100),
    HireDate DATE,
    BirthDate DATE
);

#dim geography
CREATE TABLE DimGeography (
    GeographyKey INT PRIMARY KEY,
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    SalesTerritoryKey INT
);

#dim product
CREATE TABLE DimProduct (
    ProductKey INT PRIMARY KEY,
    ProductSubcategoryKey INT,
    Product VARCHAR(200),
    Color VARCHAR(50),
    Model VARCHAR(100),
    Subcategory VARCHAR(100),
    Category VARCHAR(100)
);

#dim reseller
CREATE TABLE DimReseller (
    ResellerKey INT PRIMARY KEY,
    GeographyKey INT,
    BusinessType VARCHAR(100),
    ResellerName VARCHAR(150)
);

#dim salesterritory
CREATE TABLE DimSalesTerritory (
    SalesTerritoryKey INT PRIMARY KEY,
    SalesTerritoryRegion VARCHAR(100),
    SalesTerritoryCountry VARCHAR(100),
    SalesTerritoryGroup VARCHAR(100)
);

























































