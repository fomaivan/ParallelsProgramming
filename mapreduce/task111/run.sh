OUT_DIR="/tmp/vovadir"
NUM_REDUCERS=18

hdfs dfs -rm -r -skipTrash ${OUT_DIR}.tmp > /dev/null

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name="task111 step1" \
    -D mapreduce.job.reduces=$NUM_REDUCERS \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -files mapper1.py,reducer1.py \
    -mapper mapper1.py \
    -reducer reducer1.py \
    -input /data/wiki/en_articles_part \
    -output ${OUT_DIR}.tmp \
    > /dev/null

hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name="task111 step2" \
    -D mapreduce.job.reduces=1 \
    -files mapper2.py,reducer2.py \
    -mapper mapper2.py \
    -reducer reducer2.py \
    -input ${OUT_DIR}.tmp \
    -output ${OUT_DIR} \
    > /dev/null

hdfs dfs -cat ${OUT_DIR}/part-00000 2>/dev/null | head -10