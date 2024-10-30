library(ggplot2)
library(dplyr)
# Cargar Datos
train_data <- read.csv("data/arbolado-mendoza-dataset-train.csv")

# Factor
train_data$inclinacion_peligrosa <- as.factor(train_data$inclinacion_peligrosa)
train_data$seccion <- as.factor(train_data$seccion)

# Gráfico de barras para la inclinación peligrosa por sección
ggplot(train_data, aes(x = seccion, fill = inclinacion_peligrosa)) +
  geom_bar(position = "fill") +
  labs(title = "Inclinación Peligrosa por Sección",
       x = "Sección", y = "Proporción de Inclinación Peligrosa") +
  theme_minimal() +
  scale_fill_manual(values = c("0" = "skyblue", "1" = "red"))



# Asegúrate de que inclinacion_peligrosa sea numérico
train_data$inclinacion_peligrosa <- as.numeric(as.character(train_data$inclinacion_peligrosa))

result <- train_data %>%
  dplyr::group_by(seccion) %>%
  dplyr::summarize(peligrosa = sum(inclinacion_peligrosa, na.rm = TRUE), total = n(), .groups = 'drop')

# Crear el gráfico
ggplot(data = result) +
  geom_bar(aes(x = seccion, y = total, fill = "Total"), stat = "identity", position = "dodge", alpha = 1, width = 0.7) +
  geom_bar(aes(x = seccion, y = peligrosa, fill = "Peligrosas"), stat = "identity", position = "dodge", alpha = 1, width = 0.7) +
  labs(title = "Por Sección", x = "Sección", y = "Total") +
  scale_fill_manual(values = c("Total" = "skyblue", "Peligrosas" = "red")) +
  guides(fill = guide_legend(title = "Tipo")) +
  theme_minimal() +
  scale_x_discrete(expand = c(0, 0))



