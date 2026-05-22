import requests

user_message = "Can you tell me about black holes in 3-4 lines"

request_message = {
    "message": user_message
}

url = "https://thakur0709.app.n8n.cloud/webhook-test/ecaa823e-e150-4bc0-948a-2d3fc6b0be06"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json())

# import requests

# user_message = "Can you tell me about black holes in 3-4 lines"

# response = requests.post(
#     "https://thakur0709.app.n8n.cloud/webhook-test/ecaa823e-e150-4bc0-948a-2d3fc6b0be06",
#     json={"message": user_message}
# )

# print("Status Code:", response.status_code)
# print("Response Text:", repr(response.text))
# print("Headers:", response.headers)