from bs4 import BeautifulSoup
import requests
# with open("website.html") as file:
#     data = file.read()
#
# soup = BeautifulSoup(data, "html.parser")
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.get("href"))
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
article_texts = []
article_lists = []
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all("a", class_="titlelink")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    list = article_tag.get("href")
    article_lists.append(list)
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]
# print(article_texts)
# print(article_lists)
# print(article_upvote)
maximum_number = max(article_upvote)
maximum_index = article_upvote.index(maximum_number)

print(article_texts[maximum_index])
print(article_lists[maximum_index])