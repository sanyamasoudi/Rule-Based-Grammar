# Generated from E:/JOZVEH/Compiler/Final Project/RuleBased_AutoML/AutoML - Copy/Grammar/AutoMLDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,63,261,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,4,0,66,8,0,
        11,0,12,0,67,1,1,1,1,1,1,1,1,1,1,1,1,5,1,76,8,1,10,1,12,1,79,9,1,
        1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,91,8,3,1,4,1,4,1,4,1,
        4,1,4,1,4,5,4,99,8,4,10,4,12,4,102,9,4,1,4,3,4,105,8,4,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,5,8,123,8,
        8,10,8,12,8,126,9,8,1,8,1,8,1,8,3,8,131,8,8,1,9,1,9,1,10,1,10,1,
        10,1,11,1,11,1,11,5,11,141,8,11,10,11,12,11,144,9,11,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,3,13,153,8,13,1,14,1,14,1,14,5,14,158,8,14,
        10,14,12,14,161,9,14,1,15,1,15,1,15,3,15,166,8,15,1,15,1,15,1,15,
        3,15,171,8,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,5,18,
        182,8,18,10,18,12,18,185,9,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,
        1,20,1,21,1,21,1,22,1,22,1,22,1,22,5,22,201,8,22,10,22,12,22,204,
        9,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,5,23,216,
        8,23,10,23,12,23,219,9,23,1,24,1,24,3,24,223,8,24,1,25,1,25,1,25,
        1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,28,1,28,
        1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,5,30,250,8,30,10,30,
        12,30,253,9,30,1,30,1,30,3,30,257,8,30,1,31,1,31,1,31,0,0,32,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,0,7,1,0,5,8,1,0,11,15,1,0,60,61,1,0,24,32,1,
        0,38,43,1,0,36,37,1,0,55,58,251,0,65,1,0,0,0,2,69,1,0,0,0,4,82,1,
        0,0,0,6,90,1,0,0,0,8,92,1,0,0,0,10,106,1,0,0,0,12,108,1,0,0,0,14,
        116,1,0,0,0,16,130,1,0,0,0,18,132,1,0,0,0,20,134,1,0,0,0,22,137,
        1,0,0,0,24,145,1,0,0,0,26,147,1,0,0,0,28,154,1,0,0,0,30,162,1,0,
        0,0,32,172,1,0,0,0,34,174,1,0,0,0,36,176,1,0,0,0,38,186,1,0,0,0,
        40,192,1,0,0,0,42,194,1,0,0,0,44,196,1,0,0,0,46,207,1,0,0,0,48,222,
        1,0,0,0,50,224,1,0,0,0,52,230,1,0,0,0,54,236,1,0,0,0,56,238,1,0,
        0,0,58,240,1,0,0,0,60,245,1,0,0,0,62,258,1,0,0,0,64,66,3,2,1,0,65,
        64,1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,1,1,0,0,
        0,69,70,5,1,0,0,70,71,5,59,0,0,71,72,5,2,0,0,72,73,3,4,2,0,73,77,
        5,3,0,0,74,76,3,6,3,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,
        77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,4,0,0,81,3,1,0,
        0,0,82,83,7,0,0,0,83,5,1,0,0,0,84,91,3,8,4,0,85,91,3,20,10,0,86,
        91,3,26,13,0,87,91,3,44,22,0,88,91,3,58,29,0,89,91,3,60,30,0,90,
        84,1,0,0,0,90,85,1,0,0,0,90,86,1,0,0,0,90,87,1,0,0,0,90,88,1,0,0,
        0,90,89,1,0,0,0,91,7,1,0,0,0,92,93,5,9,0,0,93,94,5,59,0,0,94,95,
        5,10,0,0,95,104,3,10,5,0,96,100,5,3,0,0,97,99,3,12,6,0,98,97,1,0,
        0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,
        0,102,100,1,0,0,0,103,105,5,4,0,0,104,96,1,0,0,0,104,105,1,0,0,0,
        105,9,1,0,0,0,106,107,7,1,0,0,107,11,1,0,0,0,108,109,5,16,0,0,109,
        110,5,17,0,0,110,111,5,18,0,0,111,112,3,14,7,0,112,113,5,19,0,0,
        113,114,5,18,0,0,114,115,3,16,8,0,115,13,1,0,0,0,116,117,5,60,0,
        0,117,15,1,0,0,0,118,119,5,20,0,0,119,124,3,18,9,0,120,121,5,21,
        0,0,121,123,3,18,9,0,122,120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,
        0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,22,
        0,0,128,131,1,0,0,0,129,131,3,18,9,0,130,118,1,0,0,0,130,129,1,0,
        0,0,131,17,1,0,0,0,132,133,7,2,0,0,133,19,1,0,0,0,134,135,5,23,0,
        0,135,136,3,22,11,0,136,21,1,0,0,0,137,142,3,24,12,0,138,139,5,21,
        0,0,139,141,3,24,12,0,140,138,1,0,0,0,141,144,1,0,0,0,142,140,1,
        0,0,0,142,143,1,0,0,0,143,23,1,0,0,0,144,142,1,0,0,0,145,146,7,3,
        0,0,146,25,1,0,0,0,147,148,5,33,0,0,148,149,5,59,0,0,149,152,3,28,
        14,0,150,151,5,34,0,0,151,153,3,36,18,0,152,150,1,0,0,0,152,153,
        1,0,0,0,153,27,1,0,0,0,154,159,3,30,15,0,155,156,5,21,0,0,156,158,
        3,30,15,0,157,155,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,
        1,0,0,0,160,29,1,0,0,0,161,159,1,0,0,0,162,165,3,32,16,0,163,164,
        5,35,0,0,164,166,3,32,16,0,165,163,1,0,0,0,165,166,1,0,0,0,166,170,
        1,0,0,0,167,168,3,42,21,0,168,169,3,34,17,0,169,171,1,0,0,0,170,
        167,1,0,0,0,170,171,1,0,0,0,171,31,1,0,0,0,172,173,5,59,0,0,173,
        33,1,0,0,0,174,175,5,61,0,0,175,35,1,0,0,0,176,183,3,38,19,0,177,
        178,5,36,0,0,178,182,3,38,19,0,179,180,5,37,0,0,180,182,3,38,19,
        0,181,177,1,0,0,0,181,179,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,
        0,183,184,1,0,0,0,184,37,1,0,0,0,185,183,1,0,0,0,186,187,3,40,20,
        0,187,188,5,35,0,0,188,189,3,40,20,0,189,190,3,42,21,0,190,191,3,
        18,9,0,191,39,1,0,0,0,192,193,5,59,0,0,193,41,1,0,0,0,194,195,7,
        4,0,0,195,43,1,0,0,0,196,197,5,44,0,0,197,198,5,59,0,0,198,202,5,
        3,0,0,199,201,3,46,23,0,200,199,1,0,0,0,201,204,1,0,0,0,202,200,
        1,0,0,0,202,203,1,0,0,0,203,205,1,0,0,0,204,202,1,0,0,0,205,206,
        5,4,0,0,206,45,1,0,0,0,207,208,5,45,0,0,208,209,5,46,0,0,209,210,
        5,47,0,0,210,211,3,48,24,0,211,212,5,48,0,0,212,217,5,59,0,0,213,
        214,5,21,0,0,214,216,5,59,0,0,215,213,1,0,0,0,216,219,1,0,0,0,217,
        215,1,0,0,0,217,218,1,0,0,0,218,47,1,0,0,0,219,217,1,0,0,0,220,223,
        3,52,26,0,221,223,3,50,25,0,222,220,1,0,0,0,222,221,1,0,0,0,223,
        49,1,0,0,0,224,225,5,49,0,0,225,226,3,48,24,0,226,227,3,56,28,0,
        227,228,3,48,24,0,228,229,5,50,0,0,229,51,1,0,0,0,230,231,3,54,27,
        0,231,232,5,35,0,0,232,233,3,54,27,0,233,234,3,42,21,0,234,235,3,
        18,9,0,235,53,1,0,0,0,236,237,5,59,0,0,237,55,1,0,0,0,238,239,7,
        5,0,0,239,57,1,0,0,0,240,241,5,51,0,0,241,242,5,59,0,0,242,243,5,
        52,0,0,243,244,5,59,0,0,244,59,1,0,0,0,245,246,5,53,0,0,246,251,
        3,62,31,0,247,248,5,21,0,0,248,250,3,62,31,0,249,247,1,0,0,0,250,
        253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,256,1,0,0,0,253,
        251,1,0,0,0,254,255,5,54,0,0,255,257,5,59,0,0,256,254,1,0,0,0,256,
        257,1,0,0,0,257,61,1,0,0,0,258,259,7,6,0,0,259,63,1,0,0,0,19,67,
        77,90,100,104,124,130,142,152,159,165,170,181,183,202,217,222,251,
        256
    ]

