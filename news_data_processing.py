import os
import re
import time

def news_category_extract(category):
    with open("sohu_news.txt", "r") as f:
    i = 0
    for line in f.readlines():
        if i % 2 == 0:
            cate = re.match(r".+http://([a-z]+)?", line.strip())
        if i % 2 != 0:
            if cate and cate.group(1) in category:
                path = os.path.join("news_data", category[cate.group(1)])
                content = line.strip()[9:-10]
                if content and len(content) > 500:
                    with open(os.path.join(path, str(i)), 'w') as f_content:
                        f_content.write(content)
        i += 1

def train_test_split(data_size=7000, test_split=0.3):
    data_size = 7000
    test_split = 0.3
    if not os.path.exists("train_test_data"):
        os.mkdir("train_test_data")
    if not os.path.exists(os.path.join("train_test_data", "train")):
        os.mkdir(os.path.join("train_test_data", "train"))
    if not os.path.exists(os.path.join("train_test_data", "test")):
        os.mkdir(os.path.join("train_test_data", "test"))
    for cate in category.values():
        src_path = os.path.join("news_data", cate)
        train_path = os.path.join("train_test_data", "train", cate)
        if not os.path.exists(train_path):
            os.mkdir(train_path)
        test_path = os.path.join("train_test_data", "test", cate)
        if not os.path.exists(test_path):
            os.mkdir(test_path)
        src_file_list = os.listdir(src_path)
        random.shuffle(src_file_list)
        i = 1
        for file in src_file_list:
            src_file = os.path.join(src_path, file)
            if os.path.isfile(src_file):
                if i > data_size:
                    break
                if i < data_size * (1-test_split):
                    shutil.copy(src_file, train_path)
                else:
                    shutil.copy(src_file, test_path)
                i += 1

if __name__ == '__main__':
    category = {
        "business": "财经",
        "sports": "体育",
        "yule": "娱乐"
    }
    if not os.path.exists("news_data"):
        os.mkdir("news_data")
    for cate in category.values():
        os.mkdir(os.path.join("news_data", cate))
    news_category_extract(category)
