library(dplyr)

train_data <- read.csv("data/arbolado-mendoza-dataset-train.csv")

cuts <- train_data %>% 
  summarise(
    min_val = min(circ_tronco_cm, na.rm = TRUE),
    q1 = quantile(circ_tronco_cm, 0.25, na.rm = TRUE),
    median = quantile(circ_tronco_cm, 0.50, na.rm = TRUE),
    q3 = quantile(circ_tronco_cm, 0.75, na.rm = TRUE),
    max_val = max(circ_tronco_cm, na.rm = TRUE)
  ) %>% 
  unlist()

tags <- c("bajo", "medio", "alto", "muy alto")

# Crea la variable categórica circ_tronco_cm_cat
train_data <- train_data %>%
  mutate(circ_tronco_cm_cat = cut(circ_tronco_cm, breaks = cuts, labels = tags, include.lowest = TRUE))

#write.csv(train_data, 'data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv')