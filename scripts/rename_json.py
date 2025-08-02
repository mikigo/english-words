import json
import os
import shutil

from .groups import groups

with open("../bookLists.txt", "r", encoding="utf-8") as f:
    txt = json.load(f)

books = txt.get("data").get("normalBooksInfo")


for j in os.listdir("../jsons"):

    for book in books:
        id = book.get("id")
        title: str = book.get("title")
        for g in groups:
            if title.startswith(g):
                os.makedirs(f"../books/{g}", exist_ok=True)
                if j == f"{id}.json":
                    shutil.copy(f"../jsons/{j}", f"../books/{g}/{title}.json")
