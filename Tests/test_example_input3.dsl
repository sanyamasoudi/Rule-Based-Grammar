model AutoMLRegressionModel task regression {
    mlModel autoML type AutoML {
        parameter name = "generation" value = 50
        parameter name = "population_size" value = 25
    }
    select feature data.t2lesvol, data.t2overbv
    metric r2_score
    start autoML with feature
    show models, metrics
}
