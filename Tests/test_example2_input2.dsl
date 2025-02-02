model SVMModel task classification {
    mlModel MySVM type SVM {
        parameter name = "kernel" value = "linear"
        parameter name = "C" value = 0.5
    }
    metric precision, recall
    select feature feature1,feature2
    start SVMModel with MySVM
    show metrics
}
