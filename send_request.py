import requests
import json
import time
import hashlib

# Request information
first_name = "Johannes"
last_name = "Valter"
email = "j.v.valter@gmail.com"
bio = "I'm highly adaptable and a quick learner. Trying to break into dev work. I really do not qualify i have no experiance in PHP, but I enjoy a challenge."
technologies = ["python", "PostgreSQL"]
timestamp = int(time.time())
signature_input = str(timestamp) + "credy"
signature = hashlib.sha1(signature_input.encode()).hexdigest()
vcs_uri = "https://github.com/illov/need-job"

# Define the data payload
payload = {
    "first_name": first_name,
    "last_name": last_name,
    "email": email,
    "bio": bio,
    "technologies": technologies,
    "timestamp": timestamp,
    "signature": signature,
    "vcs_uri": vcs_uri
}

# Convert payload to JSONx format
jsonx_payload = json.dumps(payload)

# Send the POST request
url = "https://cv.microservices.credy.com/v1"
headers = {'Content-Type': 'application/jsonx'}
response = requests.post(url, data=jsonx_payload, headers=headers)

# Print the response
print(response.status_code)
print(response.text)
