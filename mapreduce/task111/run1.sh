OUT_DIR="/tmp/vovadir"
NUM_REDUCERS=1

hadoop fs -rm -r -skipTrash $OUT_DIR*

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name="task111 step1" \
    -D mapreduce.job.reduces=$NUM_REDUCERS \
    -files mapper1.py,reducer1.py \
    -mapper mapper1.py \
    -reducer reducer1.py \
    -input /data/wiki/en_articles_part \
    -output $OUT_DIR

for num in `seq 0 $(($NUM_REDUCERS - 1))`
do
    hdfs dfs -cat ${OUT_DIR}/part-0000$num | head
done