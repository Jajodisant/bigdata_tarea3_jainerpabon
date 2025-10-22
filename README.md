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











