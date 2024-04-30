import requests

IAM_TOKEN = '<IAM_TOKEN>'
folder_id = '<folder>'
target_language = 'ru'
sourse_language = 'en'

path = './folder_div10000'
res_path = './folder_res'

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {0}".format(IAM_TOKEN)
}

for i in range(0, 300):
    with open(path + f'/{i}.txt', 'r') as f:
        n = int(f.read())
    for j in range(n):
        with open(path + f'/{i}_{j}.txt', 'r') as f:
            txt = f.read()
            texts = [txt]
            body = {
                        "sourceLanguageCode": sourse_language,
                        "targetLanguageCode": target_language,
                        "texts": texts,
                        "folderId": folder_id,
                    }
            response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                        json = body,
                                        headers = headers
                                    )
            with open(res_path + f'/{i}_{j}.txt', 'w') as f:
                f.write(response.text)