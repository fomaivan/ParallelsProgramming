ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;
USE pd2023068_test;
DROP TABLE IF EXISTS LogsTemp;

CREATE EXTERNAL TABLE LogsTemp (
    ip STRING,
    querry_time INT,
    site_http STRING,
    client_page SMALLINT,
    http_scode SMALLINT,
    client_app STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
WITH SERDEPROPERTIES (
    "input.regex" = '^(\\S+)\\s+(\\d{8})\\d*\\t(\\S+)\\t(\\d+)\\t(\\d+)\\t(\\S+).*$'
)
STORED AS TEXTFILE
LOCATION '/data/user_logs/user_logs_S';

SELECT * FROM LogsTemp LIMIT 10;
