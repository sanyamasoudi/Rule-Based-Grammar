model SVMModel task classification {
    mlModel MySVM type SVM {
        parameter name = "kernel" value = "sigmoid"
        parameter name = "C" value = 1.5
    }
    metric f1_score, recall
    select feature feature2,feature3,feature6
    start SVMModel with MySVM
    show metrics
}
