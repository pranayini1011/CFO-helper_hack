import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("CFO Helper - Budget Forecast Simulator")

# Sidebar sliders for budget inputs with ₹ symbol
st.sidebar.header("Adjust Budget Parameters")
revenue = st.sidebar.slider("Monthly Revenue (₹)", 10000, 100000, 50000, step=1000)
marketing = st.sidebar.slider("Marketing Spend (₹)", 1000, 20000, 5000, step=500)
staff_costs = st.sidebar.slider("Staff Costs (₹)", 5000, 50000, 20000, step=500)
other_expenses = st.sidebar.slider("Other Expenses (₹)", 1000, 15000, 5000, step=500)

# Calculate profits
profit_before_tax = revenue - (marketing + staff_costs + other_expenses)
tax_rate = 0.25
tax = profit_before_tax * tax_rate if profit_before_tax > 0 else 0
net_profit = profit_before_tax - tax

# Show results in app with ₹ symbol
st.header("Forecast Results")
st.write(f"Profit Before Tax: ₹{profit_before_tax:,.2f}")
st.write(f"Estimated Tax (@ 25%): ₹{tax:,.2f}")
st.write(f"Net Profit: ₹{net_profit:,.2f}")

# Create a chart for 12-month forecast
months = np.arange(1, 13)
monthly_revenue = np.full(12, revenue)
monthly_expenses = np.full(12, marketing + staff_costs + other_expenses)
monthly_profit = monthly_revenue - monthly_expenses

plt.figure(figsize=(10, 4))
plt.plot(months, monthly_revenue, label='Revenue')
plt.plot(months, monthly_expenses, label='Expenses')
plt.plot(months, monthly_profit, label='Profit')
plt.xlabel('Month')
plt.ylabel('Amount (₹)')
plt.title('12-Month Financial Forecast')
plt.legend()
plt.grid(True)

st.pyplot(plt)
