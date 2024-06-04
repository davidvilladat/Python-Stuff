import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Define the tasks and their durations
tasks = {
    "AWS Certified Big Data – Specialty": {"start": datetime.date(2024, 6, 4), "end": datetime.date(2024, 8, 4)},
    "Certified Analytics Professional (CAP)": {"start": datetime.date(2024, 8, 5), "end": datetime.date(2024, 10, 5)},
    "Advanced Project Management Certification (PMP)": {"start": datetime.date(2024, 10, 6), "end": datetime.date(2024, 12, 6)},
    "Deep Learning Specialization": {"start": datetime.date(2024, 12, 7), "end": datetime.date(2025, 3, 7)},
    "Advanced SQL for Data Scientists": {"start": datetime.date(2025, 3, 8), "end": datetime.date(2025, 5, 8)},
    "Leadership Training Program": {"start": datetime.date(2025, 5, 9), "end": datetime.date(2025, 7, 9)},
    "Change Management Certification": {"start": datetime.date(2025, 7, 10), "end": datetime.date(2025, 9, 10)},
}

# Convert the tasks to a DataFrame
df = pd.DataFrame(tasks).T
df['Task'] = df.index

# Plot the Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))

# Define a color for the bars
colors = ['#4CAF50', '#2196F3', '#FF5722', '#9C27B0', '#FFC107', '#00BCD4', '#E91E63']

for i, (task, row) in enumerate(df.iterrows()):
    ax.barh(task, (row['end'] - row['start']).days, left=row['start'], color=colors[i % len(colors)])

# Set the labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Task')
ax.set_title('Learning Path Gantt Chart')

# Format the x-axis to show dates
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
