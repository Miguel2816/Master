# PEC1 - TÉCNICAS DE ANÁLISIS ESTADÍSTICO

# PARTE 1

setwd('/Users/miguel.perezibm.com/Desktop/MIGUEL/Courses/Master/03-Tecnicas-Analisis-Estadistico/01-Analisis-Aprendizaje-Estadistico/05-PEC1')

# Ejercicio 1:

# apartado a:

library(readr)
matches <- read_csv(paste(getwd(), "/matchesA.csv", sep=""))

# apartado b:

mean_goldEarned <- sum(matches$goldEarned)/length(matches$goldEarned)
paste(mean_goldEarned)

# apartado c:

mean_goldEarned1 <- mean(matches$goldEarned)
paste(mean_goldEarned1)

# apartado d:

sd_goldEarned <- sqrt(sum((matches$goldEarned - mean_goldEarned)^2) / 
                       (length(matches$goldEarned)-1))
paste(sd_goldEarned)

# apartado e:

sd_goldEarned1 <- sd(matches$goldEarned)
paste(sd_goldEarned1)

# apartado f:

max_goldEarned <- max(matches$goldEarned)
min_goldEarned <- min(matches$goldEarned)
range_goldEarned <-paste(c("[", min_goldEarned, "-", max_goldEarned, "]"),
                         collapse = "")

table_goldEarned <- matrix(c(max_goldEarned, min_goldEarned, range_goldEarned),
                           ncol = 3, byrow = TRUE)

colnames(table_goldEarned) <- c("Máximo", "Mínimo", "Rango")

table_goldEarned <- as.table(table_goldEarned)
write.table(table_goldEarned, file = "ej1-apf.txt", sep = ",")

# apartado g:

quartile_goldEarned <- quantile(matches$goldEarned, c(0.25, 0.5, 0.75))

table_quantile <- matrix(c(quartile_goldEarned[1], quartile_goldEarned[2], 
                           quartile_goldEarned[3]),
                           ncol = 3, byrow = TRUE)

colnames(table_quantile) <- c("Q1", "Q2", "Q3")

table_quantile <- as.table(table_quantile)
write.table(table_quantile, file = "ej1-apg.txt", sep = ",")

# apartado h:

library(ggplot2)
ggplot(data=matches, aes(goldEarned)) + geom_histogram()

# Ejercicio 2:

matches$kda <- ifelse(matches$deaths==0, round(2*(matches$kills+matches$assists), 
                                                 digits=2), 
                      round((matches$kills + matches$assists)/matches$deaths,
                      digits=2))
library(magrittr)
library(dplyr)

matches_sample <- matches %>%
  select("kills", "deaths", "assists", "kda") %>%
  sample_n(10)
write.table(matches_sample, file = "ej2.txt", sep = ",", row.names=FALSE)

# Ejercicio 3:

# apartado a:

matches_win <- filter(matches, win == TRUE)
matches_lost <- filter(matches, win == FALSE)

mean_goldEarned_win <- round(mean(matches_win$goldEarned), digits=2)
mean_goldEarned_lost <- round(mean(matches_lost$goldEarned), digits=2)

table_mean <- matrix(c(mean_goldEarned_win, mean_goldEarned_lost),
                         ncol = 2, byrow = TRUE)

colnames(table_mean) <- c("Media Partidas Ganadas", "Media Partidas Perdidas")

table_mean <- as.table(table_mean)
write.table(table_mean, file = "ej3-apa.txt", sep = ",", row.names=FALSE)

# apartado b:

sd_goldEarned_win <- round(sd(matches_win$goldEarned), digits=2)
sd_goldEarned_lost <- round(sd(matches_lost$goldEarned), digits=2)

table_sd <- matrix(c(sd_goldEarned_win, sd_goldEarned_lost),
                     ncol = 2, byrow = TRUE)

colnames(table_sd) <- c("Sd Partidas Ganadas", "Sd Partidas Perdidas")

table_sd <- as.table(table_sd)
write.table(table_sd, file = "ej3-apb.txt", sep = ",", row.names=FALSE)

# apartado c:

median_goldEarned_win <- median(matches_win$goldEarned)
median_goldEarned_lost <- median(matches_lost$goldEarned)

table_mediana <- matrix(c(median_goldEarned_win, median_goldEarned_lost),
                   ncol = 2, byrow = TRUE)

