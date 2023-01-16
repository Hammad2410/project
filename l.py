import pendulum

# Get input string in the format "yyyy-mm-ddThh:mm:ss.microsecondsZ"
input_string = input("Enter the time in the format yyyy-mm-ddThh:mm:ss.microsecondsZ: ")

# Parse the input string to create a datetime object
utc_time = pendulum.parse(input_string)

# Convert Zulu time to Pakistan time
pakistan_time = utc_time.in_timezone('Asia/Karachi')

# Format the date and time as "dd-mm-yy time"
date_time_format = pakistan_time.format("DD-MM-YY HH:mm:ss")

# Print the converted time
print("Zulu time: ", utc_time)
print("Pakistan time: ", date_time_format)
