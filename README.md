## News-Category-Counting--MapReducer
This project implements a Hadoop MapReduce job to process a cleaned news dataset and extract statistical insights based on news categories. The goal is to count the frequency of each unoque category using separate MApper and Reducer Python scripts.

The project demonstrates:
* Text processing with Hadoop MapReduce.
* Working with HDFS (Hadoop Distributed File Syetem)
* Parcing large-scale JSON-derived data
* Counting and sorting news article categories efficiently.

# Dataset
The dataset is a newsCategoryDataset form https://www.kaggle.com/datasets/rmisra/news-category-dataset. This News_Category_dataset_V3.json json dataset file is converted in to txt within News_Cleaned.txt using convert_json_to_text.py. 
Run command: python3 convert_json_to_text.py

# Setup Instructions
* Hadoop version: Hadoop 3.4.1
* Python3 version: Python 3.12.3
* SSH version OpenSSH_9.6p1 Ubuntu-3ubuntu13.11, OpenSSL 3.0.13
* Java version: openjdk version "21.0.7"
* Above obtained News_Cleaned.txt is uploaded to HDFS - command to run: hdfs dfs -put news_cleaned.txt path
* Mapper: mapper.py
* Reducer: reducer.py
* Make the mapper and reducerscripts executable - command to run: chmod +x mapper.py reducer.py
* Run the MapReduce job: hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/your_username/news_cleaned.txt \
-output /user/your_username/news_output \
-mapper mapper.py \
-reducer reducer.py \
-file mapper.py \
-file reducer.py
* Check the output on HDFS: hdfs dfs -cat /user/your_username/news_output/part-00000




