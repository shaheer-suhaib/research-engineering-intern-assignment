# Assignment: Mental Health in Tech (2016–2020) Sentiment & Trends Analysis

## Background & Context

Workplace mental health is a critical issue in the tech industry. Surveys by the Open Sourcing Mental Illness (OSMI) organization have shown that over half of tech professionals reported having a diagnosed mental health condition in 2016 [GITHUB.COM]. The OSMI multi-year survey data (2016–2020) captures employees’ attitudes toward mental health in the workplace and the prevalence of mental health conditions [OSMHHELP.ORG]. This assignment uses the Kaggle dataset "Mental Health in Tech Dashboard (2016-2020)" to explore these issues. You will perform sentiment analysis on survey responses, analyze trends in workplace mental health over time and across demographics, and present your findings in an interactive dashboard (or a static report). An optional bonus task invites you to apply predictive modeling to forecast future mental health trends.

## Objectives

1. **Sentiment Analysis**: Use NLP techniques to classify the sentiment of employee responses related to workplace mental health (e.g., comments about workplace support or personal experiences).
2. **Trend Analysis**: Examine how workplace mental health metrics and attitudes have changed from 2016 to 2020. Compare trends across different companies and demographic groups (such as gender, age, or job role).
3. **Interactive Dashboard**: Present your analysis in a clear, interactive visualization dashboard (preferred) to allow exploration of the data. If a dashboard is not feasible, provide a well-organized static report with charts.
4. **Predictive Modeling (Bonus)**: (Optional) Apply a forecasting or advanced analytics model to predict future workplace mental health trends (e.g., predicting 2021 sentiment or trend continuation) based on the 2016–2020 data.

## Dataset

The analysis uses the publicly available Kaggle dataset:

