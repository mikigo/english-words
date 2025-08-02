groups = [
    "人教版小学",
    "人教版初中",
    "人教版高中",
    "四级",
    "六级",
    "考研",
    "雅思",
    "新东方",
    "专四",
    "专八",
]
list = [{
    "type": "file",
    "name": "index",
    "label": "英语"
  }]
for g in groups:
    list.append(
        {
            "type": "dir",
            "name": g,
            "label": g,
            "collapsed": "true",
            "overviewHeaders": "[1]"
        }
    )

import json
print(json.dumps(list, ensure_ascii=False, indent=2))