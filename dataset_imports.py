from sklearn import datasets

iris = datasets.load_iris(as_frame=True)
df = iris.data
df["target"] = iris.target
print(df.head())

df.to_csv("iris.csv", index=False)
