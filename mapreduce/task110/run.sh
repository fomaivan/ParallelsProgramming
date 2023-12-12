OUT_DIR="Oh_Task"
NUM_REDUCERS=10

hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
  -D mapreduce.job.reduces="${NUM_REDUCERS}" \
  -D mapreduce.job.name="task110" \
  -files mapper.py,reducer.py \
  -mapper mapper.py \
  -reducer reducer.py \
  -input /data/ids_part \
  -output "$OUT_DIR" \
   > /dev/null

for num in `seq 0 $(($NUM_REDUCERS - 1))`
do
    hdfs dfs -cat ${OUT_DIR}/part-0000$num 2>/dev/null | head -5
done