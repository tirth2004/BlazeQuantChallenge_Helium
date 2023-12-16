# crypto_pie_chart.py
import streamlit as st
import matplotlib.pyplot as plt

def crypto_pie_chart():
    # Data for the pie chart
    labels = ['Bitcoin', 'Ethereum', 'Other Cryptos']
    sizes = [821.9, 266, 1600 - (821.9 + 266)]  # Total market cap is 1600B
    percentages = [51.375, 16.62, 100 - (51.375 + 16.62)]  # Percentages of total cap

    # Plotting the pie chart with enhanced styling
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90, colors=['gold', 'lightcoral', 'lightblue'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart in Streamlit with enhanced styling
    st.subheader("Market Capitalization Distribution")
    st.pyplot(fig)

    # Display additional information with enhanced styling
    st.write("Total market cap of crypto is around 1.6T.")
    st.write("Bitcoin has the highest cap of 821.9B (51.375% of total cap).")
    st.write("Ethereum is at 2nd with a cap of 266B (16.62% of total cap).")
    st.write("Helium (HNT) stands at 75th position with a market cap of 785M (0.049% of total cap of crypto).")