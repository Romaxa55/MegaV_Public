#!/usr/bin/env python3
"""Submit the MegaV Pages hub URLs to IndexNow (Bing, Yandex, Seznam, Naver share one endpoint)."""
import json, re, os, urllib.request, urllib.error
KEY = "a1e6b0dea2cf1d15a205037f0d02c8dd"
HOST = "romaxa55.github.io"
KEYLOC = f"https://{HOST}/MegaV_Public/{KEY}.txt"
here = os.path.dirname(os.path.abspath(__file__))
sm = open(os.path.join(here, "..", "docs", "sitemap.xml")).read()
urls = re.findall(r"<loc>([^<]+)</loc>", sm)
payload = {"host": HOST, "key": KEY, "keyLocation": KEYLOC, "urlList": urls}
req = urllib.request.Request("https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode(), headers={"Content-Type": "application/json; charset=utf-8"})
try:
    r = urllib.request.urlopen(req, timeout=30)
    print("IndexNow HTTP", r.status, "—", len(urls), "URLs submitted")
except urllib.error.HTTPError as e:
    print("IndexNow HTTP", e.code, e.read().decode()[:300])
