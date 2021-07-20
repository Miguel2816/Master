# This Python file uses the following encoding: latin-1

from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("PEC").setMaster("local")
sc = SparkContext(conf=conf)

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import array, col, desc, explode, lit, rank, row_number, struct, trim
from pyspark.sql import functions as F
from pyspark.sql.types import StructField, StructType, StringType, IntegerType
from pyspark.sql.window import Window
from typing import Iterable

sparkSQL = SparkSession \
    .builder \
    .appName("PEC") \
    .master("local") \
    .getOrCreate()

# EJERCICIO 2

## Crear schema set de datos Municipios
schema_mun = StructType([
    StructField('Codigo', IntegerType(), True),
    StructField('Comunidad', StringType(), True),
    StructField('Provincia', StringType(), True),
    StructField('Municipio', StringType(), True),
    StructField('Poblacion', IntegerType(), True)
])

## Cargar archivo municipios de su ubicación local
df_mun = sparkSQL.read.option("delimiter", ";").option("encoding", "ISO-8859-1")\
    .csv("/home/bigdata/Escritorio/pec/PECMunicipios.csv", header=True, schema=schema_mun)

## Eliminar los espacios en los campos correspondientes
df_mun = df_mun.withColumn("Comunidad", trim(col("Comunidad")))
df_mun = df_mun.withColumn("Provincia", trim(col("Provincia")))
df_mun = df_mun.withColumn("Municipio", trim(col("Municipio")))

## Cargar archivo elecciones de su ubicación local
df_elec = sparkSQL.read.option("delimiter", ";").option("encoding", "ISO-8859-1")\
    .csv("/home/bigdata/Escritorio/pec/PECElecciones.csv", header=True)

## Modificar el tipo de todas las columnas del dataframe a integer
for col in df_elec.columns:
  df_elec = df_elec.withColumn(
    col,
    F.col(col).cast("integer")
  )

## Mostrar por pantalla el df de los municipios y su schema
df_mun.show()
df_mun.printSchema()

## Mostrar por pantalla el df de las elecciones y su schema
df_elec.show()
df_elec.printSchema()

# EJERCICIO 3

## Ordenar el dataframe de municipios de forma ascendente y descendente
df3_asc = df_mun.sort(df_mun.Poblacion.asc(), df_mun.Municipio.asc())
df3_desc = df_mun.sort(df_mun.Poblacion.desc(), df_mun.Municipio.asc())

## Seleccionar los 10 primeros municipios y guardar el archivo en el path seleccionado con el encabezado
df3_asc_10 = df3_asc.select("Municipio", "Poblacion").limit(10)
df3_asc_10.write.format('csv').option('header', True).mode('overwrite').option('sep',',')\
   .save('/home/bigdata/Escritorio/pec/ej3-municipios-menor-pob')

## Seleccionar los 10 primeros municipios y guardar el archivo en el path seleccionado con el encabezado
df3_desc_10 = df3_desc.select("Municipio", "Poblacion").limit(10)
df3_desc_10.write.format('csv').option('header', True).mode('overwrite').option('sep',',')\
   .save('/home/bigdata/Escritorio/pec/ej3-municipios-mayor-pob')

# Apartado a: Mostrar lo mismo incluyendo la Comunidad Autónoma y la Provincia
df3_asc_total_10 = df3_asc.select("Comunidad", "Provincia", "Municipio", "Poblacion").limit(10)
df3_asc_total_10.write.format('csv').option('header', True).mode('overwrite').option('sep',',')\
   .save('/home/bigdata/Escritorio/pec/ej3a-com-prov-mun-menor-pob')

df3_desc_total_10 = df3_desc.select("Comunidad", "Provincia", "Municipio", "Poblacion").limit(10)
df3_desc_total_10.write.format('csv').option('header', True).mode('overwrite').option('sep',',')\
   .save('/home/bigdata/Escritorio/pec/ej3a-com-prov-mun-mayor-pob')

# EJERCICIO 4

## Unir las tablas por el campo Código
df = df_mun.join(df_elec, ["Codigo"])

## Generar la partición y ordenar. Entiendo participación como Votantes más Blancos.
df_part = df.withColumn('Participacion', ((df.Votantes + df.Blanco)/df.Censo)*100)
df4_asc = df_part.sort(df_part.Participacion.asc(), df_part.Municipio.asc())
df4_desc = df_part.sort(df_part.Participacion.desc(), df_part.Municipio.asc())

## Seleccionar los campos deseados, especificar que sean 10 municipios y guardar el archivo
df4_asc = df4_asc.select("Comunidad", "Provincia", "Municipio", "Poblacion", "Censo", "Participacion").limit(10)
df4_asc.write.format('csv').option('header', True).mode('overwrite').option('sep',',')\
    .save('/home/bigdata/Escritorio/pec/ej4-municipios-menor-participacion')

