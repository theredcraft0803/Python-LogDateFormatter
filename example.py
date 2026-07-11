from datetime import datetime
# Import the LogDateUtils class from your module file
from log_date_utils import LogDateUtils 

print("=== Python Logging Example ===")

# Scenario 1: Get the current timestamp (Default behavior)
# No arguments are passed, so it automatically defaults to datetime.now()
current_timestamp = LogDateUtils.get_log_date_format()
print(f"Current Time Log: {current_timestamp} Application started successfully.")

# Scenario 2: Get a timestamp for a specific/custom date
# Create a specific datetime object (e.g., Christmas Eve 2025 at 18:30:00)
custom_date = datetime(2025, 12, 24, 18, 30, 0)
custom_timestamp = LogDateUtils.get_log_date_format(custom_date)
print(f"Custom Time Log:  {custom_timestamp} Scheduled maintenance backup completed.")
