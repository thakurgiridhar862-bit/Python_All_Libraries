import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("TITANIC DATASET ANALYSIS")
print("=" * 50)


def load_data():
    df = pd.read_csv("Task_2_Titanic_EDA/data/data_titanic.csv")
    return df


def dataset_overview(df):
    print("\nDATASET OVERVIEW")
    print("-" * 50)

    print("\nFIRST FIVE ROWS")
    print("-" * 50)
    print(df.head())

    print(f"\nTotal Rows             : {df.shape[0]}")
    print(f"Total Columns          : {df.shape[1]}")
    print(f"Total Missing Values   : {df.isnull().sum().sum()}")
    print(f"Total Duplicate Values : {df.duplicated().sum()}")

    print("\nMISSING VALUES")
    print("-" * 50)
    print(df.isnull().sum().sort_values(ascending=False))

    print("\nDATA TYPES")
    print("-" * 50)
    print(df.dtypes)

    print("\nSTATISTICAL SUMMARY")
    print("-" * 50)
    print(df.describe(include="all"))


def data_cleaning(df):
    print("\nDATA CLEANING")
    print("=" * 50)

    print("\nBefore Cleaning")
    print("-" * 50)
    print(f"Shape: {df.shape}")
    print(df.isnull().sum().sort_values(ascending=False))

    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df = df.drop(columns=["Cabin", "PassengerId", "Ticket"])
    df = df.drop_duplicates()

    print("\nAfter Cleaning")
    print("-" * 50)
    print(f"Shape: {df.shape}")
    print(df.isnull().sum().sort_values(ascending=False))

    return df


