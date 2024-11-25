"""
Streamlit application for simulating Agile Sprint Planning and analyzing datasets using Agile principles.

This application provides the following functionalities:
1. **Agile Sprint Planning**:
    - Displays a table of sprint tasks along with their estimated effort points, priority levels, and team member assignments.
    - Visualizes the distribution of effort and priority for each team member using pie charts.
    - Displays task complexity distribution based on priority levels.

2. **Iris Dataset Analysis**:
    - Allows users to load and visualize the Iris dataset (a commonly used dataset for classification tasks).
    - Displays basic overview of the Iris dataset, including the first few rows.
    - Provides various visualizations for the Iris dataset, including:
      - Species distribution pie chart.
      - Scatter plot of sepal length vs. sepal width by species.
      - Box plot of petal length distribution by species.
      - Histogram of petal width distribution by species.
      - Pairplot of sepal and petal dimensions.
      
3. **Deployment Instructions**:
    - Provides deployment instructions for hosting the Streamlit app on Streamlit Cloud.

### Author Information:
- **Author**: Madhurima Rawat
- **Date**: November 23, 2024

Libraries Used:
- **streamlit**: For creating the web app interface.
- **pandas**: For data manipulation and analysis.
- **seaborn**: For loading the Iris dataset and creating various plots.
- **matplotlib**: For creating pie charts and other plots.

Output:
- A clean and interactive interface for simulating Agile Sprint Planning and analyzing datasets.
- Interactive charts and visualizations for sprint effort distribution and task priority.
- Display of Iris dataset visualizations such as pie charts, scatter plots, box plots, and pair plots.

Usage:
- Display sprint planning data with effort points, task assignments, and priorities.
- Analyze the Iris dataset with various visualizations to gain insights into the data.
"""

# Importing required libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Function to include background image and opacity
def display_background_image(url, opacity):
    """
    Displays a background image with a specified opacity on the web app using CSS.

    Args:
    - url (str): URL of the background image.
    - opacity (float): Opacity level of the background image.
    """
    # Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Call function to display the background image with opacity
display_background_image(
    "https://1.bp.blogspot.com/-NFhT7E4-TUQ/XqWXsuNJmJI/AAAAAAAALZw/iR8sFnKfwz89GD1ihOlNujDtLreJYjTBACLcBGAsYHQ/s1600/Agile.jpg",
    0.8,
)


# App Title
st.title("Agile Sprint Planning & Data Analysis")
st.subheader("Simulate sprint planning and analyze datasets using Agile principles.")

# Data for Agile Sprint Planning
data = {
    "Task": [
        "Data collection and preprocessing",
        "Build sprint visualization pipeline",
        "Deploy app to Streamlit cloud",
        "Fix crash on invalid user input",
        "Add effort slider for estimation",
        "Add team assignment functionality",
    ],
    "Points (Effort)": [4, 6, 8, 9, 5, 3],
    "Priority": ["Medium", "High", "High", "High", "Medium", "Low"],
    "Assigned To": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie"],
}

df = pd.DataFrame(data)

# Display Task Table
st.header("Sprint Tasks Overview")
st.dataframe(df)

# Effort and Priority Distribution for Each Team Member
st.subheader("Effort and Priority Distribution for Each Team Member")
team_members = df["Assigned To"].unique()

# Colors for each chart with a valid pastel color palette
effort_colors = sns.color_palette("pastel", len(df["Assigned To"].unique()))
priority_colors = sns.color_palette("viridis", len(df["Priority"].unique()))

# Adjust the size of the pie charts
for member in team_members:
    member_tasks = df[df["Assigned To"] == member]

    # Effort Distribution Pie Chart
    fig_effort, ax_effort = plt.subplots(figsize=(15, 15))  # Same size for uniformity
    member_tasks.plot.pie(
        y="Points (Effort)",
        labels=member_tasks["Task"],
        autopct="%1.1f%%",
        colors=effort_colors,  # Different pastel colors for effort chart
        ax=ax_effort,
        legend=False,
        startangle=90,
        textprops={"fontsize": 8, "fontweight": "bold"},  # Make percentage values bold
    )
    ax_effort.set_title(
        f"Effort Distribution: {member}", fontsize=35, fontweight="bold"
    )
    ax_effort.set_ylabel("")  # Remove default y-axis label
    ax_effort.set_aspect("equal")  # Ensure the pie chart is circular
    ax_effort.legend(fontsize=10, prop={"weight": "bold"})  # Make the legend bold

    # Priority Distribution Pie Chart
    priority_counts = member_tasks["Priority"].value_counts()
    fig_priority, ax_priority = plt.subplots(figsize=(5, 5))  # Same size for uniformity
    priority_counts.plot.pie(
        autopct="%1.1f%%",
        colors=priority_colors,  # Different pastel colors for priority chart
        ax=ax_priority,
        startangle=90,
        textprops={"fontsize": 8, "fontweight": "bold"},  # Make percentage values bold
    )
    ax_priority.set_title(
        f"Priority Distribution: {member}", fontsize=12, fontweight="bold"
    )
    ax_priority.set_ylabel("")  # Remove default y-axis label
    ax_priority.set_aspect("equal")  # Ensure the pie chart is circular
    ax_priority.legend(fontsize=10, prop={"weight": "bold"})  # Make the legend bold

    # Display both charts side by side in columns
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig_effort, use_container_width=True)
    with col2:
        st.pyplot(fig_priority, use_container_width=True)


