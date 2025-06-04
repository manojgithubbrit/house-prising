from sklearn.linear_model import LinearRegression

X = [[1000, 2], [1500, 3], [1800, 3]]  # [Area, Bedrooms]
y = [30, 45, 50]  # House Price in Lakhs

model = LinearRegression()
model.fit(X, y)

print("Predicted Price:", model.predict([[1600, 2]]))  # Predict for a new house