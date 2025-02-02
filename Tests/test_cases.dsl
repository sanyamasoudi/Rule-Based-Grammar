test_example_input1:
    model AutoMLRegressionModel task regression {
        mlModel autoML type AutoML {
            parameter name = "generation" value = 100
            parameter name = "population_size" value = 50
        }
        select feature
            data.t2lesvol,data.t2overbv, data.t2voljux
        metric mse, r2_score
        start autoML with feature
        show models, metrics
    }
test_example_input2:
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
test_example_input3:
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
test_example_input4:
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
test_example_input5:
    model AutoMLRegressionModel task regression {
        mlModel autoML type AutoML {
            parameter name = "generation" value = 100
            parameter name = "population_size" value = 80
        }
        select feature data.t2lesvol, data.t2overbv, data.t2voljux
        metric mse, r2_score
        start autoML with feature
        show models, metrics
    }
test_example_input6:
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
test_example_input7:
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
test_example_input8:
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
test_example2_input1:
    model SVMModel task classification {
        mlModel MySVM type SVM {
            parameter name = "kernel" value = "rbf"
            parameter name = "C" value = 1.0
        }
        metric all
        select feature feature1,feature2,feature3
        start SVMModel with MySVM
        show metrics
    }

test_example2_input2:
    model SVMModel task classification {
        mlModel MySVM type SVM {
            parameter name = "kernel" value = "linear"
            parameter name = "C" value = 0.5
        }
        metric precision, recall
        select feature feature1,feature2
        start SVMModel with MySVM
        show metrics
    }

test_example2_input3:
    model SVMModel task classification {
        mlModel MySVM type SVM {
            parameter name = "kernel" value = "poly"
            parameter name = "C" value = 2.0
        }
        metric accuracy
        select feature feature3
        start SVMModel with MySVM
        show metrics
    }
test_example2_input4:
    model SVMModel task classification {
        mlModel MySVM type SVM {
            parameter name = "kernel" value = "rbf"
            parameter name = "C" value = 1.5
        }
        metric f1_score
        select feature feature1,feature2,feature3
        start SVMModel with MySVM
        show metrics
    }
test_example2_input5:
    model SVMModel task classification {
        mlModel MySVM type SVM {
            parameter name = "kernel" value = "sigmoid"
            parameter name = "C" value = 0.75
        }
        metric precision, recall, accuracy
        select feature feature1
        start SVMModel with MySVM
        show metrics
    }

test_example2_input6:
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

test_example2_input7:
    model SVMModel task classification {
        mlModel MySVM type SVM {
            parameter name = "kernel" value = "poly"
            parameter name = "C" value = 1.0
        }
        metric accuracy, precision, recall
        select feature feature1,feature4,feature5
        start SVMModel with MySVM
        show metrics
    }

test_example2_input8:
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

test_example2_input9:
    model SVMModel task classification {
        mlModel MySVM type SVM {
            parameter name = "kernel" value = "poly"
            parameter name = "C" value = 2.0
        }
        metric accuracy, f1_score
        select feature feature4,feature5,feature6
        start SVMModel with MySVM
        show metrics
    }

test_example3_input1:
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

test_example3_input2:
    model PatientRiskPrediction task classification {
        mlModel RFModel type RandomForest {
            parameter name = "max_depth" value = [15, 25]
            parameter name = "n_estimators" value = [150, 250]
        }
        metric f1_score, precision
        select featureSet dataset.age, dataset.blood_pressure, dataset.cholesterol
        where dataset.age > 18 and dataset.blood_pressure >= 140
        ruleSet RiskRules {
            rule: if (dataset.cholesterol > 240) then high_risk, immediate_attention
            rule: if (dataset.cholesterol <= 240 and dataset.glucose <= 110) then low_risk, routine_check
        }
        start PatientRiskPrediction with RFModel
        show models, metrics, rules from PatientRiskPrediction
    }

