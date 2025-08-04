import os
import shutil
import subprocess

def main():
    # 配置路径和排除规则
    os.chdir('..')
    doc_build_dir = os.path.join(os.getcwd(), 'doc_build')
    exclude_pattern = os.path.join('static', 'search_index.*.json')

    # 检查doc_build目录是否存在
    if not os.path.isdir(doc_build_dir):
        print("错误: doc_build目录不存在")
        return

    # 获取当前分支用于后续恢复
    current_branch = subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
        text=True
    ).strip()

    try:
        # 切换到gh-pages分支并拉取最新代码
        subprocess.run(['git', 'checkout', 'gh-pages'], check=True)
        subprocess.run(['git', 'pull', 'origin', 'gh-pages'], check=True)

        # 清理现有文件（保留.git、.nojekyll、node_modules和doc_build）
        for item in os.listdir('.'):
            if item in ('.git', '.nojekyll', 'node_modules', 'doc_build'):
                continue
            item_path = os.path.join(os.getcwd(), item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            else:
                shutil.rmtree(item_path)

        # 定义文件排除函数
        def ignore_files(src, names):
            if os.path.basename(src) == 'static':
                return [name for name in names if name.startswith('search_index.') and name.endswith('.json')]
            return []

        # 复制doc_build内容（排除指定文件）
        shutil.copytree(
            doc_build_dir,
            '.',
            ignore=ignore_files,
            dirs_exist_ok=True
        )

        # 确保.nojekyll文件存在
        if not os.path.exists('.nojekyll'):
            with open('.nojekyll', 'w') as f:
                pass

        # 提交更改
        subprocess.run(['git', 'add', '.'], check=True)
        try:
            subprocess.run([
                'git', 'commit', '-m', 'Update documentation from doc_build'
            ], check=True)
            print("更改已成功提交")
        except subprocess.CalledProcessError:
            print("没有需要提交的更改")
            return

        # 推送到远程gh-pages分支
        subprocess.run(['git', 'push', 'origin', 'gh-pages'], check=True)
        print("成功推送到gh-pages分支")

    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 恢复到原始分支
        if current_branch != 'gh-pages':
            subprocess.run(['git', 'checkout', current_branch], check=True)

if __name__ == "__main__":
    main()