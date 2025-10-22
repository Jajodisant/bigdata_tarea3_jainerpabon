from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, TimestampType

# Configurar la sesión de Spark con soporte para Kafka
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .master("local[*]") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()

# Reducir el nivel de logs para que no se llene la consola
spark.sparkContext.setLogLevel("WARN")

# Definir el esquema de los datos que recibimos de Kafka
schema = StructType([
    StructField("sensor_id", IntegerType()),
    StructField("temperature", FloatType()),
    StructField("humidity", FloatType()),
    StructField("timestamp", TimestampType())
])

# Leer el stream desde Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor_data") \
    .option("startingOffsets", "latest") \
    .load()

# Extraer el valor (que viene en binario) y convertirlo a JSON según el esquema
json_df = df.selectExpr("CAST(value AS STRING) as json_value")
sensor_df = json_df.select(from_json(col("json_value"), schema).alias("data")).select("data.*")

# Mostrar los datos procesados en tiempo real por consola
query = sensor_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()


