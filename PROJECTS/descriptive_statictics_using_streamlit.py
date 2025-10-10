import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your Excel/CSV file
df = pd.read_csv(r"C:\Users\Supravata\Desktop\datascience\pdfs\excels\Inc_Exp_Data.csv")

# Streamlit app
st.title("Comprehensive Data Visualizations")
st.write("This app displays a variety of Seaborn plots exploring your uploaded dataset.")

# Function to create and display a plot
def display_plot(title, plot_func):
    st.subheader(title)
    fig, ax = plt.subplots(figsize=(5,5))
    plot_func(ax)
    st.pyplot(fig)
    plt.close(fig)

# Example plots (you can customize based on your dataset's columns)


def no_of_earning_members_plot(ax):
    df['No_of_Earning_Members'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title("Bar Plot: No_of_Earning_Members")
    ax.set_xlabel("No_of_Earning_Members")
    ax.set_ylabel("Count")


def line_plot(ax):
    df.plot(x='Mthly_HH_Income', y='Mthly_HH_Expense',ax=ax)
    ax.set_title("Line Plot: Mthly_HH_Income vs Mthly_HH_Expense")
    mean_expense = df['Mthly_HH_Expense'].mean()
    IQR = df['Mthly_HH_Expense'].quantile(0.75)-df['Mthly_HH_Expense'].quantile(0.25)

def bar_plot(ax):
   df['Highest_Qualified_Member'].value_counts().plot(kind='bar',ax=ax)



# Let user choose which plot to view
plot_options = {
    "No_of_Earning_Members": no_of_earning_members_plot,
    "Line Plot": line_plot,
    "Bar Plot": bar_plot,
}

choice = st.selectbox("Choose a plot type", list(plot_options.keys()))
display_plot(choice, plot_options[choice])

# Show dataset
st.subheader("Uploaded Data Preview")
st.dataframe(df.head())
st.dataframe(df['No_of_Earning_Members'].value_counts())
