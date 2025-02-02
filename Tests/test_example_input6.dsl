model AutoMLRegressionModel task regression {
    mlModel autoML type AutoML {
        parameter name = "generation" value = 120
        parameter name = "population_size" value = 50
    }
    select feature data.t2lesvol, data.t2overbv, data.t2voljux, data.t2volnew
    metric mse, r2_score, mae
    start autoML with feature
    show models, metrics
}
