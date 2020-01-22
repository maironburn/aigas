from pyspark.sql import SparkSession, SQLContext
from common_config import BONIFICACION_SAMPLE
from time import sleep
from src.helper.json_helper import get_entity_from_samples
from pyspark.sql import DataFrame

"""
diferencias entre pandas df y spark df
https://medium.com/@chris_bour/6-differences-between-pandas-and-spark-dataframes-1380cec394d2


"""
if __name__ == "__main__":
    # spark = SparkSession.builder.master("local").appName("Word Count").config(conf=SparkConf()).getOrCreate()

    spark = SparkSession.builder \
        .master("local") \
        .appName("ProductLiquidator") \
        .getOrCreate()

    sqlContext = SQLContext(spark)
    json_sample = get_entity_from_samples(BONIFICACION_SAMPLE)
    df = spark.read.json(BONIFICACION_SAMPLE, multiLine=True)
    df.registerTempTable('temp')

    df.printSchema()
    sleep(1)
    sqlContext = SQLContext(spark)

    subquery_product_sample = sqlContext.sql('SELECT * FROM temp WHERE type = \'BonificacionNominacion\'')

    # si quisieramos convertirlo a Pandas DF -> subquery_product_sample.toPandas()
    subquery_product_sample.show()

    print("sesion creada con exito")
