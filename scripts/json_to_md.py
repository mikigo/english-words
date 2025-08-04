import json
import os

from scripts.groups import GROUPS

new_md_index = [i * 100 for i in range(1, 200)]

for root, dirs, files in os.walk("../books"):
    for i in files:

        with open(f"{root}/{i}", "r", encoding="utf-8") as f:
            lines = f.readlines()

        g = None
        for group in GROUPS:
            if i.startswith(group):
                g = group
                break
        else:
            continue
        if g is None:
            raise ValueError

        if not os.path.exists(f"../docs/{g}"):
            os.mkdir(f"../docs/{g}")

        md_name = f"{os.path.splitext(i)[0]}_1.md"

        for index, line in enumerate(lines):
            if index + 1 in new_md_index:
                md_name = f"{os.path.splitext(i)[0]}_{index + 1}.md"
            md_dir = f"../docs/{g}/{os.path.splitext(i)[0]}"

            if not os.path.exists(md_dir):
                os.mkdir(md_dir)

            if index == 0 or index + 1 in new_md_index:
                if os.path.exists(f"{md_dir}/{md_name}"):
                    os.remove(f"{md_dir}/{md_name}")

            with open(f"{md_dir}/{md_name}", "a+", encoding="utf-8") as mdf:
                if index == 0 or index + 1 in new_md_index:
                    mdf.write(f"# {os.path.splitext(md_name)[0]}\n\n")

                line = line.strip()
                if not line.startswith("{"):
                    continue

                json_data = json.loads(line)
                wordRank: int = json_data.get("wordRank")
                wordHead: str = json_data.get("headWord")
                content: dict = json_data.get("content").get("word").get("content")
                mdf.write(f"## {wordRank}. {wordHead}\n\n")

                # 翻译
                trans: list = content.get("trans")
                phone = content.get("phone")
                for t in trans:
                    # mdf.write(f"**{t.get('descCn')}**\n\n")
                    mdf.write(f"{f'`{phone}`  ' if phone else ''}**{t.get('tranCn')}**\n\n")
                    # if t.get('descOther'):
                    #     mdf.write(f"**{t.get('descOther')}**\n\n")
                    #     mdf.write(f"{t.get('tranOther')}\n\n")

                # 短语
                phrase: dict = content.get("phrase")
                if phrase:
                    mdf.write(f":::tip{{title=🤩{phrase.get('desc')}}}\n\n")
                    # mdf.write(f"> [!TIP]\n>\n")
                    for p in phrase.get('phrases'):
                        pCn = p.get('pCn')
                        pContent = p.get('pContent')
                        mdf.write(f"- {pContent} （{pCn}）\n\n")
                        # mdf.write(f"> - {pContent} （{pCn}）\n>\n")
                    mdf.write(f":::\n\n")
                    # mdf.write("\n")

                # 例句
                sentence: dict = content.get("sentence")
                if sentence:
                    mdf.write(f":::note{{title=🎤{sentence.get('desc')}}}\n\n")
                    # mdf.write(f"> [!NOTE]\n>\n")
                    for s in sentence.get('sentences'):
                        mdf.write(f"- {s.get('sContent')} （{s.get('sCn')}）\n\n")
                        # mdf.write(f"> - {s.get('sContent')} （{s.get('sCn')}）\n>\n")
                    mdf.write(f":::\n\n")
                    # mdf.write("\n")

                # 同义词
                syno: dict = content.get("syno")
                if syno:
                    mdf.write(f":::warning{{title=🤔同义词}}\n\n")
                    # mdf.write(f"> [!WARNING]\n>\n")
                    for s in syno.get('synos'):
                        hwds = s.get('hwds')
                        l = []
                        for h in hwds:
                            l.append(h.get('w'))
                        l = ", ".join(l)
                        l += f" （{s.get('tran')}）"
                        mdf.write(f"- {l}\n\n")
                        # mdf.write(f"> - {l}\n>\n")
                    mdf.write("\n")