# Task Complexity Distribution
st.subheader("Task Complexity Distribution (Priority Levels)")
priority_distribution = df["Priority"].value_counts()
fig, ax = plt.subplots(figsize=(6, 6))
priority_distribution.plot.pie(
    autopct="%1.1f%%",
    colors=sns.color_palette("pastel"),
    ax=ax,
    startangle=90,
    textprops={"fontsize": 10, "fontweight": "bold"},
)
ax.set_title("Task Complexity Distribution by Priority", fontsize=12, fontweight="bold")
ax.set_ylabel("")  # Remove default y-axis label
st.pyplot(fig)

# Load Iris Dataset for Comparison
st.header("Data Analysis: Iris Dataset")
if st.checkbox("Analyze Iris Dataset"):
    # Load dataset
    iris = sns.load_dataset("iris")
    st.write("Iris Dataset Overview:")
    st.dataframe(iris.head())

    # Species Distribution Pie Chart
    st.subheader("Species Distribution")
    species_distribution = iris["species"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    species_distribution.plot.pie(
        autopct="%1.1f%%",
        colors=sns.color_palette("pastel"),
        ax=ax,
        startangle=90,
        textprops={"fontsize": 10, "fontweight": "bold"},
    )
    ax.set_title("Species Distribution", fontweight="bold", fontsize=12)
    plt.xticks(fontweight="bold")
    plt.yticks(fontweight="bold")
    plt.xlabel("Species", fontweight="bold")
    ax.set_ylabel("", fontweight="bold")  # Remove default y-axis label
    st.pyplot(fig)

    # Scatter Plot
    st.subheader("Scatter Plot: Sepal Dimensions")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        x="sepal_length",
        y="sepal_width",
        hue="species",
        data=iris,
        palette="pastel",
        alpha=0.8,
        ax=ax,
    )
    ax.set_title("Sepal Length vs Sepal Width by Species", fontweight="bold")
    plt.xticks(fontweight="bold")
    plt.yticks(fontweight="bold")
    plt.xlabel("Sepal Length", fontweight="bold")
    plt.ylabel("Sepal Width", fontweight="bold")
    # Set legend with bold fontweight
    plt.legend(loc="upper right", prop={"weight": "bold"})
    st.pyplot(fig)

    # Box Plot
    st.subheader("Box Plot: Petal Dimensions")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x="species", y="petal_length", data=iris, palette="pastel", ax=ax)
    plt.xticks(fontweight="bold")
    plt.yticks(fontweight="bold")
    plt.xlabel("Species", fontweight="bold")
    plt.ylabel("Petal Length", fontweight="bold")
    ax.set_title("Petal Length Distribution by Species", fontweight="bold")
    st.pyplot(fig)

    # Histogram
    st.subheader("Histogram: Petal Width Distribution")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(
        iris,
        x="petal_width",
        hue="species",
        kde=True,
        palette="pastel",
        alpha=0.8,
        ax=ax,
    )
    ax.set_title("Petal Width Distribution by Species", fontweight="bold")
    plt.xticks(fontweight="bold")
    plt.yticks(fontweight="bold")
    plt.xlabel("Species", fontweight="bold")
    plt.ylabel("Petal Length", fontweight="bold")
    st.pyplot(fig)

    # Pairplot for Iris Dataset
    st.subheader("Pairplot: Sepal and Petal Dimensions")
    pair_plot = sns.pairplot(iris, hue="species", palette="pastel")
    st.pyplot(pair_plot)

# Deployment Notes
st.header("Deployment Steps")
st.markdown(
    """
### **1. Create GitHub Repository**
- Push all code (including this Streamlit app) to a repository.

### **2. Add `requirements.txt`**
Create a file named `requirements.txt` in your repository with the following content:
`streamlit pandas matplotlib seaborn`

### **3. Deploy to Streamlit Cloud**
- Log in to [Streamlit Cloud](https://streamlit.io/).
- Connect your GitHub repository.
- Deploy your app directly by selecting the `main` branch.

### **4. Test the App**
- Open the deployed app link.
- Test file upload, effort estimation, task allocation, and visualizations.
"""
)

# Footer with Author Info
st.write(
    """
**Analyze Effort Distribution and Task Allocation to improve sprint outcomes.**
---
**Author**: Madhurima Rawat | © 2024
"""
)
