import os
import requests
import json

# Mastodon instance URL and access token
instance_url = "MASTODON_INSTANCE"
access_token = "MASTODON_ACCESS_TOKEN"

# Create a directory to store the backup
backup_directory = "mastodon_backup"
if not os.path.exists(backup_directory):
    os.makedirs(backup_directory)

# Get the account's toots
account_id = "MASTODON_ACCOUNT_ID"
toots_url = f"{instance_url}/api/v1/accounts/{account_id}/statuses"
headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(toots_url, headers=headers)
toots = response.json()

# Save each toot as a separate JSON file
for index, toot in enumerate(toots):
    toot_filename = os.path.join(backup_directory, f"toot_{index}.json")
    with open(toot_filename, "w") as file:
        json.dump(toot, file, indent=4)

print("Backup completed.")
