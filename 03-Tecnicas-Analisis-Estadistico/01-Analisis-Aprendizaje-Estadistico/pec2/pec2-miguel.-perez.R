# PEC2 - TÉCNICAS DE ANÁLISIS ESTADÍSTICO

# Path

setwd('/Users/miguel.perezibm.com/Desktop/MIGUEL/Courses/Master/03-Tecnicas-Analisis-Estadistico/01-Analisis-Aprendizaje-Estadistico/06-PEC2')

# Paquetes Necesarios

library(readr)
library(dplyr)
library(ggplot2)
library(stringr)
library(magrittr)
library(car)
library(corrplot)
library(psych)

# Abrir los csv y unir

df1 <- read_csv(paste(getwd(), "/life-expectancy-data.csv", sep=""))
df2 <- read_csv(paste(getwd(), "/Pob-Dens-2015.csv", sep=""))
df2015 <- filter(df1, Year == 2015)
df2014 <- filter(df1, Year == 2014)
df <- merge(df2015, df2, by = 'Country')
df_union_2014 <- merge(df2014, df2, by = 'Country')

# Tratamiento de valores nulos

colnames(df)[colSums(is.na(df)) > 0]

# Alcohol
sum(is.na(df$Alcohol))
sum(is.na(df1$Alcohol))
sum(is.na(df_union_2014$Alcohol))
df$Alcohol <- df_union_2014$Alcohol

# HepatitisB
sum(is.na(df$`Hepatitis B`))
sum(is.na(df1$`Hepatitis B`))

# BMI
sum(is.na(df$BMI))

# Total Expenditure
sum(is.na(df$`Total expenditure`))
sum(is.na(df1$`Total expenditure`))
sum(is.na(df_union_2014$`Total expenditure`))
df$`Total expenditure` <- df_union_2014$`Total expenditure`

# GDP
sum(is.na(df$GDP))
sum(is.na(df1$GDP))

# Thinness 1-19 years
sum(is.na(df$`thinness  1-19 years`))

# Thinness 5-9 years
sum(is.na(df$`thinness 5-9 years`))

# Income composition of resources
sum(is.na(df$`Income composition of resources`))
sum(is.na(df1$`Income composition of resources`))

# Schooling
sum(is.na(df$Schooling))
sum(is.na(df1$Schooling))


# Eliminar variables

borrar_variables <- c("Hepatitis B", "GDP", "Population", "Schooling", "Year",
                      "Income composition of resources", "under-five deaths")
df <- dplyr::select(df, -all_of(borrar_variables))
df <- na.omit(df)

# Variable Status como factor

df$Status <- ifelse(df$Status == 'Developing', 0, 1)
df$Status <- as.factor(df$Status)

# Variable Med Age como Numeric

df$`Med. Age` <- as.numeric(df$`Med. Age`)


# Modificar Nombres por Comodidad

df <- df %>% rename_at(vars(c('Status', 'Life expectancy', 'Adult Mortality', 
                              'infant deaths', 'Alcohol', 
                              'percentage expenditure', 'Measles', 'BMI',
                              'Polio', 'Total expenditure', 'Diphtheria', 
                              'HIV/AIDS',  'Med. Age', 'thinness  1-19 years', 
                              'thinness 5-9 years', 'Poblacion 2015', 
                              'Densidad (P/Km2)', 'Country')), 
                       ~ c('des', 'esp', 'mort_a', 'mort_i', 'alc', 'per_exp', 
                           'sar', 'bmi', 'pol', 'tot_exp', 'diph', 'hiv_aids', 
                           'ed_med', 'th5', 'th19', 'pob', 'd_pob', 'pais'))

# Análisis variables

summary(df)

multi.hist(x = df[,3:8], dcol = c("blue", "red"), dlty = c("dotted", "solid"),
           main = c('esp vida', 'mort adulta', 'mort infantil', 
                    'alcohol', 'per exp', 'sar'))

multi.hist(x = df[,9:14], dcol = c("blue", "red"), dlty = c("dotted", "solid"),
           main = c('bmi', 'polio', 'tot_exp', 'diphtheria', 'hiv/aids',
                    'thinness 1-5'))

multi.hist(x = df[,15:18], dcol = c("blue", "red"), dlty = c("dotted", "solid"),
           main = c('thinness 1-19', 'edad media', 'poblacion', 'dens pob'))

cor.test(df$th19,df$th5)
df <- dplyr::select(df, -all_of(c("th19", "per_exp")))


# Modelo Inicial

modelo <- lm(formula = esp ~ des + mort_a + mort_i + alc + sar + bmi + pol + 
               tot_exp + diph + hiv_aids + ed_med + th5 + pob + d_pob, 
             data = df)

summary(modelo)

# Selección de Variables

step(object = modelo, direction = "both", trace = 0)

# Intervalo de confianza

confint(lm(formula = esp ~ mort_a + tot_exp + diph + hiv_aids + ed_med + th5, 
           data = df))

# Nuevo Modelo

modelo_final <- lm(formula = esp ~ mort_a + tot_exp + diph + hiv_aids + ed_med + 
                     th5, data = df)

summary(modelo_final)

# Correlación

corrplot(cor(dplyr::select(df, esp, mort_a, tot_exp, diph, hiv_aids, ed_med, 
                           th5)),
         method = "number", tl.col = "black")

# Factor de Inflación de la Varianza (VIF)

vif(modelo_final)

# Graficar el modelo

par(mfrow = c(1,1))
plot(modelo_final)

# Modelo sin incluir mortalidad

modelo_sin_mort <- lm(formula = esp ~ tot_exp + diph + hiv_aids + ed_med + th5, 
                      data = df)

summary(modelo_sin_mort)
