import csv
import re

def extract_log_data(log_file):
  """
  This function extracts the data from a log file into CSV format.

  Args:
    log_file: The path to the log file.

  Returns:
    A list of tuples containing the data from the log file in CSV format.
  """

  # Open the log file.
  with open(log_file, "r") as log_file:

    # Create a list to store the data from the log file.
    data_list = []

    # Read the log file line by line.
    for line in log_file:

      # Extract the data from the line and convert them to a tuple.
      data_tuple = tuple(line.split(" "))

      # Add the data tuple to the list of data.
      data_list.append(data_tuple)

  # Return the list of data.
  return data_list


if __name__ == "__main__":
  # Get the path to the log file.
  log_file = input("Enter the path to the log file: ")

  # Extract the data from the log file.
  data_list = extract_log_data(log_file)

  # Write the data to a CSV file.
  with open("output.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    for data_tuple in data_list:
      csv_writer.writerow(data_tuple)
