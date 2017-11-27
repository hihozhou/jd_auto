#!/usr/bin/python3
# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 下面填入京东的用户名以及密码
jdAccount = {
    "username": "",
    "password": ""
}

chrome_options = Options()
# 不加载图片提升速度
prefs = {"profile.managed_default_content_settings.images": 2}
# 无界面配置，需要验证码时需要注释掉
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("prefs", prefs)

chrome = webdriver.Chrome(chrome_options=chrome_options)  # 打开浏览窗口
chrome.get(url="https://passport.jd.com/new/login.aspx?")
# accountLoginButton = chrome.find_element_by_xpath("//*[@id=\"content\"]/div/div[1]/div/div[2]/a")#获取扫码登录节点
accountLoginButton = chrome.find_element_by_xpath("//*[@id=\"content\"]/div/div[1]/div/div[3]/a")  # 获取账户登录节点
accountLoginButton.click()  # 点击账户登录按钮

User = chrome.find_element_by_id("loginname")  # 找到用户输入框
User.clear()  # 清除用户输入框内容
User.send_keys(jdAccount["username"])  # 填入帐号
Passwd = chrome.find_element_by_id("nloginpwd")  # 找到密码输入框
Passwd.clear()  # 清除密码输入框内容
Passwd.send_keys(jdAccount["password"])  # 填入密码
chrome.find_element_by_id("loginsubmit").click()  # 点击登录提交按钮
time.sleep(0.5)
print(chrome.get_cookies())
chrome.quit()  # 推出关闭窗口
