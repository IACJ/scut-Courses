

# 第三章 - SQL 练习（1）
SELECT CNO,COUNT(SNO) FROM SC WHERE CNO LIKE 'CS%' GROUP BY CNO  ORDER BY COUNT(SNO) DESC

SELECT CNO,COUNT(SNO) as stucount
FROM SC
WHERE CNO LIKE ‘CS%’
GROUP BY CNO
ORDER BY stucount DESC


# 练习（2）
SELECT Sno,AVG(Grade) FROM SC  GROUP BY Sno HAVING COUNT(*) > 2 AND MIN(Grade) >= 80

SELECT SNO,avg(GRADE)
FROM SC
GROUP BY SNO
HAVING COUNT(CNO)>＝２ and min(GRADE)>=80

# 练习(3) 
SELECT Cno,MAX(Grade) FROM SC GROUP BY Cno HAVING MAX(Grade) > 90

SELECT CNO,max(GRADE)
FROM SC
GROUP BY CNO
120
HAVING max(GRADE）>90

# 练习（4）

SELECT deptno,AVG(sal) FROM Emp GROUP BY deptno HAVING AVG(sal) > 2000


# 
SELECT  DISTINCT Sno,COUNT(*) FROM SC GROUP BY Sno 
WHERE COUNT(*) = SELECT MAX(COUNT(*)) FROM SC GROUP BY Sno

# 练习1

# SELECT Sname FROM SC,Sudent GROUP BY Sname.Sno
# WHERE  SC.Sno = Student.Sno AND  Cno LIKE 'ee%' AND Ssex='女';

SELECT Sname FROM Student 
WHERE Student.Sno = (SELECT DISTINCT SC.Sno FROM SC WHERE Cno LIKE 'ee%') AND Ssex='女';

WTFs


# 练习2
SELECT Sno,COUNT(*),AVG(Grade) FROM SC GROUP BY Sno;

# 练习3
SELECT Cno,COUNT(*) as stuNum, MAX(Grade),MIN(Grade),AVG(Grade) FROM SC GROUP BY Cno;

# 练习4 
SELECT Sno,Sname  FROM  SC,Student WHERE SC.Sno=Student.Sno GROUP BY Sno HAVING MIN (Grade) >80  ORDER BY Sno ASC;

SELECT Sno,Sname  FROM  SC,Student WHERE SC.Sno=Student.Sno GROUP BY Student.Sno,Student.Sname HAVING MIN (Grade) >80  ORDER BY Sno ASC;
????!!!

# 练习5 
SELECT Sname,Cno,Ccredit FROM Student,SC,Course WHERE Student.sno  = SC.sno AND Course.Cno = SC.Cno AND Grade IS NULL;

# 6
SELECT Sname FROM SC,Student,Course WHERE Student.sno  = SC.sno AND Course.Cno = SC.Cno AND Ccredit >=3 AND Grade<70;


# 7  
SELECT Sname,AVG(Grade),SUM(Ccredit) FROM SC,Student WHERE SC.Sno=Student.Sno AND Sage >= 18 AND Sage <20 GROUP BY Student.Sno, Student.Sname 

# 8 
DELETE FROM SC WHERE Sno LIKE '01%'
# 9
INSERT INTO Student(Sno,Sname,Ssex,Sdept,Sage) VALUES( ..., ...,...,...,...)

# 10
 UPDATE  Course SET Ccredit=3 WHERE Cno = 'CS-221'

# 11
CREATE TABLE Emp  
    (empid CHAR(10) PRIMARY KEY,
    empname CHAR (10) NOT NULL,
    empage SMALLINT,
    Deptno CHAR(10)
    FOREIGN KEY(DEptno) REFERENCES dept(deptno));
    











