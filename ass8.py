import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

def main():
    try:
        # Load the Iris dataset
        iris = load_iris()
        data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        data['species'] = iris.target
        data['species'] = data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

        # Display basic information about the dataset
        print("Dataset Head:")
        print(data.head())
        print("\nDataset Info:")
        print(data.info())

        # Pairplot using seaborn
        sns.pairplot(data, hue='species', diag_kind='kde', palette='Set2')
        plt.suptitle("Pairplot of Iris Dataset", y=1.02)
        plt.show()

        # Boxplot for feature comparison
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=data, x='species', y='sepal length (cm)', palette='Set3')
        plt.title("Boxplot of Sepal Length by Species")
        plt.xlabel("Species")
        plt.ylabel("Sepal Length (cm)")
        plt.show()

        # Scatter plot with customization
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=data, x='sepal length (cm)', y='sepal width (cm)', hue='species', style='species', palette='Set1')
        plt.title("Scatter Plot of Sepal Dimensions")
        plt.xlabel("Sepal Length (cm)")
        plt.ylabel("Sepal Width (cm)")
        plt.legend(title="Species")
        plt.show()

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the dataset file is available.")
    except KeyError as e:
        print(f"Error: {e}. Please check the dataset columns.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()