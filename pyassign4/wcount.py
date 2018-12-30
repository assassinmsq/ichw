{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"wcount.py: count words from an Internet file.\n",
    "\n",
    "__author__ = \"Ma Siqi\"\n",
    "__pkuid__  = \"1800011760\"\n",
    "__email__  = \"1800011760@pku.edu.cn\"\n",
    "\"\"\"\n",
    "\n",
    "import sys\n",
    "from urllib.request import urlopen\n",
    "import collections\n",
    "import re\n",
    "\n",
    "def wcount(lines, topn=10):\n",
    "    \"\"\"count words from lines of text string, then sort by their counts \n",
    "    in reverse order, output the topn (word count), each in one line.\n",
    "    \"\"\"\n",
    "    doc = urlopen(lines)\n",
    "    docstr = doc.read()\n",
    "    doc.close()\n",
    "    Txt = docstr.decode()\n",
    "    # 得到文本字符串\n",
    "    txt = Txt.lower()\n",
    "    # 全部小写\n",
    "    t = re.sub(\"[\\s+\\.\\!\\/_,$%^*(+\\\"\\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+\", \"\",txt)\n",
    "    # 去除标点符号\n",
    "    lst = txt.split()\n",
    "    n = collections.Counter(lst)\n",
    "    # 统计每个单词的频率\n",
    "    res = sorted(n.items(),key = lambda ky:ky[1], reverse = True)\n",
    "    # 按频率降序排列\n",
    "    print(res)\n",
    "    for z,b in res:\n",
    "        print(z,b)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    if  len(sys.argv) == 1:\n",
    "        print('Usage: {} url [topn]'.format(sys.argv[0]))\n",
    "        print('  url: URL of the txt file to analyze ')\n",
    "        print('  topn: how many (words count) to output. If not given, will output top 10 words')\n",
    "        sys.exit(1)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
