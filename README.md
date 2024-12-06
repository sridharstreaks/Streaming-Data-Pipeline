# Mock Streaming Data Pipeline with Kafka, Spark, PostgreSQL, Docker, Airflow and Cassandra

In today's fast-paced, data-driven world, real-time data analysis is a game-changer for businesses, enabling swift and informed decision-making. This project integrates **Kafka**, **Spark**, **PostgreSQL**, **Docker**, **Airflow** and **Cassandra** to build a robust real-time data pipeline for seamless data processing.

## Objectives

This project aims to overcome these challenges by implementing a real-time data analysis system leveraging cutting-edge technologies:

- **Real-Time Data Ingestion**: Capturing user interactions as they occur with minimal latency.
- **Scalable Architecture**: Building a distributed system capable of handling increasing data loads.
- **Improved Data Quality**: Ensuring data integrity through real-time validation and schema management.
- **Automation**: Streamlining workflows to reduce manual intervention and errors.
- **Monitoring**: Using tools like **Kafdrop** to oversee Kafka topics, offsets, and consumer health.
- **Business Integration**: Delivering actionable insights directly into business applications for rapid response.
- **Data-Driven Decisions**: Enabling stakeholders with timely and accurate insights.

## Highlights

- **Lightweight Airflow Setup**: This project uses the latest, lightweight version of **Apache Airflow**, reducing resource overhead compared to traditional setups.
- **Spark-Kafka Integration**: Significant experimentation with Spark, Kafka, and JAR packages has led to a carefully selected combination. If switching to newer versions, proceed cautiously, as updates may disrupt stream processing.

---

## Getting Started

### Project Files:

- **`kafka_stream.py`**: [kafka_stream.py](dags/kafka_stream.py) fetches user data from [Random User API](https://randomuser.me), processes it, and streams it into a Kafka topic named `user_data`. This task is automated using **Apache Airflow**'s PythonOperator.

- **`spark-streaming.py`**: [spark-streaming.py](spark-streaming.py) establishes connections to Cassandra and Kafka, creates necessary keyspaces and tables, and sets up Spark streaming for real-time processing.

---

### Running the Project

1. **Clone the Repository**:

2. **Navigate to the Project Directory**:

3. **Set Up a Python Virtual Environment**:

   ```bash
   pip3 install virtualenv
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Required Packages**:

   ```bash
   pip3 install -r ./requirements.txt
   ```

5. **Install Docker and Docker Compose** (If hadn't already):

6. **Build Docker Containers**:

   ```bash
   docker compose up
   ```

   Check containers using Docker Desktop or the CLI.

7. **Monitor Airflow Tasks**:

   Access the Airflow UI at `localhost:8080` using the credentials:
   - **Username**: `admin`
   - **Password**: `admin`

8. **Run Spark Streaming**:

   ```bash
   python3 spark-streaming.py
   ```
   
9. **Monitor Kafka Topics with Kafdrop**:

   Access the **Kafdrop UI** for monitoring Kafka topics, offsets, and consumer performance at `localhost:9000`.

10. **Query Cassandra Data**:

   Connect to Cassandra to verify stored data:

   ```bash
   docker exec -it cassandra_db cqlsh -u cassandra -p cassandra localhost 9042
   ```
11. **Monitoring the Pipeline""

    spark with be still listening to any new messages until it is manually stopped. You can increase the user metadata by extending the time of airflow dag.

## References

1. [Real-Time Data Streaming](https://www.youtube.com/watch?v=GqAcTrqKcrY)

---

⚡️ *That's all for my project! If you have any questions, feel free to reach out. Thanks for reading!* ⚡️