test_example3_input3:
    model PatientRiskPrediction task classification {
        mlModel RFModel type RandomForest {
            parameter name = "max_depth" value = [20, 30]
            parameter name = "n_estimators" value = [200, 300]
        }
        metric accuracy, recall, precision
        select featureSet dataset.age, dataset.blood_pressure, dataset.cholesterol, dataset.smoking_status
        where dataset.age > 18 and dataset.blood_pressure >= 140 and dataset.smoking_status == "current_smoker"
        ruleSet RiskRules {
            rule: if (dataset.cholesterol > 240 and dataset.smoking_status == "current_smoker") then high_risk, immediate_attention
            rule: if (dataset.cholesterol <= 240 and dataset.glucose <= 110) then low_risk, routine_check
        }
        start PatientRiskPrediction with RFModel
        show models, metrics, rules from PatientRiskPrediction
    }

test_example3_input4:
    model PatientRiskPrediction task classification {
        mlModel RFModel type RandomForest {
            parameter name = "max_depth" value = [5, 10]
            parameter name = "n_estimators" value = [50, 100]
        }
        metric accuracy, precision, recall, f1_score
        select featureSet dataset.age, dataset.blood_pressure, dataset.cholesterol, dataset.activity_level
        where dataset.age > 30 and dataset.activity_level == "low"
        ruleSet RiskRules {
            rule: if (dataset.cholesterol > 240 and dataset.activity_level == "low") then high_risk, immediate_attention
            rule: if (dataset.cholesterol <= 240 and dataset.glucose <= 110 and dataset.activity_level == "high") then low_risk, routine_check
        }
        start PatientRiskPrediction with RFModel
        show models, metrics, rules from PatientRiskPrediction
    }

test_example3_input5:
    model PatientRiskPrediction task classification {
        mlModel RFModel type RandomForest {
            parameter name = "max_depth" value = [5, 15]
            parameter name = "n_estimators" value = [50, 150]
        }
        metric accuracy, f1_score
        select featureSet dataset.age, dataset.blood_pressure, dataset.cholesterol, dataset.family_history
        where dataset.age > 18 and dataset.family_history == "yes"
        ruleSet RiskRules {
            rule: if (dataset.cholesterol > 240 and dataset.family_history == "yes") then high_risk, immediate_attention
            rule: if (dataset.cholesterol <= 240 and dataset.glucose <= 110 and dataset.family_history == "no") then low_risk, routine_check
        }
        start PatientRiskPrediction with RFModel
        show models, metrics, rules from PatientRiskPrediction
    }

test_example3_input6:
    model PatientRiskPrediction task classification {
        mlModel RFModel type RandomForest {
            parameter name = "max_depth" value = [20, 30]
            parameter name = "n_estimators" value = [200, 300]
        }
        metric accuracy, f1_score, recall
        select featureSet dataset.age, dataset.blood_pressure, dataset.cholesterol, dataset.smoking_status, dataset.exercise_frequency
        where dataset.age > 18 and dataset.blood_pressure >= 140 and dataset.exercise_frequency <= 2
        ruleSet RiskRules {
            rule: if (dataset.cholesterol > 240 and dataset.smoking_status == "current_smoker") then high_risk, immediate_attention
            rule: if (dataset.cholesterol <= 240 and dataset.glucose <= 110 and dataset.exercise_frequency >= 3) then low_risk, routine_check
        }
        start PatientRiskPrediction with RFModel
        show models, metrics, rules from PatientRiskPrediction
    }

test_example3_input7:
    model PatientRiskPrediction task classification {
        mlModel RFModel type RandomForest {
            parameter name = "max_depth" value = [15, 25]
            parameter name = "n_estimators" value = [150, 250]
        }
        metric precision, recall, f1_score
        select featureSet dataset.age, dataset.blood_pressure, dataset.cholesterol, dataset.family_history
        where dataset.age > 18 and dataset.family_history == "yes"
        ruleSet RiskRules {
            rule: if (dataset.cholesterol > 240 and dataset.family_history == "yes") then high_risk, immediate_attention
            rule: if (dataset.cholesterol <= 240 and dataset.glucose <= 110 and dataset.family_history == "no") then low_risk, routine_check
        }
        start PatientRiskPrediction with RFModel
        show models, metrics, rules from PatientRiskPrediction
    }

