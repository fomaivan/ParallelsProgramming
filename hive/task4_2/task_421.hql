ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;
USE smirnovvl;

SET mapred.job.name="smirnovvl task 421";

  SELECT querry_time, COUNT(querry_time) as views_by_day
    FROM Logs
GROUP BY querry_time
ORDER BY views_by_day DESC;
