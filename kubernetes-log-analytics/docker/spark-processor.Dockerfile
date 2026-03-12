FROM bitnami/spark:3.5

COPY spark/processor.py /opt/spark-apps/processor.py

CMD ["/opt/bitnami/spark/bin/spark-submit", "--master", "local[*]", "/opt/spark-apps/processor.py"]

