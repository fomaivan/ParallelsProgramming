ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;

SET hive.exec.max.dynamic.partitions.pernode=200;
SET hive.exec.dynamic.partition.mode=nonstrict;

USE pd2023068_test;
DROP TABLE IF EXISTS Logs;

CREATE EXTERNAL TABLE Logs (
    ip STRING,
    site_http STRING,
    client_page SMALLINT,
    http_scode SMALLINT,
    client_app STRING
)
PARTITIONED BY (querry_time INT)
STORED AS TEXTFILE;

INSERT OVERWRITE TABLE Logs PARTITION (querry_time)
SELECT ip, site_http, client_page, http_scode, client_app, querry_time FROM LogsTemp;

SELECT * FROM LogsTemp LIMIT 5;
SELECT * FROM Logs LIMIT 5;
