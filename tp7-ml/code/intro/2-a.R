# Cargar Datos
train_data <- read.csv("data/arbolado-mendoza-dataset-train.csv")

# Factor
train_data$inclinacion_peligrosa <- factor(train_data$inclinacion_peligrosa,
                                           levels = c(0, 1),
                                           labels = c("No Peligrosa", "Peligrosa"))

# Gráfico de barras con colores diferentes
ggplot(train_data, aes(x = inclinacion_peligrosa, fill = inclinacion_peligrosa)) +
  geom_bar() +
  scale_fill_manual(values = c("No Peligrosa" = "skyblue", "Peligrosa" = "salmon")) +
  labs(title = "Distribución de la Clase Inclinación Peligrosa",
       x = "Inclinación Peligrosa", y = "Cantidad de Observaciones") +
  theme_minimal()