## Seleccionar los campos deseados, especificar que sean 10 municipios y guardar el archivo
df4_desc = df4_desc.select("Comunidad", "Provincia", "Municipio", "Poblacion", "Censo", "Participacion").limit(10)
df4_desc.write.format('csv').option('header', True).mode('overwrite').option('sep',',')\
    .save('/home/bigdata/Escritorio/pec/ej4-municipios-mayor-participacion')

# EJERCICIO 5

## Para este ejercicio hay que comprobar si el número de votantes válidos es igual al de algún partido

## Se crea dataframe vacío
concat = sparkSQL.createDataFrame(sc.emptyRDD(), df.schema)

## Se comprueba para cada partido si el número de votantes validos es igual al de algún partid. En caso de que lo sea, se añade al df.
for i in df.columns[11:]:
   a = df.filter(df.Votantes == df[i])
   concat = concat.union(a)
concat.show()

# EJERCICIO 6

## Se seleccionan los campos necesarios. Se agrupa por provincia, y se obtiene la suma del resto de los campos.
df6 = df.select("Provincia", "Censo", "Votantes", "Blanco").groupby("Provincia").agg(F.sum("Censo").alias("Censo"),
                                                                                     F.sum("Votantes").alias("Votantes"),
                                                                                     F.sum("Blanco").alias("Blanco"))
## Se calcula la participación por provincia
df6 = df6.withColumn('Participacion', ((df6.Votantes + df6.Blanco)/df6.Censo)*100)

## Se ordena el dataframe por la participación, se seleccionan los campos deseados y se imprime el resultado.
df6.select("Provincia", "Participacion").sort(desc("Participacion")).show()


# EJERCICIO 7

## Se genera una función para poder aplicar melt de igual forma que se hace en pandas
def melt(df, id_vars, value_vars, var_name, value_name):
    """Conversion de un dataframe de ancho a largo."""

    _vars_and_vals = F.array(*[F.struct(F.lit(c).alias(var_name),
                                        F.col(c).alias(value_name))
                               for c in value_vars])

    # Add to the DataFrame and explode
    _tmp = df.withColumn("_vars_and_vals", F.explode(_vars_and_vals))

    cols = id_vars + [F.col("_vars_and_vals")[x].alias(x) for x in [var_name, value_name]]
    return _tmp.select(*cols)

## Generar el dataframe de ancho a largo convirtiendo todos los partidos en una columna
df_melted = melt(df, id_vars=df.columns[:11], value_vars=df.columns[11:], var_name="Partido", value_name="Votos")

## Agrupar el dataframe por comunidad y partido y sumar los votos
df_melted_sum = df_melted.select("Comunidad", "Partido", "Votos").groupby(["Comunidad", "Partido"])\
    .agg(F.sum("Votos").alias("Votos"))
## Obtener el partido más votado en cada comunidad.
df_melted_max = df_melted_sum.select("Comunidad", "Votos").groupby("Comunidad").agg(F.max("Votos").alias("Votos"))
## Obtener un dataframe con para cada comunidad, el partido más votado, y el número de votos.
df_melted_com = df_melted_sum.join(df_melted_max, ["Comunidad", "Votos"])
## Renombrar las columnas
df_melted_com = df_melted_com.withColumnRenamed("Votos", "Votos Comunidad")\
    .withColumnRenamed("Partido", "Partido Comunidad")
## Imprimir por pantalla
df_melted_com.show()


## Obtener la comunidad y la población del municipio con mayor población
df_mun_pobl = df.select("Comunidad","Poblacion").groupby("Comunidad").agg(F.max("Poblacion").alias("Poblacion"))

## Obtener dichos municipio
df_mun = df_mun_pobl.join(df, ['Comunidad', 'Poblacion'])

## Generar el dataframe de ancho a largo convirtiendo todos los partidos en una columna
df_mun_melted = melt(df_mun, id_vars=df.columns[:11], value_vars=df.columns[11:],
                     var_name="Partido", value_name="Votos")

## Agrupar por Comunidad y seleccionar el partido con más votos
df_mun_melted_max = df_mun_melted.select("Comunidad", "Votos").groupby("Comunidad")\
    .agg(F.max("Votos").alias("Votos"))
## Obtener un dataframe con la comunidad, el municipio más poblado, el partido más votado y el número de votos
df_melted_mun = df_mun_melted.select("Comunidad", 'Municipio', "Partido", "Votos").join(df_mun_melted_max, ["Comunidad",
                                                                                                            "Votos"])
