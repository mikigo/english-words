from scripts.groups import GROUPS
list = [{
    "type": "file",
    "name": "index",
    "label": "英语"
  }]
for g in GROUPS:
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