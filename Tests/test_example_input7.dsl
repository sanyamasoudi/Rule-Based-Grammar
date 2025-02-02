model AutoMLRegressionModel task regression {
    mlModel autoML type AutoML {
        parameter name = "generation" value = 100
        parameter name = "population_size" value = 50
    }
    select feature data.t2lesvol, data.t2voljux
    metric mse, r2_score
    start autoML with feature
    show models, metrics
}
