-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS AS I
WHERE I.DATETIME > (SELECT DATETIME
                   FROM ANIMAL_OUTS AS O
                   WHERE I.ANIMAL_ID = O.ANIMAL_ID)
ORDER BY I.DATETIME;