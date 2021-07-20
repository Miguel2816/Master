# PEC - Entornod de Análisis de datos R

setwd('/Users/miguel.perezibm.com/Desktop/MIGUEL/Courses/Master/02-Herramientas-de-Analisis/02-Entornos-Analisis-Datos-R/05-PEC')

# 2 Importa el dataset a R con readr, exporta un subconjunto del dataset 
# consistente en las 5 columnas que mas te gusten del mismo a formato csv. 
# Interpreta estas columnas.

library(readr)
library(dplyr)
df <- read_csv(paste(getwd(), "/Flights.csv", sep=""))
df_reduced <- select(df, 'dep_delay', 'arr_delay', 'air_time', 'distance',
                     'origin')
write_csv(df_reduced, paste(getwd(), "/Flights_reduced.csv", sep=""))


# 3.	Se deben elegir 5 variables reales o enteras y se debe calcular su media,
# mediana y moda. Filtra los valores ausentes.

df_est <- select(df, 'dep_delay', 'arr_delay', 'air_time', 'distance',
                        'hour')

get_mode <- function(col) {
  col<-col[!is.na(col)]
  uniq_col <- unique(col)
  uniq_col[which.max(tabulate(match(col, uniq_col)))]
}

media_dep_delay <- mean(df_est$dep_delay, na.rm = TRUE)
mediana_dep_delay <- median(df_est$dep_delay, na.rm = TRUE)
moda_dep_delay <- get_mode(df_est$dep_delay)

media_arr_delay <- mean(df_est$arr_delay, na.rm = TRUE)
mediana_arr_delay <- median(df_est$arr_delay, na.rm = TRUE)
moda_arr_delay <- get_mode(df_est$arr_delay)

media_air_time <- mean(df_est$air_time, na.rm = TRUE)
mediana_air_time <- median(df_est$air_time, na.rm = TRUE)
moda_air_time <- get_mode(df_est$air_time)

media_distance <- mean(df_est$distance, na.rm = TRUE)
mediana_distance <- median(df_est$distance, na.rm = TRUE)
moda_distance <- get_mode(df_est$distance)

media_hour <- mean(df_est$hour, na.rm = TRUE)
mediana_hour <- median(df_est$hour, na.rm = TRUE)
moda_hour <- get_mode(df_est$hour)

# 4.	Se debe ordenar los valores de una variable real y eliminar el 10% de
# valores más elevados y bajos (eliminación de outliers) donde esta operación
# pueda tener sentido.

library(ggplot2)
ggplot(data=df, aes(arr_delay)) + geom_histogram(bins = 30)

df_order_arr_delay <- arrange(df, arr_delay)
df_order_arr_delay <- select(df_order_arr_delay, 'arr_delay')

long_90 <- as.integer(as.integer(paste(dim(df_order_arr_delay)[1]))*0.9)
df_order_arr_delay <- df_order_arr_delay[1:long_90,]

ggplot(data=df_order_arr_delay, aes(arr_delay)) +
  geom_histogram(bins = 30)

# 5. Se debe adjuntar un gráfico de puntos de dos variables reales donde se
# pueda apreciar una correlación entre ambas (a mayor valor de una variable,
# menor de otra o viceversa). Sino existen 2 variables así en tu dataset,
# comenta que observas en el gráfico con 2 variables cualquiera.

ggplot(data=df) + geom_point(mapping=aes(x=distance, y=air_time))

# 6.	Crea una variable adicional con respecto a las que tenga tu dataset que
# sea el resultado de dividir una variable real entre otra variable real.

df$speed <- df$distance/df$air_time

# 7.	Filtra los datos de tu dataset para solo tener las instancias
# correspondientes a los meses de enero, febrero y marzo. Si tu dataset no
# tiene fechas, crea una variable adicional fecha que ponga una fecha aleatoria
# para cada instancia y filtra tu dataset por la fecha.

library(plyr)
df$new_month <- mapvalues(df$month,
                          from=c("1","2","3","4","5"),
                          to=c("Enero","Febrero","Marzo","Abril","Mayo"))

df_ene_feb_mar <- filter(df, new_month %in% (c("Enero","Febrero","Marzo")))

# 8.	Devuelve todas las instancias que cumplan que una variable alfanumérica 
# tenga la letra ‘a’. Si tu dataset no tiene una variable alfanumérica, genera 
# una variable cuyos valores alfanuméricos sean letras (‘a’,…,’z’) aleatorias y 
# devuelve solo las instancias cuyo valor para la variable alfanumérica sea ‘a’.