test_example3_input8:
    model PatientRiskPrediction task classification {
        mlModel RFModel type RandomForest {
            parameter name = "max_depth" value = [10, 20]
            parameter name = "n_estimators" value = [100, 200]
        }
        metric mae, mse
        select featureSet dataset.age, dataset.blood_pressure, dataset.cholesterol, dataset.glucose
        where dataset.age > 18 and dataset.cholesterol > 200 or dataset.blood_pressure >= 140
        ruleSet RiskRules {
            rule: if (dataset.cholesterol > 240 and dataset.blood_pressure > 150) then high_risk, immediate_attention
            rule: if (dataset.cholesterol <= 240 and dataset.glucose <= 110) then low_risk, routine_check
        }
        start PatientRiskPrediction with RFModel
        show models, metrics, rules from PatientRiskPrediction
    }

test_example3_input9:
    model PatientRiskPrediction task classification {
        mlModel RFModel type RandomForest {
            parameter name = "max_depth" value = [5, 15]
            parameter name = "n_estimators" value = [50, 150]
        }
        metric accuracy, precision, recall, f1_score
        select featureSet dataset.age, dataset.blood_pressure, dataset.cholesterol, dataset.activity_level
        where dataset.age > 30 and dataset.activity_level == "low"
        ruleSet RiskRules {
            rule: if (dataset.cholesterol > 240 and dataset.activity_level == "low") then high_risk, immediate_attention
            rule: if (dataset.cholesterol <= 240 and dataset.glucose <= 110 and dataset.activity_level == "high") then low_risk, routine_check
        }
        start PatientRiskPrediction with RFModel
        show models, metrics, rules from PatientRiskPrediction
    }

test_example4_input1:
    model MSModel task classification {
        mlModel RandomForest type AutoML {
            parameter name = "max_depth" value = [10, 20, 30]
            parameter name = "n_estimators" value = [100, 200]
        }
        metric mse, r2_score, mae
        select features {
            age, gender, brain_scan.score > 0.7
        } where condition age >= 18 and brain_scan.size <= 1000
        ruleSet MSRules {
            rule: if brain_scan.score > 0.8 then high_risk, intensive_care
            rule: if brain_scan.score <= 0.8 then low_risk, monitoring
        }
        start MSModel with features
        show models, metrics from MSModel
}

test_example4_input2:
    model MSModel task classification {
        mlModel RandomForest type AutoML {
            parameter name = "max_depth" value = [30, 40]
            parameter name = "n_estimators" value = [300]
        }
        metric mae, mse
        select features age, gender
        where condition age >= 30 and brain_scan.size <= 900
        ruleSet MSRules {
            rule: if brain_scan.score > 0.85 then high_risk, intensive_care
            rule: if brain_scan.score <= 0.85 then low_risk, monitoring
        }
        start MSModel with features
        show models, metrics from MSModel
    }


test_example4_input3:
    model MSModel task classification {
        mlModel RandomForest type AutoML {
            parameter name = "max_depth" value = [20, 25, 30]
            parameter name = "n_estimators" value = [150, 250, 350]
        }
        metric r2_score, mae
        select features age, gender, brain_scan.score
        where condition age >= 18
        ruleSet MSRules {
            rule: if brain_scan.score > 0.7 then high_risk, intensive_care
            rule: if brain_scan.score <= 0.7 then low_risk, monitoring
        }
        start MSModel with features
        show models, metrics from MSModel
    }

test_example4_input4:
    model MSModel task classification {
        mlModel RandomForest type AutoML {
            parameter name = "max_depth" value = [10, 20]
            parameter name = "n_estimators" value = [100, 200]
        }
        metric f1_score, precision
        select features age, brain_scan.size, brain_scan.score
        where condition age >= 30 and brain_scan.size <= 700
        ruleSet MSRules {
            rule: if brain_scan.score > 0.9 then high_risk, intensive_care
            rule: if brain_scan.score <= 0.9 then low_risk, monitoring
        }
        start MSModel with features
        show models, metrics from MSModel
    }

