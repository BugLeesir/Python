"""
-- Active: 1674490178818@@127.0.0.1@3306@sakila
SHOW DATABASES;
-- 我是注释
USE world;
SELECT DATABASE();

CREATE DATABASE test CHARSET utf8;

#删除库
DROP DATABASE test;

SHOW TABLES;

# 创建表
CREATE TABLE Student(
    id INT,
    name VARCHAR(10),
    age INT
);

USE test;

-- Active: 1674490178818@@127.0.0.1@3306@test
#SQL语句中字符串用单引号包裹
# 插入数据
INSERT INTO
    student(id, name, age)
VALUES (4, 'hahaha', 88), (7, 'hurahura', 77);

INSERT INTO student VALUES(3,'李云瑞',19);

#数据删除 
DELETE FROM student WHERE id=3;

#更新数据 
UPDATE student set name='wocao' WHERE id=4;

#数据查询
SELECT id,name FROM student;

SELECT * FROM student WHERE id<5;

# 分组聚合
SELECT id ,COUNT(*) FROM student GROUP BY id;

# 分页排序
SELECT * FROM student ORDER BY age;

# 逆序
SELECT * FROM student ORDER BY age DESC;

# 分页
SELECT * FROM student ORDER BY age LIMIT 1,1;


"""


from pymysql import Connection

# 构建到MySQL数据库的连接
conn = Connection(
    host="localhost", port=3306, user="root", password="143323", autocommit=True  #自动提交
)
print(conn.get_server_info())

# 执行非查询性质SQL
# 获取游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("test")

# 执行SQL
# cursor.execute("create table test_table(id int);")

# cursor.execute("drop table test_table;")

# 执行查询性质的SQL
# conn.select_db("world")
# cursor.execute("select * from city")
# results=cursor.fetchall()
# for r in results:
#     print(r)

# 数据更改确认(手动确认)
cursor.execute("insert into student values(10,'你好',68)")
conn.commit()

# 关闭连接
conn.close()
