# 📊 Importing required libraries
import matplotlib.pyplot as plt
import seaborn as sns

# 🎨 Apply a custom style
sns.set_style("whitegrid")  # Clean background with gridlines

# 📅 Define years and hypothetical run data
years = list(range(2015, 2025))
kohli_runs = [850, 900, 870, 920, 880, 910, 890, 940, 930, 950]
rohit_runs = [780, 820, 800, 860, 840, 870, 860, 880, 890, 910]
sehwag_runs = [700, 750, 720, 760, 740, 780, 770, 790, 800, 820]

# 📈 Create the plot
plt.figure(figsize=(10, 6))

# Plot each player's data with distinct styles
plt.plot(years, kohli_runs, label='Virat Kohli', color='blue', linestyle='-')
plt.plot(years, rohit_runs, label='Rohit Sharma', color='green', linestyle='--')
plt.plot(years, sehwag_runs, label='Virender Sehwag', color='red', linestyle='-.')

# 🏷️ Add labels and title
plt.xlabel('Year')
plt.ylabel('Runs Scored')
plt.title('Hypothetical Runs Comparison (2015–2024)')

# 📌 Add legend
plt.legend()

# 📐 Optional: Add grid and tighter layout
plt.grid(True)
plt.tight_layout()

# 📤 Show the plot
plt.show()
