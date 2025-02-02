# class AutoMLCodeGenerator:
#     def __init__(self):
#         self.code_stack = []  # Stack to hold code sections
#         self.operand_stack = []  # Stack to hold data like parameters, metrics, features
#
#         self.model_name = None
#         self.task = None
#         self.ml_model = None
#         self.parameters = {}
#         self.metrics = []
#         self.features = []
#
#     def generate_code(self, ast):
#         # Push imports onto the code stack
#         self.code_stack.append(self._generate_imports())
#
#         # Process the AST and populate the operand stack
#         for node in ast:
#             if node['label'] == 'classification':
#                 self.task = node.get('text', "classification")
#
#             elif node['label'] == 'mlModel':
#                 self.ml_model = node.get('text', "unknown_model")
#
#             elif node['label'] == 'parameter':
#                 parameter_name = node.get('text', "unknown_param")
#                 parameter_values = node.get('value', [])
#                 self.parameters[parameter_name] = parameter_values
#
#             elif node['label'] == 'metric':
#                 self.metrics.append(node.get('text', "unknown_metric"))
#
#             elif node['label'] == 'featureMatch':
#                 self.features.append(node.get('text', "unknown_feature"))
#
#         # Push dataset and model training code onto the code stack
#         self.code_stack.append(self._generate_dataset())
#         self.code_stack.append(self._generate_model_training())
#
#         # Combine the code stack into the final output code
#         self.output_code = "\n".join(self.code_stack)
#         return self.output_code
#
#     def _generate_imports(self):
#         return """import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# """
#
#     def _generate_dataset(self):
#         # Use the operand stack (features) to generate the dataset code
#         features_list = ", ".join([f"'{feature}'" for feature in self.features])
#         return f"""
# # Load dataset
# X = data[[{features_list}]]
# y = data['target']
#
# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# """
#
#     def _generate_model_training(self):
#         # Use the operand stack (parameters) to generate model training code
#         params = ", ".join([f"{key}={value}" for key, value in self.parameters.items()])
#         return f"""
# # Train model
# model = {self.ml_model}({params})
# model.fit(X_train, y_train)
#
# # Evaluate model
# predictions = model.predict(X_test)
# accuracy = accuracy_score(y_test, predictions)
# precision = precision_score(y_test, predictions, average='weighted')
# recall = recall_score(y_test, predictions, average='weighted')
# f1 = f1_score(y_test, predictions, average='weighted')
#
# print(f"Accuracy: {{accuracy}}, Precision: {{precision}}, Recall: {{recall}}, F1 Score: {{f1}}")
# """







# class AutoMLCodeGenerator:
#     def __init__(self):
#         self.non_operands = ['classification', 'mlModel', 'parameter', 'metric', 'featureMatch']
#         self.operand_stack = []  # Stack for operands
#         self.code_stack = []  # Stack for generated code
#
#     def is_operand(self, item):
#         return item not in self.non_operands
#
#     def generate_code(self, post_order_array):
#         for item in post_order_array:
#             if not self.is_operand(item['label']):
#                 self.generate_code_based_on_non_operand(item['label'], item)
#             else:
#                 self.operand_stack.append(item['text'])
#
#         # Instead of combining the code stack directly, call generate_program to produce the output
#         return self.generate_program()
#
#     def generate_code_based_on_non_operand(self, label, item):
#         if label == 'classification':
#             self.generate_classification()
#
#         elif label == 'mlModel':
#             self.generate_ml_model()
#
#         elif label == 'parameter':
#             self.generate_parameter()
#
#         elif label == 'metric':
#             self.generate_metric()
#
#         elif label == 'featureMatch':
#             self.generate_feature_match()
#
#     def generate_classification(self):
#         self.code_stack.append("# Task: Classification\n")
#
#     def generate_ml_model(self):
#         model = self.operand_stack.pop()
#         self.code_stack.append(f"model = {model}()\n")
#
#     def generate_parameter(self):
#         parameter_value = self.operand_stack.pop()
#         parameter_name = self.operand_stack.pop()
#         self.code_stack.append(f"{parameter_name} = {parameter_value}\n")
#
#     def generate_metric(self):
#         metric = self.operand_stack.pop()
#         self.code_stack.append(f"# Metric: {metric}\n")
#
#     def generate_feature_match(self):
#         feature = self.operand_stack.pop()
#         self.code_stack.append(f"# Feature: {feature}\n")
#
#     def generate_program(self):
#         imports = self._generate_imports()
#         dataset_code = self._generate_dataset()
#         model_training_code = self._generate_model_training()
#
#         program_code = imports + dataset_code + model_training_code
#         return program_code
#
#     def _generate_imports(self):
#         return """import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# """
#
#     def _generate_dataset(self):
#         features_list = ", ".join([f"'{feature}'" for feature in self.operand_stack])
#         return f"""
# # Load dataset
# X = data[[{features_list}]]
# y = data['target']
#
# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# """
#
#     def _generate_model_training(self):
#         return """
# # Train model
# model.fit(X_train, y_train)
#
# # Evaluate model
# predictions = model.predict(X_test)
# accuracy = accuracy_score(y_test, predictions)
# precision = precision_score(y_test, predictions, average='weighted')
# recall = recall_score(y_test, predictions, average='weighted')
# f1 = f1_score(y_test, predictions, average='weighted')
#
# print(f"Accuracy: {{accuracy}}, Precision: {{precision}}, Recall: {{recall}}, F1 Score: {{f1}}")
# """








