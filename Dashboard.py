import streamlit as st

import plotly.express as plx
import pandas as pd
import warnings
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from wordcloud import WordCloud

st.set_page_config(layout="wide", page_title="Mental Health Dashboard", page_icon="🧠")

warnings.filterwarnings('ignore')

@st.cache_data
def load():
    data = pd.read_csv("df_encoded.csv")
    return data

data = load()


def plot_mh_pie_charts(df, filter_columns=None):
    if filter_columns:
        for column, values in filter_columns.items():
            if values:
                df = df[df[column].isin(values)]

    current_mh_mapping = {0: "Don't Know", 1: "Maybe", 2: "No", 3: "Possibly", 4: "Yes"}
    past_mh_mapping = {0: "Don't Know", 1: "Maybe", 2: "No", 3: "Possibly", 4: "Unknown", 5: "Yes"}

    df['current_mh_disorder_mapped'] = df['current_mh_disorder'].map(current_mh_mapping)
    df['past_mh_disorder_mapped'] = df['past_mh_disorder'].map(past_mh_mapping)

    current_counts = df['current_mh_disorder_mapped'].value_counts()
    past_counts = df['past_mh_disorder_mapped'].value_counts()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    ax1.pie(current_counts, labels=current_counts.index, autopct='%1.1f%%',
            startangle=90, colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'], 
            explode=(0.05,) + (0,) * (len(current_counts)-1), textprops={'fontsize': 12})
    ax1.set_title('Current Mental Health Status', fontsize=14, pad=20)

    ax2.pie(past_counts, labels=past_counts.index, autopct='%1.1f%%',
            startangle=90, colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7CAC9'], 
            explode=(0.05,) + (0,) * (len(past_counts)-1), textprops={'fontsize': 12})
    ax2.set_title('Past Mental Health History', fontsize=14, pad=20)

    plt.suptitle('Mental Health Prevalence', fontsize=18, y=1.05)
    plt.tight_layout()
    return fig

