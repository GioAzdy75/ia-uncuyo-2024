# Función para agregar columna prediction_prob con valores aleatorios entre 0 y 1
generate_random_prob <- function(data) {
  data$prediction_prob <- runif(nrow(data), min = 0, max = 1)
  return(data)
}
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
# Función biggerclass_classifier para predecir siempre la clase mayoritaria
biggerclass_classifier <- function(data) {
  # Encontrar la clase mayoritaria
  majority_class <- as.numeric(names(sort(table(data$inclinacion_peligrosa), decreasing = TRUE))[1])
  
  # Asignar la clase mayoritaria a la columna prediction_class
  data$prediction_class <- majority_class
  return(data)
}

# Cargar el archivo de validación
validation_data <- read.csv("data/arbolado-mendoza-dataset-validation.csv")

# Aplicar el clasificador de clase mayoritaria
validation_data <- biggerclass_classifier(validation_data)

# Calcular la matriz de confusión usando dplyr
library(dplyr)

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

# Graficar la matriz de confusión
library(ggplot2)
ggplot(confusion_df, aes(x = Prediction, y = Actual, fill = Count)) +
  geom_tile(color = "white") +
  geom_text(aes(label = Count), vjust = 1) +
  scale_fill_gradient(low = "lightblue", high = "blue") +
  labs(title = "Matriz de Confusión (Clasificador Clase Mayoritaria)",
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


# Valores de la matriz de confusión del clasificador de clase mayoritaria (del punto 5)
TP_majority <- confusion_matrix$True_Positive
TN_majority <- confusion_matrix$True_Negative
FP_majority <- confusion_matrix$False_Positive
FN_majority <- confusion_matrix$False_Negative

# Cálculo de métricas para el clasificador de clase mayoritaria
accuracy_majority <- accuracy(TP_majority, TN_majority, FP_majority, FN_majority)
precision_majority <- precision(TP_majority, FP_majority)
sensitivity_majority <- sensitivity(TP_majority, FN_majority)
specificity_majority <- specificity(TN_majority, FP_majority)

# Imprimir resultados
cat("\nMétricas para el Clasificador de Clase Mayoritaria:\n")
cat("Accuracy:", accuracy_majority, "\n")
cat("Precision:", precision_majority, "\n")
cat("Sensitivity:", sensitivity_majority, "\n")
cat("Specificity:", specificity_majority, "\n")


