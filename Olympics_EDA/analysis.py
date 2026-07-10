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


def top_participating_countries(df):
    print("\nTOP 10 PARTICIPATING COUNTRIES")
    print("-" * 60)

    country_count = (
        df.groupby("NOC")["ID"].nunique().sort_values(ascending=False).head(10)
    )
    print(country_count)
    plt.figure(figsize=(10, 6))

    plot = sns.barplot(x=country_count.values, y=country_count.index)
    plt.title("Top 10 Countries by Athlete Participation")
    plt.xlabel("Unique Athletes")
    plt.ylabel("Country Code")
    for container in plot.containers:
        plot.bar_label(container, fmt="%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/06_top_countries_participation.png", dpi=300)
    plt.show()


def top_sports(df):
    print("\nTOP 10 SPORTS")
    print("-" * 60)

    sport_count = df["Sport"].value_counts().head(10)
    print(sport_count)
    plt.figure(figsize=(10, 6))

    plot = sns.barplot(x=sport_count.values, y=sport_count.index)
    plt.title("Top 10 Sports by Participation")
    plt.xlabel("Participation Records")
    plt.ylabel("Sport")
    for container in plot.containers:
        plot.bar_label(container, fmt="%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/07_top_sports.png", dpi=300)
    plt.show()


def sports_and_events_growth(df):
    print("\nSPORTS AND EVENTS GROWTH")
    print("-" * 60)

    growth_data = (
        df.groupby(["Year", "Season"])
        .agg(Sports=("Sport", "nunique"), Events=("Event", "nunique"))
        .reset_index()
    )
    print(growth_data.tail(12))
    plt.figure(figsize=(14, 6))

    sns.lineplot(data=growth_data, x="Year", y="Sports", hue="Season", marker="o")
    plt.title("Growth of Olympic Sports Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Sports")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/08_sports_growth.png", dpi=300)
    plt.show()
    plt.figure(figsize=(14, 6))

    sns.lineplot(data=growth_data, x="Year", y="Events", hue="Season", marker="o")
    plt.title("Growth of Olympic Events Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Events")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/09_events_growth.png", dpi=300)
    plt.show()


def prepare_medal_data(df):

    medal_df = df[df["Medal"].notna()].copy()

    unique_medals = medal_df.drop_duplicates(
        subset=["Year", "Season", "Event", "NOC", "Medal"]
    )
    print("\nMEDAL DATA")
    print("-" * 60)
    print(f"Athlete Medal Records : {len(medal_df)}")
    print(f"Unique Medal Records  : {len(unique_medals)}")
    return medal_df, unique_medals


def medal_distribution(unique_medals):
    print("\nMEDAL DISTRIBUTION")
    print("-" * 60)

    medal_count = (
        unique_medals["Medal"].value_counts().reindex(["Gold", "Silver", "Bronze"])
    )
    print(medal_count)
    plt.figure(figsize=(8, 5))

    plot = sns.barplot(x=medal_count.index, y=medal_count.values)
    plt.title("Overall Medal Distribution")
    plt.xlabel("Medal")
    plt.ylabel("Unique Medal Records")
    for container in plot.containers:
        plot.bar_label(container, fmt="%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/10_medal_distribution.png", dpi=300)
    plt.show()


def top_medal_countries(unique_medals):
    print("\nTOP 10 MEDAL WINNING COUNTRIES")
    print("-" * 60)

    country_medals = unique_medals["NOC"].value_counts().head(10)
    print(country_medals)
    plt.figure(figsize=(10, 6))

    plot = sns.barplot(x=country_medals.values, y=country_medals.index)
    plt.title("Top 10 Countries by Total Medals")
    plt.xlabel("Unique Medal Records")
    plt.ylabel("Country Code")
    for container in plot.containers:
        plot.bar_label(container, fmt="%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/11_top_medal_countries.png", dpi=300)
    plt.show()


def country_medal_table(unique_medals):
    print("\nCOUNTRY MEDAL TABLE")
    print("-" * 60)

    medal_table = pd.crosstab(unique_medals["NOC"], unique_medals["Medal"])

    for medal in ["Gold", "Silver", "Bronze"]:
        if medal not in medal_table.columns:
            medal_table[medal] = 0

    medal_table = medal_table[["Gold", "Silver", "Bronze"]]

    medal_table["Total"] = medal_table.sum(axis=1)

    medal_table = medal_table.sort_values(
        by=["Gold", "Silver", "Bronze"], ascending=False
    )
    print(medal_table.head(15))

    medal_table.head(15).to_csv("Olympics_EDA/data/top_15_country_medal_table.csv")


def top_medal_athletes(medal_df):
    print("\nTOP 10 MEDAL WINNING ATHLETES")
    print("-" * 60)

    athlete_medals = (
        medal_df.groupby(["Name", "Gender"])["Medal"]
        .count()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name="Medals")
    )
    print(athlete_medals)
    plt.figure(figsize=(11, 7))

    plot = sns.barplot(data=athlete_medals, x="Medals", y="Name", hue="Gender")
    plt.title("Top 10 Medal Winning Athletes")
    plt.xlabel("Medal Records")
    plt.ylabel("Athlete")
    for container in plot.containers:
        plot.bar_label(container, fmt="%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/12_top_medal_athletes.png", dpi=300)
    plt.show()


