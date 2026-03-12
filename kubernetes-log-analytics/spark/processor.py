import os
import re
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc

LOG_PATH = os.getenv("LOG_PATH", "/data/logs/server.log")
RESULT_PATH = os.getenv("RESULT_PATH", "/data/results/summary.json")

LOG_PATTERN = re.compile(
    r"(?P<ts>\\S+)\\s+(?P<ip>\\S+)\\s+(?P<method>\\S+)\\s+(?P<endpoint>\\S+)\\s+(?P<status>\\d+)\\s+(?P<latency>\\d+)ms"
)


def parse_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    data = match.groupdict()
    return (
        data["ts"],
        data["ip"],
        data["method"],
        data["endpoint"],
        int(data["status"]),
        int(data["latency"]),
    )


def main():
    spark = SparkSession.builder.appName("LogAnalytics").getOrCreate()

    rdd = spark.sparkContext.textFile(LOG_PATH).map(parse_line).filter(lambda x: x is not None)
    df = rdd.toDF(["ts", "ip", "method", "endpoint", "status", "latency"])

    errores = df.filter(col("status") >= 400).groupBy("status").agg(count("*").alias("total")).orderBy(desc("total"))
    sospechosas = df.groupBy("ip").agg(count("*").alias("requests")).orderBy(desc("requests")).limit(5)
    endpoints = df.groupBy("endpoint").agg(count("*").alias("hits")).orderBy(desc("hits")).limit(10)

    result = {
        "errores_frecuentes": [row.asDict() for row in errores.collect()],
        "ips_sospechosas": [row.asDict() for row in sospechosas.collect()],
        "endpoints_mas_usados": [row.asDict() for row in endpoints.collect()],
    }

    os.makedirs(os.path.dirname(RESULT_PATH), exist_ok=True)
    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    spark.stop()


if __name__ == "__main__":
    main()

