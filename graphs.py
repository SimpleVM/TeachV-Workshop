import pandas as pd
import matplotlib.pyplot as plt

# === Config ===
CSV_PATH = "ADJUST_PATH"

# === Read CSV ===
df = pd.read_csv(CSV_PATH)

# === Data Cleaning / Preparation ===
# Remove commas from population fields if present and convert to int
df['2022 Population'] = df['2022 Population'].astype(str).str.replace(',', '').astype(int)
df['2020 Population'] = df['2020 Population'].astype(str).str.replace(',', '').astype(int)

df['relative_change'] = (df['2022 Population'] - df['2020 Population']) / df['2020 Population']

# Top 5 growth
top_growth = df.sort_values('relative_change', ascending=False).head(5)

# Top 5 decline
top_decline = df.sort_values('relative_change').head(5)

def make_bar_plot(data, title, filename):
    plt.figure(figsize=(10,6))
    bars = plt.bar(
        data['Country/Territory'], 
        data['relative_change'] * 100, 
        color=['green' if x>0 else 'red' for x in data['relative_change']]
    )
    plt.ylabel('Relative Change (%)')
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.ylim(min(0, data['relative_change'].min()*100), max(0, data['relative_change'].max()*100)+2)

    # Annotate bars with 2020/2022 population
    for i, bar in enumerate(bars):
        country = data.iloc[i]
        # Height for annotation above/below bar depending on growth/decline.
        y_loc = bar.get_height() + (0.2 if bar.get_height() > 0 else -0.2)
        label = f"{country['2020 Population']} ➔ {country['2022 Population']}"
        plt.text(
            bar.get_x() + bar.get_width()/2, y_loc, 
            label, ha='center', va='bottom' if bar.get_height()>0 else 'top', fontsize=9
        )

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

make_bar_plot(
    top_growth,
    'Top 5 Countries/Territories by Relative Population Growth (2020-2022)',
    'population_growth.png'
)

make_bar_plot(
    top_decline,
    'Top 5 Countries/Territories by Relative Population Decline (2020-2022)',
    'population_decline.png'
)

print("Plots saved as population_growth.png and population_decline.png")