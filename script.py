import requests

API_TOKEN = 'e5486a11c12b2031b7b498be20e0644d'
ROOM_ID = '384510253'  # 送りたいチャットルームのID
MESSAGE = '【お知らせ】私のメッセージが通ります。'

headers = {
    'X-ChatWorkToken': API_TOKEN
}

payload = {
    'body': MESSAGE
}

response = requests.post(
    f'https://api.chatwork.com/v2/rooms/{ROOM_ID}/messages',
    headers=headers,
    data=payload
)

if response.status_code == 200:
    print('✅ メッセージ送信成功！')
else:
    print(f'❌ エラー: {response.status_code}')
    print(response.text)