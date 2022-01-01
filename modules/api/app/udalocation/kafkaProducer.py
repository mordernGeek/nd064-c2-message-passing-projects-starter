from kafka import KafkaProducer

TOPIC_NAME = 'location'
KAFKA_SERVER = 'localhost:9092'

kafkaProducer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

kafkaProducer.send(TOPIC_NAME, b'Sending a message to Udaconnect!')

kafkaProducer.flush()