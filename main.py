
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