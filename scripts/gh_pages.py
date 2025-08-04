import os
import shutil


def main():

    # 切换到上级目录
    os.chdir('..')

    # 删除搜索索引文件 - Windows版本
    for file in os.listdir('doc_build/static'):
        if file.startswith('search_index.') and file.endswith('.json'):
            os.remove(os.path.join('doc_build/static', file))

    # 克隆仓库 - 使用HTTPS协议可能更可靠
    if os.path.exists('gh-pages'):
        os.remove('gh-pages')
    os.system('git clone git@github.com:mikigo/English-Words.git -b gh-pages gh-pages')

    # 复制文件 - Windows版本
    if os.path.exists('gh-pages'):
        # 清空gh-pages目录，除了.git目录
        # 使用os.system命令清空目录
        if os.path.exists('gh-pages/.git'):
            # 保留.git目录，清空其他内容
            for item in os.listdir('gh-pages'):
                if item != '.git':
                    item_path = os.path.join('gh-pages', item)
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    else:
                        shutil.rmtree(item_path)
        else:
            # 如果没有.git目录，直接清空整个目录
            os.system("rd /s /q gh-pages\\*")  # 清空gh-pages目录
    else:
        raise FileNotFoundError("gh-pages directory does not exist.")
    # 将doc_build目录的内容复制到gh-pages目录下
    shutil.copytree('doc_build', 'gh-pages', dirs_exist_ok=True)

    # 创建.nojekyll文件
    if not os.path.exists('gh-pages/.nojekyll'):
        with open('gh-pages/.nojekyll', 'w') as f:
            pass

    # 切换到仓库目录
    os.chdir('gh-pages')

    # Git操作保持不变
    os.system('git add .')
    os.system('git commit -m "Update documentation from doc_build"')
    os.system('git push origin gh-pages')

    # 切换回原始目录，使用os.system删除临时目录
    os.chdir('..')
    os.system('rd /s /q gh-pages')


if __name__ == '__main__':
    main()