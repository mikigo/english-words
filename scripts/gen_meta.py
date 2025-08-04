from scripts.groups import GROUPS
lst = [{
    "type": "file",
    "name": "index",
    "label": "英语"
  }]
for g in GROUPS:
    lst.append(
        {
            "type": "dir",
            "name": g,
            "label": g,
            "collapsed": "true",
            "overviewHeaders": "[1]"
        }
    )

import json
print(json.dumps(lst, ensure_ascii=False, indent=2))