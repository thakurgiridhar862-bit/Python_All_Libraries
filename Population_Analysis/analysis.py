import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv("Task_1_Population_Analysis/data/newdata.csv")

df["Population_Millions"] = df["2024"] / 1_000_000


# ==================================================
# POPULATION STATISTICS
# ==================================================

max_country = df.loc[df["Population_Millions"].idxmax()]
min_country = df.loc[df["Population_Millions"].idxmin()]

avg_pop = df["Population_Millions"].mean()
median_pop = df["Population_Millions"].median()

print("\nHIGHEST POPULATION COUNTRY")
print("-" * 40)
print(f"Country    : {max_country['Country Name']}")
print(f"Population : {max_country['Population_Millions']:.2f} M")

print("\nLOWEST POPULATION COUNTRY")
print("-" * 40)
print(f"Country    : {min_country['Country Name']}")
print(f"Population : {min_country['Population_Millions']:.4f} M")

print("\nPOPULATION STATISTICS")
print("-" * 40)
print(f"Average Population : {avg_pop:.2f} M")
print(f"Median Population  : {median_pop:.2f} M")


# ==================================================
# GRAPH 1: POPULATION DISTRIBUTION HISTOGRAM
# ==================================================

plt.figure(figsize=(12, 6))

ax = sns.histplot(
    df["Population_Millions"], bins=25, color="steelblue", edgecolor="black"
)

ax.axvline(
    x=avg_pop,
    color="red",
    linestyle="--",
    linewidth=3,
    label=f"Average Population: {avg_pop:.2f} M",
)

plt.title("Distribution of Population Across Countries (2024)")
plt.xlabel("Population (Millions)")
plt.ylabel("Number of Countries")
plt.grid(axis="y", alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("Task_1_Population_Analysis/graphs/dist_pop.png", dpi=300)

plt.show()


# ==================================================
# GRAPH 2: TOP 10 MOST POPULATED COUNTRIES
# ==================================================

top10 = df.sort_values(by="Population_Millions", ascending=False)[
    ["Country Name", "Population_Millions"]
].head(10)

plt.figure(figsize=(12, 6))

ax1 = sns.barplot(
    data=top10, x="Population_Millions", y="Country Name", palette="viridis"
)

for container in ax1.containers:
    labels = [f"{value:.1f} M" for value in container.datavalues]
    ax1.bar_label(container, labels=labels, padding=5)

plt.title("Top 10 Most Populated Countries in 2024")
plt.xlabel("Population (Millions)")
plt.ylabel("Country")
plt.grid(axis="x", alpha=0.5)
plt.tight_layout()

plt.savefig("Task_1_Population_Analysis/graphs/top10_most_pop_country.png", dpi=300)

plt.show()


# ==================================================
# GRAPH 3: REGION-WISE POPULATION DISTRIBUTION
# ==================================================

region_pop = (
    df.groupby("Region")["Population_Millions"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

print("\nREGION-WISE POPULATION")
print("-" * 40)
print(region_pop)

plt.figure(figsize=(12, 6))

ax2 = sns.barplot(data=region_pop, x="Population_Millions", y="Region", palette="magma")

for container in ax2.containers:
    labels = [f"{value:.1f} M" for value in container.datavalues]
    ax2.bar_label(container, labels=labels, padding=5)

plt.title("Region-Wise Population Distribution (2024)")
plt.xlabel("Population (Millions)")
plt.ylabel("Region")
plt.grid(axis="x", alpha=0.5)
plt.tight_layout()

plt.savefig("Task_1_Population_Analysis/graphs/region_wise_population.png", dpi=300)

plt.show()
