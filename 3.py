import urllib.parse

# Open the log file
with open('connectio.log', 'r') as f:
    # Read the contents of the file line by line
    for line in f:
        # Parse the URL from the line
        url = urllib.parse.urlparse(line)
        # Print the URL
        print(url)