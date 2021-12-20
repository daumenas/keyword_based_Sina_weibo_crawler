import requests
import re
 # Construct Search Content
# f = open("./data/nba.txt", "w+")
for i in range(1,200):
    data = {
         'containerid': '100103type=1&q=#nba',
        'page_type':'searchall',
        'page':i,
    }

     #    ,
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',}

    url = "https://m.weibo.cn/api/container/getIndex?"
     #
    html = requests.get(url,headers=headers,params=data)
     #    , if 200, the access is successful
    if html.content:
        response = html.json()
        cards = response["data"]["cards"]
        with open("./data/nba.txt", "w", encoding="utf-8") as f:
            f.write(str(cards))
        # print(cards)
        result = []
         # Traversing a list of Cards
        # for card in cards:
        #          # "MBLOG" button exists in this dictionary
        #     mblogs = "mblog"
        #     if mblogs in card:
        #         print(card[mblogs])
        #                  #Extach the text content
        #         text = card[mblogs]["text"]
        #                  # Extract the body, remove the HTML tag using regular expressions
        #                  # RE.Compile regular expression character string creation mode object, Re.s makes all characters, matching, including wire walking
        #         dr = re.compile(r'<[^>]+>',re.S)
        #                  # Save the data in the form of a dictionary in the list
        #         result.append({
        #              'Publish Time': card[mblogs]["created_at"],
        #              'User ID': card[mblogs]["user"]["id"],
        #              'Comment number': card[mblogs]["comments_count"]})
        #         f.write(str(result))
        #         print(result)

# f.close()