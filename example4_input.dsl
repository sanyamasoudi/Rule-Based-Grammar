model MSModel task classification {
    mlModel randomForest type AutoML {
        parameter name = "max_depth" value = [10, 20, 30]
        parameter name = "n_estimators" value = [100, 200]
    }

    metric mse, r2_score, mae

    select feature {
        age, gender, brain_scan.score > 0.7
    } where condition age >= 18 and brain_scan.size <= 1000

    ruleSet MSRules {
        rule: if brain_scan.score > 0.8 then high_risk, intensive_care
        rule: if brain_scan.score <= 0.8 then low_risk, monitoring
    }

    start MSModel with features

    show models, metrics from MSModel
}
