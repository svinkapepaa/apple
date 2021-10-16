
#Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9
# $ git config -- global user.name "Komiljonov Uba"
# fatal: not in a git directory

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9
# $ git config --global user.name "Komiljonov Uba"

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9
# $ git config --global user.email "vsyodlyadelaubaydulloha@gmail.com"

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9
# $ git init
# Initialized empty Git repository in C:/Users/user/Desktop/m3l9/.git/

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git add -A

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git status
# On branch master

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (first)
# $ py main.py
# 0

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (first)
# $ py main.py
# 11

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (first)
# $ git add -A

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (first)
# $ git commit -m 'first change'
# [first 9af3f1f] first change
#  3 files changed, 111 insertions(+), 7 deletions(-)
#  delete mode 100644 desktop.ini
#  create mode 100644 result.txt

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (first)
# $ git checkout master
# Switched to branch 'master'

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git checkout 'first'
# Switched to branch 'first'

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (first)
# $ git checkout 'master'
# Switched to branch 'master'

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git merge first
# Updating 997576c..9af3f1f
# Fast-forward
#  desktop.ini |   6 ----
#  main.py     | 111 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
#  result.txt  |   1 +
#  3 files changed, 111 insertions(+), 7 deletions(-)
#  delete mode 100644 desktop.ini
#  create mode 100644 result.txt

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git branch
#   first
# * master


# No commits yet

# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#         new file:   desktop.ini
#         new file:   main.py


# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git commit -m "birinchi save"
# [master (root-commit) a6b3bf3] birinchi save
#  2 files changed, 6 insertions(+)
#  create mode 100644 desktop.ini
#  create mode 100644 main.py

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git log
# commit a6b3bf3396ea4c7aacfe326910fdde83f1f07c03 (HEAD -> master)
# Author: Komiljonov Uba <vsyodlyadelaubaydulloha@gmail.com>
# Date:   Sat Oct 16 16:28:34 2021 +0300

#     birinchi save

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git reset --hard a6b3bf
# HEAD is now at a6b3bf3 birinchi save

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ py main.py
# 11

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git add -A

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git commit -m 'first step'
# [master 997576c] first step
#  2 files changed, 4 insertions(+)
#  create mode 100644 test.txt

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git log
# commit 997576cd527509ee2822831243de896dcc64f253 (HEAD -> master)
# Author: Komiljonov Uba <vsyodlyadelaubaydulloha@gmail.com>
# Date:   Sat Oct 16 16:43:29 2021 +0300

#     first step

# commit a6b3bf3396ea4c7aacfe326910fdde83f1f07c03
# Author: Komiljonov Uba <vsyodlyadelaubaydulloha@gmail.com>
# Date:   Sat Oct 16 16:28:34 2021 +0300

#     birinchi save

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git log -p -1
# commit 997576cd527509ee2822831243de896dcc64f253 (HEAD -> master)
# Author: Komiljonov Uba <vsyodlyadelaubaydulloha@gmail.com>
# Date:   Sat Oct 16 16:43:29 2021 +0300

#     first step

# diff --git a/main.py b/main.py
# index e69de29..d580c33 100644
# --- a/main.py
# +++ b/main.py
# @@ -0,0 +1,3 @@
# +file = open('test.txt', 'r')
# +result = file.read()
# +print(len(result))
# \ No newline at end of file
# diff --git a/test.txt b/test.txt
# new file mode 100644
# index 0000000..70c379b
# --- /dev/null
# +++ b/test.txt
# @@ -0,0 +1 @@
# +Hello world
# \ No newline at end of file

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $
# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git brench -D first
# git: 'brench' is not a git command. See 'git --help'.

# The most similar command is
#         branch

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git branch
#   first
# * master

# Убайдуллох@Lenovo MINGW32 ~/Desktop/m3l9 (master)
# $ git branch -D first
# Deleted branch first (was 9af3f1f).

file = open('test.txt', 'r')
result = file.read()
print(len(result))
with open ('result.txt' , 'w') as f:
    f.write(f"text.txt:{len(result)}")
