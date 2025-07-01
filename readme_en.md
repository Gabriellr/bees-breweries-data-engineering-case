## BEES Data Engineering – Breweries Case

This data pipeline, developed with Docker, extracts information from the Open Brewery DB API. Using Apache Spark for processing and transformation, and Mage.ai for orchestration, it applies the Medallion architecture to structure the data in three layers.

The data is stored in a cloud-based Data Lake (AWS S3). In the Bronze layer, raw data from the API is saved in Parquet format; in the Silver layer, the data is transformed and partitioned by location; and in the Gold layer, the data is aggregated and enriched with metrics such as the number of breweries by type and region.

## Technologies and Tools

- **Mage.ai** – Pipeline orchestration
- **PySpark** – Distributed processing
- **Pandas** – Lightweight data manipulation
- **AWS S3** – Data lake layers
- **boto3** – Programmatic integration with S3
- **Docker** – Environment containerization

## Pipeline Architecture

The pipeline was developed based on the **Medallion architecture**, using modern, scalable technologies and following data engineering best practices.

### Layered Structure (Medallion)

The architecture organizes data into three main layers:

- **🔹 Bronze (Raw)**\
  Stores raw data collected directly from the API without transformations. Serves as the immutable source of truth.

- **🔸 Silver (Curated)**\
  Cleans, normalizes, and enriches the data. Saves it in columnar format (Parquet), partitioned by country and region.

- **🥇 Gold (Analytics)**\
  Data ready for analytical consumption. This layer contains **aggregations by brewery type and location**, optimizing performance for dashboards and reports.



## Installation

### Prerequisites

- Docker installed on your machine (recommended version >= 20.x)

### Steps to Run the Project

1. **Clone the Repository**

   Clone this project to your local machine:

   ```bash
   git clone https://github.com/Gabriellr/bees-breweries-data-engineering-case.git
   cd bees-breweries-data-engineering-case
   ```

2. **Configure Environment Variables**\
   Create a `.env` file in the root directory with your AWS credentials for reading and writing to the S3 bucket. Example:

   ```env
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   AWS_DEFAULT_REGION=us-east-1
   ```

3. **Install and Start Docker**\
   Make sure Docker Desktop is installed and running on your machine.\
   With Docker ready, navigate to the `mage-docker` project root and run the following command to start Mage.ai:

   ```bash
   docker-compose up --build
   ```

4. **Running the Pipeline via Mage.ai Interface**

To manually run your pipeline in Mage.ai, follow the steps below:

1. Access the web interface at: [http://localhost:6789](http://localhost:6789) or [http://localhost:6789/pipelines/elt\_proj\_breweries/triggers](http://localhost:6789/pipelines/elt_proj_breweries/triggers)

2. In the side menu, click on the **Pipelines** tab.

3. Select the desired pipeline (e.g., `elt_proj_breweries`).

4. On the pipeline page, go to the **Triggers** tab.

5. Click the \`\` button to start the manual execution of the pipeline.

You will be able to **track progress**, **check logs**, and **view real-time results** directly through the graphical interface.

---

### 🚀 Recommended Improvement: Observability and Data Governance with AWS

The pipeline was developed using free and open-source tools (`Mage.ai`, `PySpark`, `Docker`, and `AWS S3`), prioritizing accessibility and ease of reproduction. However, for enterprise or production environments, the adoption of AWS managed services is highly recommended to significantly improve **observability**, **governance**, and **operational efficiency**:

- **Monitoring & Alerts:**\
  Use **Amazon CloudWatch** in combination with **Amazon SNS** to monitor failures, execution times, and trigger automated real-time alerts.

- **Data Cataloging:**\
  Integrate **AWS Glue Data Catalog** to register metadata from the Bronze, Silver, and Gold layers, enabling data discovery, versioning, and auditing.

- **Data Virtualization:**\
  Adopt **Amazon Athena** for SQL queries directly on data stored in S3, without the need for additional ETL processes or loading into databases.

- **Data Quality Monitoring:**\
  Incorporate tools like **AWS Deequ** (Spark) or **Amazon DataZone** to track data integrity, consistency, and business rule compliance automatically.

> *These features were not used in this version to maintain a zero-cost project, but they are highly recommended for environments with higher volume, criticality, and compliance or scalability requirements.*