colnames(table_mediana) <- c("Mediana Partidas Ganadas", 
                             "Mediana Partidas Perdidas")

table_mediana <- as.table(table_mediana)
write.table(table_mediana, file = "ej3-apc.txt", sep = ",", row.names=FALSE)

# apartado d:

quartile_goldEarned_win <- quantile(matches_win$goldEarned, c(0.25, 0.5, 0.75))
quartile_goldEarned_lost <- quantile(matches_lost$goldEarned, c(0.25, 0.5, 0.75))

table_quartile <- matrix(c(quartile_goldEarned_win[1], 
                           quartile_goldEarned_win[2],
                           quartile_goldEarned_win[3],
                           quartile_goldEarned_lost[1],
                           quartile_goldEarned_lost[2],
                           quartile_goldEarned_lost[3]),
                        ncol = 3, byrow = TRUE)

colnames(table_quartile) <- c("Q1", "Q2", "Q3")
rownames(table_quartile) <- c("Partidas Ganadas","Partidas Perdidas")

table_quartile <- as.table(table_quartile)
write.table(table_quartile, file = "ej3-apd.txt", sep = ",")

# apartado e:

table_win_lost <- matrix(c(mean_goldEarned_win, sd_goldEarned_win, 
                           quartile_goldEarned_win[1], 
                           median_goldEarned_win,
                           quartile_goldEarned_win[3],
                           mean_goldEarned_lost, sd_goldEarned_lost,
                           quartile_goldEarned_lost[1],
                           median_goldEarned_lost,
                           quartile_goldEarned_lost[3],
                           mean_goldEarned, sd_goldEarned,
                           quartile_goldEarned[1], quartile_goldEarned[2], 
                           quartile_goldEarned[3]), ncol = 5, byrow = TRUE)

colnames(table_win_lost) <- c("Mean","Sd","Quartile 25%", "Median", 
                              "Quartile 75%")
rownames(table_win_lost) <- c("Partidas Ganadas","Partidas Perdidas", 
                              "Partidas Totales")

table_win_lost <- as.table(table_win_lost)
write.table(table_win_lost, file = "ej3-ape.txt", sep = ",")

# Ejercicio 4:

# apartado a

boosterpacks <- read_csv(paste(getwd(), "/boosterPacksA.csv", sep=""))

# apartado b

total_cartas <- 5*dim(boosterpacks)[1]

frec_abs_com <- sum(boosterpacks$Com)
frec_abs_rare <- sum(boosterpacks$Rare)
frec_abs_grare <- sum(boosterpacks$gRare)
frec_abs_dorada <- sum(boosterpacks$gCom) + sum(boosterpacks$gRare) +
  sum(boosterpacks$gEpic) + sum(boosterpacks$gLeg)
frec_abs_no_dorada <- total_cartas - frec_abs_dorada

frec_rel_com <- round(frec_abs_com/total_cartas, digits=2)
frec_rel_rare <- round(frec_abs_rare/total_cartas, digits=2)
frec_rel_grare <- round(frec_abs_grare/total_cartas, digits=2)
frec_rel_dorada <- round(frec_abs_dorada/total_cartas, digits=2)
frec_rel_no_dorada <- round(frec_abs_no_dorada/total_cartas, digits=2)

boosterpacks_freq <- matrix(c(frec_abs_com, frec_abs_rare, frec_abs_grare, 
                           frec_abs_no_dorada, frec_abs_dorada,
                           frec_rel_com, frec_rel_rare, frec_rel_grare, 
                           frec_rel_no_dorada, frec_rel_dorada), 
                         ncol = 5, byrow = TRUE)

colnames(boosterpacks_freq) <- c("Com", "Rare", "gRare", "No Dorada", "Dorada")
rownames(boosterpacks_freq) <- c("Cartas Totales", "Prob. relativa")

boosterpacks_freq <- as.table(boosterpacks_freq)
write.table(boosterpacks_freq, file = "ej4-apb.txt", sep = ",")

# Ejercicio 5:

# apartado a:

dbinom(1,size = 30, prob = 0.034)

# apartado b:

pbinom(3,size = 30, prob = 0.034)

# apartado c:

1 - pbinom(15,size = 30, prob = 0.034)


# Ejercicio 6 

# apartado a:

dbinom(2,size = 12, prob = 0.32)

# apartado b:

