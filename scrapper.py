from bs4 import BeautifulSoup
import requests
import re
import os
from tqdm import *

def parse_page(run_result="CE", page_num=1):
    pass

def parse_submission(suburl):
    base_sub_url = 'https://atcoder.jp'
    h = requests.get(base_sub_url + suburl).text
    soup = BeautifulSoup(h, 'html.parser')
    src = soup.find_all(class_='prettyprint')[0].get_text()
    return src

base_ce_url = 'https://atcoder.jp/contests/abs/submissions?f.Language=3016&f.Status=AC&f.Task=&f.User=&page='

CE_DIR = "C:/Users/admin/repo_for_lm/cf_java/NCE"

cnt = 0

for i in trange(1, 112):

    h = requests.get(base_ce_url + '1').text
    soup = BeautifulSoup(h, 'html.parser')

    for link in soup.find_all('a'):
        x = link.get('href')
        try:
            if "submissions/" in x and not 'me' in x:
                src = parse_submission(x)
                cnt += 1
                with open(os.path.join(CE_DIR, str(cnt) + '.java'), 'w', encoding='utf8') as f:
                    f.write(src)

        except TypeError as e:
            pass
