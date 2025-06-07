## News-Category-Counting--MapReducer
This project implements a Hadoop MapReduce job to process a cleaned news dataset and extract statistical insights based on news categories. The goal is to count the frequency of each unique category using separate Mapper and Reducer Python scripts.

The project demonstrates:
* Text processing with Hadoop MapReduce.
* Working with HDFS (Hadoop Distributed File Syetem)
* Parcing large-scale JSON-derived data
* Counting and sorting news article categories efficiently.

# Dataset
The dataset used is the News Category Dataset from Kaggle (https://www.kaggle.com/datasets/rmisra/news-category-dataset). The original News_Category_Dataset_v3.json file was converted into a plain text format and saved as News_Cleaned.txt using the convert_json_to_text.py script.
Run command: python3 convert_json_to_text.py

# Setup Instructions
* Hadoop version: Hadoop 3.4.1
* Python3 version: Python 3.12.3
* SSH version OpenSSH_9.6p1 Ubuntu-3ubuntu13.11, OpenSSL 3.0.13
* Java version: openjdk version "21.0.7"
* Above obtained News_Cleaned.txt is uploaded to HDFS - command: hdfs dfs -put news_cleaned.txt path
* Mapper: mapper.py
* Reducer: reducer.py
* Make the mapper and reducerscripts executable - command: chmod +x mapper.py reducer.py
* Run the MapReduce job: hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/your_username/news_cleaned.txt \
-output /user/your_username/news_output \
-mapper mapper.py \
-reducer reducer.py \
-file mapper.py \
-file reducer.py
* Check the output on HDFS: hdfs dfs -cat /user/your_username/news_output/part-00000