def plot_industry_support_hist(df, filter_columns=None, bins=10):
    title_suffix = ""
    if filter_columns:
        for column, values in filter_columns.items():
            if values:
                df = df[df[column].isin(values)]
    else:
        title_suffix = " (All Respondents)"
    
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.histplot(df['industry_support_rating'], bins=bins, kde=True, color='#45B7D1', 
                 edgecolor='white', linewidth=1.2, ax=ax)
    
    ax.set_xlabel("Industry Support Rating", fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    ax.set_title(f"Distribution of Industry Support Rating {title_suffix}", fontsize=14, pad=20)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    st.pyplot(fig)

def plot_trend_by_country(df, column, selected_countries=None):
    trend_data = df.groupby(["year", "work_country"])[column].mean().unstack()
    
    if selected_countries:
        trend_data = trend_data[selected_countries]
    
    fig, ax = plt.subplots(figsize=(14, 8))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    trend_data.plot(kind="line", marker="o", ax=ax, linewidth=2.5, markersize=8, color=colors[:len(trend_data.columns)])
    
    ax.set_title(f"Trend of {column.replace('_', ' ').title()} Over Years by Country", fontsize=16, pad=20)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel(f"Average {column.replace('_', ' ').title()}", fontsize=12)
    ax.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    st.pyplot(fig)


def comfort_dis_mh(df, filter_columns=None):
    if filter_columns:
        for column, values in filter_columns.items():
            if values:  # Apply filter only if the list is not empty
                df = df[df[column].isin(values)]
                print(f"Filtered {column} for {values}: {df.shape[0]} rows found")  # Debugging line


    mapping = {
      
        0: "Maybe",
        1: "No",
      
        3: "Yes"
    }
    
   
    df['comfort_coworkers'] = df['comfort_coworkers'].map(mapping)
    df['comfort_supervisor'] = df['comfort_supervisor'].map(mapping)

    # Count values after mapping
    a = df['comfort_coworkers'].value_counts()
    b = df['comfort_supervisor'].value_counts()

    print(f"WITH COWERKERS {a.to_dict()}") 
    print(f"WITH SUPERVISERS {b.to_dict()}")  

   
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

 
    ax1.pie(a, labels=a.index, autopct='%1.1f%%',
            startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'], 
            explode=(0.1,) + (0,) * (len(a)-1))
    ax1.set_title('WITH COWERKERS')

 
    ax2.pie(b, labels=b.index, autopct='%1.1f%%',
            startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6'], 
            explode=(0.1,) + (0,) * (len(b)-1))
    ax2.set_title('WITH SUPERVISERS')

    plt.suptitle(f'COMFORT DISCUSSING MH', fontsize=16)
    plt.tight_layout()
    st.pyplot(fig)

@st.cache_data
def view_suggestion(df):

    keywords = df['Keywords'].dropna().explode().astype(str)


    text = " ".join(keywords)

    # Generate Word Cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    fig, ax = plt.subplots(figsize=(14, 8))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")

    
    st.pyplot(fig)

filter_columns ={}

with st.sidebar:
    st.title("🧠 Dashboard Filters")
    st.markdown("---")
    
    Demographics = []
    Employment_t = []
   

    if "Demographics" not in st.session_state:
        st.session_state.Demographics = False
    if "Employment_t" not in st.session_state:
        st.session_state.Employment_t = False
 

    if st.button("Demographics", key="demo_btn"):
        st.session_state.Demographics = not st.session_state.Demographics

    if st.session_state.Demographics:
        with st.expander("Demographics Filters"):

            if st.checkbox("Gender"):
                filter_columns["gender"] = []
                if st.checkbox("Male"):
                    filter_columns["gender"].append(1)
                if st.checkbox("Female"):
                    filter_columns["gender"].append(2)

            if st.checkbox("Country"):
                filter_columns["work_country"] = []
                countries = ['UK', 'USA', 'Canada', 'Germany', 'India', 'UAE']
                for country in countries:
                    if st.checkbox(country):
                        filter_columns["work_country"].append(country)

    if st.button("Employment Type", key="emp_btn"):
        st.session_state.Employment_t = not st.session_state.Employment_t

    if st.session_state.Employment_t:
        with st.expander("Employment Filters"):
            filter_columns["tech_role"] = []
            if st.checkbox("Tech"):
                filter_columns['tech_role'].append(1)
            if st.checkbox("Non-Tech"):
                filter_columns['tech_role'].append(0)

  

    st.markdown("---")
    bins = st.slider("Number of Bins", min_value=5, max_value=50, value=10, step=1)

col1, col2 = st.columns([3, 1])
with col1:
    st.title("Mental Health Dashboard")
    st.markdown("---")

tab1, tab2, tab3,tab4,tab5 = st.tabs(["Mental Health Prevalence", "Industry Support", "Country Trends","COMFORT DISCUSSING MH","Mental Health Suggestions BY People"])

with tab1:
    st.header("Prevalence of Mental Health")
    fig = plot_mh_pie_charts(data, filter_columns=filter_columns)
    st.pyplot(fig)

with tab2:
    st.header("Industry Support Rating")
    plot_industry_support_hist(data, filter_columns, bins)

with tab3:
    st.header("Trends By Country Over the Years")
    col1, col2 = st.columns([1, 3])
    with col1:
        use_in = st.radio(
            "PLOT TREND BY",
            ["Having MH Disorder", "Having MH Benefits", "Having Industry Support"],
            index=2
        )
        country = st.multiselect(
            "Select Countries", 
            ["USA", "UK", "India", "Germany", "UAE"],
            default=["USA", "UK"]
        )
    if use_in == "Having Industry Support":
        plot_trend_by_country(data, "industry_support_rating", country)
    elif use_in == "Having MH Disorder":
        plot_trend_by_country(data, "current_mh_disorder", country)
    else:
        plot_trend_by_country(data, "mh_benefits", country)
with tab4:
    st.header("COMFORT DISCUSSING Mental Health")
    comfort_dis_mh(data, filter_columns)
with tab5:
    d = pd.read_csv("processed_mh_support_suggestions.csv")
    view_suggestion(d)
