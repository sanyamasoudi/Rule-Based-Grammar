model SVMModel task classification {
    mlModel MySVM type SVM {
        parameter name = "kernel" value = "poly"
        parameter name = "C" value = 2.0
    }
    metric accuracy, f1_score
    select feature feature4,feature5,feature6
    start SVMModel with MySVM
    show metrics
}
