# Generated from E:/JOZVEH/Compiler/Final Project/RuleBased_AutoML/AutoML - Copy/Grammar/AutoMLDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AutoMLDSLParser import AutoMLDSLParser
else:
    from AutoMLDSLParser import AutoMLDSLParser

# This class defines a complete generic visitor for a parse tree produced by AutoMLDSLParser.

class AutoMLDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AutoMLDSLParser#dsl.
    def visitDsl(self, ctx:AutoMLDSLParser.DslContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#model.
    def visitModel(self, ctx:AutoMLDSLParser.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#task.
    def visitTask(self, ctx:AutoMLDSLParser.TaskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#modelElement.
    def visitModelElement(self, ctx:AutoMLDSLParser.ModelElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#mlModel.
    def visitMlModel(self, ctx:AutoMLDSLParser.MlModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#mlModelType.
    def visitMlModelType(self, ctx:AutoMLDSLParser.MlModelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#parameter.
    def visitParameter(self, ctx:AutoMLDSLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#parameterName.
    def visitParameterName(self, ctx:AutoMLDSLParser.ParameterNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#valueList.
    def visitValueList(self, ctx:AutoMLDSLParser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#value.
    def visitValue(self, ctx:AutoMLDSLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#metric.
    def visitMetric(self, ctx:AutoMLDSLParser.MetricContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#metricNameList.
    def visitMetricNameList(self, ctx:AutoMLDSLParser.MetricNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#metricName.
    def visitMetricName(self, ctx:AutoMLDSLParser.MetricNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#featureSelection.
    def visitFeatureSelection(self, ctx:AutoMLDSLParser.FeatureSelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#featureList.
    def visitFeatureList(self, ctx:AutoMLDSLParser.FeatureListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#featureMatch.
    def visitFeatureMatch(self, ctx:AutoMLDSLParser.FeatureMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#featureExpr.
    def visitFeatureExpr(self, ctx:AutoMLDSLParser.FeatureExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#featureValue.
    def visitFeatureValue(self, ctx:AutoMLDSLParser.FeatureValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#conditionList.
    def visitConditionList(self, ctx:AutoMLDSLParser.ConditionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#condition.
    def visitCondition(self, ctx:AutoMLDSLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#conditionExpr.
    def visitConditionExpr(self, ctx:AutoMLDSLParser.ConditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#operator.
    def visitOperator(self, ctx:AutoMLDSLParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#ruleSet.
    def visitRuleSet(self, ctx:AutoMLDSLParser.RuleSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#rule.
    def visitRule(self, ctx:AutoMLDSLParser.RuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#expression.
    def visitExpression(self, ctx:AutoMLDSLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#binaryExpression.
    def visitBinaryExpression(self, ctx:AutoMLDSLParser.BinaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#simpleExpression.
    def visitSimpleExpression(self, ctx:AutoMLDSLParser.SimpleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#simpleName.
    def visitSimpleName(self, ctx:AutoMLDSLParser.SimpleNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#logicOperator.
    def visitLogicOperator(self, ctx:AutoMLDSLParser.LogicOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#start.
    def visitStart(self, ctx:AutoMLDSLParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#show.
    def visitShow(self, ctx:AutoMLDSLParser.ShowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutoMLDSLParser#visualization.
    def visitVisualization(self, ctx:AutoMLDSLParser.VisualizationContext):
        return self.visitChildren(ctx)



del AutoMLDSLParser