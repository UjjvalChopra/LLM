#First commit
import pandas as pd

# Read files and add source identifier
df1 = pd.read_csv('transactions_log.csv')
df1['log_type'] = 'transaction'

df2 = pd.read_csv('payments_log.csv')
df2['log_type'] = 'payment'

df3 = pd.read_csv('account_state_log.csv')
df3['log_type'] = 'account_state'

# Combine files
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Convert timestamps with a more flexible format
combined_df['timestamp'] = pd.to_datetime(combined_df['timestamp'], format='mixed')
combined_df = combined_df.sort_values('timestamp')

# Save the combined data
combined_df.to_csv('combined_logs_with_type.csv', index=False)

# Print summary
print("\nRecords by log type:")
print(combined_df['log_type'].value_counts())
print("\nDate range:", combined_df['timestamp'].min(), "to", combined_df['timestamp'].max())

numeric_columns = combined_df.select_dtypes(include=['float64', 'int64']).columns
variances = combined_df[numeric_columns].var()

print("\nVariances for numeric fields:")
for column, variance in variances.items():
    print(f"{column}: {variance:.2f}")

numeric_columns = combined_df.select_dtypes(include=['float64', 'int64']).columns
means = combined_df[numeric_columns].mean()
variances = combined_df[numeric_columns].var()

print("\nStatistics for numeric fields:")
print("\nField                  Mean          Variance")
print("-" * 50)
for column in numeric_columns:
   print(f"{column:20} {means[column]:12.2f} {variances[column]:12.2f}")
