import os
import shutil
import subprocess
from pathlib import Path


def commit_to_gh_pages():
    # 确保 doc_build 目录存在
    os.chdir("..")
    doc_build_dir = Path("doc_build")
    if not doc_build_dir.exists():
        print("❌ Error: doc_build directory not found!")
        return

    # 检查是否在 Git 仓库中
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("❌ Error: Not in a Git repository!")
        return

    # 获取当前分支
    current_branch = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        check=True,
        capture_output=True,
        text=True
    ).stdout.strip()

    print(f"Current branch: {current_branch}")

    # 切换到 gh-pages 分支（如果不存在则创建）
    try:
        subprocess.run(["git", "checkout", "gh-pages"], check=True)
    except subprocess.CalledProcessError:
        print("Creating new gh-pages branch...")
        subprocess.run(["git", "checkout", "--orphan", "gh-pages"], check=True)
        subprocess.run(["git", "rm", "-rf", "."], check=True)

    # 清空 gh-pages 分支（保留 .git 目录）
    for item in os.listdir("."):
        if item == ".git":
            continue
        if os.path.isdir(item):
            shutil.rmtree(item)
        else:
            os.remove(item)

    # 复制 doc_build 内容到当前目录
    for item in doc_build_dir.glob("*"):
        if item.name == ".git":
            continue
        dest = Path(".") / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)

    # 提交更改
    subprocess.run(["git", "add", "."], check=True)
    try:
        subprocess.run(["git", "commit", "-m", "Deploy docs to gh-pages"], check=True)
    except subprocess.CalledProcessError:
        print("No changes to commit.")

    # 推送到远程 gh-pages 分支
    subprocess.run(["git", "push", "origin", "gh-pages"], check=True)
    print("✅ Successfully deployed to gh-pages branch!")

    # 切换回原分支
    subprocess.run(["git", "checkout", current_branch], check=True)


if __name__ == "__main__":
    commit_to_gh_pages()