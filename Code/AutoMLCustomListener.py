from Repository.ast import AST
from Repository.make_ast_subtree import make_ast_subtree
from gen.AutoMLDSLListener import AutoMLDSLListener


# class AutoMLCustomListener(AutoMLDSLListener):
#     def __init__(self, rule_names):
#         self.overridden_rules = [
#             'dsl', 'model', 'mlModel', 'parameter', 'featureSelection',
#             'metric', 'ruleSet', 'start', 'show'
#         ]
#         self.rule_names = rule_names
#         self.ast = AST()
#
#     def exitEveryRule(self, ctx):
#         rule_name = self.rule_names[ctx.getRuleIndex()]
#         if rule_name not in self.overridden_rules:
#             make_ast_subtree(self.ast, ctx, rule_name)
#
#     def exitDsl(self, ctx):
#         make_ast_subtree(self.ast, ctx, "dsl", keep_node=True)
#
#     def exitModel(self, ctx):
#         make_ast_subtree(self.ast, ctx, "model", keep_node=True)
#
#     def exitMlModel(self, ctx):
#         make_ast_subtree(self.ast, ctx, "mlModel", keep_node=True)
#
#     def exitParameter(self, ctx):
#         make_ast_subtree(self.ast, ctx, "parameter", keep_node=True)
#
#     def exitFeatureSelection(self, ctx):
#         make_ast_subtree(self.ast, ctx, "featureSelection", keep_node=True)
#
#     def exitMetric(self, ctx):
#         make_ast_subtree(self.ast, ctx, "metric", keep_node=True)
#
#     def exitRuleSet(self, ctx):
#         make_ast_subtree(self.ast, ctx, "ruleSet", keep_node=True)
#
#     def exitRule(self, ctx):
#         make_ast_subtree(self.ast, ctx, "rule", keep_node=True)
#
#     def exitExpression(self, ctx):
#         if ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['and', 'or']:
#             make_ast_subtree(self.ast, ctx, "binaryExpression", keep_node=True)
#         else:
#             make_ast_subtree(self.ast, ctx, "simpleExpression", keep_node=True)
#
#     def exitLogicOperator(self, ctx):
#         make_ast_subtree(self.ast, ctx, "logicOperator", keep_node=True)
#
#     def exitStart(self, ctx):
#         make_ast_subtree(self.ast, ctx, "start", keep_node=True)
#
#     def exitShow(self, ctx):
#         make_ast_subtree(self.ast, ctx, "show", keep_node=True)





# class AutoMLCustomListener(AutoMLDSLListener):
#     def __init__(self, rule_names):
#         self.overridden_rules = [
#             'dsl', 'model', 'mlModel', 'parameter', 'featureSelection',
#             'metric', 'ruleSet', 'start', 'show'
#         ]
#         self.rule_names = rule_names
#         self.ast = AST()
#
#     def exitEveryRule(self, ctx):
#         rule_name = self.rule_names[ctx.getRuleIndex()]
#         if rule_name not in self.overridden_rules:
#             make_ast_subtree(self.ast, ctx, rule_name)
#
#     def exitDsl(self, ctx):
#         make_ast_subtree(self.ast, ctx, "dsl", keep_node=True)
#
#     def exitModel(self, ctx):
#         make_ast_subtree(self.ast, ctx, "model", keep_node=True)
#
#     def exitMlModel(self, ctx):
#         make_ast_subtree(self.ast, ctx, "mlModel", keep_node=True)
#
#     def exitParameter(self, ctx):
#         make_ast_subtree(self.ast, ctx, "parameter", keep_node=True)
#
#     def exitFeatureSelection(self, ctx):
#         make_ast_subtree(self.ast, ctx, "featureSelection", keep_node=True)
#
#     def exitMetric(self, ctx):
#         make_ast_subtree(self.ast, ctx, "metric", keep_node=True)
#
#     def exitRuleSet(self, ctx):
#         make_ast_subtree(self.ast, ctx, "ruleSet", keep_node=True)
#
#     def exitRule(self, ctx):
#         make_ast_subtree(self.ast, ctx, "rule", keep_node=True)
#
#     def exitExpression(self, ctx):
#         if ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['and', 'or']:
#             make_ast_subtree(self.ast, ctx, "binaryExpression", keep_node=True)
#         else:
#             make_ast_subtree(self.ast, ctx, "simpleExpression", keep_node=True)
#
#     def exitLogicOperator(self, ctx):
#         make_ast_subtree(self.ast, ctx, "logicOperator", keep_node=True)
#
#     def exitStart(self, ctx):
#         make_ast_subtree(self.ast, ctx, "start", keep_node=True)
#
#     def exitShow(self, ctx):
#         make_ast_subtree(self.ast, ctx, "show", keep_node=True)







class AutoMLCustomListener(AutoMLDSLListener):
    def __init__(self, rule_names):
        self.overridden_rules = [
            'dsl', 'model', 'mlModel', 'parameter', 'featureSelection',
            'metric', 'ruleSet', 'start', 'show'
        ]
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitDsl(self, ctx):
        make_ast_subtree(self.ast, ctx, "dsl", keep_node=True)

    def exitModel(self, ctx):
        make_ast_subtree(self.ast, ctx, "model", keep_node=True)

    def exitMlModel(self, ctx):
        make_ast_subtree(self.ast, ctx, "mlModel", keep_node=True)

    def exitParameter(self, ctx):
        make_ast_subtree(self.ast, ctx, "parameter", keep_node=True)

    def exitFeatureSelection(self, ctx):
        make_ast_subtree(self.ast, ctx, "featureSelection", keep_node=True)

    def exitMetric(self, ctx):
        make_ast_subtree(self.ast, ctx, "metric", keep_node=True)

    def exitRuleSet(self, ctx):
        make_ast_subtree(self.ast, ctx, "ruleSet", keep_node=True)

    def exitRule(self, ctx):
        make_ast_subtree(self.ast, ctx, "rule", keep_node=True)

    def exitExpression(self, ctx):
        make_ast_subtree(self.ast, ctx, "expression", keep_node=True)

    def exitLogicOperator(self, ctx):
        make_ast_subtree(self.ast, ctx, "logicOperator", keep_node=True)

    def exitStart(self, ctx):
        make_ast_subtree(self.ast, ctx, "start", keep_node=True)

    def exitShow(self, ctx):
        make_ast_subtree(self.ast, ctx, "show", keep_node=True)
