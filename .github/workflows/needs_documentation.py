import os
import json
from github import Github

print("Creating documentation issue...")

# Load the JSON payload of the event
with open(os.environ["GITHUB_EVENT_PATH"], "r") as f:
    event_data = json.load(f)

# Get the pull request number from the event payload
pull_number = event_data["pull_request"]["number"]
print(f"Pull request number: {pull_number}")

      
# Create a PyGithub object using the GitHub access token
g = Github(os.environ["GITHUB_TOKEN"])

# Get the repository object for the current repository
repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])

# Get the pull request object for the merged pull request
pull = repo.get_pull(int(pull_number))

# Check if the pull request has the 'needs-documentation' label
if "needs-documentation" in [label.name for label in pull.labels]:

    # Create a new issue object and add the 'documentation' label to it
    issue_title = f"Create documentation for changes in #{pull_number}"
    issue_body = f"The changes proposed in pull request #{pull_number} require documentation. Please create documentation for the changes made in this pull request."
    new_issue = repo.create_issue(title=issue_title, body=issue_body, labels=["documentation"])

    # Log a message indicating that an issue was created for the merged pull request
    print(f"Created documentation issue for pull request #{pull_number}.")
