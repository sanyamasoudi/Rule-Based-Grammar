model SVMModel task classification {
    mlModel MySVM type SVM {
        parameter name = "kernel" value = "poly"
        parameter name = "C" value = 2.0
    }
    metric accuracy
    select feature feature3
    start SVMModel with MySVM
    show metrics
}
