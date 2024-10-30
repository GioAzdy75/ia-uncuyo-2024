# Cargar Datos
train_data <- read.csv("data/arbolado-mendoza-dataset-train.csv")


#Hist 1
hist(train_data$circ_tronco_cm, breaks = 5, 
     main = "Histograma de circ_tronco_cm con 5 Bins",
     xlab = "circ_tronco_cm", col = "skyblue")
#Hist 2
hist(train_data$circ_tronco_cm, breaks = 10, 
     main = "Histograma de circ_tronco_cm con 10 Bins",
     xlab = "circ_tronco_cm", col = "lightgreen")
#Hist 3
hist(train_data$circ_tronco_cm, breaks = 15, 
     main = "Histograma de circ_tronco_cm con 15 Bins",
     xlab = "circ_tronco_cm", col = "purple")
#Hist 4
hist(train_data$circ_tronco_cm, breaks = 20, 
     main = "Histograma de circ_tronco_cm con 20 Bins",
     xlab = "circ_tronco_cm", col = "pink")
##Hist 5
hist(train_data$circ_tronco_cm, breaks = 40, 
     main = "Histograma de circ_tronco_cm con 40 Bins",
     xlab = "circ_tronco_cm", col = "coral")
