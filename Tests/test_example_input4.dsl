model AutoMLRegressionModel task regression {
    mlModel autoML type AutoML {
        parameter name = "generation" value = 150
        parameter name = "population_size" value = 60
    }
    select feature data.t2lesvol, data.t2overbv, data.t2voljux
    metric mse, r2_score
    start autoML with feature
    show models, metrics
}
