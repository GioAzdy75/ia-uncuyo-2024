# Cargar Datos
train_data <- read.csv("data/arbolado-mendoza-dataset-train.csv")

# factor
train_data$inclinacion_peligrosa <- as.factor(train_data$inclinacion_peligrosa)

# Histograma de circ_tronco_cm separado por inclinación peligrosa
library(ggplot2)
ggplot(train_data, aes(x = circ_tronco_cm, fill = inclinacion_peligrosa)) +
  geom_histogram(bins = 15, position = "dodge") +
  labs(title = "Histograma de circ_tronco_cm por inclinación peligrosa",
       x = "circ_tronco_cm", y = "Frecuencia") +
  theme_minimal() +
  scale_fill_manual(values = c("skyblue", "salmon"), 
                    name = "Inclinación Peligrosa")
