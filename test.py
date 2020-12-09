import re
from hashlib import md5
import nbformat
import pickle

def read_ipynb_file(file_path):
    with open(file_path) as file:
        out = str(nbformat.read(file_path, as_version=4))
    return out

path = 'question/EDA_question.ipynb'

out = read_ipynb_file(path)

ws_std = re.findall(r'ws_std\s*=\s* \d*[.,]?\d*', out)[0].replace(' ', '')
p_range = re.findall(r'p_range\s*=\s*\d*[.,]?\d*', out)[0].replace(' ', '')
corr = re.findall(r'corr\s*=\s* \d*[.,]?\d*', out)[0].replace(' ', '')
dew_month = re.findall(r'dew_month\s*=\s* \d*[.,]?\d*', out)[0].replace(' ', '')
max_gust_value =  re.findall(r'max_gust_value\s*=\s* \d*[.,]?\d*', out)[0].replace(' ', '')
max_gust_month =  re.findall(r'max_gust_month\s*=\s* \d*[.,]?\d*', out)[0].replace(' ', '')
avg_temp =  re.findall(r'avg_temp\s*=\s* \d*[.,]?\d*', out)[0].replace(' ', '')
temp_range =  re.findall(r'temp_range\s*=\s* \d*[.,]?\d*', out)[0].replace(' ', '')
max_p_range_day =  re.findall(r'max_p_range_day\s*=\s*\'\d*[-,]?\d*[-,]?\d*\'', out)[0].replace(' ', '').replace("'", "")
median_b_days = re.findall(r'median_b_days\s*=\s* \d*[.,]?\d*', out)[0].replace(' ', '')
num_days_std = re.findall(r'num_days_std\s*=\s* \d*[.,]?\d*', out)[0].replace(' ', '')

variables = ["ws_std", "p_range", "corr", "dew_month", "max_gust_month", "max_gust_value", "avg_temp", "temp_range", "max_p_range_day", "num_days_std", "median_b_days"]
answers = [ws_std, p_range, corr, dew_month, max_gust_month, max_gust_value, avg_temp, temp_range, max_p_range_day, num_days_std, median_b_days]

answer_dict = dict()

for var, ans in zip(variables, answers):
    answer_dict[var] = md5(str.encode(ans)).hexdigest()

with open('test_files/hash.pk', 'rb') as file:
    hash_dict = pickle.load(file)


def test_ws_std():
    assert hash_dict["ws_std"] == answer_dict["ws_std"]

def test_p_range():
    assert hash_dict["p_range"] == answer_dict["p_range"]
    
def test_corr():
    assert hash_dict["corr"] == answer_dict["corr"]

def test_dew_month():
    assert hash_dict["dew_month"] == answer_dict["dew_month"]

def test_max_gust_month():
    assert hash_dict["max_gust_month"] == answer_dict["max_gust_month"]

def test_max_gust_value():
    assert hash_dict["max_gust_value"] == answer_dict["max_gust_value"]

def test_avg_temp():
    assert hash_dict["avg_temp"] == answer_dict["avg_temp"]

def test_temp_range():
    assert hash_dict["temp_range"] == answer_dict["temp_range"]

def test_max_p_range_day():
    assert hash_dict["max_p_range_day"] == answer_dict["max_p_range_day"]

def test_num_days_std():
    assert hash_dict["num_days_std"] == answer_dict["num_days_std"]

def test_median_b_days():
    assert hash_dict["median_b_days"] == answer_dict["median_b_days"]
