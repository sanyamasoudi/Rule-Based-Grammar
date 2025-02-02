// Generated from E:/JOZVEH/Compiler/Final Project/RuleBased_AutoML/AutoML - Copy/Grammar/AutoMLDSL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link AutoMLDSLParser}.
 */
public interface AutoMLDSLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#dsl}.
	 * @param ctx the parse tree
	 */
	void enterDsl(AutoMLDSLParser.DslContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#dsl}.
	 * @param ctx the parse tree
	 */
	void exitDsl(AutoMLDSLParser.DslContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#model}.
	 * @param ctx the parse tree
	 */
	void enterModel(AutoMLDSLParser.ModelContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#model}.
	 * @param ctx the parse tree
	 */
	void exitModel(AutoMLDSLParser.ModelContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#task}.
	 * @param ctx the parse tree
	 */
	void enterTask(AutoMLDSLParser.TaskContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#task}.
	 * @param ctx the parse tree
	 */
	void exitTask(AutoMLDSLParser.TaskContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#modelElement}.
	 * @param ctx the parse tree
	 */
	void enterModelElement(AutoMLDSLParser.ModelElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#modelElement}.
	 * @param ctx the parse tree
	 */
	void exitModelElement(AutoMLDSLParser.ModelElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#mlModel}.
	 * @param ctx the parse tree
	 */
	void enterMlModel(AutoMLDSLParser.MlModelContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#mlModel}.
	 * @param ctx the parse tree
	 */
	void exitMlModel(AutoMLDSLParser.MlModelContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#mlModelType}.
	 * @param ctx the parse tree
	 */
	void enterMlModelType(AutoMLDSLParser.MlModelTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#mlModelType}.
	 * @param ctx the parse tree
	 */
	void exitMlModelType(AutoMLDSLParser.MlModelTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(AutoMLDSLParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(AutoMLDSLParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#valueList}.
	 * @param ctx the parse tree
	 */
	void enterValueList(AutoMLDSLParser.ValueListContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#valueList}.
	 * @param ctx the parse tree
	 */
	void exitValueList(AutoMLDSLParser.ValueListContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(AutoMLDSLParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(AutoMLDSLParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#metric}.
	 * @param ctx the parse tree
	 */
	void enterMetric(AutoMLDSLParser.MetricContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#metric}.
	 * @param ctx the parse tree
	 */
	void exitMetric(AutoMLDSLParser.MetricContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#metricNameList}.
	 * @param ctx the parse tree
	 */
	void enterMetricNameList(AutoMLDSLParser.MetricNameListContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#metricNameList}.
	 * @param ctx the parse tree
	 */
	void exitMetricNameList(AutoMLDSLParser.MetricNameListContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#metricName}.
	 * @param ctx the parse tree
	 */
	void enterMetricName(AutoMLDSLParser.MetricNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#metricName}.
	 * @param ctx the parse tree
	 */
	void exitMetricName(AutoMLDSLParser.MetricNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#featureSelection}.
	 * @param ctx the parse tree
	 */
	void enterFeatureSelection(AutoMLDSLParser.FeatureSelectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#featureSelection}.
	 * @param ctx the parse tree
	 */
	void exitFeatureSelection(AutoMLDSLParser.FeatureSelectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#featureList}.
	 * @param ctx the parse tree
	 */
	void enterFeatureList(AutoMLDSLParser.FeatureListContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#featureList}.
	 * @param ctx the parse tree
	 */
	void exitFeatureList(AutoMLDSLParser.FeatureListContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#featureMatch}.
	 * @param ctx the parse tree
	 */
	void enterFeatureMatch(AutoMLDSLParser.FeatureMatchContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#featureMatch}.
	 * @param ctx the parse tree
	 */
	void exitFeatureMatch(AutoMLDSLParser.FeatureMatchContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#conditionList}.
	 * @param ctx the parse tree
	 */
	void enterConditionList(AutoMLDSLParser.ConditionListContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#conditionList}.
	 * @param ctx the parse tree
	 */
	void exitConditionList(AutoMLDSLParser.ConditionListContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(AutoMLDSLParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(AutoMLDSLParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(AutoMLDSLParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(AutoMLDSLParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#ruleSet}.
	 * @param ctx the parse tree
	 */
	void enterRuleSet(AutoMLDSLParser.RuleSetContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#ruleSet}.
	 * @param ctx the parse tree
	 */
	void exitRuleSet(AutoMLDSLParser.RuleSetContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#rule}.
	 * @param ctx the parse tree
	 */
	void enterRule(AutoMLDSLParser.RuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#rule}.
	 * @param ctx the parse tree
	 */
	void exitRule(AutoMLDSLParser.RuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(AutoMLDSLParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(AutoMLDSLParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#binaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterBinaryExpression(AutoMLDSLParser.BinaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#binaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitBinaryExpression(AutoMLDSLParser.BinaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#simpleExpression}.
	 * @param ctx the parse tree
	 */
	void enterSimpleExpression(AutoMLDSLParser.SimpleExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#simpleExpression}.
	 * @param ctx the parse tree
	 */
	void exitSimpleExpression(AutoMLDSLParser.SimpleExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#logicOperator}.
	 * @param ctx the parse tree
	 */
	void enterLogicOperator(AutoMLDSLParser.LogicOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#logicOperator}.
	 * @param ctx the parse tree
	 */
	void exitLogicOperator(AutoMLDSLParser.LogicOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(AutoMLDSLParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(AutoMLDSLParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#show}.
	 * @param ctx the parse tree
	 */
	void enterShow(AutoMLDSLParser.ShowContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#show}.
	 * @param ctx the parse tree
	 */
	void exitShow(AutoMLDSLParser.ShowContext ctx);
	/**
	 * Enter a parse tree produced by {@link AutoMLDSLParser#visualization}.
	 * @param ctx the parse tree
	 */
	void enterVisualization(AutoMLDSLParser.VisualizationContext ctx);
	/**
	 * Exit a parse tree produced by {@link AutoMLDSLParser#visualization}.
	 * @param ctx the parse tree
	 */
	void exitVisualization(AutoMLDSLParser.VisualizationContext ctx);
}