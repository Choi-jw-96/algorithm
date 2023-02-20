-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, "%Y-%m-%d") AS OUT_DATE, 
    CASE 
    WHEN OUT_DATE IS NULL 
    THEN"출고미정"  
    WHEN OUT_DATE <= "2022-05-01"
    THEN "출고완료"
    ELSE "출고대기"
    END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;

# SELECT 
#     order_id, 
#     product_id, 
#     LEFT(out_date,10) AS OUT_DATE, 
#     if(LEFT(out_date,10) <= '2022-05-01', '출고완료',if(out_date is null, '출고미정','출고대기')) as 출고여부
# from food_order
# order by order_id