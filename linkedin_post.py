import requests

access_token = '787gud6kvmp0zp'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'X-Restli-Protocol-Version': '2.0.0'
}

me = requests.get('https://api.linkedin.com/v2/me', headers=headers).json()
urn = me['id']

post_text = """
🚀 Project control isn’t optional—it's critical for success.

Whether using Primavera, Power BI, or Agile—master the process and you master the outcome.

#ProjectManagement #PMO #Construction #KPI
"""

post_data = {
  "author": f"urn:li:person:{urn}",
  "lifecycleState": "PUBLISHED",
  "specificContent": {
    "com.linkedin.ugc.ShareContent": {
      "shareCommentary": {
        "text": post_text
      },
      "shareMediaCategory": "NONE"
    }
  },
  "visibility": {
    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
  }
}

response = requests.post('https://api.linkedin.com/v2/ugcPosts', headers=headers, json=post_data)

if response.status_code == 201:
    print("✅ Post published successfully!")
else:
    print("❌ Error:", response.status_code, response.text)