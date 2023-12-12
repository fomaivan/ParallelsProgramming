add jar Identity/jar/Identity.jar;
--add jar Identity/target/Identity-1.0-SNAPSHOT.jar;

USE velkerr_test;

create temporary function identity as 'com.hobod.IdentityUDF';

select identity(ip)
from Subnets
limit 10;
