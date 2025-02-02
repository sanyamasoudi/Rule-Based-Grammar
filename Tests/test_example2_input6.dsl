model SVMModel task classification {
    mlModel MySVM type SVM {
        parameter name = "kernel" value = "linear"
        parameter name = "C" value = 1.0
    }
    metric accuracy, f1_score
    select feature feature1,feature2,feature3
    start SVMModel with MySVM
    show metrics
}
