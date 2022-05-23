from ast import Str
from sqlite3 import Date
from tokenize import String
import librosa
import re
from lxml import etree
from datetime import date, datetime
from borax.calendars.birthday import actual_age_lunar
from typing import *
from borax.calendars.lunardate import LunarDate
from borax.calendars.festivals2 import LunarFestival, Period
import requests
from traitlets import Bool



def cut(obj: str, sec: int=40) -> list:
    """cut the string into list

    Args:
        obj (str): text need to be cut
        sec (int, optional): words count. Defaults to 40.

    Returns:
        list: list of words
    """
    obj.strip()
    str_list = [obj[i:i+sec] for i in range(0,len(obj),sec)]
    print(str_list)
    return str_list

def get_duration(file_path: str) -> float:
    """get duration of mp3 file

    Args:
        file_path (str): mp3 file path

    Returns:
        float: duration of mp3 file
    """
    duration = librosa.get_duration(filename=file_path)
    return duration

def deal_text(text: str) -> str:
    """deal the text

    Args:
        text (str): text need to be deal

    Returns:
        str: deal text
    """
    # text = "    "+text
    text = text.replace("。","。\n")
    text = text.replace("？","？\n")
    text = text.replace("！","！\n")
    text = text.replace("；","；\n")
    return text

def get_web_text() -> list:
    """Get random text from web

    Returns:
        list: article title and content
    """
    ans = []
    url = "https://meiriyiwen.com/random"
    res = requests.get(url=url)
    html = res.text
    root = etree.HTML(html)
    title = root.xpath('//*[@id="article_show"]/h1/text()')[0]
    # print(title)
    ans.append(title)
    content = root.xpath('//*[@id="article_show"]/div[1]/p')
    for item in content:
        text = item.text
        # print(text)
        text = text.replace('\r','')
        text = text.replace('\n','')
        ans.append(text)
    return ans

def get_actual_age_lunar(birthday: Tuple[int,int,int]) -> int:
    """Get actual age of lunar

    Args:
        year (int): year
        month (int): month
        day (int): day

    Returns:
        int: actual age of lunar
    """
    birthday = date(birthday[0],birthday[1],birthday[2])
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    res = actual_age_lunar(birthday, today=date(year,month,day))
    return res


def get_birthday_date_this_year(birthday: Tuple[int, int, int], leap_day_included: Bool=True) -> list:
    solar_birth = date(birthday[0], birthday[1], birthday[2])
    lunar_birth = LunarDate.from_solar(solar_birth) # 出生那天的农历日期
    # print(lunar_birth)  

    # 农历生日对应的节日对象
    lunar_birth_festival = LunarFestival(month=lunar_birth.month, day=lunar_birth.day)

    wd_list = lunar_birth_festival.list_days(*Period.lunar_year(datetime.now().year))

    if not leap_day_included:
        wd_list = [wd for wd in wd_list if wd.lunar.leap == 0] # 去掉其中的闰月日期

    res = []

    for _date in wd_list:
        # print(_date.solar, _date.lunar.cn_str())
        res.append([_date.solar, _date.lunar.cn_str()])
    # print(wd_list)
    return res

if __name__ == "__main__":
    birthday = (1997, 6, 24)
    age = get_actual_age_lunar(birthday)
    ans = get_birthday_date_this_year(birthday)
    print(age)
    for item in ans:
        print(item)