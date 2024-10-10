# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset and set the index to the date column
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data: filter out the top and bottom 2.5% of the dataset
lower_limit = df['value'].quantile(0.025)  # 2.5th percentile
upper_limit = df['value'].quantile(0.975)  # 97.5th percentile
df = df[(df['value'] >= lower_limit) & (df['value'] <= upper_limit)]

# Function to draw a line plot
def draw_line_plot():
    plt.figure(figsize=(12, 6))  # Set the figure size
    plt.plot(df.index, df['value'], color='blue', linewidth=2)  # Create a line plot
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')  # Set the title
    plt.xlabel('Date')  # X-axis label
    plt.ylabel('Page Views')  # Y-axis label
    plt.xticks(rotation=45)  # Rotate X-axis ticks
    plt.tight_layout()  # Adjust layout
    plt.savefig('line_plot.png')  # Save the line plot
    plt.show()  # Show the plot

# Function to draw a bar plot
def draw_bar_plot():
    # Group the data by year and month
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Calculate average daily page views
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Arrange the months in a specific order
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[months_order]  # Arrange months in order

    # Draw the bar plot
    df_bar.plot(kind='bar', figsize=(12, 6))
    plt.title('Average Daily Page Views per Month')  # Set the title
    plt.xlabel('Years')  # X-axis label
    plt.ylabel('Average Page Views')  # Y-axis label
    plt.legend(title='Months')  # Legend title
    plt.tight_layout()  # Adjust layout
    plt.savefig('bar_plot.png')  # Save the bar plot
    plt.show()  # Show the plot

# Function to draw a box plot
def draw_box_plot():
    # Make a copy of the data
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month

    # Add month names
    df_box['month'] = df_box['month'].apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))

    plt.figure(figsize=(12, 6))

    # Year-wise box plot
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')  # Set the title
    plt.xlabel('Year')  # X-axis label
    plt.ylabel('Page Views')  # Y-axis label

    # Month-wise box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box, order=['January', 'February', 'March', 'April', 
                                                            'May', 'June', 'July', 'August', 
                                                            'September', 'October', 'November', 'December'])
    plt.title('Month-wise Box Plot (Seasonality)')  # Set the title
    plt.xlabel('Month')  # X-axis label
    plt.ylabel('Page Views')  # Y-axis label

    plt.tight_layout()  # Adjust layout
    plt.savefig('box_plot.png')  # Save the box plot
    plt.show()  # Show the plot

# Calling the functions
draw_line_plot()
draw_bar_plot()
draw_box_plot()
