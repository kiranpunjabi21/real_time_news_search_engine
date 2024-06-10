from bytewax.connectors.kafka import KafkaSinkMessage, KafkaSource,KafkaSink
from settings import settings
#from logger import get_logger

#Kafka consumer configuration

def build_kafka_stream():

    kafka_config = {'bootstrap.servers':settings.UPSTASH_KAFKA_ACCOUNT,
                    'username' : settings.UPSTASH_KAFKA_UNAME,
                    'password' : settings.UPSTASH_KAFKA_PASS,
                    'auto.offset.reset':'earliest'}
 

    kafka_input = KafkaSource(topics= [settings.UPSTASH_KAFKA_TOPIC],
                             brokers = [settings.UPSTASH_KAFKA_ENDPOINT],
                             add_config = kafka_config)
    
    #logger.info("KAFKA CONSUMER CREATED SUCCESSFULLY")

    return kafka_input


while True:
    message = consumer.poll()

    if message is None:
        continue
    if message.error():
        if message.error().code() == KafkaError._PARTITION_EOF:
            print(f'Reached end of partition {message.topic()}')
        else:
            print(f'Error while consuming from topic {message.topic()}')
    else:
        print(f'Received message: {message.value().decode('utf-8')}')



# Close the Kafka consumer
consumer.close()
