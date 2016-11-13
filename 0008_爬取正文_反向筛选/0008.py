#!/usr/bin/env pyhton3
#get the text in a html file
# coding: utf-8
# 在 python 3 下运行

import re, urllib.request

def get_text(url):
    content = url.read()
    try:
        content = content.decode('utf-8')
    except:
        content = content.decode('gbk')

    content = re.sub(r'<script.+?</script>', '', content, flags = re.DOTALL)
    content = re.sub(r'<!--.+?-->', '', content, flags = re.DOTALL)
    content = re.sub(r'<style.+?</style>', '', content, flags = re.DOTALL)
    content = re.sub(r'<[^>]*>', '', content)
    content = re.sub(r'\n', '', content)

    print(content)

def main():
    with urllib.request.urlopen('http://www.baidu.com') as url:
        get_text(url)

if __name__ == '__main__':
    main()
