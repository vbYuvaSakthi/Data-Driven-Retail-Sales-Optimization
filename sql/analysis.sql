#Total sales
SELECT ROUND(SUM(SalesAmount),2) AS TotalSales
FROM FactInternetSales;

#Total Orders
SELECT COUNT(DISTINCT SalesOrderNumber) AS TotalOrders
FROM FactInternetSales;

#Average Order Value
SELECT ROUND(AVG(SalesAmount),2) AS AvgOrderValue
FROM FactInternetSales;

#Profit Margin
SELECT ROUND((SUM(Profit)/SUM(SalesAmount))*100,2) AS ProfitMargin
FROM FactInternetSales;

#total profit
SELECT ROUND(SUM(Profit),2) AS TotalProfit
FROM FactInternetSales;

#sales by territory
SELECT
    st.SalesTerritoryRegion,
    ROUND(SUM(fi.SalesAmount),2) AS TotalSales
FROM FactInternetSales fi
JOIN DimSalesTerritory st
ON fi.SalesTerritoryKey = st.SalesTerritoryKey
GROUP BY st.SalesTerritoryRegion
ORDER BY TotalSales DESC;

#customer occupation analysis
SELECT
    dc.Occupation,
    ROUND(AVG(fi.SalesAmount),2) AS AvgSales
FROM FactInternetSales fi
JOIN DimCustomer dc
ON fi.CustomerKey = dc.CustomerKey
GROUP BY dc.Occupation
ORDER BY AvgSales DESC;

#age group analysis
SELECT
    dc.AgeGroup,
    ROUND(SUM(fi.SalesAmount),2) AS TotalSales
FROM FactInternetSales fi
JOIN DimCustomer dc
ON fi.CustomerKey = dc.CustomerKey
GROUP BY dc.AgeGroup
ORDER BY TotalSales DESC;

#product performance
SELECT
    dp.Product,
    ROUND(SUM(fi.SalesAmount),2) AS TotalSales
FROM FactInternetSales fi
JOIN DimProduct dp
ON fi.ProductKey = dp.ProductKey
GROUP BY dp.Product
ORDER BY TotalSales DESC
LIMIT 10;

#category performance
SELECT
    dp.Category,
    ROUND(SUM(fi.SalesAmount),2) AS TotalSales,
    ROUND(SUM(fi.Profit),2) AS TotalProfit
FROM FactInternetSales fi
JOIN DimProduct dp
ON fi.ProductKey = dp.ProductKey
GROUP BY dp.Category
ORDER BY TotalSales DESC;

#internet vs reseller sales
SELECT
    'Internet' AS SalesChannel,
    ROUND(SUM(SalesAmount),2) AS TotalSales
FROM FactInternetSales

UNION ALL

SELECT
    'Reseller',
    ROUND(SUM(SalesAmount),2)
FROM FactResellerSales;

#top 10 customers by revenue
SELECT
    dc.CustomerName,
    ROUND(SUM(fi.SalesAmount),2) AS Revenue
FROM FactInternetSales fi
JOIN DimCustomer dc
ON fi.CustomerKey = dc.CustomerKey
GROUP BY dc.CustomerName
ORDER BY Revenue DESC
LIMIT 10;

#top 10 reseller by sales
SELECT
    dr.ResellerName,
    ROUND(SUM(fr.SalesAmount),2) AS TotalSales
FROM FactResellerSales fr
JOIN DimReseller dr
ON fr.ResellerKey = dr.ResellerKey
GROUP BY dr.ResellerName
ORDER BY TotalSales DESC
LIMIT 10;



