1-dbinom(12, size= 12, prob = 0.32)

# apartado c:

pbinom(8, size = 12, prob = 0.32) - pbinom(3, size = 12, prob = 0.32)

# apartado d:

cum_probs <- pbinom(0:12, size = 12, prob = 0.32)
tiro <- c(0:12)

library(tibble)
cum_probs_df <- tibble(cum_probs, tiro)
ggplot(cum_probs_df, aes(x = tiro, y = cum_probs)) + geom_step() +
  scale_x_continuous(breaks = seq(0, 12, by = 1))

# Ejercicio 7:

# apartado a:

dpois(0, lambda = 3)

# apartado b:

1 - ppois(5, lambda = 3)

# apartado c:

ppois(4, lambda = 3) - ppois(1, lambda = 3)

# apartado d:

cum_probs_pepitas <- ppois(0:5, lambda = 3)
pepitas <- c(0:5)

cum_probs_pepitas_df <- tibble(cum_probs_pepitas, pepitas)
ggplot(cum_probs_pepitas_df, aes(x = pepitas, y = cum_probs_pepitas)) + 
  geom_step() + scale_x_continuous(breaks = seq(0, 5, by = 1))

# Ejercicio 8:

# apartado a1:

1 - pnorm(125, mean = 100, sd = 16)

# apartado a2:

pnorm(120, mean = 100, sd = 16) - pnorm(90, mean = 100, sd = 16)

# apartado b1:

nc_8 <- 0.95
alfa_8 <- 1-nc_8
alfa_medios_8 <- alfa_8/2
z_alfa2_8 <- qnorm(1-alfa_medios_8)

media_muestral_8 <- 96
n_8 <- 50
s_8 <- 16

int_izq_8 <- media_muestral_8 - z_alfa2_8*(s_8/sqrt(n_8))
int_dch_8 <- media_muestral_8 + z_alfa2_8*(s_8/sqrt(n_8))

int_izq_8
int_dch_8

# apartado b2:

nc_8 <- 0.95
alfa_8 <- 1-nc_8
z_alfa_8 <- qnorm(1-alfa_8)

media_muestral_8 <- 96
media_pob_8 <- 100
n_8 <- 50
s_8 <- 16

z_cero_8 <- (media_muestral_8-media_pob_8)/s_8/sqrt(n_8)

-z_alfa_8
z_cero_8
z_alfa_8

# Ejercicio 9:

# apartado a1:

pnorm(3100, mean = 2950, sd = 300)

# apartado a2:

1 - pnorm(3250, mean = 2950, sd = 300) + pnorm(2750, mean = 2950, sd = 300)

# apartado b1:

nc_9 <- 0.90
alfa_9 <- 1-nc_9
alfa_medios_9 <- alfa_9/2
z_alfa2_9 <- qnorm(1-alfa_medios_9)

media_muestral_9 <- 3000
n_9 <- 40
s_9 <- 300

int_izq_9 <- media_muestral_9 - z_alfa2_9*(s_9/sqrt(n_9))
int_dch_9 <- media_muestral_9 + z_alfa2_9*(s_9/sqrt(n_9))

int_izq_9
int_dch_9

# apartado b2: 

nc_9 <- 0.90
alfa_9 <- 1-nc_9
z_alfa_9 <- qnorm(1-alfa_9)

media_muestral_9 <- 3000
media_pob_9 <- 2950
n_9 <- 40
s_9 <- 300

z_cero_9 <- (media_muestral_9-media_pob_9)/s_9/sqrt(n_9)

-z_alfa_9
z_cero_9
z_alfa_9

# Ejercicio 10:

# apartado a1:

pnorm(5, mean = 5.8, sd = 1.7)

# apartado a2:

pnorm(8, mean = 5.8, sd = 1.7) - pnorm(5, mean = 5.8, sd = 1.7)

# apartado b:

nc_10 <- 0.95
alfa_10 <- 1-nc_10
alfa_medios_10 <- alfa_10/2
z_alfa2_10 <- qnorm(1-alfa_medios_10)

media_muestral_10 <- 6
n_10 <- 35
s_10 <- 1.7

int_izq_10 <- media_muestral_10 - z_alfa2_10*(s_10/sqrt(n_10))
int_dch_10 <- media_muestral_10 + z_alfa2_10*(s_10/sqrt(n_10))

int_izq_10
int_dch_10

