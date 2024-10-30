# Función para agregar columna prediction_prob con valores aleatorios entre 0 y 1
generate_random_prob <- function(data) {
  data$prediction_prob <- runif(nrow(data), min = 0, max = 1)
  return(data)
}

# Función random_classifier para generar la columna prediction_class
random_classifier <- function(data) {
  data$prediction_class <- ifelse(data$prediction_prob > 0.5, 1, 0)
  return(data)
}

# Cargar el archivo de validación
validation_data <- read.csv("data/arbolado-mendoza-dataset-validation.csv")

# Generar columna prediction_prob y aplicar random_classifier
validation_data <- generate_random_prob(validation_data)
validation_data <- random_classifier(validation_data)

# Convertir la variable objetivo
validation_data$inclinacion_peligrosa <- as.numeric(validation_data$inclinacion_peligrosa == "1")

# Calcular la matriz de confusión
confusion_matrix <- validation_data %>%
  summarise(
    True_Positive = sum(inclinacion_peligrosa == 1 & prediction_class == 1),
    True_Negative = sum(inclinacion_peligrosa == 0 & prediction_class == 0),
    False_Positive = sum(inclinacion_peligrosa == 0 & prediction_class == 1),
    False_Negative = sum(inclinacion_peligrosa == 1 & prediction_class == 0)
  )

print(confusion_matrix)


# Crear un dataframe de la matriz de confusión
confusion_df <- data.frame(
  Prediction = c("Peligroso", "Peligroso", "No Peligroso", "No Peligroso"),
  Actual = c("Peligroso", "No Peligroso", "Peligroso", "No Peligroso"),
  Count = c(confusion_matrix$True_Positive, confusion_matrix$False_Positive, 
            confusion_matrix$False_Negative, confusion_matrix$True_Negative)
)

# Graficar la matriz de confusión usando ggplot2
library(ggplot2)
ggplot(confusion_df, aes(x = Prediction, y = Actual, fill = Count)) +
  geom_tile(color = "white") +
  geom_text(aes(label = Count), vjust = 1) +
  scale_fill_gradient(low = "lightblue", high = "blue") +
  labs(title = "Matriz de Confusión",
       x = "Predicción",
       y = "Actual") +
  theme_minimal()


#6
# Función para calcular Accuracy
accuracy <- function(TP, TN, FP, FN) {
  (TP + TN) / (TP + TN + FP + FN)
}

# Función para calcular Precision
precision <- function(TP, FP) {
  TP / (TP + FP)
}

# Función para calcular Sensitivity (Recall)
sensitivity <- function(TP, FN) {
  TP / (TP + FN)
}

# Función para calcular Specificity
specificity <- function(TN, FP) {
  TN / (TN + FP)
}


# Valores de la matriz de confusión del clasificador aleatorio (del punto 4)
TP_random <- confusion_matrix$True_Positive
TN_random <- confusion_matrix$True_Negative
FP_random <- confusion_matrix$False_Positive
FN_random <- confusion_matrix$False_Negative

# Cálculo de métricas para el clasificador aleatorio
accuracy_random <- accuracy(TP_random, TN_random, FP_random, FN_random)
precision_random <- precision(TP_random, FP_random)
sensitivity_random <- sensitivity(TP_random, FN_random)
specificity_random <- specificity(TN_random, FP_random)

# Imprimir resultados
cat("Métricas para el Clasificador Aleatorio:\n")
cat("Accuracy:", accuracy_random, "\n")
cat("Precision:", precision_random, "\n")
cat("Sensitivity:", sensitivity_random, "\n")
cat("Specificity:", specificity_random, "\n")
