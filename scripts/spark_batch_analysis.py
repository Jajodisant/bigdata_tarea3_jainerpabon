from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, round, sum as _sum, count

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("Análisis por lotes de ventas de supermercado") \
    .getOrCreate()

# 📂 Cargar el archivo CSV
input_path = "/media/sf_SuperMarket_Sales/supermarket-spark-project/sales.csv"
print("======================================")
print(f">>> Cargando datos desde: {input_path}")
print("======================================")


df = spark.read.csv(input_path, header=True, inferSchema=True)

# Mostrar esquema inicial
print("====================================")
print(">>> Esquema de los datos originales:")
print("====================================")

df.printSchema()

# Mostrar algunas filas
print("========================================")
print(">>> Primeras filas del dataset original:")
print("========================================")
df.show(5)

# 🧹 Renombrar columnas a español para mantener consistencia
df = df.withColumnRenamed("branch", "marca") \
       .withColumnRenamed("city", "ciudad") \
       .withColumnRenamed("gender", "genero")

# Filtrar filas válidas (sin valores nulos)
df_clean = df.na.drop()

# Contar registros limpios
total_registros = df_clean.count()
print("=================================================")
print(f"✅ Total de registros limpios: {total_registros}")
print("=================================================")

# 📊 Promedio de ventas por ciudad
avg_sales_ciudad = df_clean.groupBy("ciudad").agg(
    round(avg("total_price"), 2).alias("promedio_ventas"))

print("==================================")
print(">>> Promedio de ventas por ciudad:")
print("==================================")

avg_sales_ciudad.show()

# 📦 Total de ventas por categoría de producto
ventas_categoria = df_clean.groupBy("product_category").agg(
    round(_sum("total_price"), 2).alias("total_ventas"))

print("==============================================")
print(">>> Total de ventas por categoría de producto:")
print("==============================================")

ventas_categoria.show()

# 🙋 Ventas totales por tipo de cliente
ventas_cliente = df_clean.groupBy("customer_type").agg(
    round(_sum("total_price"), 2).alias("total_ventas"))

print("=======================================")
print(">>> Ventas totales por tipo de cliente:")
print("=======================================")

ventas_cliente.show()

# 💰 Total de impuestos recaudados
total_impuestos = df_clean.agg(round(_sum("tax"), 2).alias("total_impuestos"))

print("==================================")
print(">>> Total de impuestos recaudados:")
print("==================================")

total_impuestos.show()

# 🧾 Guardar resultados
output_tmp = "/tmp/spark_batch_results"
output_path = "/media/sf_SuperMarket_Sales/supermarket-spark-project/output/batch_results"

avg_sales_ciudad.write.mode("overwrite").csv(output_path + "/promedio_ventas_por_ciudad", header=True)
ventas_categoria.write.mode("overwrite").csv(output_path + "/ventas_por_categoria", header=True)
ventas_cliente.write.mode("overwrite").csv(output_path + "/ventas_por_cliente", header=True)
total_impuestos.write.mode("overwrite").csv(output_path + "/total_impuestos", header=True)

# 🪄 Copiar los archivos ya escritos correctamente a la carpeta compartida
import shutil, os

if os.path.exists(output_final):
    shutil.rmtree(output_final)
os.makedirs(output_final, exist_ok=True)
shutil.copytree(output_tmp, output_final, dirs_exist_ok=True)

print("===========================================")
print(f">>> Resultados guardados en: {output_path}")
print("===========================================")

# Finalizar la sesión
spark.stop()
print(">>> PROCESO COMPLETADO CON ÉXITO. <<<")
