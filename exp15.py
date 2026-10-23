from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

print("Prediction:", model.predict([[4]]))