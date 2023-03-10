-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER, COUNT(DISTINCT USER_INFO.USER_ID) AS USERS
FROM ONLINE_SALE
INNER JOIN USER_INFO
    ON ONLINE_SALE.USER_ID = USER_INFO.USER_ID
WHERE GENDER IS NOT NULL    
GROUP BY YEAR, MONTH, GENDER
ORDER BY
    YEAR, MONTH, GENDER;
    
# SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH,B.GENDER
# ,COUNT(DISTINCT A.USER_ID) AS USERS

# FROM ONLINE_SALE A 
# LEFT JOIN USER_INFO B ON A.USER_ID=B.USER_ID 
# WHERE B.GENDER IS NOT NULL 
# GROUP BY 1,2,3
# ORDER BY YEAR(SALES_DATE) ASC,MONTH(SALES_DATE) ASC,B.GENDER ASC