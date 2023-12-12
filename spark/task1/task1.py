import re
import sys
from pyspark import SparkContext, SparkConf

ARTICLE_PATTERN = re.compile(
    r"(?P<id>\d+)\t"
    r"(?P<text>.*)"
)

def parse_article(line):
    match = re.search(ARTICLE_PATTERN, line)
    if not match:
        return ""

    text = match.group('text')

    words = re.findall(r'\w+', text)
    words = [re.sub(r'^\W+|\W+$', '', word) for word in words]

    bigram_strings = ('_'.join([words[i], words[i+1]]) for i in range(len(words)-1))

    return " ".join(bigram_strings)


if __name__ == "__main__":
    config = SparkConf().setAppName("bigramm_task").setMaster("yarn")
    spark_context = SparkContext(conf=config)

    lines = spark_context.textFile("%s" % sys.argv[1])
    bigram_articles = lines.map(parse_article)

    bigram_articles_lower = bigram_articles.map(lambda x: x.strip().lower()) 
    bigram_lists = bigram_articles_lower.flatMap(lambda x: x.split(" "))

    filtered_bigrams = bigram_lists.filter(lambda bigram: bigram.startswith("narodnaya_"))
    bigram_pairs = filtered_bigrams.map(lambda x: (x, 1))

    reduced_bigram_pairs = bigram_pairs.reduceByKey(lambda a, b: a + b)
    sorted_bigram_pairs = reduced_bigram_pairs.sortBy(lambda a: a[0])

    for line in sorted_bigram_pairs.collect():
        print("%s %d" % (line[0], line[1]))