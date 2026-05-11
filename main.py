import requests
u = input("Enter Github username ")
url = f"https://api.github.com/users/{u}/events"
r = requests.get(url)
if r.status_code != 200:
    print("Error: user not found or API issue")
    exit()
events = r.json()
print("\n--- Github Activity Log ---\n")
for event in events[:10]:
    event_type = event["type"]
    repo = event["repo"]["name"]

    print(f"{event_type}-> {repo}")