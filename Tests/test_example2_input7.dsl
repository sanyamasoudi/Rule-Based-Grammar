model SVMModel task classification {
    mlModel MySVM type SVM {
        parameter name = "kernel" value = "poly"
        parameter name = "C" value = 1.0
    }
    metric accuracy, precision, recall
    select feature feature1,feature4,feature5
    start SVMModel with MySVM
    show metrics
}
