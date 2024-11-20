import streamlit as st
import matplotlib.pyplot as plt

def plot_stock_data(stock_data):
    st.subheader("Stock Price Over Time")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')
    ax.set_title("Stock Price Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    st.pyplot(fig)

def plot_technical_indicators(stock_data):
    st.subheader("Technical Indicators")

    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')
    if 'Moving_Avg' in stock_data.columns:
        ax1.plot(stock_data.index, stock_data['Moving_Avg'], label='Moving Average', color='orange')
    ax1.set_title("Close Price with Moving Average")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Price")
    ax1.legend()
    st.pyplot(fig)

    if 'RSI' in stock_data.columns:
        fig, ax2 = plt.subplots(figsize=(10, 5))
        ax2.plot(stock_data.index, stock_data['RSI'], label='RSI', color='green')
        ax2.axhline(y=70, color='red', linestyle='--', label='Overbought')
        ax2.axhline(y=30, color='blue', linestyle='--', label='Oversold')
        ax2.set_title("Relative Strength Index (RSI)")
        ax2.set_xlabel("Date")
        ax2.set_ylabel("RSI")
        ax2.legend()
        st.pyplot(fig)
    else:
        st.warning("RSI data not available to plot.")


def plot_predictions(actual, predicted, title="Stock Price Prediction"):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(actual, label="Actual Prices", color="blue")
        plt.plot(predicted, label="Predicted Prices", color="orange", linestyle="--")
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Stock Price")
        plt.legend()
        plt.grid(True)

        # Use Streamlit to display the plot
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Error in plotting predictions: {e}")