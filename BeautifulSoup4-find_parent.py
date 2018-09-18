# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:01:47 2018

@author: danieltseng
"""


# 前面介紹的 find_all 都是向下搜尋子節點. 如果需要向上搜尋父節點的話，
# 可以改用 find_parents 函數（或是 find_parent），
# 它可讓我們以某個特定節點為起始點，向上搜尋父節點：

html_doc = """
<body>
    <p class="my_par">
        <a id="link1" href="/my_link1">Link 1</a>
        <a id="link2" href="/my_link2">Link 2</a>
        <a id="link3" href="/my_link3">Link 3</a>
        <a id="link3" href="/my_link4">Link 4</a>
    </p>
</body>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
link2_tag = soup.find(id="link2")

# 往上層尋找 p 節點
p_tag = link2_tag.find_parents("p")
print(p_tag)



# 如果想要在在同一層往前尋找特定節點，則可用 find_previous_siblings 函數
#（或是 find_previous_sibling）
link_tag = link2_tag.find_previous_siblings("a")
print(link_tag)


# 如果想要在在同一層往後尋找特定節點，則可用 find_next_siblings 函數
#（或是 find_next_sibling）
link_tag = link2_tag.find_next_siblings("a")
print(link_tag)