library(stringr)
df_a <- df[grepl('a', str_to_lower(df$new_month)),]

# 9.	Ordena una variable real y devuelve las 10 instancias con mayor valor para 
# esa variable.

df_order_arr_delay_desc <- arrange(df, desc(arr_delay))
order_arr_delay_desc <- df_order_arr_delay_desc[1:10,]$arr_delay
paste(order_arr_delay_desc)

# 10.	A partir de una variable real, haz una variable categórica factor cuyo 
# valor sea A si el valor es superior a la mediana y B si el valor es inferior 
# a la mediana.

df$factor_variable <- ifelse(df$distance > mediana_distance, "A", "B") 

# 11.	Imprime un gráfico de facetas en rejilla cuyas gráficas sean gráficas de 
# puntos que muestre los datos de 2 variables real y una categórica.

ggplot(data=df) + geom_point(mapping=aes(x=distance, y=air_time)) +
  facet_wrap(~ new_month, nrow = 2)

# 12.	Se debe adjuntar un gráfico de puntos de 2 variables reales en el cuál se 
# muestren con colores los valores de una variable categórica o factor o una 
# variable alfanumérica.

ggplot(data=df) + geom_point(mapping=aes(x=distance, y=air_time, 
                                         color=origin))

# 13.	Se debe calcular la media y desviación típica de los 10 valores más altos 
# de una variable real filtrada por un valor de una variable categórica de un 
# día de cada mes a elegir por el alumno de una variable que represente una 
# fecha.

df_dia_1 <- filter(df, day == 1)
df_dia_1 <- arrange(df_dia_1, desc(air_time))[1:10,]
df_dia_1_nueve <- arrange(df_dia_1, desc(air_time))[1:9,]

media_air_time_10 <- mean(df_dia_1$air_time)
sd_air_time_10 <- sd(df_dia_1$air_time)

media_air_time_9 <- mean(df_dia_1_nueve$air_time)
sd_air_time_9 <- sd(df_dia_1_nueve$air_time)

# 14.	Se debe generar un gráfico de barras similar al mostrado en la primera 
# figura del apartado 3.8 del libro de Data Science de las variables de tu 
# dataset que prefieras.

ggplot(data = df) +
  geom_bar(mapping = aes(x = origin, colour = new_month))

ggplot(data = df) +
  geom_bar(mapping = aes(x = origin, fill = new_month))

# 15.	Describe para que sirven. los pipes en R y pon un ejemplo con tu conjunto 
# de datos en el que uses, para una operación, 3 pipes consecutivos.

library(magrittr)
library(lubridate)

df_day_freq <- df %>%
  mutate(date = make_date(year, month, day)) %>%
  dplyr::count(date, sort = TRUE) %>%
  slice(1:10)

# 16.	Haz un gráfico de cajas de una variable real y otra categórica.

ggplot(data = df, mapping = aes(x = origin, y = distance)) +
  geom_boxplot()

# 17.	Devuelve la moda de letras ‘a’ de una variable alfanumérica de todas sus 
# instancias.

month_count_a <- str_count(str_to_lower(df$new_month), "a")
month_mode_a <- get_mode(month_count_a)

# 18.	Crea una columna que contenga un periodo de tiempo en semanas entre dos 
# columnas previas. Sino dispones de esta información en tu dataset, crea 
# columnas sintéticamente.

df$date <- paste(df$year, df$month, df$day, sep="-") %>% ymd() %>% as.Date()
df$date_random <- sample(seq(as.Date('2015-01-01'), as.Date('2016-01-01'), 
                           by="day"), dim(df)[1], replace = TRUE)
df$diff_in_weeks <- as.numeric(difftime(df$date_random, df$date, 
                                        units = c('weeks')))
df <- df %>% select('year':'date', 'diff_in_weeks', 'date_random')

# 19.	Devuelve el sumatorio de los valores de una variable real agrupados por 
# una variable categórica o por mes de una variable de fecha.

df_sum_air_time <- aggregate(df$air_time, by=list(Meses=df$new_month), 
                             FUN=sum) %>%
  arrange(desc(x))

# 20.	¿Podrías predecir una variable real en base a otras variables de tu 
# dataset? Razona como lo harías.

# Primer método con gráfica

