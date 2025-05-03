import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Streamlit page configuration
st.set_page_config(page_title="Startup Funding Suite", layout="wide")

# Mock AI-driven content suggestion function
def generate_content_suggestion(section, user_input):
    suggestions = {
        "executive_summary": "Summarize your business vision, mission, and unique value proposition. Example: [Your Company] aims to revolutionize [industry] by offering [unique solution].",
        "grant_objective": "Clearly state the purpose of the grant and its impact. Example: This grant will fund [specific project] to achieve [specific outcome].",
        "market_analysis": "Describe your target market and trends. Example: The [industry] market is growing at [X%] annually, with demand for [product/service]."
    }
    return suggestions.get(section, "Enter details to receive a tailored suggestion.") if not user_input else f"Refined: {user_input} (AI suggestion: Ensure clarity and specificity.)"

# Mock financial forecasting function
def calculate_financial_forecast(revenue, expenses, years=3):
    forecast = []
    for year in range(1, years + 1):
        growth_rate = 0.1  # Assume 10% annual growth
        revenue *= (1 + growth_rate)
        expenses *= (1 + 0.05)  # Assume 5% expense increase
        profit = revenue - expenses
        forecast.append({"Year": year, "Revenue": revenue, "Expenses": expenses, "Profit": profit})
    return pd.DataFrame(forecast)

# Mock grant database
grant_db = pd.DataFrame([
    {"Grant": "Small Business Innovation Grant", "Amount": "$50,000", "Deadline": "2025-06-30", "Eligibility": "Startups with < 50 employees"},
    {"Grant": "Nonprofit Community Fund", "Amount": "$25,000", "Deadline": "2025-07-15", "Eligibility": "Nonprofits serving local communities"},
    {"Grant": "Tech Startup Accelerator", "Amount": "$100,000", "Deadline": "2025-08-01", "Eligibility": "Tech startups with MVP"}
])

# Mock competitor data
competitor_data = pd.DataFrame([
    {"Competitor": "Competitor A", "Market Share": 30, "Revenue": 500000, "Growth Rate": 15},
    {"Competitor": "Competitor B", "Market Share": 20, "Revenue": 300000, "Growth Rate": 10},
    {"Competitor": "Competitor C", "Market Share": 10, "Revenue": 100000, "Growth Rate": 5}
])

# Sidebar navigation
st.sidebar.title("Startup Funding Suite")
page = st.sidebar.radio("Navigate", ["Business Plan Writer", "Grant Writing Tool", "Competitive Analysis Dashboard", "Grant Database"])

# Business Plan Writer
if page == "Business Plan Writer":
    st.title("Business Plan Writing Tool")
    st.write("Create a professional business plan with AI-driven suggestions and financial forecasting.")

    # Free template section
    st.header("Free Business Plan Template")
    with st.expander("Executive Summary"):
        user_input = st.text_area("Enter your executive summary:", key="exec_summary")
        suggestion = generate_content_suggestion("executive_summary", user_input)
        st.write(f"AI Suggestion: {suggestion}")
        if st.button("Save Section", key="save_exec"):
            st.success("Executive Summary saved!")

    with st.expander("Market Analysis"):
        user_input = st.text_area("Enter your market analysis:", key="market_analysis")
        suggestion = generate_content_suggestion("market_analysis", user_input)
        st.write(f"AI Suggestion: {suggestion}")
        if st.button("Save Section", key="save_market"):
            st.success("Market Analysis saved!")

    # Financial Forecasting
    st.header("Financial Forecasting")
    revenue = st.number_input("Initial Annual Revenue ($)", min_value=0, value=100000)
    expenses = st.number_input("Initial Annual Expenses ($)", min_value=0, value=80000)
    if st.button("Generate Forecast"):
        forecast_df = calculate_financial_forecast(revenue, expenses)
        st.dataframe(forecast_df)
        fig = px.line(forecast_df, x="Year", y=["Revenue", "Expenses", "Profit"], title="Financial Forecast")
        st.plotly_chart(fig)

# Grant Writing Tool
elif page == "Grant Writing Tool":
    st.title("Grant Writing Tool (Premium Feature)")
    st.write("Craft compelling grant proposals with AI-driven suggestions.")

    with st.expander("Grant Objective"):
        user_input = st.text_area("Enter your grant objective:", key="grant_objective")
        suggestion = generate_content_suggestion("grant_objective", user_input)
        st.write(f"AI Suggestion: {suggestion}")
        if st.button("Save Section", key="save_grant"):
            st.success("Grant Objective saved!")

    with st.expander("Project Budget"):
        budget_items = st.text_area("List budget items (e.g., Equipment: $10,000):")
        if st.button("Validate Budget"):
            st.write("Budget validated! Ensure all costs are justified in the proposal.")

    st.info("Upgrade to SuperGrok for full access to grant writing features: https://x.ai/grok")

# Competitive Analysis Dashboard
elif page == "Competitive Analysis Dashboard":
    st.title("Competitive Analysis Dashboard")
    st.write("Visualize competitor data and market trends.")

    # Competitor Data Visualization
    st.header("Competitor Overview")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(competitor_data, x="Competitor", y="Market Share", title="Market Share")
        st.plotly_chart(fig)
    with col2:
        fig = px.bar(competitor_data, x="Competitor", y="Revenue", title="Revenue")
        st.plotly_chart(fig)

    # Growth Rate Trend
    st.header("Growth Trends")
    fig = px.line(competitor_data, x="Competitor", y="Growth Rate", title="Competitor Growth Rates")
    st.plotly_chart(fig)

    # Market Trend Input
    st.header("Custom Market Trend Analysis")
    trend_keyword = st.text_input("Enter a market trend keyword (e.g., AI, sustainability):")
    if st.button("Analyze Trend"):
        st.write(f"Analyzing market trend: {trend_keyword}. (Placeholder: Real-time data integration required.)")

# Grant Database
elif page == "Grant Database":
    st.title("Grant Opportunity Database")
    st.write("Explore funding opportunities for your business or nonprofit.")

    # Filter grants
    eligibility = st.selectbox("Filter by Eligibility", ["All", "Startups with < 50 employees", "Nonprofits serving local communities", "Tech startups with MVP"])
    filtered_grants = grant_db if eligibility == "All" else grant_db[grant_db["Eligibility"] == eligibility]
    st.dataframe(filtered_grants)

    # Grant Details
    selected_grant = st.selectbox("Select a grant to view details:", filtered_grants["Grant"])
    if selected_grant:
        grant_details = filtered_grants[filtered_grants["Grant"] == selected_grant].iloc[0]
        st.write(f"**Grant**: {grant_details['Grant']}")
        st.write(f"**Amount**: {grant_details['Amount']}")
        st.write(f"**Deadline**: {grant_details['Deadline']}")
        st.write(f"**Eligibility**: {grant_details['Eligibility']}")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Startup Funding Suite by xAI")
st.sidebar.write("Access more features with SuperGrok: [Learn More](https://x.ai/grok)")
