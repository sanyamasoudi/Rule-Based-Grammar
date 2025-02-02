model SVMModel task classification {
    mlModel MySVM type SVM {
        parameter name = "kernel" value = "sigmoid"
        parameter name = "C" value = 0.75
    }
    metric precision, recall, accuracy
    select feature feature1
    start SVMModel with MySVM
    show metrics
}
