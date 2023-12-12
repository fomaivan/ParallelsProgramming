ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;
USE smirnovvl;

SELECT TRANSFORM(ip)
 USING 'rev' as rev
  FROM IPRegions LIMIT 10;