def categorical_analysis(df, column, title, graph_name, insight):
    print("\n" + title.upper())
    print("-" * 50)

    print(df[column].value_counts())

    percentage = df[column].value_counts(normalize=True) * 100

    print("\nCATEGORY PERCENTAGE")
    print("-" * 50)
    print(percentage.round(2))

    plt.figure(figsize=(10, 6))
    ax = sns.countplot(data=df, x=column)

    for container in ax.containers:
        ax.bar_label(container, padding=5)

    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Number of Passengers")
    plt.grid(axis="y", alpha=0.3)

    plt.savefig(f"Task_2_Titanic_EDA/graphs/{graph_name}", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

    print("\nINSIGHT")
    print("-" * 50)
    print(insight)


def numerical_analysis(df, column, title, hist_name, box_name, insight):
    print("\n" + title.upper())
    print("-" * 50)

    print(df[column].describe())

    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=column, kde=True, bins=10)

    plt.title(f"{column} Histogram")
    plt.xlabel(column)
    plt.ylabel("Number of Passengers")
    plt.grid(axis="y", alpha=0.3)

    plt.savefig(f"Task_2_Titanic_EDA/graphs/{hist_name}", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, y=column)

    plt.title(f"{column} Boxplot")
    plt.ylabel(column)
    plt.grid(axis="y", alpha=0.3)

    plt.savefig(f"Task_2_Titanic_EDA/graphs/{box_name}", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

    print("\nINSIGHT")
    print("-" * 50)
    print(insight)


def univariate_analysis(df):
    print("\nUNIVARIATE ANALYSIS")
    print("=" * 50)

    categorical_analysis(
        df,
        "Survived",
        "Survival Distribution Analysis",
        "survival_distribution.png",
        "Most passengers did not survive the Titanic disaster.",
    )

    categorical_analysis(
        df,
        "Sex",
        "Gender Distribution Analysis",
        "gender_distribution.png",
        "The majority of passengers on board were male.",
    )

    categorical_analysis(
        df,
        "Pclass",
        "Passenger Class Distribution Analysis",
        "pclass_distribution.png",
        "Most passengers traveled in Third Class.",
    )

    categorical_analysis(
        df,
        "Embarked",
        "Embarked Port Distribution Analysis",
        "embarked_distribution.png",
        "Most passengers boarded the Titanic from Southampton.",
    )

    categorical_analysis(
        df,
        "SibSp",
        "Siblings / Spouse Distribution Analysis",
        "sibsp_distribution.png",
        "Most passengers traveled without siblings or spouses.",
    )

    categorical_analysis(
        df,
        "Parch",
        "Parents / Children Distribution Analysis",
        "parch_distribution.png",
        "Most passengers traveled without parents or children.",
    )

    numerical_analysis(
        df,
        "Fare",
        "Fare Distribution Analysis",
        "fare_distribution.png",
        "fare_distribution_boxplot.png",
        "Most passengers paid relatively low fares, while a few paid significantly higher fares.",
    )

    numerical_analysis(
        df,
        "Age",
        "Age Distribution Analysis",
        "age_distribution.png",
        "age_distribution_boxplot.png",
        "Most passengers were young adults.",
    )


def categorical_bivariate_analysis(df, title, column, hue, graph_name, insight):
    print("\n" + title.upper())
    print("-" * 50)

    print(pd.crosstab(df[column], df[hue]))

    plt.figure(figsize=(10, 6))
    ax = sns.countplot(data=df, x=column, hue=hue)

    for container in ax.containers:
        ax.bar_label(container, padding=5)

    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Number of Passengers")
    plt.grid(axis="y", alpha=0.3)

    plt.savefig(f"Task_2_Titanic_EDA/graphs/{graph_name}", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

    print("\nINSIGHT")
    print("-" * 50)
    print(insight)


def numerical_bivariate_analysis(df, column, title, graph_name, insight):
    print("\n" + title.upper())
    print("-" * 50)

    print(df.groupby("Survived")[column].describe().round(2))

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="Survived", y=column)

    plt.title(title)
    plt.xlabel("Survived")
    plt.ylabel(column)
    plt.grid(axis="y", alpha=0.3)

    plt.savefig(f"Task_2_Titanic_EDA/graphs/{graph_name}", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

    print("\nINSIGHT")
    print("-" * 50)
    print(insight)


def bivariate_analysis(df):
    print("\nBIVARIATE ANALYSIS")
    print("=" * 50)

    categorical_bivariate_analysis(
        df,
        "Gender Vs Survival Status",
        "Sex",
        "Survived",
        "gender_vs_survival_status.png",
        "Female passengers had a much higher survival rate than male passengers.",
    )

    categorical_bivariate_analysis(
        df,
        "Embarked Port Vs Survival Status",
        "Embarked",
        "Survived",
        "embarked_port_vs_survival_status.png",
        "Survival rates differed across embarkation ports, with Cherbourg showing comparatively better survival.",
    )

    categorical_bivariate_analysis(
        df,
        "Passenger Class Vs Survival Status",
        "Pclass",
        "Survived",
        "pclass_vs_survival_status.png",
        "First-class passengers had the highest survival rate, whereas Third-class passengers had the lowest.",
    )

    numerical_bivariate_analysis(
        df,
        "Age",
        "Age Vs Survival Status",
        "age_vs_survival_status.png",
        "Younger passengers had slightly better survival chances than older passengers.",
    )

    numerical_bivariate_analysis(
        df,
        "Fare",
        "Fare Vs Survival Status",
        "fare_vs_survival_status.png",
        "Passengers who paid higher fares generally had a higher survival rate.",
    )


def correlation_analysis(df):
    print("\nCORRELATION ANALYSIS")
    print("=" * 50)

    correlation = df.select_dtypes(include="number").corr()

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
    )

    plt.title("Correlation Heatmap")

    plt.savefig(
        "Task_2_Titanic_EDA/graphs/correlation_heatmap.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.show()
    plt.close()

    print("\nINSIGHT")
    print("-" * 50)
    print(
        "Fare and Pclass show a noticeable relationship with survival, while most other numerical features have weak correlations."
    )


if __name__ == "__main__":
    main()
