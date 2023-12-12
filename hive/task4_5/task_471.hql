ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;
ADD FILE ./script.sh;

USE smirnovvl;

SELECT TRANSFORM(ip, querry_time, site_http, client_page, http_scode, client_app)
 USING './script.sh' as ip, querry_time, scr, client_page, http_scode, client_app
  FROM Logs
 LIMIT 10;