# class AutoMLCodeGenerator:
#     def __init__(self):
#         self.non_operands = ['classification', 'mlModel', 'parameter', 'metric', 'featureMatch', 'ruleSet', 'start', 'show']
#         self.operand_stack = []  # Stack for operands
#         self.code_stack = []  # Stack for generated code
#         self.scope_stack = []  # Stack for managing scopes like rule sets

#     def is_operand(self, item):
#         return item not in self.non_operands

#     def generate_code(self, post_order_array):
#         for item in post_order_array:
#             if not self.is_operand(item['label']):
#                 self.generate_code_based_on_non_operand(item['label'], item)
#             else:
#                 self.operand_stack.append(item['text'])

#         # Instead of combining the code stack directly, call generate_program to produce the output
#         return self.generate_program()

#     def generate_code_based_on_non_operand(self, label, item):
#         if label == 'classification':
#             self.generate_classification()

#         elif label == 'mlModel':
#             self.generate_ml_model()

#         elif label == 'parameter':
#             self.generate_parameter()

#         elif label == 'metric':
#             self.generate_metric()

#         elif label == 'featureMatch':
#             self.generate_feature_match()

#         elif label == 'ruleSet':
#             self.generate_rule_set()

#         elif label == 'start':
#             self.generate_start()

#         elif label == 'show':
#             self.generate_show()

#     def generate_classification(self):
#         self.code_stack.append("# Task: Classification\n")

#     def generate_ml_model(self):
#         model = self.operand_stack.pop()
#         self.code_stack.append(f"model = {model}()\n")

#     def generate_parameter(self):
#         parameter_value = self.operand_stack.pop()
#         parameter_name = self.operand_stack.pop()
#         self.code_stack.append(f"{parameter_name} = {parameter_value}\n")

#     def generate_metric(self):
#         metrics = self.operand_stack.pop()
#         metric_list = ", ".join(metrics.split(", "))
#         self.code_stack.append(f"# Metrics: {metric_list}\n")

#     def generate_feature_match(self):
#         feature_conditions = self.operand_stack.pop()
#         self.code_stack.append(f"# Feature selection: {feature_conditions}\n")

#     def generate_rule_set(self):
#         self.scope_stack.append("begin_scope")
#         rules = self.operand_stack.pop()
#         self.code_stack.append(f"# Rules:\n{rules}\n")
#         self.scope_stack.pop()

#     def generate_start(self):
#         model_name = self.operand_stack.pop()
#         self.code_stack.append(f"# Start model training with {model_name}\n")

#     def generate_show(self):
#         items = self.operand_stack.pop()
#         self.code_stack.append(f"# Show: {items}\n")

#     def generate_program(self):
#         imports = self._generate_imports()
#         dataset_code = self._generate_dataset()
#         model_training_code = self._generate_model_training()

