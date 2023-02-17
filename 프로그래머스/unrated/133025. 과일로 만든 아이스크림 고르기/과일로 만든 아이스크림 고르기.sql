-- 코드를 입력하세요
SELECT FLAVOR
FROM FIRST_HALF

INNER JOIN ICECREAM_INFO
    USING (FLAVOR)

WHERE TOTAL_ORDER > 3000
    AND
    INGREDIENT_TYPE = "fruit_based"
ORDER BY
    FLAVOR;