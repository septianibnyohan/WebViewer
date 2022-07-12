# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import requests
from fake_headers import Headers, browsers
from requests.exceptions import RequestException
from selenium import webdriver

from webviewer.basic import type_keyword
from webviewer.download_driver import *
import openpyxl

cwd = os.getcwd()
patched_drivers = os.path.join(cwd, 'patched_drivers')

def main():
    return

def main_viewer(proxy_type, proxy, position):
    return

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