test_example4_input5:
    model MSModel task classification {
        mlModel RandomForest type AutoML {
            parameter name = "max_depth" value = [20, 30]
            parameter name = "n_estimators" value = [200, 300]
        }
        metric mse, mae, r2_score
        select features age, gender, brain_scan.score
        where condition age >= 18 and brain_scan.score <= 0.7
        ruleSet MSRules {
            rule: if brain_scan.score > 0.6 then low_risk, monitoring
            rule: if brain_scan.score <= 0.6 then very_low_risk, no_action
        }
        start MSModel with features
        show models, metrics from MSModel
    }

test_example4_input6:
    model MSModel task classification {
        mlModel RandomForest type AutoML {
            parameter name = "max_depth" value = [15, 25]
            parameter name = "n_estimators" value = [150, 250]
        }
        metric accuracy, recall
        select features age, gender, brain_scan.score
        where condition age >= 18 and brain_scan.size <= 800
        ruleSet MSRules {
            rule: if brain_scan.score > 0.8 and gender == "female" then high_risk, intensive_care
            rule: if brain_scan.score <= 0.8 and gender == "male" then low_risk, monitoring
        }
        start MSModel with features
        show models, metrics from MSModel
    }

test_example4_input7:
    model MSModel task classification {
        mlModel RandomForest type AutoML {
            parameter name = "max_depth" value = [15, 25, 35]
            parameter name = "n_estimators" value = [150, 250, 350]
        }
        metric accuracy, f1_score, precision
        select features age, gender, brain_scan.score, brain_scan.size
        where condition age >= 18
        ruleSet MSRules {
            rule: if brain_scan.score > 0.8 then high_risk, intensive_care
            rule: if brain_scan.score <= 0.8 then low_risk, monitoring
        }
        start MSModel with features
        show models, metrics from MSModel
    }

test_example4_input8:
    model MSModel task classification {
        mlModel RandomForest type AutoML {
            parameter name = "max_depth" value = [20, 30, 40]
            parameter name = "n_estimators" value = [200, 400]
        }
        metric accuracy, precision, recall, f1_score
        select features age, gender, brain_scan.score, brain_scan.size, brain_scan.type
        where condition age >= 30 and brain_scan.size <= 600 and brain_scan.type == "MRI"
        ruleSet MSRules {
            rule: if brain_scan.score > 0.9 then high_risk, intensive_care
            rule: if brain_scan.score <= 0.9 then low_risk, monitoring
        }
        start MSModel with features
        show models, metrics from MSModel
    }

test_example4_input9:
    model MSModel task classification {
        mlModel RandomForest type AutoML {
            parameter name = "max_depth" value = [20, 30, 40]
            parameter name = "n_estimators" value = [200, 400]
        }
        metric accuracy, precision, recall, f1_score
        select features age, gender, brain_scan.score, brain_scan.size, brain_scan.type
        where condition age >= 30 and brain_scan.size <= 600 and brain_scan.type == "MRI"
        ruleSet MSRules {
            rule: if brain_scan.score > 0.9 then high_risk, intensive_care
            rule: if brain_scan.score <= 0.9 then low_risk, monitoring
        }
        start MSModel with features
        show models, metrics from MSModel
    }

test_example4_input10:
    model MSModel task classification {
        mlModel RandomForest type AutoML {
            parameter name = "max_depth" value = [25, 35, 45]
            parameter name = "n_estimators" value = [300, 500]
        }
        metric mae, mse, r2_score
        select features age, gender, brain_scan.score, brain_scan.size, medication_history
        where condition age >= 40 and brain_scan.size <= 700 and medication_history == "yes"
        ruleSet MSRules {
            rule: if brain_scan.score > 0.8 and medication_history == "yes" then high_risk, intensive_care
            rule: if brain_scan.score <= 0.8 and medication_history == "no" then low_risk, monitoring
        }
        start MSModel with features
        show models, metrics from MSModel
    }

