import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import matplotlib.dates as mdates




# things to remember 
# the data still need to be cleaned 
# - inverserrate and exchangeRate are sometimes in string vs float 

plt.style.use('seaborn-v0_8-whitegrid')

def eda_krw_to_usd(csv_filepath="allDB.csv"):
    """
    Performs an Exploratory Data Analysis (EDA) for KRW to USD exchange rates.

    Args:
        csv_filepath (str): The path to the CSV file containing the exchange rate data.
    """
    try:
        # Load the dataset
        df = pd.read_csv(csv_filepath)
    except FileNotFoundError:
        print(f"Error: The file {csv_filepath} was not found.")
        print("Please ensure 'takeHomeTest.py' has been run to generate 'allDB.csv'.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file {csv_filepath} is empty.")
        return

    print("Columns in the loaded CSV:", df.columns.tolist())

    # Filter for KRW as baseCurrency and USD as targetCurrency
    # Based on floatrates.com, if base is KRW, target is USD, exchangeRate is how many USD 1 KRW is.
    # If you want USD per KRW, this is correct.
    # If you want KRW per USD, you might need to use inverseRate or filter differently
    # if the source data provides USD as base and KRW as target.
    # Assuming 'exchangeRate' for base=KRW, target=USD is what we need (1 KRW = X USD)
    df_krw_usd = df[(df['baseCurrency'] == 'KRW') & (df['targetCurrency'] == 'USD')].copy() # Use .copy() to avoid SettingWithCopyWarning

    if df_krw_usd.empty:
        print("No data found for KRW to USD. Please check the contents of 'allDB.csv'.")
        print("Ensure 'baseCurrency' is 'KRW' and 'targetCurrency' is 'USD' in your data.")
        return

    # Data Cleaning and Preparation
    # Convert 'pubDate' to datetime objects
    df_krw_usd['pubDate'] = pd.to_datetime(df_krw_usd['pubDate'], errors='coerce')

    # Convert 'exchangeRate' to numeric, coercing errors will turn non-numeric to NaT/NaN
    df_krw_usd['exchangeRate'] = pd.to_numeric(df_krw_usd['exchangeRate'], errors='coerce')
    
    # Also convert 'inverseRate' if you plan to use it (e.g., for KRW per USD)
    df_krw_usd['inverseRate'] = pd.to_numeric(df_krw_usd['inverseRate'], errors='coerce')


    # Drop rows where conversion failed (if any)
    df_krw_usd.dropna(subset=['pubDate', 'exchangeRate'], inplace=True)

    if df_krw_usd.empty:
        print("Data became empty after cleaning (date/rate conversion). Please check data quality.")
        return

    # Sort data by date
    df_krw_usd.sort_values('pubDate', inplace=True)

    print(f"\n--- EDA for KRW to USD (1 KRW = X USD) ---")
    print(f"Data points found: {len(df_krw_usd)}")

    # Descriptive Statistics for exchangeRate (1 KRW = X USD)
    print("\nDescriptive Statistics for exchangeRate (1 KRW = X USD):")
    print(df_krw_usd['exchangeRate'].describe())

    # If you are interested in KRW per 1 USD, you would use the 'inverseRate'
    # The 'inverseRate' from floatrates.com when base=KRW and target=USD means 1 USD = X KRW
    if 'inverseRate' in df_krw_usd.columns:
        print("\nDescriptive Statistics for inverseRate (1 USD = X KRW):")
        print(df_krw_usd['inverseRate'].describe())
        # Let's focus the plots on KRW per USD (inverseRate) as it's more common
        rate_to_plot = 'inverseRate'
        y_label_plot = 'Exchange Rate (KRW per 1 USD)'
        plot_title_suffix = 'KRW per 1 USD'
    else:
        rate_to_plot = 'exchangeRate'
        y_label_plot = 'Exchange Rate (USD per 1 KRW)'
        plot_title_suffix = 'USD per 1 KRW'


    # --- Visualizations ---

    # 1. Time Series Plot
    plt.figure(figsize=(14, 7))
    plt.plot(df_krw_usd['pubDate'], df_krw_usd[rate_to_plot], label=plot_title_suffix, color='dodgerblue')
    plt.title(f'Time Series of {plot_title_suffix} Exchange Rate')
    plt.xlabel('Date')
    plt.ylabel(y_label_plot)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.YearLocator()) # Show ticks per year
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("krw_usd_time_series.png")
    plt.show()

    # 2. Histogram of the Exchange Rate
    plt.figure(figsize=(10, 6))
    sns.histplot(df_krw_usd[rate_to_plot], kde=True, color='skyblue')
    plt.title(f'Distribution of {plot_title_suffix} Exchange Rate')
    plt.xlabel(y_label_plot)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig("krw_usd_histogram.png")
    plt.show()

    # 3. Box Plot of the Exchange Rate
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=df_krw_usd[rate_to_plot], color='lightcoral')
    plt.title(f'Box Plot of {plot_title_suffix} Exchange Rate')
    plt.ylabel(y_label_plot)
    plt.tight_layout()
    plt.savefig("krw_usd_boxplot.png")
    plt.show()

    print("\nEDA plots saved as krw_usd_time_series.png, krw_usd_histogram.png, and krw_usd_boxplot.png")
    print("Analysis complete.")

if __name__ == "__main__":
    # Ensure 'allDB.csv' is in the same directory as this script,
    # or provide the correct path.
    # This CSV should be generated by running takeHomeTest.py
    eda_krw_to_usd(csv_filepath="./allDB.csv")