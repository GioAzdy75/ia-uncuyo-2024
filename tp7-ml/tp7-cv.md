create_folds()
```
create_folds <- function(data, k) {
  set.seed(777)
  indices <- sample(1:nrow(data)) # Mezcla aleatoria de índices
  fold_size <- floor(nrow(data) / k)
  folds <- list()
  
  for (i in 1:k) {
    start <- (i - 1) * fold_size + 1
    end <- min(i * fold_size, nrow(data))
    folds[[paste0("Fold", i)]] <- indices[start:end]
  }
  
  return(folds)
}
```

cross_validation()
```
cross_validation <- function(data, k) {
  folds <- create_folds(data, k)
  metrics <- data.frame(Accuracy = numeric(k), Precision = numeric(k),
                        Sensitivity = numeric(k), Specificity = numeric(k))
  
  # Definir fórmula de entrenamiento
  train_formula <- formula(inclinacion_peligrosa ~ altura + circ_tronco_cm + lat + long + seccion + especie)
  
  # Asegurarse de que los factores tengan los mismos niveles en todo el dataset
  all_levels <- levels(data$especie)
  data$especie <- factor(data$especie, levels = all_levels)
  
  for (i in 1:k) {
    test_indices <- folds[[paste0("Fold", i)]]
    data_train <- data[-test_indices, ]
    data_test <- data[test_indices, ]
    
    # Asegurarse de que 'especie' tenga los mismos niveles en train y test
    data_train$especie <- factor(data_train$especie, levels = all_levels)
    data_test$especie <- factor(data_test$especie, levels = all_levels)
    
    # Entrenar el modelo
    tree_model <- rpart(train_formula, data = data_train)
    
    # Realizar predicciones
    predictions <- predict(tree_model, data_test, type = "class")
    predictions <- as.numeric(as.character(predictions))  # Convertir factores a numéricos
    actual <- data_test$inclinacion_peligrosa
    
    # Calcular métricas
    fold_metrics <- calculate_metrics(predictions, actual)
    metrics[i, ] <- fold_metrics
  }
  
  # Calcular media y desviación estándar
  metrics_summary <- data.frame(
    Metric = c("Accuracy", "Precision", "Sensitivity", "Specificity"),
    Mean = colMeans(metrics),
    StdDev = apply(metrics, 2, sd)
  )
  
  return(metrics_summary)
}
```

![](images/cv.jpg)