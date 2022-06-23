# Packs
import os
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.types import StringType
from pyspark.sql.types import IntegerType

# Show local folder
cwd = os.getcwd()
print(cwd)

# Set file Structure
schema = StructType().add('paciente',StringType(),True).add('idade',IntegerType(),True).add('sexo',StringType(),True).add('peso',IntegerType(), True).add('diagnostico',StringType(),True).add('internecao',StringType(),True).add('obito',IntegerType(),True)

# Define spark context, load csv file and show tbl
sc = SparkContext('local')
spark = SparkSession(sc)
df = spark.read.options(delimiter=';').option("header",True).schema(schema).csv('./spark_code/amostra.csv')
df.show()