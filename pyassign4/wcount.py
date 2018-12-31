"""wcount.py: count words from an Internet file.

__author__ = "Ma Siqi"
__pkuid__  = "1800011760"
__email__  = "1800011760@pku.edu.cn"
"""


import sys
from urllib.request import urlopen
from urllib import error
import collections
import re


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts 
    in reverse order, output the topn (word count), each in one line.
    """
    doc = urlopen(lines)
    docstr = doc.read()
    doc.close()
    Txt = docstr.decode()
    # 得到文本字符串
    txt = Txt.lower()
    # 全部小写
    t = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+;:"," ",txt)
    # 去除标点符号
    lst = t.split()
    n = collections.Counter(lst)
    # 统计每个单词的频率
    res = sorted(n.items(),key = lambda ky:ky[1], reverse = True)
    # 按频率降序排列
    if int(topn) > len(res):
        for i in res:
            print(i[0],i[1])
    else:
        for i in range(topn):
            print(res[i][0],res[i][1])
    

if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    elif len(sys.argv) == 2:
        try:
            wcount(sys.argv[1])
        except error.URLError as e:
            print(e.reason)
    elif len(sys.argv) == 3:
        try:
            wcount(sys.argv[1],int(sys.argv[2]))
        except error.URLError as e:
            print(e.reason)
