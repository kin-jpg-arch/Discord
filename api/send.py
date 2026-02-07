import requests

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }

    data = request.json()

    webhook = data.get("webhook")
    username = data.get("username") or "Webhook Sender"
    content = data.get("content")
    image = data.get("image")
    embed_title = data.get("embed_title")
    embed_desc = data.get("embed_desc")

    payload = {
        "username": username,
        "content": content
    }

    # ===== Embed 구성 =====
    if embed_title or embed_desc or image:
        embed = {
            "title": embed_title,
            "description": embed_desc,
            "color": 0x5865F2
        }

        if image:
            embed["image"] = {"url": image}

        payload["embeds"] = [embed]

    requests.post(webhook, json=payload)

    return {
        "statusCode": 200,
        "body": "sent"
    }
