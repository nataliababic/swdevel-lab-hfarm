from mymodules.csv_cleaning import load_data, preprocess_data, process_durata_column, save_data

input_file_path = '/app/app/bologna.csv'
output_file_path = '/app/app/updated_bologna.csv'

# Load data
data = load_data(input_file_path)

# Preprocess data
data = preprocess_data(data)

# Process Durata column
data = process_durata_column(data)

# Save the updated data
save_data(data, output_file_path)
