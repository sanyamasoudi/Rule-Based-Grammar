// Generated from E:/JOZVEH/Compiler/Final Project/RuleBased_AutoML/AutoML - Copy/Grammar/AutoMLDSL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link AutoMLDSLParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface AutoMLDSLVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#dsl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDsl(AutoMLDSLParser.DslContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#model}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModel(AutoMLDSLParser.ModelContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#task}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTask(AutoMLDSLParser.TaskContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#modelElement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModelElement(AutoMLDSLParser.ModelElementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#mlModel}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMlModel(AutoMLDSLParser.MlModelContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#mlModelType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMlModelType(AutoMLDSLParser.MlModelTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#parameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter(AutoMLDSLParser.ParameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#valueList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValueList(AutoMLDSLParser.ValueListContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#value}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValue(AutoMLDSLParser.ValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#metric}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMetric(AutoMLDSLParser.MetricContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#metricNameList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMetricNameList(AutoMLDSLParser.MetricNameListContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#metricName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMetricName(AutoMLDSLParser.MetricNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#featureSelection}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFeatureSelection(AutoMLDSLParser.FeatureSelectionContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#featureList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFeatureList(AutoMLDSLParser.FeatureListContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#featureMatch}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFeatureMatch(AutoMLDSLParser.FeatureMatchContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#conditionList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConditionList(AutoMLDSLParser.ConditionListContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#condition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCondition(AutoMLDSLParser.ConditionContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#operator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperator(AutoMLDSLParser.OperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#ruleSet}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRuleSet(AutoMLDSLParser.RuleSetContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#rule}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRule(AutoMLDSLParser.RuleContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(AutoMLDSLParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#binaryExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinaryExpression(AutoMLDSLParser.BinaryExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#simpleExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleExpression(AutoMLDSLParser.SimpleExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#logicOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicOperator(AutoMLDSLParser.LogicOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#start}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStart(AutoMLDSLParser.StartContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#show}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShow(AutoMLDSLParser.ShowContext ctx);
	/**
	 * Visit a parse tree produced by {@link AutoMLDSLParser#visualization}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVisualization(AutoMLDSLParser.VisualizationContext ctx);
}