class AutoMLDSLParser ( Parser ):

    grammarFileName = "AutoMLDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'model'", "'task'", "'{'", "'}'", "'predict'", 
                     "'classification'", "'regression'", "'clustering'", 
                     "'mlModel'", "'type'", "'RandomForest'", "'DecisionTree'", 
                     "'SVM'", "'AutoML'", "'KMeans'", "'parameter'", "'name'", 
                     "'='", "'value'", "'['", "','", "']'", "'metric'", 
                     "'mse'", "'r2_score'", "'mae'", "'rmse'", "'accuracy'", 
                     "'precision'", "'recall'", "'f1_score'", "'all'", "'select'", 
                     "'where'", "'.'", "'and'", "'or'", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "'!='", "'ruleSet'", "'rule'", "':'", 
                     "'if'", "'then'", "'('", "')'", "'start'", "'with'", 
                     "'show'", "'from'", "'models'", "'features'", "'metrics'", 
                     "'rules'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "STRING", 
                      "FLOAT", "WS", "COMMENT" ]

    RULE_dsl = 0
    RULE_model = 1
    RULE_task = 2
    RULE_modelElement = 3
    RULE_mlModel = 4
    RULE_mlModelType = 5
    RULE_parameter = 6
    RULE_parameterName = 7
    RULE_valueList = 8
    RULE_value = 9
    RULE_metric = 10
    RULE_metricNameList = 11
    RULE_metricName = 12
    RULE_featureSelection = 13
    RULE_featureList = 14
    RULE_featureMatch = 15
    RULE_featureExpr = 16
    RULE_featureValue = 17
    RULE_conditionList = 18
    RULE_condition = 19
    RULE_conditionExpr = 20
    RULE_operator = 21
    RULE_ruleSet = 22
    RULE_rule = 23
    RULE_expression = 24
    RULE_binaryExpression = 25
    RULE_simpleExpression = 26
    RULE_simpleName = 27
    RULE_logicOperator = 28
    RULE_start = 29
    RULE_show = 30
    RULE_visualization = 31

    ruleNames =  [ "dsl", "model", "task", "modelElement", "mlModel", "mlModelType", 
                   "parameter", "parameterName", "valueList", "value", "metric", 
                   "metricNameList", "metricName", "featureSelection", "featureList", 
                   "featureMatch", "featureExpr", "featureValue", "conditionList", 
                   "condition", "conditionExpr", "operator", "ruleSet", 
                   "rule", "expression", "binaryExpression", "simpleExpression", 
                   "simpleName", "logicOperator", "start", "show", "visualization" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    ID=59
    STRING=60
    FLOAT=61
    WS=62
    COMMENT=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DslContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.ModelContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.ModelContext,i)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_dsl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDsl" ):
                listener.enterDsl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDsl" ):
                listener.exitDsl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDsl" ):
                return visitor.visitDsl(self)
            else:
                return visitor.visitChildren(self)




    def dsl(self):

        localctx = AutoMLDSLParser.DslContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dsl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.model()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AutoMLDSLParser.ID, 0)

        def task(self):
            return self.getTypedRuleContext(AutoMLDSLParser.TaskContext,0)


        def modelElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.ModelElementContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.ModelElementContext,i)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel" ):
                listener.enterModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel" ):
                listener.exitModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel" ):
                return visitor.visitModel(self)
            else:
                return visitor.visitChildren(self)




    def model(self):

        localctx = AutoMLDSLParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(AutoMLDSLParser.T__0)
            self.state = 70
            self.match(AutoMLDSLParser.ID)
            self.state = 71
            self.match(AutoMLDSLParser.T__1)
            self.state = 72
            self.task()
            self.state = 73
            self.match(AutoMLDSLParser.T__2)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 11276599852794368) != 0):
                self.state = 74
                self.modelElement()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(AutoMLDSLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TaskContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_task

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTask" ):
                listener.enterTask(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTask" ):
                listener.exitTask(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTask" ):
                return visitor.visitTask(self)
            else:
                return visitor.visitChildren(self)




    def task(self):

        localctx = AutoMLDSLParser.TaskContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_task)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mlModel(self):
            return self.getTypedRuleContext(AutoMLDSLParser.MlModelContext,0)


        def metric(self):
            return self.getTypedRuleContext(AutoMLDSLParser.MetricContext,0)


        def featureSelection(self):
            return self.getTypedRuleContext(AutoMLDSLParser.FeatureSelectionContext,0)


        def ruleSet(self):
            return self.getTypedRuleContext(AutoMLDSLParser.RuleSetContext,0)


        def start(self):
            return self.getTypedRuleContext(AutoMLDSLParser.StartContext,0)


        def show(self):
            return self.getTypedRuleContext(AutoMLDSLParser.ShowContext,0)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_modelElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelElement" ):
                listener.enterModelElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelElement" ):
                listener.exitModelElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelElement" ):
                return visitor.visitModelElement(self)
            else:
                return visitor.visitChildren(self)




    def modelElement(self):

        localctx = AutoMLDSLParser.ModelElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_modelElement)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.mlModel()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.metric()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.featureSelection()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.ruleSet()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.start()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 6)
                self.state = 89
                self.show()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MlModelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AutoMLDSLParser.ID, 0)

        def mlModelType(self):
            return self.getTypedRuleContext(AutoMLDSLParser.MlModelTypeContext,0)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.ParameterContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.ParameterContext,i)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_mlModel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMlModel" ):
                listener.enterMlModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMlModel" ):
                listener.exitMlModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMlModel" ):
                return visitor.visitMlModel(self)
            else:
                return visitor.visitChildren(self)




    def mlModel(self):

        localctx = AutoMLDSLParser.MlModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mlModel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(AutoMLDSLParser.T__8)
            self.state = 93
            self.match(AutoMLDSLParser.ID)
            self.state = 94
            self.match(AutoMLDSLParser.T__9)
            self.state = 95
            self.mlModelType()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 96
                self.match(AutoMLDSLParser.T__2)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 97
                    self.parameter()
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.match(AutoMLDSLParser.T__3)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MlModelTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_mlModelType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMlModelType" ):
                listener.enterMlModelType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMlModelType" ):
                listener.exitMlModelType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMlModelType" ):
                return visitor.visitMlModelType(self)
            else:
                return visitor.visitChildren(self)




    def mlModelType(self):

        localctx = AutoMLDSLParser.MlModelTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mlModelType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterName(self):
            return self.getTypedRuleContext(AutoMLDSLParser.ParameterNameContext,0)


        def valueList(self):
            return self.getTypedRuleContext(AutoMLDSLParser.ValueListContext,0)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = AutoMLDSLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(AutoMLDSLParser.T__15)
            self.state = 109
            self.match(AutoMLDSLParser.T__16)
            self.state = 110
            self.match(AutoMLDSLParser.T__17)
            self.state = 111
            self.parameterName()
            self.state = 112
            self.match(AutoMLDSLParser.T__18)
            self.state = 113
            self.match(AutoMLDSLParser.T__17)
            self.state = 114
            self.valueList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AutoMLDSLParser.STRING, 0)

        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_parameterName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterName" ):
                listener.enterParameterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterName" ):
                listener.exitParameterName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterName" ):
                return visitor.visitParameterName(self)
            else:
                return visitor.visitChildren(self)




    def parameterName(self):

        localctx = AutoMLDSLParser.ParameterNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameterName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(AutoMLDSLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.ValueContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.ValueContext,i)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_valueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueList" ):
                listener.enterValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueList" ):
                listener.exitValueList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueList" ):
                return visitor.visitValueList(self)
            else:
                return visitor.visitChildren(self)




    def valueList(self):

        localctx = AutoMLDSLParser.ValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_valueList)
        self._la = 0 # Token type
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(AutoMLDSLParser.T__19)
                self.state = 119
                self.value()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 120
                    self.match(AutoMLDSLParser.T__20)
                    self.state = 121
                    self.value()
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 127
                self.match(AutoMLDSLParser.T__21)
                pass
            elif token in [60, 61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AutoMLDSLParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(AutoMLDSLParser.FLOAT, 0)

        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = AutoMLDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not(_la==60 or _la==61):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetricContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metricNameList(self):
            return self.getTypedRuleContext(AutoMLDSLParser.MetricNameListContext,0)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_metric

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetric" ):
                listener.enterMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetric" ):
                listener.exitMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetric" ):
                return visitor.visitMetric(self)
            else:
                return visitor.visitChildren(self)




    def metric(self):

        localctx = AutoMLDSLParser.MetricContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_metric)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(AutoMLDSLParser.T__22)
            self.state = 135
            self.metricNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetricNameListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metricName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.MetricNameContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.MetricNameContext,i)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_metricNameList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetricNameList" ):
                listener.enterMetricNameList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetricNameList" ):
                listener.exitMetricNameList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetricNameList" ):
                return visitor.visitMetricNameList(self)
            else:
                return visitor.visitChildren(self)




    def metricNameList(self):

        localctx = AutoMLDSLParser.MetricNameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_metricNameList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.metricName()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 138
                self.match(AutoMLDSLParser.T__20)
                self.state = 139
                self.metricName()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetricNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_metricName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetricName" ):
                listener.enterMetricName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetricName" ):
                listener.exitMetricName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetricName" ):
                return visitor.visitMetricName(self)
            else:
                return visitor.visitChildren(self)




    def metricName(self):

        localctx = AutoMLDSLParser.MetricNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_metricName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8573157376) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureSelectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AutoMLDSLParser.ID, 0)

        def featureList(self):
            return self.getTypedRuleContext(AutoMLDSLParser.FeatureListContext,0)


        def conditionList(self):
            return self.getTypedRuleContext(AutoMLDSLParser.ConditionListContext,0)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_featureSelection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeatureSelection" ):
                listener.enterFeatureSelection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeatureSelection" ):
                listener.exitFeatureSelection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeatureSelection" ):
                return visitor.visitFeatureSelection(self)
            else:
                return visitor.visitChildren(self)




    def featureSelection(self):

        localctx = AutoMLDSLParser.FeatureSelectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_featureSelection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(AutoMLDSLParser.T__32)
            self.state = 148
            self.match(AutoMLDSLParser.ID)
            self.state = 149
            self.featureList()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 150
                self.match(AutoMLDSLParser.T__33)
                self.state = 151
                self.conditionList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def featureMatch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.FeatureMatchContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.FeatureMatchContext,i)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_featureList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeatureList" ):
                listener.enterFeatureList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeatureList" ):
                listener.exitFeatureList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeatureList" ):
                return visitor.visitFeatureList(self)
            else:
                return visitor.visitChildren(self)




    def featureList(self):

        localctx = AutoMLDSLParser.FeatureListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_featureList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.featureMatch()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 155
                self.match(AutoMLDSLParser.T__20)
                self.state = 156
                self.featureMatch()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def featureExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.FeatureExprContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.FeatureExprContext,i)


        def operator(self):
            return self.getTypedRuleContext(AutoMLDSLParser.OperatorContext,0)


        def featureValue(self):
            return self.getTypedRuleContext(AutoMLDSLParser.FeatureValueContext,0)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_featureMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeatureMatch" ):
                listener.enterFeatureMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeatureMatch" ):
                listener.exitFeatureMatch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeatureMatch" ):
                return visitor.visitFeatureMatch(self)
            else:
                return visitor.visitChildren(self)




    def featureMatch(self):

        localctx = AutoMLDSLParser.FeatureMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_featureMatch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.featureExpr()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 163
                self.match(AutoMLDSLParser.T__34)
                self.state = 164
                self.featureExpr()


            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17317308137472) != 0):
                self.state = 167
                self.operator()
                self.state = 168
                self.featureValue()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AutoMLDSLParser.ID, 0)

        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_featureExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeatureExpr" ):
                listener.enterFeatureExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeatureExpr" ):
                listener.exitFeatureExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeatureExpr" ):
                return visitor.visitFeatureExpr(self)
            else:
                return visitor.visitChildren(self)




    def featureExpr(self):

        localctx = AutoMLDSLParser.FeatureExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_featureExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(AutoMLDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(AutoMLDSLParser.FLOAT, 0)

        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_featureValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeatureValue" ):
                listener.enterFeatureValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeatureValue" ):
                listener.exitFeatureValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeatureValue" ):
                return visitor.visitFeatureValue(self)
            else:
                return visitor.visitChildren(self)




    def featureValue(self):

        localctx = AutoMLDSLParser.FeatureValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_featureValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(AutoMLDSLParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.ConditionContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.ConditionContext,i)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_conditionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionList" ):
                listener.enterConditionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionList" ):
                listener.exitConditionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionList" ):
                return visitor.visitConditionList(self)
            else:
                return visitor.visitChildren(self)




    def conditionList(self):

        localctx = AutoMLDSLParser.ConditionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_conditionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.condition()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36 or _la==37:
                self.state = 181
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [36]:
                    self.state = 177
                    self.match(AutoMLDSLParser.T__35)
                    self.state = 178
                    self.condition()
                    pass
                elif token in [37]:
                    self.state = 179
                    self.match(AutoMLDSLParser.T__36)
                    self.state = 180
                    self.condition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.ConditionExprContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.ConditionExprContext,i)


        def operator(self):
            return self.getTypedRuleContext(AutoMLDSLParser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(AutoMLDSLParser.ValueContext,0)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = AutoMLDSLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.conditionExpr()
            self.state = 187
            self.match(AutoMLDSLParser.T__34)
            self.state = 188
            self.conditionExpr()
            self.state = 189
            self.operator()
            self.state = 190
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AutoMLDSLParser.ID, 0)

        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_conditionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionExpr" ):
                listener.enterConditionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionExpr" ):
                listener.exitConditionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionExpr" ):
                return visitor.visitConditionExpr(self)
            else:
                return visitor.visitChildren(self)




    def conditionExpr(self):

        localctx = AutoMLDSLParser.ConditionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_conditionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(AutoMLDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = AutoMLDSLParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17317308137472) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AutoMLDSLParser.ID, 0)

        def rule_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.RuleContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.RuleContext,i)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_ruleSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleSet" ):
                listener.enterRuleSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleSet" ):
                listener.exitRuleSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleSet" ):
                return visitor.visitRuleSet(self)
            else:
                return visitor.visitChildren(self)




    def ruleSet(self):

        localctx = AutoMLDSLParser.RuleSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ruleSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(AutoMLDSLParser.T__43)
            self.state = 197
            self.match(AutoMLDSLParser.ID)
            self.state = 198
            self.match(AutoMLDSLParser.T__2)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 199
                self.rule_()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self.match(AutoMLDSLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(AutoMLDSLParser.ExpressionContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AutoMLDSLParser.ID)
            else:
                return self.getToken(AutoMLDSLParser.ID, i)

        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule" ):
                return visitor.visitRule(self)
            else:
                return visitor.visitChildren(self)




    def rule_(self):

        localctx = AutoMLDSLParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(AutoMLDSLParser.T__44)
            self.state = 208
            self.match(AutoMLDSLParser.T__45)
            self.state = 209
            self.match(AutoMLDSLParser.T__46)
            self.state = 210
            self.expression()
            self.state = 211
            self.match(AutoMLDSLParser.T__47)
            self.state = 212
            self.match(AutoMLDSLParser.ID)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 213
                self.match(AutoMLDSLParser.T__20)
                self.state = 214
                self.match(AutoMLDSLParser.ID)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleExpression(self):
            return self.getTypedRuleContext(AutoMLDSLParser.SimpleExpressionContext,0)


        def binaryExpression(self):
            return self.getTypedRuleContext(AutoMLDSLParser.BinaryExpressionContext,0)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = AutoMLDSLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expression)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.simpleExpression()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.binaryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.ExpressionContext,i)


        def logicOperator(self):
            return self.getTypedRuleContext(AutoMLDSLParser.LogicOperatorContext,0)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_binaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpression" ):
                listener.enterBinaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpression" ):
                listener.exitBinaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpression" ):
                return visitor.visitBinaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def binaryExpression(self):

        localctx = AutoMLDSLParser.BinaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_binaryExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(AutoMLDSLParser.T__48)
            self.state = 225
            self.expression()
            self.state = 226
            self.logicOperator()
            self.state = 227
            self.expression()
            self.state = 228
            self.match(AutoMLDSLParser.T__49)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.SimpleNameContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.SimpleNameContext,i)


        def operator(self):
            return self.getTypedRuleContext(AutoMLDSLParser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(AutoMLDSLParser.ValueContext,0)


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_simpleExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpression" ):
                listener.enterSimpleExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpression" ):
                listener.exitSimpleExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpression" ):
                return visitor.visitSimpleExpression(self)
            else:
                return visitor.visitChildren(self)




    def simpleExpression(self):

        localctx = AutoMLDSLParser.SimpleExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_simpleExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.simpleName()
            self.state = 231
            self.match(AutoMLDSLParser.T__34)
            self.state = 232
            self.simpleName()
            self.state = 233
            self.operator()
            self.state = 234
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AutoMLDSLParser.ID, 0)

        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_simpleName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleName" ):
                listener.enterSimpleName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleName" ):
                listener.exitSimpleName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleName" ):
                return visitor.visitSimpleName(self)
            else:
                return visitor.visitChildren(self)




    def simpleName(self):

        localctx = AutoMLDSLParser.SimpleNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_simpleName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(AutoMLDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_logicOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOperator" ):
                listener.enterLogicOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOperator" ):
                listener.exitLogicOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOperator" ):
                return visitor.visitLogicOperator(self)
            else:
                return visitor.visitChildren(self)




    def logicOperator(self):

        localctx = AutoMLDSLParser.LogicOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_logicOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            _la = self._input.LA(1)
            if not(_la==36 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AutoMLDSLParser.ID)
            else:
                return self.getToken(AutoMLDSLParser.ID, i)

        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = AutoMLDSLParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(AutoMLDSLParser.T__50)
            self.state = 241
            self.match(AutoMLDSLParser.ID)
            self.state = 242
            self.match(AutoMLDSLParser.T__51)
            self.state = 243
            self.match(AutoMLDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def visualization(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutoMLDSLParser.VisualizationContext)
            else:
                return self.getTypedRuleContext(AutoMLDSLParser.VisualizationContext,i)


        def ID(self):
            return self.getToken(AutoMLDSLParser.ID, 0)

        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_show

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShow" ):
                listener.enterShow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShow" ):
                listener.exitShow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShow" ):
                return visitor.visitShow(self)
            else:
                return visitor.visitChildren(self)




    def show(self):

        localctx = AutoMLDSLParser.ShowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_show)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(AutoMLDSLParser.T__52)
            self.state = 246
            self.visualization()
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 247
                self.match(AutoMLDSLParser.T__20)
                self.state = 248
                self.visualization()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 254
                self.match(AutoMLDSLParser.T__53)
                self.state = 255
                self.match(AutoMLDSLParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisualizationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AutoMLDSLParser.RULE_visualization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualization" ):
                listener.enterVisualization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualization" ):
                listener.exitVisualization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualization" ):
                return visitor.visitVisualization(self)
            else:
                return visitor.visitChildren(self)




    def visualization(self):

        localctx = AutoMLDSLParser.VisualizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_visualization)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 540431955284459520) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





