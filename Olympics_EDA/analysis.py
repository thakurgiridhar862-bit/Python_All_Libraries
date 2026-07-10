import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 60)
print("OLYMPICS HISTORY ANALYSIS")
print("=" * 60)


def load_data():
    df = pd.read_csv("Olympics_EDA/data/athlete_events.csv")
    return df


def dataset_overview(df):
    print("\nDATASET OVERVIEW")
    print("-" * 60)

    memory = df.memory_usage(deep=True).sum() / 1024 / 1024
    print(f"Total Rows             : {df.shape[0]}")
    print(f"Total Columns          : {df.shape[1]}")
    print(f"Total Missing Values   : {df.isnull().sum().sum()}")
    print(f"Total Duplicate Values : {df.duplicated().sum()}")
    print(f"Memory Usage           : {memory:.2f} MB")
    print("\nFIRST FIVE ROWS")
    print("-" * 60)
    print(df.head())
    print("\nCOLUMN NAMES")
    print("-" * 60)
    print("\n".join(df.columns))
    print("\nDATA TYPES")
    print("-" * 60)
    print(df.dtypes.to_string())
    print("\nNUMERICAL SUMMARY")
    print("-" * 60)
    print(df.describe().round(2))


def missing_values_report(df):
    print("\nMISSING VALUES REPORT")
    print("-" * 60)

    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100

    missing_data = pd.DataFrame(
        {"Missing Values": missing_count, "Percentage": missing_percent}
    )

    missing_data = missing_data[missing_data["Missing Values"] > 0].sort_values(
        by="Missing Values", ascending=False
    )
    print(missing_data.round(2))
    print("\nINSIGHTS")
    print("-" * 60)
    print(f"Column with highest missing values : {missing_count.idxmax()}")
    print(
        "Age, Height and Weight contain missing values because "
        "physical details were not recorded for every athlete."
    )
    print(
        "Medal contains many missing values because most athletes did not win a medal."
    )

    no_missing = df.columns[df.isnull().sum() == 0]
    print(f"Columns with no missing values : {', '.join(no_missing)}")
    plt.figure(figsize=(9, 5))

    plot = sns.barplot(x=missing_data.index, y=missing_data["Missing Values"].values)
    plt.title("Missing Values by Column")
    plt.xlabel("Columns")
    plt.ylabel("Missing Values")
    plt.xticks(rotation=45)
    for container in plot.containers:
        plot.bar_label(container, fmt="%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/01_missing_values.png", dpi=300)
    plt.show()


def clean_data(df):
    print("\nDATA CLEANING")
    print("-" * 60)

    rows_before = df.shape[0]

    df = df.drop_duplicates().copy()

    rows_after = df.shape[0]
    print(f"Rows Before Cleaning     : {rows_before}")
    print(f"Duplicate Rows Removed   : {rows_before - rows_after}")
    print(f"Rows After Cleaning      : {rows_after}")

    df["Gender"] = df["Sex"].replace({"M": "Male", "F": "Female"})

    df["Won_Medal"] = df["Medal"].notna()

    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[0, 15, 20, 25, 30, 35, 40, 50, 100],
        labels=[
            "Below 16",
            "16-20",
            "21-25",
            "26-30",
            "31-35",
            "36-40",
            "41-50",
            "Above 50",
        ],
    )
    print("\nNew Columns Added")
    print("-" * 60)
    print("Gender")
    print("Won_Medal")
    print("Age_Group")
    return df


def overall_statistics(df):
    print("\nOVERALL OLYMPICS STATISTICS")
    print("-" * 60)
    print(f"Starting Year       : {df['Year'].min()}")
    print(f"Ending Year         : {df['Year'].max()}")
    print(f"Unique Athletes     : {df['ID'].nunique()}")
    print(f"Countries           : {df['NOC'].nunique()}")
    print(f"Teams               : {df['Team'].nunique()}")
    print(f"Sports              : {df['Sport'].nunique()}")
    print(f"Events              : {df['Event'].nunique()}")
    print(f"Host Cities         : {df['City'].nunique()}")
    print(f"Olympic Games       : {df['Games'].nunique()}")


def season_analysis(df):
    print("\nSUMMER AND WINTER OLYMPICS")
    print("-" * 60)

    season_data = (
        df.groupby("Season")
        .agg(
            Records=("ID", "count"),
            Athletes=("ID", "nunique"),
            Sports=("Sport", "nunique"),
            Events=("Event", "nunique"),
        )
        .sort_values("Records", ascending=False)
    )
    print(season_data)

    plot_data = season_data.reset_index()
    plt.figure(figsize=(8, 5))

    plot = sns.barplot(data=plot_data, x="Season", y="Records")
    plt.title("Summer and Winter Olympics Participation")
    plt.xlabel("Season")
    plt.ylabel("Participation Records")
    for container in plot.containers:
        plot.bar_label(container, fmt="%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/02_season_analysis.png", dpi=300)
    plt.show()


def participation_over_years(df):
    print("\nATHLETE PARTICIPATION OVER YEARS")
    print("-" * 60)

    yearly_athletes = (
        df.groupby(["Year", "Season"])["ID"].nunique().reset_index(name="Athletes")
    )
    print(yearly_athletes.tail(12))
    plt.figure(figsize=(14, 6))

    sns.lineplot(data=yearly_athletes, x="Year", y="Athletes", hue="Season", marker="o")
    plt.title("Athlete Participation Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Unique Athletes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/03_participation_over_years.png", dpi=300)
    plt.show()


def gender_analysis(df):
    print("\nGENDER ANALYSIS")
    print("-" * 60)

    gender_count = df["Gender"].value_counts()
    print(gender_count)
    plt.figure(figsize=(7, 5))

    plot = sns.barplot(x=gender_count.index, y=gender_count.values)
    plt.title("Gender Distribution of Athletes")
    plt.xlabel("Gender")
    plt.ylabel("Participation Records")
    for container in plot.containers:
        plot.bar_label(container, fmt="%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/04_gender_distribution.png", dpi=300)
    plt.show()


def gender_participation_over_years(df):
    print("\nGENDER PARTICIPATION OVER YEARS")
    print("-" * 60)

    gender_year = (
        df.groupby(["Year", "Gender"])["ID"].nunique().reset_index(name="Athletes")
    )
    print(gender_year.tail(12))
    plt.figure(figsize=(14, 6))

    sns.lineplot(data=gender_year, x="Year", y="Athletes", hue="Gender")
    plt.title("Gender Participation Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Unique Athletes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/05_gender_participation.png", dpi=300)
    plt.show()


def main():

    df = load_data()

    dataset_overview(df)

    missing_values_report(df)

    df = clean_data(df)

    overall_statistics(df)

    season_analysis(df)

    participation_over_years(df)

    gender_analysis(df)

    gender_participation_over_years(df)

    top_participating_countries(df)

    top_sports(df)

    sports_and_events_growth(df)

    medal_df, unique_medals = prepare_medal_data(df)

    medal_distribution(unique_medals)

    top_medal_countries(unique_medals)

    country_medal_table(unique_medals)

    top_medal_athletes(medal_df)

    age_analysis(df)

    age_group_analysis(df)

    physical_analysis(df)

    host_city_analysis(df)

    india_analysis(df, unique_medals)

    correlation_analysis(df)

    final_insights(df, unique_medals)


if __name__ == "__main__":
    main()
