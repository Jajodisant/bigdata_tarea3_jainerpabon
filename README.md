# **Proyecto Big Data – Análisis de Ventas de Supermercado**

Este proyecto corresponde a la Tarea 3: Procesamiento de Datos con Apache Spark del curso Fundamentos de la Infraestructura de Big Data (UNAD). El objetivo fue analizar un conjunto de datos de ventas de supermercado, aplicando procesamiento batch y streaming mediante Apache Spark y Apache Kafka.

# **📂 Estructura del repositorio**
    bigdata_tarea3_jainerpabon/
  │
  ├── capturas/
  │   ├── batch_resultado.png
  │   ├── spark_ui_environment.png
  │   ├── spark_ui_jobs.png
  │   ├── kafka_producer_output.png
  │
  ├── scripts/
  │   ├── batch_supermarket_sales.py
  │   ├── kafka_producer.py
  │   └── kafka_spark_consumer.py
  │
  ├── sales.csv
  ├── README.md
  └── .gitignore

# **⚙️ Contenido del proyecto**
## **1️⃣ Procesamiento Batch (por lotes)**
**Script:** scripts/batch_supermarket_sales.py
+ Carga el archivo real sales.csv.
+ Realiza limpieza y transformación de datos.
+ Calcula el promedio de ventas por sucursal.
+ Guarda los resultados procesados en la carpeta resultados_batch/.

## **2️⃣ Procesamiento en Tiempo Real (Streaming)**
**Scripts:**
+ scripts/kafka_producer.py → genera datos simulados de sensores (ventas, temperatura, humedad, etc.) y los envía a un topic de Kafka.
+ scripts/kafka_spark_consumer.py → consume los datos en tiempo real, los procesa en ventanas de tiempo de 10 segundos y calcula promedios por sensor.

## **📸 Evidencias incluidas**
Las capturas de ejecución y análisis se encuentran en la carpeta capturas/ e incluyen:
+ Ejecución de los scripts.
+ Consola de Spark Streaming mostrando batches procesados.
+ Paneles de Spark: Environment, Jobs, Executors y Streaming Query Statistics.

## **🧭 Instrucciones para ejecución**
### **Clonar el repositorio:**
+ git clone https://github.com/Jajodisant/bigdata_tarea3_jainerpabon.git
+ cd bigdata_tarea3_jainerpabon/scripts

### **Iniciar servicios de Kafka:**
+ sudo /opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties &
+ sudo /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties &

### **Ejecutar el productor de datos simulados:**
+ python3 kafka_producer.py

### **En otra terminal, iniciar el consumidor de Spark Streaming:**
+ spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 kafka_spark_consumer.py

### **Para el análisis batch:**
+ spark-submit batch_supermarket_sales.py

## **🧾 Descripción del repositorio**
Implementación práctica de procesamiento batch y streaming con Apache Spark y Kafka, utilizando el dataset Supermarket Sales, para demostrar el flujo completo de 
análisis de datos en entornos de Big Data.

## **👤 Autoría**
**Estudiante:** Jainer Pabón
**Tutor:** Jaime Rubiano Llorente
**Curso:** Big Data
**Universidad:** UNAD – Escuela de Ciencias Básicas, Tecnología e Ingeniería






