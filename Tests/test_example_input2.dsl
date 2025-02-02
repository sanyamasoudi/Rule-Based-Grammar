model AutoMLRegressionModel task regression {
    mlModel autoML type AutoML {
        parameter name = "generation" value = 200
        parameter name = "population_size" value = 100
    }
    select feature data.t2lesvol, data.t2overbv, data.t2voljux
    metric mse
    start autoML with feature
    show models, metrics
}