#         program_code = imports + dataset_code + model_training_code
#         return program_code

#     def _generate_imports(self):
#         return """import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# """

#     def _generate_dataset(self):
#         features_list = ", ".join([f"'{feature}'" for feature in self.operand_stack])
#         return f"""
# # Load dataset
# X = data[[{features_list}]]
# y = data['target']

# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# """

#     def _generate_model_training(self):
#         return """
# # Train model
# model.fit(X_train, y_train)

# # Evaluate model
# predictions = model.predict(X_test)
# accuracy = accuracy_score(y_test, predictions)
# precision = precision_score(y_test, predictions, average='weighted')
# recall = recall_score(y_test, predictions, average='weighted')
# f1 = f1_score(y_test, predictions, average='weighted')

# print(f"Accuracy: {{accuracy}}, Precision: {{precision}}, Recall: {{recall}}, F1 Score: {{f1}}")
# """




class AutoMLCodeGenerator:
    def __init__(self):
        self.isFeature = "featureSelection"
        self.non_operands = ["classification", "mlModel", "parameter", "metric", "ruleSet", "start", "show"]
        self.operand_stack = []
        self.code_stack = []  
        self.scope_stack = []
        self.feature_stack = []
        self.prev_item = None

    def is_operand(self, item):
        return item not in self.non_operands

    def is_feature(self, item):
        return item == self.isFeature
    
    def generate_code(self, post_order_array):
        for item in post_order_array:
            if not self.is_operand(item['label']):
                self.generate_code_based_on_non_operand(item['label'], item)
            else:
                if item['label'] == 'featureMatch':
                    if self.prev_item:
                        self.feature_stack.append(self.prev_item['label'])
                else:
                    self.operand_stack.append(item['label'])
                self.prev_item = item

        return self.generate_program()

    def generate_code_based_on_non_operand(self, label, item):
        if label == 'classification':
            self.generate_classification()

        elif label == 'mlModel':
            self.generate_ml_model()

        elif label == 'parameter':
            self.generate_parameter()

        elif label == 'metric':
            self.generate_metric()

        elif label == 'featureSelection':
            self.generate_feature_selection()

        elif label == 'ruleSet':
            self.generate_rule_set()

        elif label == 'start':
            self.generate_start()

        elif label == 'show':
            self.generate_show()

    def generate_classification(self):
        self.code_stack.append("# Task: Classification\n")

    def generate_ml_model(self):
        model = self.operand_stack.pop()
        self.code_stack.append(f"model = {model}()\n")

    def generate_parameter(self):
        parameter_value = self.operand_stack.pop()
        parameter_name = self.operand_stack.pop()
        self.code_stack.append(f"{parameter_name} = {parameter_value}\n")

    def generate_metric(self):
        metrics = self.operand_stack.pop() or ""
        metric_list = ", ".join(metrics.split(", ")) if metrics else ""
        self.code_stack.append(f"# Metrics: {metric_list}\n")

    def generate_feature_selection(self):
        feature_conditions = self.operand_stack.pop()
        self.code_stack.append(f"# Feature selection: {feature_conditions}\n")

    def generate_rule_set(self):
        self.scope_stack.append("begin_scope")
        rules = self.operand_stack.pop()
        self.code_stack.append(f"# Rules:\n{rules}\n")
        self.scope_stack.pop()

    def generate_start(self):
        model_name = self.operand_stack.pop()
        self.code_stack.append(f"# Start model training with {model_name}\n")

    def generate_show(self):
        items = self.operand_stack.pop()
        self.code_stack.append(f"# Show: {items}\n")

    def generate_program(self):
        imports = self._generate_imports()
        dataset_code = self._generate_dataset()
        model_training_code = self._generate_model_training()

        program_code = imports + dataset_code + model_training_code
        return program_code

    def _generate_imports(self):
        return """import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
"""

    def _generate_dataset(self):
        features_list = ", ".join([f"'{feature}'" for feature in self.feature_stack])
        return f"""
# Load dataset
X = data[{features_list}]
y = data['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
"""

    def _generate_model_training(self):
        return """
# Train model
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')
f1 = f1_score(y_test, predictions, average='weighted')

print(f"Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1 Score: {f1}")
"""
