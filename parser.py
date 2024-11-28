import requests
from pprint import pprint
cookies = {
    'bh': 'Ek8iTm90X0EgQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjEyMCIsICJZYUJyb3dzZXIiO3Y9IjI0LjEiLCAiWW93c2VyIjt2PSIyLjUiGgUieDg2IiIMIjI0LjEuMy44MDkiKgI/MDoJIldpbmRvd3MiQggiMTUuMC4wIkoEIjY0IlJmIk5vdF9BIEJyYW5kIjt2PSI4LjAuMC4wIiwgIkNocm9taXVtIjt2PSIxMjAuMC42MDk5LjIzNCIsICJZYUJyb3dzZXIiO3Y9IjI0LjEuMy44MDkiLCAiWW93c2VyIjt2PSIyLjUiWgI/MA==',
    'lastVisitedPage': '%7B%7D',
    'yandexuid': '8468017531730750165',
    'yashr': '9399949951730750165',
    'yuidss': '8468017531730750165',
    'ymex': '2046110172.yrts.1730750172',
    '_ym_uid': '1678626165741065506',
    '_ym_d': '1730752471',
    'L': 'ZSd1dVYCR3oDdGJRAHQHAGxXQAFdUWpbCUApMwg5GwcKKA==.1730752481.15940.369737.fcac89341d2e92494621c1fae22eab41',
    'yandex_login': 'bukaartemm',
    'my': 'YwA=',
    'gdpr': '0',
    'amcuid': '8141599911730828248',
    'allow_next': 'true',
    'font_loaded': 'YSv1',
    'is_gdpr': '0',
    'is_gdpr_b': 'CI6mChD9ngIoAg==',
    'i': 'w/EmpSOvQsrgOgJgY43uIGsS8+pLtsjik+ZRCUNG4F5o3sMG+tl+z/vZerz+dJqKVkjIPu6aKgjScJ3MJDFArT3QqcE=',
    'Session_id': '3:1732176490.5.0.1730752481346:MoxiTw:1daa.1.2:1|1153634826.-1.2.3:1730752481|3:10298543.586436.0aFLyRUBAjbUSTeZignWO0DTqio',
    'sessar': '1.1196.CiAPgicftWj3YzpSqQhNpA3Htoe1Mbp5X-4dpyMEP6L8lA.tRGSLFwe5_FlBkXOTrnTvt8Rzo7d7aS8b393tfHZLlI',
    'sessionid2': '3:1732176490.5.0.1730752481346:MoxiTw:1daa.1.2:1|1153634826.-1.2.3:1730752481|3:10298543.586436.fakesign0000000000000000000',
    '_ym_isad': '2',
    'yabs-vdrf': 'CwZvdcW2Ru8q0npHdC02A-sW00',
    'isa': 'iY3sBsvki2eQDFXjIJI2YinSLmkn1WnPdBrs8ymouuSSr84BCxSYJv3hzA3wzu4hti5G9cLA3dAfqIYv+Hl8+2ANgHA=',
    'sae': '0:0B4150B4-2FF3-433A-8ABD-730AB74C3515:p:24.10.3.825:w:d:RU:20220121',
    'yclid_src': 'music.yandex.ru/promo/lt-pay-promo/:17203374847070306303:8468017531730750165',
    '_ymab_param': 'MCuMQoCUcaK_ja3S2bSE1vNa4WCNdMEa6c1HN9M4-64pERayEpAxkzcNB-Yrrj6MIcZCYhQM-2IwAf-D2KemZMGT-Io',
    '_yasc': 'tbbN9REM+4o+1W41R4/mL/b45X4bH2dR1RXvcrGsAqXOYV2xpUEl/di4n+OZu5WJUMWX3WSxdpmQ/wQQjFw=',
    'chromecast': "''",
    'device_id': 'ac408bc14ff947c6aa4b9a267b64c0a9c1bdfc8e5',
    '_ym_visorc': 'b',
    'fullscreen-saved-data': '%7B%22on-iskraaugust-out-music-1%22%3A%7B%22compositeId%22%3A%22on-iskraaugust-out-music-1%22%2C%22actualUntil%22%3A1756884666816%7D%2C%22web-selector-nov2-1%22%3A%7B%22compositeId%22%3A%22web-selector-nov2-1%22%2C%22actualUntil%22%3A1763735901696%7D%7D',
    'yabs-udb': 'S7bqQ6zk8D2yqOFGjz6BqBhGlj2v8D61qB3GkT62qB0WqB_GiD60qO7GkD2zqBC0',
    'cycada': 'mQXcPbaDFmB3dhCFstYuzGUtlMsIyzh8AAlGc804jpk=',
    'yp': '1732276508.uc.ru#1732276508.duc.ru#1762286167.cld.2355920#1980170977.dark_promo.5#1733220452.hdrc.1#2004180585.multib.1#2047559975.pcs.1#1763735975.swntab.0#2046112481.udn.cDpidWthYXJ0ZW1t#1736604481.vhstfltr_onb.3:1728828480975#1733506587.csc.1#1747159436.vhstfltr.nohost:www.youtube.com#1732372777.gpauto.55_832168:37_554924:140:1:1732199967#1732441939.szm.1_25:1536x864:1471x740#1732701139.dlp.3',
    'gpb': 'gpauto.55_832168%3A37_554924%3A140%3A1%3A1732199967',
    'ys': 'svt.1#def_bro.1#wprid.1732199919778180-9155111492964451389-balancer-l7leveler-kubr-yp-sas-132-BAL#ybzcc.ru#newsca.native_cache',
    'active-browser-timestamp': '1732200075874',
    'bh': 'ElEiQ2hyb21pdW0iO3Y9IjEyOCIsICJOb3Q7QT1CcmFuZCI7dj0iMjQiLCAiWWFCcm93c2VyIjt2PSIyNC4xMCIsICJZb3dzZXIiO3Y9IjIuNSIaBSJ4ODYiKgI/MDoJIldpbmRvd3MiQggiMTUuMC4wIkoEIjY0IlJoIkNocm9taXVtIjt2PSIxMjguMC42NjEzLjE4NiIsICJOb3Q7QT1CcmFuZCI7dj0iMjQuMC4wLjAiLCAiWWFCcm93c2VyIjt2PSIyNC4xMC4zLjgyNSIsICJZb3dzZXIiO3Y9IjIuNSJaAj8wYNqN/bkGaiHcyuH/CJLYobEDn8/h6gP7+vDnDev//fYPtsaEnwHzgQI=',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru,en;q=0.9',
    # 'cookie': "bh=Ek8iTm90X0EgQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjEyMCIsICJZYUJyb3dzZXIiO3Y9IjI0LjEiLCAiWW93c2VyIjt2PSIyLjUiGgUieDg2IiIMIjI0LjEuMy44MDkiKgI/MDoJIldpbmRvd3MiQggiMTUuMC4wIkoEIjY0IlJmIk5vdF9BIEJyYW5kIjt2PSI4LjAuMC4wIiwgIkNocm9taXVtIjt2PSIxMjAuMC42MDk5LjIzNCIsICJZYUJyb3dzZXIiO3Y9IjI0LjEuMy44MDkiLCAiWW93c2VyIjt2PSIyLjUiWgI/MA==; lastVisitedPage=%7B%7D; yandexuid=8468017531730750165; yashr=9399949951730750165; yuidss=8468017531730750165; ymex=2046110172.yrts.1730750172; _ym_uid=1678626165741065506; _ym_d=1730752471; L=ZSd1dVYCR3oDdGJRAHQHAGxXQAFdUWpbCUApMwg5GwcKKA==.1730752481.15940.369737.fcac89341d2e92494621c1fae22eab41; yandex_login=bukaartemm; my=YwA=; gdpr=0; amcuid=8141599911730828248; allow_next=true; font_loaded=YSv1; is_gdpr=0; is_gdpr_b=CI6mChD9ngIoAg==; i=w/EmpSOvQsrgOgJgY43uIGsS8+pLtsjik+ZRCUNG4F5o3sMG+tl+z/vZerz+dJqKVkjIPu6aKgjScJ3MJDFArT3QqcE=; Session_id=3:1732176490.5.0.1730752481346:MoxiTw:1daa.1.2:1|1153634826.-1.2.3:1730752481|3:10298543.586436.0aFLyRUBAjbUSTeZignWO0DTqio; sessar=1.1196.CiAPgicftWj3YzpSqQhNpA3Htoe1Mbp5X-4dpyMEP6L8lA.tRGSLFwe5_FlBkXOTrnTvt8Rzo7d7aS8b393tfHZLlI; sessionid2=3:1732176490.5.0.1730752481346:MoxiTw:1daa.1.2:1|1153634826.-1.2.3:1730752481|3:10298543.586436.fakesign0000000000000000000; _ym_isad=2; yabs-vdrf=CwZvdcW2Ru8q0npHdC02A-sW00; isa=iY3sBsvki2eQDFXjIJI2YinSLmkn1WnPdBrs8ymouuSSr84BCxSYJv3hzA3wzu4hti5G9cLA3dAfqIYv+Hl8+2ANgHA=; sae=0:0B4150B4-2FF3-433A-8ABD-730AB74C3515:p:24.10.3.825:w:d:RU:20220121; yclid_src=music.yandex.ru/promo/lt-pay-promo/:17203374847070306303:8468017531730750165; _ymab_param=MCuMQoCUcaK_ja3S2bSE1vNa4WCNdMEa6c1HN9M4-64pERayEpAxkzcNB-Yrrj6MIcZCYhQM-2IwAf-D2KemZMGT-Io; _yasc=tbbN9REM+4o+1W41R4/mL/b45X4bH2dR1RXvcrGsAqXOYV2xpUEl/di4n+OZu5WJUMWX3WSxdpmQ/wQQjFw=; chromecast=''; device_id=ac408bc14ff947c6aa4b9a267b64c0a9c1bdfc8e5; _ym_visorc=b; fullscreen-saved-data=%7B%22on-iskraaugust-out-music-1%22%3A%7B%22compositeId%22%3A%22on-iskraaugust-out-music-1%22%2C%22actualUntil%22%3A1756884666816%7D%2C%22web-selector-nov2-1%22%3A%7B%22compositeId%22%3A%22web-selector-nov2-1%22%2C%22actualUntil%22%3A1763735901696%7D%7D; yabs-udb=S7bqQ6zk8D2yqOFGjz6BqBhGlj2v8D61qB3GkT62qB0WqB_GiD60qO7GkD2zqBC0; cycada=mQXcPbaDFmB3dhCFstYuzGUtlMsIyzh8AAlGc804jpk=; yp=1732276508.uc.ru#1732276508.duc.ru#1762286167.cld.2355920#1980170977.dark_promo.5#1733220452.hdrc.1#2004180585.multib.1#2047559975.pcs.1#1763735975.swntab.0#2046112481.udn.cDpidWthYXJ0ZW1t#1736604481.vhstfltr_onb.3:1728828480975#1733506587.csc.1#1747159436.vhstfltr.nohost:www.youtube.com#1732372777.gpauto.55_832168:37_554924:140:1:1732199967#1732441939.szm.1_25:1536x864:1471x740#1732701139.dlp.3; gpb=gpauto.55_832168%3A37_554924%3A140%3A1%3A1732199967; ys=svt.1#def_bro.1#wprid.1732199919778180-9155111492964451389-balancer-l7leveler-kubr-yp-sas-132-BAL#ybzcc.ru#newsca.native_cache; active-browser-timestamp=1732200075874; bh=ElEiQ2hyb21pdW0iO3Y9IjEyOCIsICJOb3Q7QT1CcmFuZCI7dj0iMjQiLCAiWWFCcm93c2VyIjt2PSIyNC4xMCIsICJZb3dzZXIiO3Y9IjIuNSIaBSJ4ODYiKgI/MDoJIldpbmRvd3MiQggiMTUuMC4wIkoEIjY0IlJoIkNocm9taXVtIjt2PSIxMjguMC42NjEzLjE4NiIsICJOb3Q7QT1CcmFuZCI7dj0iMjQuMC4wLjAiLCAiWWFCcm93c2VyIjt2PSIyNC4xMC4zLjgyNSIsICJZb3dzZXIiO3Y9IjIuNSJaAj8wYNqN/bkGaiHcyuH/CJLYobEDn8/h6gP7+vDnDev//fYPtsaEnwHzgQI=",
    'priority': 'u=1, i',
    'referer': 'https://music.yandex.ru/chart',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "YaBrowser";v="24.10", "Yowser";v="2.5"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.186", "Not;A=Brand";v="24.0.0.0", "YaBrowser";v="24.10.3.825", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36',
    'x-current-uid': '1153634826',
    'x-requested-with': 'XMLHttpRequest',
    'x-retpath-y': 'https://music.yandex.ru/chart',
    'x-yandex-music-client-now': '2024-11-21T17:42:41+03:00',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.8299351487489035',
}

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, cookies=cookies, headers=headers)
print(response.status_code)
pprint(response.json()['chartPositions'])
for track in response.json()['chartPositions']:
    position = track['chartPosition']['position']
    title = track['track']['title']
    autor = track['track']['artists'][0]['name']
    artist = [artist['name'] for artist in track['track']['artists']]
    autors = ', '.join(artist)
    print(f"№-{position} - {title} - {autors}")
