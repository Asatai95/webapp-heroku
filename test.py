import requests

DEVELOPER_KEY = '' # 取得したデベロッパーキー
USER_ID = '' # プロフィール情報を取得したい人のユーザID(例はよく使われるChris氏のユーザID)


# webAPIからJSONの形式の文字列の結果をもらう
def get_profile():

    # URIスキーム
    url = 'https://www.googleapis.com/plus/v1/people/' + USER_ID +'?key=' + DEVELOPER_KEY

    # webAPIからのリクエストを送信
    response = requests.get(url)

    # json に変換
    json_data = response.json()

    return json_data


if __name__ == '__main__':

    user_prof = get_profile()
    print(user_prof)
