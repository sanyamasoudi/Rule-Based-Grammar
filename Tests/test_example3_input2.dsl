model PatientRiskPrediction task classification {
    mlModel RFModel type RandomForest {
        parameter name = "max_depth" value = [15, 25]
        parameter name = "n_estimators" value = [150, 250]
    }
    metric f1_score, precision
    select featureSet dataset.age, dataset.blood_pressure, dataset.cholesterol
    where dataset.age > 18 and dataset.blood_pressure >= 140
    ruleSet RiskRules {
        rule: if dataset.cholesterol > 240 then high_risk, immediate_attention
        rule: if (dataset.cholesterol <= 240 and dataset.glucose <= 110) then low_risk, routine_check
    }
    start PatientRiskPrediction with RFModel
    show models, metrics, rules from PatientRiskPrediction
}
