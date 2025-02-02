model PatientRiskPrediction task classification {
    mlModel RFModel type RandomForest {
        parameter name = "max_depth" value = [10, 20]
        parameter name = "n_estimators" value = [100, 200]
    }

    metric accuracy, precision, recall, f1_score

    select featureSet
        dataset.age, dataset.blood_pressure, dataset.cholesterol, dataset.glucose
    where dataset.age > 18 and dataset.cholesterol > 200 or dataset.blood_pressure >= 140

    ruleSet RiskRules {
        rule: if (dataset.cholesterol > 240 and dataset.blood_pressure > 150) then high_risk, immediate_attention
        rule: if (dataset.cholesterol <= 240 and dataset.glucose <= 110) then low_risk, routine_check
    }

    start PatientRiskPrediction with RFModel

    show models, metrics, rules from PatientRiskPrediction
}