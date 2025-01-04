import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import io

def load_data(file_path):
    ##Loads a CSV file and returns a DataFrame.
    try:
        df = pd.read_csv(file_path)
        print(f"Data successfully loaded. Dimensions: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading the file: {e}")
        return None

def generate_summary(df):
    ##Generates descriptive statistics for the DataFrame.
    print("\nData Summary:")
    print(df.info())
    print("\nDescriptive Statistics:")
    print(df.describe())

def plot_and_save_distribution(df, column, output_dir):
    ##Generates and saves a histogram for the specified column.
    if column in df.columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[column].dropna(), kde=True, bins=20)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        
        # Save the plot
        file_path = os.path.join(output_dir, f"distribution_{column}.png")
        plt.savefig(file_path)
        print(f"Distribution plot saved as: {file_path}")
        plt.show()
    else:
        print(f"The column '{column}' does not exist in the data.")

def plot_and_save_correlation_heatmap(df, output_dir):
    ##Generates and saves a heatmap of correlations.
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", square=True)
    plt.title("Correlation Heatmap")
    
    # Save the plot
    file_path = os.path.join(output_dir, "correlation_heatmap.png")
    plt.savefig(file_path)
    print(f"Correlation heatmap saved as: {file_path}")
    plt.show()

def save_report(df, output_path):
    ##Saves a summary of the data and descriptive statistics to a text file.
    try:
        with open(output_path, "w") as f:
            # Capture df.info() output
            buffer = io.StringIO()
            df.info(buf=buffer)
            info_output = buffer.getvalue()
            
            # Write info and descriptive statistics to file
            f.write("Data Summary:\n")
            f.write(info_output)
            f.write("\n\nDescriptive Statistics:\n")
            f.write(df.describe().to_string())
        print(f"Report saved to: {output_path}")
    except Exception as e:
        print(f"Error saving the report: {e}")

def main():
    # Path to the CSV file
    file_path = input("Enter the path to the CSV file: ")
    data = load_data(file_path)
    if data is not None:
        # Output directory for saved plots and reports
        output_dir = input("\nEnter the directory to save outputs (e.g., plots and reports): ")
        os.makedirs(output_dir, exist_ok=True)
        print(f"Output directory created: {output_dir}")
        
        generate_summary(data)
        
        # Request column for distribution plot
        column = input("\nEnter the column name to plot the distribution: ")
        plot_and_save_distribution(data, column, output_dir)
        
        # Generate and save correlation heatmap
        print("\nGenerating and saving correlation heatmap...")
        plot_and_save_correlation_heatmap(data, output_dir)
        
        # Save report
        report_path = os.path.join(output_dir, "data_report.txt")
        save_report(data, report_path)

if __name__ == "__main__":
    main()
