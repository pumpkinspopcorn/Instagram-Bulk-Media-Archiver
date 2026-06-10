import json

urls = []

with open("saved_posts.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    try:
        url = item["string_map_data"]["Saved on"]["href"]
        urls.append(url)
    except:
        pass

with open("urls.txt", "w", encoding="utf-8") as f:
    for url in urls:
        f.write(url + "\n")

print(f"Extracted {len(urls)} URLs")