## Renombrar las columnas
df_melted_mun = df_melted_mun.withColumnRenamed("Votos", "Votos Municipio")\
    .withColumnRenamed("Partido", "Partido Municipio")

## Unir el dataframe con el partido más votado en cada comunidad y en el municipio más poblado de cada comunidad
df_melted_com_mun = df_melted_com.join(df_melted_mun, ["Comunidad"])

## Imprimir por pantalla el resultado final
df_melted_com_mun.select("Comunidad", "Partido Comunidad", "Votos Comunidad",
                         "Municipio", "Partido Municipio", "Votos Municipio").show()

# EJERCICIO 8

# Apartado 8.1

## Ordenar dataframe de forma descente por población
df_pob_desc = df.sort(df.Poblacion.desc(), df.Municipio.asc()).limit(20)
## Conversión a formato largo
df_pob_desc_melted = melt(df_pob_desc, id_vars=df_pob_desc.columns[:11], value_vars=df_pob_desc.columns[11:],
                          var_name="Partido", value_name="Votos")
## Crear ventana por municipio
window = Window.partitionBy(df_pob_desc_melted['Municipio']).orderBy(df_pob_desc_melted['Votos'].desc())
## Generar campo rank para crear un ranking de los partidos más votados en cada municipio
df_pob_desc_melted = df_pob_desc_melted.select(df_pob_desc_melted.columns + [row_number().over(window).alias('rank')])
## Filtrar por dicho campo para obtener los 5 más votados
df_pob_desc_melted = df_pob_desc_melted.filter(df_pob_desc_melted["rank"] < 6).drop("rank")
## Generar participación
df_pob_desc_melted = df_pob_desc_melted.withColumn('Participacion', ((df_pob_desc_melted.Votantes +
                                                                      df_pob_desc_melted.Blanco)/
                                                                     df_pob_desc_melted.Censo)*100)
## Guardar formato largo en un archivo
df_pob_desc_melted.select("Municipio", "Participacion", "Partido", "Votos").write.format('csv').option('header', True)\
    .mode('overwrite').option('sep',',').save('/home/bigdata/Escritorio/pec/ej81-partidos-mas-votados-largo')
## Transformar a formato ancho
df_pob_desc_melted = df_pob_desc_melted.groupby("Municipio", "Participacion").pivot("Partido").sum("Votos")
## Guardar a un archivo y mostrar por pantall formato ancho
df_pob_desc_melted.write.format('csv').option('header', True).mode('overwrite').option('sep',',')\
    .save('/home/bigdata/Escritorio/pec/ej81-partidos-mas-votados-ancho')
df_pob_desc_melted.show()

# Apartado 8.2

## Ordenar dataframe de forma descente por población
df_pob_asc = df.sort(df.Poblacion.desc(), df.Municipio.asc()).filter(df.Poblacion < 10000).limit(20)
## Conversión a formato largo
df_pob_asc_melted = melt(df_pob_asc, id_vars=df_pob_asc.columns[:11], value_vars=df_pob_asc.columns[11:],
                          var_name="Partido", value_name="Votos")
## Crear ventana por municipio
window = Window.partitionBy(df_pob_asc_melted['Municipio']).orderBy(df_pob_asc_melted['Votos'].desc())
## Generar campo rank para crear un ranking de los partidos más votados en cada municipio
df_pob_asc_melted = df_pob_asc_melted.select(df_pob_asc_melted.columns + [row_number().over(window).alias('rank')])
## Filtrar por dicho campo para obtener los 5 más votados
df_pob_asc_melted = df_pob_asc_melted.filter(df_pob_asc_melted["rank"] < 6).drop("rank")
## Generar participación
df_pob_asc_melted = df_pob_asc_melted.withColumn('Participacion', ((df_pob_asc_melted.Votantes +
                                                                      df_pob_asc_melted.Blanco)/
                                                                     df_pob_asc_melted.Censo)*100)
## Guardar formato largo en un archivo
df_pob_asc_melted.select("Municipio", "Participacion", "Partido", "Votos").write.format('csv').option('header', True)\
    .mode('overwrite').option('sep',',').save('/home/bigdata/Escritorio/pec/ej82-partidos-mas-votados-largo')
## Transformar a formato ancho
df_pob_asc_melted = df_pob_asc_melted.groupby("Municipio", "Participacion").pivot("Partido").sum("Votos")
## Guardar a un archivo y mostrar por pantall formato ancho
df_pob_asc_melted.write.format('csv').option('header', True).mode('overwrite').option('sep',',')\
    .save('/home/bigdata/Escritorio/pec/ej82-partidos-mas-votados-ancho')
df_pob_asc_melted.show()
