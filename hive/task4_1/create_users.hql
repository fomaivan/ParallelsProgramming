ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;
USE smirnovvl;
DROP TABLE IF EXISTS Users;

CREATE EXTERNAL TABLE Users (
    ip STRING,
    user_browser STRING,
    sex STRING,
    age TINYINT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY  '\t'
STORED AS TEXTFILE
LOCATION '/data/user_logs/user_data_M';

SELECT * FROM Users LIMIT 10;
