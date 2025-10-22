import time, json, pandas as pd
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Ajusta la ruta del archivo CSV si lo tienes en otra carpeta
df = pd.read_csv('/media/sf_SuperMarket_Sales/supermarket-spark-project/sales.csv')

for _, row in df.iterrows():
    data = row.to_dict()
    producer.send('ventas_stream', json.dumps(data).encode('utf-8'))
    print("Enviado:", data)
    time.sleep(1)  # simula 1 mensaje por segundo

producer.flush()
producer.close()
