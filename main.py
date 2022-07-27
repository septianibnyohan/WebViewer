# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
from random import choice

import requests
from fake_headers import Headers, browsers
from requests.exceptions import RequestException
from selenium import webdriver

from webviewer.basic import type_keyword
from webviewer.download_driver import *
import openpyxl

from webviewer.proxies import scrape_api

proxy = None

used_proxies = []

cwd = os.getcwd()
patched_drivers = os.path.join(cwd, 'patched_drivers')
config_path = os.path.join(cwd, 'config.json')

viewports = ['2560,1440', '1920,1080', '1440,900',
             '1536,864', '1366,768', '1280,1024', '1024,768']

def main():
    global cancel_all, proxy_list, total_proxies, proxies_from_api, threads, hash_config, futures, cpu_usage

    if category == 'r' and proxy_api:
        proxies_from_api = scrape_api(link=filename)

def main_viewer(proxy_type, proxy, position):
    header = Headers(
        browser="chrome",
        os=osname,
        headers=False
    ).generate()
    agent = header['User-Agent']

    if category == 'r' and proxy_api:
        for _ in range(20):
            proxy = choice(proxies_from_api)
            if proxy not in used_proxies:
                break
        used_proxies.append(proxy)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def update_chrome_version():
    link = 'https://gist.githubusercontent.com/MShawon/29e185038f22e6ac5eac822a1e422e9d/raw/versions.txt'

    output = requests.get(link, timeout=60).text
    chrome_versions = output.split('\n')

    browsers.chrome_ver = chrome_versions

def view_web():
    return;

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # /media/septian/General/projects/web-viewer/ref/data.xlsx
    print_hi('PyCharm')
    update_chrome_version()
    osname, exe_name = download_driver(patched_drivers=patched_drivers)

    with open(config_path, 'r', encoding='utf-8-sig') as openfile:
        config = json.load(openfile)

    api = config["http_api"]["enabled"]
    host = config["http_api"]["host"]
    port = config["http_api"]["port"]
    database = config["database"]
    views = config["views"]
    minimum = config["minimum"] / 100
    maximum = config["maximum"] / 100
    category = config["proxy"]["category"]
    proxy_type = config["proxy"]["proxy_type"]
    filename = config["proxy"]["filename"]
    auth_required = config["proxy"]["authentication"]
    proxy_api = config["proxy"]["proxy_api"]
    refresh = config["proxy"]["refresh"]
    background = config["background"]
    bandwidth = config["bandwidth"]
    playback_speed = config["playback_speed"]
    max_threads = config["max_threads"]
    min_threads = config["min_threads"]

    xlsx_file = "data.xlsx"
    wb_obj = openpyxl.load_workbook(xlsx_file)
    sheet = wb_obj.active

    for row in sheet.iter_rows():
        for cell in row:
            print(cell.value, end=" ")
        print()

    driver = webdriver.Chrome()
    driver.get('https:/www.google.com')
    type_keyword(driver, "wedew", True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
