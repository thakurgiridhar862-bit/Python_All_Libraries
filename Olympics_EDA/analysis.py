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
