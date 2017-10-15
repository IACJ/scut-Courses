# 更新题 ----------------------------------------------------

# 20
UPDATE students SET teacher='老黑' WHERE name='小明';

# 75
UPDATE students SET teacher='张海' WHERE name='明明';

# 76
UPDATE students SET name='老黑' WHERE teacher='大力';

# 152
UPDATE P SET COLOR='黄' WHERE PN='P6';

# 删除题 ----------------------------------------------------
# 16
DELETE FROM students WHERE name='小伟' and teacher='大张';

# 17
DELETE FROM students WHERE 1;

# 41
DELETE
FROM SC
WHERE Cid IN 
    (SELECT Cid
    FROM Course AS C,Teacher AS T
    WHERE C.Tid=T.Tid
            AND Tname='VondieBeatty' );

# 43

DELETE
FROM SC
WHERE Sid='1002'
        AND Cid='201';
