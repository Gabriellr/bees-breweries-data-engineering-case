FROM mageai/mageai:latest

USER root

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}
COPY requirements.txt /requirements.txt

# Instala Java 17 (já no seu código)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Define JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Variável para Spark baixar pacote hadoop-aws no runtime
ENV SPARK_JARS_PACKAGES=org.apache.hadoop:hadoop-aws:3.3.4

# Instala dependências Python do projeto (incluindo pyspark e boto3)
RUN pip install --no-cache-dir --verbose -r /requirements.txt

# Verificações opcionais
RUN java -version
RUN python --version
RUN pip list