- [**Mental Health in Tech Dashboard (2016-2020)**](https://www.kaggle.com/datasets/sivas1292/mental-health-in-tech-dashboard-2016-to-2020)
## Dataset Description

The Mental Health in Tech Dashboard (2016-2020) dataset is a compilation of annual surveys conducted by OSMI from 2016 through 2020. It includes multiple-choice and free-response answers from tech employees about mental health. Key fields include:
- Demographic information (age, gender, role, country)
- Company info (company name or size)
- Responses to questions about mental health (e.g., if they have a mental health condition, workplace support availability, attitudes toward discussing mental health, etc.)
- Open-ended text responses about the employees’ experiences or opinions

The data is organized by year, allowing a year-over-year comparison of trends. Ensure you review the dataset documentation on Kaggle for detailed schema and question descriptions.

## Tasks and Deliverables

Your assignment is to produce an analysis and report covering the following components:

### 1. Sentiment Analysis (NLP)

- **Data Preparation**: Identify survey questions or fields that contain free-text responses regarding mental health in the workplace. Clean and preprocess this text data (remove noise, handle missing values, etc.).
- **Sentiment Classification**: Apply NLP techniques to determine the sentiment of each response. You may use a pre-trained sentiment analysis model or create a simple classifier. Categorize sentiment as positive, negative, or neutral. Document which tool or library you use (e.g., NLTK/VADER, TextBlob, spaCy, or transformer models) and how you validated its accuracy.
- **Analysis of Sentiments**: Summarize the overall sentiment distribution. Determine if the majority of comments are positive or negative regarding workplace mental health. Highlight examples of common positive sentiments (e.g., praising company support) versus negative sentiments (e.g., frustration with lack of support). Break down sentiment by year or by demographic group to see if sentiment is improving or worsening over time.

### 2. Workplace Mental Health Trends (2016–2020)

- **Year-over-Year Trends**: Track key metrics across 2016, 2017, 2018, 2019, and 2020. Focus on metrics that reflect mental health in the workplace, such as:
  - Prevalence of Mental Health Conditions
  - Workplace Support
  - Comfort Discussing Mental Health
  - Policy Awareness
- **Visualization of Trends**: Create line charts or bar charts to visualize how these metrics change over time. Include annotations or labels to highlight notable changes. Discuss any trends observed and relate them to possible real-world contexts.
- **Company Comparison**: Compare trends across different companies or company sizes. Present comparisons using appropriate charts (grouped bar charts, multiple line plots, etc.). Ensure anonymity if required.
- **Demographic Insights**: Analyze how mental health responses vary by demographics. Explore at least one demographic factor in depth and use charts to illustrate these differences. Discuss what these differences might mean for targeted mental health initiatives.

### 3. Interactive Dashboard Presentation

- **Design an Interactive Dashboard**: Build an interactive dashboard to showcase the findings from your sentiment analysis and trends analysis. The dashboard should allow users to explore the data visually.
- **Dashboard Content**: Include the following in your dashboard:
  - A summary Sentiment Analysis view
  - A Time Trends view with an interactive time series chart
  - A Comparison view for comparing companies or demographic groups
  - Any other insightful visualization you find relevant
- **Interactivity and Usability**: Ensure the dashboard is well-labeled and easy to use. Include titles, axis labels, and brief descriptions/tooltips. Aim for a clean layout.
- **Static Report Alternative**: If creating an interactive dashboard is not feasible, submit a static report containing well-formatted static charts for all the above components.

### 4. Predictive Modeling (Bonus)

- **Forecast Future Trends**: Using the data from 2016–2020, attempt to predict a mental health metric for a future time period (e.g., forecast the 2021 values of key metrics).
- **Model Choices**: Use time series forecasting or train a regression model using year and demographic factors as features to predict an outcome. Justify why the modeling approach is appropriate for your question.
- **Evaluation of Predictions**: Focus on how well your model fits the existing data and whether the predictions seem reasonable. Report the accuracy or error metrics.
- **Visualization**: Include the forecast in your dashboard or report. Show a line chart of 2016–2020 actual values and a dotted line for 2021 predicted value.

## Submission Instructions

Please include the following in your submission:

- **Code and Analysis**: All code used for data processing, analysis, and visualization. Ensure your code is well-documented with comments and organized into sections.
- **Interactive Dashboard**: If you built a dashboard, provide your source code files and instructions to run it locally. Include a README.md with setup steps. If you used an online tool, provide a link and a backup screenshot.
- **Report**: Submit a report documenting your findings. This can be in the form of a PDF exported from your Jupyter Notebook or a separate written report with embedded figures and discussion.
- **Rubric Checklist**: (Optional but recommended) Include a brief section referencing the rubric criteria and noting where in your submission each criterion is addressed.

### Important Notes

- **Data Privacy**: Do not share any raw data publicly that might violate privacy.
- **Reproducibility**: Your code should run on another machine with the dataset. Do not hard-code file paths; use relative paths and include instructions if any non-standard steps are required to get the data.
- **Clarity**: Use markdown cells and comments liberally to explain each step of your analysis.
- **Limitations**: Mention any limitations or assumptions in your report.
- **Extra Credit**: If you did additional analysis beyond the scope, briefly include it in an appendix or an extra section.

## Evaluation Rubric

Your submission will be evaluated based on the following criteria:

- **Data Cleaning & Understanding (10%)**: Proper handling of data loading, missing values, and outliers. Evidence of understanding the dataset structure and context.
- **Sentiment Analysis (20%)**: Quality of NLP analysis, including correct preprocessing of text, a sensible approach to classify sentiment, and accurate interpretation of results.
- **Trend Analysis & Insights (25%)**: Depth of analysis for year-over-year trends, company comparisons, and demographic differences. Clear identification of at least two meaningful trends or patterns in the data.
- **Visualizations & Dashboard (20%)**: Quality and clarity of visual presentations. The interactive dashboard (or static visual report) should be logically organized and allow a viewer to grasp key results.
- **Communication & Documentation (15%)**: Clarity of writing in the report and comments in code. The narrative should explain what you found and how you found it.
- **Technical Soundness (10%)**: Correct use of data science techniques. The code should run without errors and be reasonably optimized.
- **Bonus: Predictive Modeling (Up to +10%)**: Successfully implementing the optional predictive task. Points will be awarded for a reasonable modeling approach, correct evaluation, and interpreting the results.
## Submission Requirements
You will submit all your deleiverables on github repo, and please do mail me the link to your github repo at khawajamurad@outlook.com
Please ensure you include:

1. A detailed README file (with screenshots of your solution, a hosted web platform).
2. A text-based explanation of your code and thought process underlying system design.
3. A link to a video recording of your dashboard hosted on YouTube or Google Drive.
Both of these last two make it easier for us to run your code and evaluate the assignment.
### Grading Note

A submission that meets all the core requirements (Tasks 1–3) with clarity and correctness can earn full credit (100%). The bonus task is truly extra. We will particularly reward thoughtful analysis – showing that you can think like a data scientist. This means exploring the data deeply, verifying assumptions, and not just generating charts but also explaining and interpreting them. Make sure your conclusions are supported by the data.
Focus on the analysis you are presenting and the story you are telling us through it. A well-designed and scalable system is more important than a complex one with a ton of features. Consider using innovative technologies in a user-friendly manner to create unique features for your platform such as AI-generated summaries that are adaptable to the data a user searches for, using your platform.

Presentation matters! Make sure your submission is easy to understand. Create an intuitive and meaningful README file or a Wiki that can be used to review your solution. Host it so it is accessible by anyone. Ensure that you share a video demo even if it is hosted, so that users understand how to interpret the insights you present.
Good luck, and enjoy the analysis! This project not only tests your technical skills (NLP, data analysis, visualization) but also your ability to draw meaningful insights from data – a key skill for a research engineer in data science. We look forward to seeing your interactive dashboards and findings on this important topic of mental health in tech.
Good Luck!

