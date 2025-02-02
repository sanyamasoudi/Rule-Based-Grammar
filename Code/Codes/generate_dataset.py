def _generate_dataset(self):
        features_list = ", ".join([f"'{feature}'" for feature in self.features])
        return f"""
# Load dataset
X = data[[{features_list}]]
y = data['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
"""

    