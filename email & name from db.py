import requests

# Replace the placeholder with your Xano endpoint URL
ENDPOINT_URL = 'API XANO'

try:
    response = requests.get(ENDPOINT_URL)
    data = response.json()

    # Check if the response is a list/array
    if isinstance(data, list):
        # Iterate over each record in the response
        for record in data:
            name = record.get('name')
            email = record.get('email')
            link = record.get('link')
            summary = record.get('summary')

            # Print the fetched data
            print("Name:", name)
            print("Email:", email)
            print("Link:", link)
            print("Summary:", summary)
            print()
    else:
        # Handle non-array response
        print("Invalid response format. Expected an array.")

except requests.exceptions.RequestException as e:
    print('Error occurred:', e)
