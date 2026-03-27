import pandas as pd
import matplotlib.pyplot as plt

# load the csv file
df = pd.read_csv('manufacturing_defect_data.csv')

# make sure Defect Rate is numeric
df['Defect Rate'] = df['Defect Rate'].astype(str).str.replace('%', '', regex=False).astype(float)

# preview the first 5 rows
print('\n--- First 5 Rows ---')
print(df.head())

# basic info
print('\n--- Dataset Info ---')
df.info()

# average defect rate by machine
print('\n--- Average Defect Rate by Machine ---')
print(df.groupby('Machine')['Defect Rate'].mean().sort_values(ascending=False))

# average defect rate by shift
print('\n--- Average Defect Rate by Shift ---')
print(df.groupby('Shift')['Defect Rate'].mean().sort_values(ascending=False))

# total defects by material
print('\n--- Total Defects by Material ---')
print(df.groupby('Material')['Defect Count'].sum().sort_values(ascending=False))

# most common defect types
print('\n--- Most Common Defect Types ---')
print(df['Defect Type'].value_counts())

#average production cost
print('\n--- Average Production Cost by Machine ---')
print(df.groupby('Machine')['Production Cost'].mean().sort_values())

#print average defect rate by operator level
print('\n--- Average Defect Rate by Operator Level ---')
print(df.groupby('Operator Level')['Defect Rate'].mean().sort_values(ascending=False))

#print average defect rate by tool condition
print('\n--- Average Defect Rate by Tool Condition ---')
print(df.groupby('Tool Condition')['Defect Rate'].mean().sort_values(ascending=False))

#print defect rate by rush order
print('\n--- Average Defect Rate by Rush Order ---')
print(df.groupby('Rush Order')['Defect Rate'].mean().sort_values(ascending=False))

#print average defect rate by machine downtime
print('\n--- Average Defect Rate by Machine Downtime ---')
print(df.groupby('Machine Downtime')['Defect Rate'].mean().sort_values(ascending=False))

#print defect rate by inspection type
print('\n--- Average Defect Rate by Inspection Type ---')
print(df.groupby('Inspection Type')['Defect Rate'].mean().sort_values(ascending=False))

#print defect rate by process type
print('\n--- Average Defect Rate by Process Type ---')
print(df.groupby('Process Type')['Defect Rate'].mean().sort_values(ascending=False))

#print average production cost by customer
print('\n--- Average Production Cost by Customer ---')
print(df.groupby('Customer')['Production Cost'].mean().sort_values(ascending=False))

#print setup minutes
print('\n--- Average Setup Minutes by Process Type ---')
print(df.groupby('Process Type')['Setup Minutes'].mean().sort_values(ascending=False))

#print average cycle time
print('\n--- Average Cycle Time by Machine ---')
print(df.groupby('Machine')['Cycle Time Seconds'].mean().sort_values(ascending=False))

#shows number of jobs
print('\n--- Total Number of Jobs ---')
print(len(df))

#shows how many jobs were allocated to each machine
print('\n--- Number of Jobs by Machine ---')
print(df['Machine'].value_counts())

#summary table for each machine
print('\n--- Defect Rate and Production Cost by Machine ---')
machine_summary = df.groupby('Machine').agg({
    'Defect Rate': 'mean',
    'Production Cost': 'mean'
}).sort_values('Defect Rate')

print(machine_summary)

#which machine gives the best balance of both
machine_summary['Defect Score'] = machine_summary['Defect Rate'] / machine_summary['Defect Rate'].max()
machine_summary['Cost Score'] = machine_summary['Production Cost'] / machine_summary['Production Cost'].max()
machine_summary['Overall Score'] = 0.7 * machine_summary['Defect Score'] + 0.3 * machine_summary['Cost Score']

print('\n--- Machine Optimization Score ---')
print(machine_summary.sort_values('Overall Score'))

#graphs

# helper function for clean bar charts
def create_bar_chart(series, title, xlabel, ylabel, rotation=45):
    plt.figure(figsize=(11, 6))
    ax = series.plot(kind='bar', edgecolor='black')

    plt.title(title, fontsize=14, pad=15)
    plt.xlabel(xlabel, fontsize=11)
    plt.ylabel(ylabel, fontsize=11)
    plt.xticks(rotation=rotation, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.tight_layout()

    # add value labels above bars
    for i, value in enumerate(series.values):
        ax.text(i, value + (series.max() * 0.01), f'{value:.2f}' if isinstance(value, float) else str(value),
                ha='center', fontsize=9)

    plt.show()


#average defect rate by machine
avg_defect_by_machine = df.groupby('Machine')['Defect Rate'].mean().sort_values(ascending=False)

create_bar_chart(
    avg_defect_by_machine,
    'Average Defect Rate by Machine',
    'Machine',
    'Average Defect Rate (%)'
)

# shows number of jobs
print('\n--- Total Number of Jobs ---')
print(len(df))

# shows how many jobs were allocated to each machine
print('\n--- Number of Jobs by Machine ---')
print(df['Machine'].value_counts())

jobs_by_machine = df['Machine'].value_counts().sort_values(ascending=False)

create_bar_chart(
    jobs_by_machine,
    'Number of Jobs by Machine',
    'Machine',
    'Number of Jobs'
)

# total defects by material
total_defects_by_material = df.groupby('Material')['Defect Count'].sum().sort_values(ascending=False)

create_bar_chart(
    total_defects_by_material,
    'Total Defects by Material',
    'Material',
    'Total Defect Count'
)

# most common defect types
most_common_defects = df['Defect Type'].value_counts().sort_values(ascending=False)

create_bar_chart(
    most_common_defects,
    'Most Common Defect Types',
    'Defect Type',
    'Count'
)

# average production cost by machine
avg_cost_by_machine = df.groupby('Machine')['Production Cost'].mean().sort_values(ascending=False)

create_bar_chart(
    avg_cost_by_machine,
    'Average Production Cost by Machine',
    'Machine',
    'Average Production Cost'
)

#average defect rate by shift
avg_defect_by_shift = df.groupby('Shift')['Defect Rate'].mean().sort_values(ascending=False)

create_bar_chart(
    avg_defect_by_shift,
    'Average Defect Rate by Shift',
    'Shift',
    'Average Defect Rate (%)',
    rotation=0
)

#line chart for machine performance ranking
print('\n--- Defect Rate and Production Cost by Machine ---')
machine_summary = df.groupby('Machine').agg({
    'Defect Rate': 'mean',
    'Production Cost': 'mean'
}).sort_values('Defect Rate')

print(machine_summary)

machine_summary['Defect Score'] = machine_summary['Defect Rate'] / machine_summary['Defect Rate'].max()
machine_summary['Cost Score'] = machine_summary['Production Cost'] / machine_summary['Production Cost'].max()
machine_summary['Overall Score'] = 0.7 * machine_summary['Defect Score'] + 0.3 * machine_summary['Cost Score']

print('\n--- Machine Optimization Score ---')
print(machine_summary.sort_values('Overall Score'))

best_machine_score = machine_summary['Overall Score'].sort_values()

plt.figure(figsize=(11, 6))
plt.plot(best_machine_score.index, best_machine_score.values, marker='o')
plt.title('Machine Optimization Score Ranking', fontsize=14, pad=15)
plt.xlabel('Machine', fontsize=11)
plt.ylabel('Overall Score (Lower is Better)', fontsize=11)
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
