library(dplyr)

dataset <- read.csv("/arbolado-mza-dataset.csv")

set.seed(777)
validation_size <- round(0.2 * nrow(dataset))

validation_indices <- sample(1:nrow(dataset), validation_size)

validation_data <- dataset[validation_indices, ]
train_data <- dataset[-validation_indices, ]

write.csv(validation_data, "C:/Users/yugii/Desktop/repositories/ia-uncuyo-2024/tp-7-2/Datos/arbolado-mendoza-dataset-validation.csv", row.names = FALSE)
write.csv(train_data, "C:/Users/yugii/Desktop/repositories/ia-uncuyo-2024/tp-7-2/Datos/arbolado-mendoza-dataset-train.csv", row.names = FALSE)


print("Se crearon los Dataset")

