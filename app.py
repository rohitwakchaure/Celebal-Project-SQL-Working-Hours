import streamlit as st
import pandas as pd

# Set the title
st.title("Employee Working Hours Dashboard")

df = pd.read_csv("employee_working_hours.csv")


# Convert date columns to datetime
df['START_DATE'] = pd.to_datetime(df['START_DATE'])
df['END_DATE'] = pd.to_datetime(df['END_DATE'])

st.subheader("Raw Data")
st.dataframe(df)

# Total Working Hours
st.subheader("📊 Total Working Hours Summary")

col1, col2 = st.columns(2)
with col1:
    total_hours = df['NO_OF_HOURS'].sum()
    st.metric("Total Hours (All Employees)", total_hours)

with col2:
    avg_hours = df['NO_OF_HOURS'].mean()
    st.metric("Average Hours per Employee", round(avg_hours, 2))

# Department-wise working hours
dept_summary = df.groupby('department_name')['NO_OF_HOURS'].sum().reset_index()
st.subheader("🧾 Department-wise Working Hours")
st.dataframe(dept_summary)

# Employee-wise working hours
emp_summary = df[['emp_name', 'department_name', 'NO_OF_HOURS']]
st.subheader("👨‍💼 Employee-wise Working Hours")
st.dataframe(emp_summary)

# Filter option
st.subheader("🔍 Filter by Department")
dept_options = df['department_name'].unique()
selected_dept = st.selectbox("Choose Department", options=['All'] + list(dept_options))

if selected_dept != 'All':
    filtered_df = df[df['department_name'] == selected_dept]
    st.write(f"Showing records for **{selected_dept}**")
    st.dataframe(filtered_df)

    total_dept_hours = filtered_df['NO_OF_HOURS'].sum()
    st.success(f"Total hours for {selected_dept}: {total_dept_hours}")