def age_analysis(df):
    print("\nAGE ANALYSIS")
    print("-" * 60)

    age_data = df.dropna(subset=["Age"])
    print(age_data["Age"].describe().round(2))

    youngest = age_data.loc[age_data["Age"].idxmin()]
    oldest = age_data.loc[age_data["Age"].idxmax()]
    print("\nYOUNGEST ATHLETE RECORD")
    print("-" * 60)
    print(f"Name  : {youngest['Name']}")
    print(f"Age   : {youngest['Age']}")
    print(f"Sport : {youngest['Sport']}")
    print(f"Year  : {youngest['Year']}")
    print("\nOLDEST ATHLETE RECORD")
    print("-" * 60)
    print(f"Name  : {oldest['Name']}")
    print(f"Age   : {oldest['Age']}")
    print(f"Sport : {oldest['Sport']}")
    print(f"Year  : {oldest['Year']}")
    plt.figure(figsize=(10, 6))

    sns.histplot(data=age_data, x="Age", bins=30, kde=True)
    plt.title("Age Distribution of Olympic Athletes")
    plt.xlabel("Age")
    plt.ylabel("Participation Records")
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/13_age_distribution.png", dpi=300)
    plt.show()


def age_group_analysis(df):
    print("\nAGE GROUP ANALYSIS")
    print("-" * 60)

    age_groups = df["Age_Group"].value_counts().sort_index()
    print(age_groups)

    age_data = age_groups.reset_index()
    age_data.columns = ["Age Group", "Records"]
    plt.figure(figsize=(11, 6))

    plot = sns.barplot(data=age_data, x="Age Group", y="Records")
    plt.title("Athlete Participation by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Participation Records")
    plt.xticks(rotation=45)
    for container in plot.containers:
        plot.bar_label(container, fmt="%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/14_age_groups.png", dpi=300)
    plt.show()


def physical_analysis(df):
    print("\nPHYSICAL CHARACTERISTICS ANALYSIS")
    print("-" * 60)

    physical_summary = df.groupby("Gender")[["Height", "Weight"]].mean().round(2)
    print(physical_summary)

    physical_data = df[["Gender", "Height", "Weight"]].dropna()

    sample_size = min(5000, len(physical_data))

    physical_sample = physical_data.sample(sample_size, random_state=42)
    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=physical_sample, x="Height", y="Weight", hue="Gender", alpha=0.6
    )
    plt.title("Height and Weight Relationship")
    plt.xlabel("Height in Centimetres")
    plt.ylabel("Weight in Kilograms")
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/15_height_weight_relationship.png", dpi=300)
    plt.show()


def host_city_analysis(df):
    print("\nTOP OLYMPIC HOST CITIES")
    print("-" * 60)

    city_count = df[["Games", "City"]].drop_duplicates()["City"].value_counts().head(10)
    print(city_count)
    plt.figure(figsize=(10, 6))

    plot = sns.barplot(x=city_count.values, y=city_count.index)
    plt.title("Top Olympic Host Cities")
    plt.xlabel("Number of Olympic Games")
    plt.ylabel("City")
    for container in plot.containers:
        plot.bar_label(container, fmt="%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/16_top_host_cities.png", dpi=300)
    plt.show()


def india_analysis(df, unique_medals):
    print("\nINDIA OLYMPICS ANALYSIS")
    print("-" * 60)

    india_df = df[df["NOC"] == "IND"]

    india_medals = unique_medals[unique_medals["NOC"] == "IND"]
    print(f"Participation Records : {len(india_df)}")
    print(f"Unique Athletes       : {india_df['ID'].nunique()}")
    print(f"Sports Participated   : {india_df['Sport'].nunique()}")
    print(f"Unique Medal Records  : {len(india_medals)}")
    print("\nINDIA MEDAL DISTRIBUTION")
    print("-" * 60)
    print(
        india_medals["Medal"]
        .value_counts()
        .reindex(["Gold", "Silver", "Bronze"])
        .fillna(0)
        .astype(int)
    )

    india_year = india_df.groupby("Year")["ID"].nunique().reset_index(name="Athletes")
    plt.figure(figsize=(14, 6))

    sns.lineplot(data=india_year, x="Year", y="Athletes", marker="o")
    plt.title("Indian Athlete Participation Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Unique Indian Athletes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/17_india_participation.png", dpi=300)
    plt.show()


def correlation_analysis(df):
    print("\nCORRELATION ANALYSIS")
    print("-" * 60)

    numerical_data = df[["Age", "Height", "Weight", "Year"]]

    correlation = numerical_data.corr()
    print(correlation.round(2))
    plt.figure(figsize=(8, 6))

    sns.heatmap(correlation, annot=True, fmt=".2f", linewidths=0.5)
    plt.title("Correlation Between Numerical Features")
    plt.tight_layout()
    plt.savefig("Olympics_EDA/graphs/18_correlation_heatmap.png", dpi=300)
    plt.show()


def final_insights(df, unique_medals):
    print("\nFINAL INSIGHTS")
    print("-" * 60)

    top_country = unique_medals["NOC"].value_counts().idxmax()
    top_sport = df["Sport"].value_counts().idxmax()

    top_city = df[["Games", "City"]].drop_duplicates()["City"].value_counts().idxmax()

    common_age_group = df["Age_Group"].value_counts().idxmax()
    print(f"Country with most unique medal records : {top_country}")
    print(f"Sport with highest participation       : {top_sport}")
    print(f"Most frequent Olympic host city        : {top_city}")
    print(f"Most common athlete age group          : {common_age_group}")
    print("Olympic participation increased strongly over time.")
    print("Female participation increased significantly in later years.")
    print("The number of sports and events expanded across Olympic history.")
    print(
        "Team-sport medal duplicates were removed before calculating "
        "country medal totals."
    )


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
