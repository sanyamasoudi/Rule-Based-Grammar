grammar AutoMLDSL;

dsl: model+;

model: 'model' ID 'task' task '{' modelElement* '}';

task: 'predict' | 'classification' | 'regression' | 'clustering';

modelElement: mlModel | metric | featureSelection | ruleSet | start | show;

mlModel: 'mlModel' ID 'type' mlModelType ('{' parameter* '}')?;

mlModelType: 'RandomForest' | 'DecisionTree' | 'SVM' | 'AutoML' | 'KMeans';

parameter: 'parameter' 'name' '=' parameterName 'value' '=' valueList;

parameterName: STRING;

valueList: '[' value (',' value)* ']' | value;

value: STRING | FLOAT;

metric: 'metric' metricNameList;

metricNameList: metricName (',' metricName)*;

metricName: 'mse' | 'r2_score' | 'mae' | 'rmse' | 'accuracy' | 'precision' | 'recall' | 'f1_score' | 'all';

featureSelection: 'select' ID featureList ('where' conditionList)?;

featureList: featureMatch (',' featureMatch)*;

featureMatch: featureExpr ('.' featureExpr)? (operator featureValue)?;

featureExpr: ID;

featureValue: FLOAT;

conditionList: condition ('and' condition | 'or' condition)*;

condition: conditionExpr '.' conditionExpr operator value;

conditionExpr: ID;

operator: '<' | '>' | '<=' | '>=' | '==' | '!=';

ruleSet: 'ruleSet' ID '{' rule* '}';

rule: 'rule' ':' 'if' expression 'then' ID (',' ID)*;

expression: simpleExpression | binaryExpression;

binaryExpression: '(' expression logicOperator expression ')';

simpleExpression: simpleName '.' simpleName operator value;

simpleName: ID;

logicOperator: 'and' | 'or';

start: 'start' ID 'with' ID;

show: 'show' visualization (',' visualization)* ('from' ID)?;

visualization: 'models' | 'features' | 'metrics' | 'rules';

ID: [a-zA-Z][a-zA-Z0-9_]*;
STRING: '"' .*? '"';
FLOAT: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;