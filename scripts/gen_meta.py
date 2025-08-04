from scripts.groups import GROUPS
lst = [{
    "text": "首页",
    "link": "/index",
    "activeMatch": "/index/"
  }]
for g in GROUPS:
    lst.append(
        {
            "text": g,
            "link": f"/{g}/index",
            "activeMatch": "/index/"
        }
    )

import json
print(json.dumps(lst, ensure_ascii=False, indent=2))