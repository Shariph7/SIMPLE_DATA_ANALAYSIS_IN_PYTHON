import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# reading the CSV Files in terminal.
# Load CSV data into a DataFrame
data_frame = pd.read_csv('ds_salaries.csv')
print(data_frame)

# Create a 3D plot
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D bar graph
work_yr = data_frame['work_year'].value_counts()
ax.bar3d(work_yr, 0, shade=True)

# Labeling the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Bar Graph from CSV Data')

# Display the plot
plt.show()