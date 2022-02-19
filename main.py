from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://web.archive.org/web/20200518073855/"
#                         "https://www.empireonline.com/movies/features/best-movies-2/")
# response.raise_for_status()
# data = response.text
#
# with open("data.txt", "w") as f:
#     f.write(data)

with open("data.txt", "r") as f:
    data = f.read()

soup = BeautifulSoup(data, "html.parser")

titles = soup.find_all(name="h3", class_="title")
titles = [title.text for title in titles]
titles = titles[::-1]
longest = len(max(titles, key=len))

with open("movies.txt", "a", encoding="utf-8") as f:
    f.write(f"{longest * '*'}\n"
            f"Empire's 100 Greatest Movies Of All Time\n"
            f"{longest * '*'}\n")
    for title in titles:
        f.write(f"{title}\n")
    print("Done!")
