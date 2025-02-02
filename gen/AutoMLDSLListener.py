# Generated from E:/JOZVEH/Compiler/Final Project/RuleBased_AutoML/AutoML - Copy/Grammar/AutoMLDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AutoMLDSLParser import AutoMLDSLParser
else:
    from AutoMLDSLParser import AutoMLDSLParser

# This class defines a complete listener for a parse tree produced by AutoMLDSLParser.
class AutoMLDSLListener(ParseTreeListener):

    # Enter a parse tree produced by AutoMLDSLParser#dsl.
    def enterDsl(self, ctx:AutoMLDSLParser.DslContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#dsl.
    def exitDsl(self, ctx:AutoMLDSLParser.DslContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#model.
    def enterModel(self, ctx:AutoMLDSLParser.ModelContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#model.
    def exitModel(self, ctx:AutoMLDSLParser.ModelContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#task.
    def enterTask(self, ctx:AutoMLDSLParser.TaskContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#task.
    def exitTask(self, ctx:AutoMLDSLParser.TaskContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#modelElement.
    def enterModelElement(self, ctx:AutoMLDSLParser.ModelElementContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#modelElement.
    def exitModelElement(self, ctx:AutoMLDSLParser.ModelElementContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#mlModel.
    def enterMlModel(self, ctx:AutoMLDSLParser.MlModelContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#mlModel.
    def exitMlModel(self, ctx:AutoMLDSLParser.MlModelContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#mlModelType.
    def enterMlModelType(self, ctx:AutoMLDSLParser.MlModelTypeContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#mlModelType.
    def exitMlModelType(self, ctx:AutoMLDSLParser.MlModelTypeContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#parameter.
    def enterParameter(self, ctx:AutoMLDSLParser.ParameterContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#parameter.
    def exitParameter(self, ctx:AutoMLDSLParser.ParameterContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#parameterName.
    def enterParameterName(self, ctx:AutoMLDSLParser.ParameterNameContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#parameterName.
    def exitParameterName(self, ctx:AutoMLDSLParser.ParameterNameContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#valueList.
    def enterValueList(self, ctx:AutoMLDSLParser.ValueListContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#valueList.
    def exitValueList(self, ctx:AutoMLDSLParser.ValueListContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#value.
    def enterValue(self, ctx:AutoMLDSLParser.ValueContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#value.
    def exitValue(self, ctx:AutoMLDSLParser.ValueContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#metric.
    def enterMetric(self, ctx:AutoMLDSLParser.MetricContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#metric.
    def exitMetric(self, ctx:AutoMLDSLParser.MetricContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#metricNameList.
    def enterMetricNameList(self, ctx:AutoMLDSLParser.MetricNameListContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#metricNameList.
    def exitMetricNameList(self, ctx:AutoMLDSLParser.MetricNameListContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#metricName.
    def enterMetricName(self, ctx:AutoMLDSLParser.MetricNameContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#metricName.
    def exitMetricName(self, ctx:AutoMLDSLParser.MetricNameContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#featureSelection.
    def enterFeatureSelection(self, ctx:AutoMLDSLParser.FeatureSelectionContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#featureSelection.
    def exitFeatureSelection(self, ctx:AutoMLDSLParser.FeatureSelectionContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#featureList.
    def enterFeatureList(self, ctx:AutoMLDSLParser.FeatureListContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#featureList.
    def exitFeatureList(self, ctx:AutoMLDSLParser.FeatureListContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#featureMatch.
    def enterFeatureMatch(self, ctx:AutoMLDSLParser.FeatureMatchContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#featureMatch.
    def exitFeatureMatch(self, ctx:AutoMLDSLParser.FeatureMatchContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#featureExpr.
    def enterFeatureExpr(self, ctx:AutoMLDSLParser.FeatureExprContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#featureExpr.
    def exitFeatureExpr(self, ctx:AutoMLDSLParser.FeatureExprContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#featureValue.
    def enterFeatureValue(self, ctx:AutoMLDSLParser.FeatureValueContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#featureValue.
    def exitFeatureValue(self, ctx:AutoMLDSLParser.FeatureValueContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#conditionList.
    def enterConditionList(self, ctx:AutoMLDSLParser.ConditionListContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#conditionList.
    def exitConditionList(self, ctx:AutoMLDSLParser.ConditionListContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#condition.
    def enterCondition(self, ctx:AutoMLDSLParser.ConditionContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#condition.
    def exitCondition(self, ctx:AutoMLDSLParser.ConditionContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#conditionExpr.
    def enterConditionExpr(self, ctx:AutoMLDSLParser.ConditionExprContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#conditionExpr.
    def exitConditionExpr(self, ctx:AutoMLDSLParser.ConditionExprContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#operator.
    def enterOperator(self, ctx:AutoMLDSLParser.OperatorContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#operator.
    def exitOperator(self, ctx:AutoMLDSLParser.OperatorContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#ruleSet.
    def enterRuleSet(self, ctx:AutoMLDSLParser.RuleSetContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#ruleSet.
    def exitRuleSet(self, ctx:AutoMLDSLParser.RuleSetContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#rule.
    def enterRule(self, ctx:AutoMLDSLParser.RuleContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#rule.
    def exitRule(self, ctx:AutoMLDSLParser.RuleContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#expression.
    def enterExpression(self, ctx:AutoMLDSLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#expression.
    def exitExpression(self, ctx:AutoMLDSLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#binaryExpression.
    def enterBinaryExpression(self, ctx:AutoMLDSLParser.BinaryExpressionContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#binaryExpression.
    def exitBinaryExpression(self, ctx:AutoMLDSLParser.BinaryExpressionContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#simpleExpression.
    def enterSimpleExpression(self, ctx:AutoMLDSLParser.SimpleExpressionContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#simpleExpression.
    def exitSimpleExpression(self, ctx:AutoMLDSLParser.SimpleExpressionContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#simpleName.
    def enterSimpleName(self, ctx:AutoMLDSLParser.SimpleNameContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#simpleName.
    def exitSimpleName(self, ctx:AutoMLDSLParser.SimpleNameContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#logicOperator.
    def enterLogicOperator(self, ctx:AutoMLDSLParser.LogicOperatorContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#logicOperator.
    def exitLogicOperator(self, ctx:AutoMLDSLParser.LogicOperatorContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#start.
    def enterStart(self, ctx:AutoMLDSLParser.StartContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#start.
    def exitStart(self, ctx:AutoMLDSLParser.StartContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#show.
    def enterShow(self, ctx:AutoMLDSLParser.ShowContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#show.
    def exitShow(self, ctx:AutoMLDSLParser.ShowContext):
        pass


    # Enter a parse tree produced by AutoMLDSLParser#visualization.
    def enterVisualization(self, ctx:AutoMLDSLParser.VisualizationContext):
        pass

    # Exit a parse tree produced by AutoMLDSLParser#visualization.
    def exitVisualization(self, ctx:AutoMLDSLParser.VisualizationContext):
        pass



del AutoMLDSLParser