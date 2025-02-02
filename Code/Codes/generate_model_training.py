def _generate_model_training(self):
        params = ", ".join([f"{key}={value}" for key, value in self.parameters.items()])
        return f"""
# Train model
model = {self.ml_model}({params})
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')
f1 = f1_score(y_test, predictions, average='weighted')

print(f"Accuracy: {{accuracy}}, Precision: {{precision}}, Recall: {{recall}}, F1 Score: {{f1}}")
"""
