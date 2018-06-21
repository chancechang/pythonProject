from util import *
from bs4 import BeautifulSoup
import threading
from log import info_logger


def get_article_list(url):
    req = build_request(url)
    res_text = req.text
    table = BeautifulSoup(res_text, 'lxml').find(
        'div', id='articlelistnew').find_all('div', {'class': 'articleh'})
    result = []
    for item in table:
        try:
            l3 = item.find('span', {'class': 'l3'})
            try:
                hinfo = item.find('em').get_text()
                if hinfo in ['新闻', '大赛', '公告', '研报']:
                    continue
            except:
                pass
            title = l3.find('a').get_text()
            url = l3.find('a').get('href')
            pub_date = item.find('span', {'class': 'l6'}).get_text()
            result.append([title, url, pub_date])
        except:
            continue
    return result


class GubaArticleList(threading.Thread):
    def __init__(self, base_info):
        super(GubaArticleList, self).__init__()
        self.base_info = base_info
        self.result = []
        self.code = base_info[-1]
        self.failed_url = []
        self.daemon = True

    def run(self):
        current_year = 2018
        pre_list = []
        page = 1
        year_state = 0
        while True:
            url = 'http://guba.eastmoney.com/list,{},f_{}.html'.format(
                self.code, page)
            try:
                art_list = get_article_list(url)
            except Exception as e:
                info_logger.error('Error:%s' % (e) + str(self.base_info) +
                                  '\tPage:%s\tcurrent_year:%s\turl:%s' % (page, current_year, url))
                self.failed_url.append([self.base_info,url, year_state, current_year, str(e)])
                break
            if art_list == pre_list:
                break
            pre_list = art_list
            for item in art_list:
                pub_date = item[-1]
                if current_year == 2014 and '07-' in pub_date:
                    return
                if '01-' in pub_date:
                    year_state = 1
                if '12-' in pub_date and year_state == 1:
                    year_state = 0
                    current_year = current_year - 1
                self.result.append(self.base_info + item +
                                   ['%s-%s' % (current_year, pub_date)])
            info_logger.info(str(
                self.base_info) + '\tPage:%s\tcurrent_year:%s\turl:%s' % (page, current_year, url))
            if current_year < 2014:
                break
            page += 1


def load_codes():
    tasks = []
    for line in open('./files/codes.txt', 'r'):
        item = eval(line)
        tasks.append(item)
        if len(tasks) < 5:
            continue
        yield tasks
        tasks = []
    yield tasks


def crawl():
    for stock_list in load_codes():
        tasks = []
        for stock in stock_list:
            task = GubaArticleList(stock)
            tasks.append(task)
        for task in tasks:
            task.start()
        for task in tasks:
            task.join()
        for task in tasks:
            com_type = task.base_info[0]
            f = open('./result/%s.txt' % (com_type), 'a')
            for item in task.result:
                f.write(str(item) + '\n')
            f.close()

            failed = open('./result/failed.txt', 'a')
            for item in task.failed_url:
                failed.write(str(item) + '\n')
            failed.close()


if __name__ == '__main__':
    crawl()
