from src.kafka_producer.json_producer import product_data_using_file
from src.constant import SAMPLE_DIR
import os
if __name__ == '__main__':
    
    # Mark breakpoint and start debuging
    topics = os.listdir(SAMPLE_DIR) # SAMPLE_DIR constatnt denotes the sample_data folder and list out the directories inside it
    print(f'topics: [{topics}]')
    for topic in topics:
        sample_topic_data_dir = os.path.join(SAMPLE_DIR,topic)
        sample_file_path = os.path.join(sample_topic_data_dir,os.listdir(sample_topic_data_dir)[0])
        product_data_using_file(topic=topic,file_path=sample_file_path)