ggplot(data = df, mapping = aes(x = distance, y = air_time)) +
  geom_point() +
  geom_smooth(se = FALSE)

# Segundo método con uso de un modelo

model <- lm(air_time ~ distance, data = df)
model
new_distance <- data.frame(
  distance = c(1000, 2000, 2475)
)
predict(model, newdata = new_distance)

# 21.	Realiza dos visualizaciones no vistas en clase que involucren a un mínimo 
# de 3 variables. Consulta la cheatsheet de R de ggplot2. Interprétalas.

df$weekday <- weekdays(df$date)
df$weekend <- mapvalues(df$weekday,
                        from=c('Monday', 'Tuesday', 'Wednesday', 'Thursday',
                               'Friday', 'Saturday', 'Sunday'),
                        to=c('No','No','No','No','No','Si','Si'))

ggplot(data = df, mapping = aes(x = origin, y = distance)) +
  geom_violin(aes(fill = weekend))

df_may_11 <- df %>%
  dplyr::filter(day == 11 & month == 5 & origin == 'LGA') %>%
  mutate(factor_variable=recode(factor_variable,
                                'A' = 0,
                                'B' = 1)) %>%
  select('dest', 'air_time', 'distance', 'factor_variable') %>%
  group_by(dest) %>%
  summarise_all(mean)

ggplot(df_may_11, aes(distance, air_time, label = dest)) + 
  geom_text(position=position_jitter(width=1,height=1))

# 22.	Devuelve un resumen de estadísticos de las variables que consideras más 
# importantes e interprétalo.

library(fBasics)

stats <- df %>%
  select('dep_delay', 'arr_delay', 'air_time', 'distance', 'hour')

stats <- basicStats(stats)[c("Mean", "Stdev", "Variance", "1. Quartile", 
                             "Median", "3. Quartile", "Minimum", "Maximum"),]

df_distance_5000 <- df %>%
  dplyr::filter(distance > 4000)

# 23.	Realiza una visualización no vista en clase y distinta de la del apartado 
# 21 que involucre un mínimo de 4 variables. Interprétala.

df_delay <- df %>%
  dplyr::filter(new_month %in% c('Enero', 'Febrero', 'Marzo', 'Abril')) %>%
  select('day', 'new_month', 'origin', 'arr_delay') %>%
  group_by(new_month, day, origin) %>%
  summarise_all(mean)
  
ggplot(data = df_delay, 
       mapping = aes(x = day, y = arr_delay, color = origin)) +
  geom_line() +
  facet_wrap(vars(new_month)) +
  theme_bw()

# 24.	Haz un ejemplo que involucre 5 pipes seguidos. Interprétalo.

df_may_11 <- df %>%
  dplyr::filter(day == 11 & month == 5 & origin == 'LGA') %>%
  mutate(factor_variable=recode(factor_variable,
                                'A' = 0,
                                'B' = 1)) %>%
  select('dest', 'air_time', 'distance', 'factor_variable') %>%
  group_by(dest) %>%
  summarise_all(mean)

# 25. En función a tu conjunto de datos, presenta las 5 conclusiones que, en tu
# opinión, son más relevantes y pueden aportar más información del conjunto de
# datos que has elegido. Apoya tu decisión con gráficos, análisis univariantes y
# multivariantes de variables que consideres necesarias. No dudes en emplear 
# conocimiento propio no visto durante el curso y que pueda encontrarse en el 
# libro R for Data Science o que conozcas previamente.

# Primera conclusión

df_date_freq <- df %>%
  dplyr::count(date, weekday, sort = TRUE) %>%
  slice(1:50)

ggplot(data=df_date_freq, aes(weekday)) +
  geom_bar()

# Segunda conclusión

corr_dist_air_time <- cor(df$distance, df$air_time)

# Tercera conclusión

ggplot(data=df) + geom_point(mapping=aes(x=dep_delay, y=arr_delay))
corr_delay <- cor(df$dep_delay, df$arr_delay)

# Cuarta conclusión

df_hour <- df %>%
  dplyr::count(hour)

ggplot(data=df_hour, aes(x = hour, y = n)) +
  geom_col()

# Quinta conclusión

df_freq_dest <- count(df, c('dest')) %>%
  arrange(desc(freq))
head_5_dest <- head(df_freq_dest, 5)

ggplot(data=head_5_dest, aes(x = dest, y = freq)) +
  geom_col()
