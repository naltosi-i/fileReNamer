import os

'''
This is file name renamer.
You can edit any file-names, 
editting with to delete or append or replace.
'''

pathBefore = '' # 変更前ファイルpath
pathAfter = '' # 変更後ファイルpath

mode = 0 # 1 = 削除, 2 = 追記, 3 = 置換
sides = 0 # 1 = 左, 2 = 右

delStrLen = 0 # 削除文字数
addStrLen = 0 # 追記文字数
addStr = '' # 追記文字列

searchDir = 0 # 1 = ディレクトリ内のすべてのファイルを検索
keyword = '' # ディレクトリ内検索キーワード (Ex. 拡張子など)

