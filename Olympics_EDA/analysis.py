import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("OLYMPICS HISTORY ANALYSIS")
print("=" * 50)


def load_data():
    df = pd.read_csv("Olympics_EDA/data/athlete_events.csv")
    return df


def dataset_overview(df):
    print("\nDATASET OVERVIEW")
    print("-" * 50)

    memory = df.memory_usage(deep=True).sum() / 1024 / 1024

    print(f"Total Rows             : {df.shape[0]}")
    print(f"Total Columns          : {df.shape[1]}")
    print(f"Total Missing Values   : {df.isnull().sum().sum()}")
    print(f"Total Duplicate Values : {df.duplicated().sum()}")
    print(f"Memory Usage           : {memory:.2f} MB")

    print("\nMISSING VALUES")
    print("-" * 50)
    print(df.isnull().sum().sort_values(ascending=False))

    print("\nCOLUMN NAMES")
    print("-" * 50)
    print("\n".join(df.columns))

    print("\nDATA TYPES")
    print("-" * 50)
    print(df.dtypes.to_string())

    print("\nNUMERICAL SUMMARY")
    print("-" * 50)
    print(df.describe())


def missing_values_report(df):
    print("\nMISSING VALUES REPORT")
    print("-" * 50)

    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100

    for col in df.columns:
        if missing_count[col] > 0:
            print(f"{col:<10} : {missing_count[col]:>6} ({missing_percent[col]:.2f}%)")

    print("\nINSIGHTS")
    print("-" * 50)

    max_col = missing_count.idxmax()

    print(f"• Column with highest missing values : {max_col}")

    print(
        "• Age, Height and Weight contain missing values "
        "because athlete physical records were not available for all participants."
    )

    print(
        "• Medal contains many missing values because most athletes "
        "did not win any medal."
    )

    no_missing = df.columns[df.isnull().sum() == 0]

    print(f"• Columns with no missing values : {', '.join(no_missing)}")
    missing_count = df.isnull().sum()
    missing_count = missing_count[missing_count > 0]

    plt.figure(figsize=(8, 5))

    sns.barplot(x=missing_count.index, y=missing_count.values)

    plt.title("Missing Values by Column")
    plt.xlabel("Columns")
    plt.ylabel("Missing Count")
    plt.xticks(rotation=45)

    for i, value in enumerate(missing_count.values):
        plt.text(i, value, str(value), ha="center")

    plt.tight_layout()

    plt.savefig("Olympics_EDA/graphs/missing_values_report.png")
    plt.show()


def main():
    df = load_data()
    dataset_overview(df)
    missing_values_report(df)


if __name__ == "__main__":
    main()
