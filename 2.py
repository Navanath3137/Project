import urllib.parse

# Open the log file
with open('Log.log', 'r') as f:
    # Read the contents of the file line by line
    for line in f:
        # Try to parse the URL from the line
        try:
            url = urllib.parse.urlparse(line)
        except ValueError:
            # If the URL is not in a recognized format, skip it
            continue
        # Print the URL
        print(url)
