import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    # GET request - fetch posts
    def fetch_posts(self, limit=5):
        response = requests.get(f"{self.base_url}/posts")
        if response.status_code == 200:
            data = response.json()
            print("Fetched Posts:")
            for post in data[:limit]:
                print(f"{post['id']}: {post['title']}")
        else:
            print("Error fetching posts:", response.status_code)

    # POST request - create new post
    def create_post(self, title, body, user_id):
        post_data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        response = requests.post(f"{self.base_url}/posts", json=post_data)
        if response.status_code == 201:
            print("\nPost Created Successfully!")
            print(response.json())
        else:
            print("Error creating post:", response.status_code)

client = APIClient("https://jsonplaceholder.typicode.com")

# Fetch first 5 posts
client.fetch_posts()

# Create a new post
client.create_post(
    title="API Client Test",
    body="This is a post sent using my API Client class.",
    user_id=10
)
