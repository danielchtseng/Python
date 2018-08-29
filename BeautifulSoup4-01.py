# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:01:47 2018

@author: danieltseng
"""


# 原始 HTML 程式碼

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

# 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
#print(soup.get_text())


# 網頁標題 HTML 標籤
title_tag = soup.title
#print(title_tag)
# 網頁的標題文字
#print(title_tag.string)


# 以 find 搜尋標籤
#a_tags = soup.find_all('a')
#for tag in a_tags:
  # 輸出超連結的文字
#  print(tag.string)
  # 輸出超連結網址
#  print(tag.get('href'))

  
# 搜尋所有超連結與粗體字
#tags = soup.find_all(["a", "b"])
#print(tags)  
# 限制搜尋結果數量
#tags = soup.find_all(["a", "b"], limit=2)
#print(tags)

#tags = soup.find(id="link1")
#print(tags)



# 前面介紹的 find_all 都是向下搜尋子節點. 如果需要向上搜尋父節點的話，
# 可以改用 find_parents 函數（或是 find_parent），
# 它可讓我們以某個特定節點為起始點，向上搜尋父節點：

  