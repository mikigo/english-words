# from scripts.groups import GROUPS
# lst = [{
#     "text": "首页",
#     "link": "/index",
#     "activeMatch": "/index/"
#   }]
# for g in GROUPS:
#     lst.append(
#         {
#             "text": g,
#             "link": f"/{g}/index",
#             "activeMatch": "/index/"
#         }
#     )
#
# import json
# print(json.dumps(lst, ensure_ascii=False, indent=2))
import os

for dir in os.listdir("../docs"):
    if dir == "public":
        continue
    if os.path.isfile(f"../docs/{dir}"):
        continue
    lst = [
        {
            "type": "file",
            "name": "index",
            "label": "章节预览"
        }
    ]

    for i in os.listdir(f"../docs/{dir}"):
        if os.path.isfile(f"../docs/{dir}/{i}"):
            continue
        lst.append({
            "type": "dir",
            "name": i,
            "label": i,
            "collapsed": True,
            "overviewHeaders": "[1]"
        })
    with open(f"../docs/{dir}/_meta.json", "w", encoding="utf-8") as f:
        import json
        json.dump(lst, f, ensure_ascii=False, indent=2)




