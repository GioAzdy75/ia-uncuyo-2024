library(ggplot2)
library(dplyr)

# Cargar Datos
train_data <- read.csv("data/arbolado-mendoza-dataset-train.csv")

# factor
train_data$inclinacion_peligrosa <- as.factor(train_data$inclinacion_peligrosa)
train_data$seccion <- as.factor(train_data$seccion)

train_data$inclinacion_peligrosa <- as.numeric(as.character(train_data$inclinacion_peligrosa))

result <- train_data %>%
  dplyr::group_by(especie) %>%
  dplyr::summarize(peligrosa=sum(inclinacion_peligrosa)/ifelse(n() == 0, sum(inclinacion_peligrosa), n()), total=1)

result$especie = reorder(result$especie, -result$peligrosa)
ggplot(data=result, aes(x=especie, fill="a")) +
  geom_bar(aes(y=total), stat="identity", position = "dodge", alpha=1, width=0.7, fill="skyblue") +
  labs(title="Inclinación Peligrosa por Especie", x="Especie", y="Proporción de Inclinación Peligrosa") +
  geom_bar(aes(y=peligrosa), data = result, stat = "identity", position="dodge", alpha = 1, width=0.7, fill="red") +
  scale_x_discrete(breaks = result$especie, expand = c(0, 0))+
  scale_fill_manual(values = c("Total" = "skyblue", "Peligrosas" = "red")) +
  guides(fill = guide_legend(title = "Por especie")) +
  theme_minimal()+
  theme(axis.text.x = element_text(angle = 90, hjust = 1))


result <- train_data %>%
  dplyr::mutate(inclinacion_peligrosa = as.numeric(as.character(inclinacion_peligrosa))) %>%
  dplyr::group_by(especie) %>%
  dplyr::summarize(peligrosa = sum(inclinacion_peligrosa, na.rm = TRUE), total = n())

# Reordenar
result$especie <- reorder(result$especie, -result$total)

# Gráfico de barras
ggplot(data = result) +
  geom_bar(aes(x = especie, y = total, fill = "Total"), stat = "identity", position = "dodge", alpha = 1, width = 0.7) +
  geom_bar(aes(x = especie, y = peligrosa, fill = "Peligrosas"), stat = "identity", position = "dodge", alpha = 1, width = 0.7) +
  labs(title = "Inclinación Peligrosa por Especie", x = "Especie", y = "Total de Arboles") +
  scale_fill_manual(values = c("Total" = "skyblue", "Peligrosas" = "red")) +
  guides(fill = guide_legend(title = "Tipo")) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
