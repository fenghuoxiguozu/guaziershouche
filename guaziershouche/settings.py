# -*- coding: utf-8 -*-

# Scrapy settings for guaziershouche project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'guaziershouche'

SPIDER_MODULES = ['guaziershouche.spiders']
NEWSPIDER_MODULE = 'guaziershouche.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'guaziershouche (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    # 'cookie':'antipas=254626546272452916; __guid=253446671.1519585368072172000.1552567052077.2583; uuid=a3a69259-0007-42da-f5ef-4b623e127738; ganji_uuid=1683256141084053758289; lg=1; jr_apply_platform=web; jr_client=pc; financeCityDomain=bj; 52949bad-ef9d-49b0-cb9f-52adcaf78893_views=3; Hm_lvt_e6e64ec34653ff98b12aab73ad895002=1552567062,1552570408; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1552567053,1552567066,1552579221; jr_from=web_index_tc; a3a69259-0007-42da-f5ef-4b623e127738_views=6; 5c3f8055-3bd9-45a2-a3ae-286f48ed3885_views=3; antipas=35qF01J8L789403966514nND3; cityDomain=su; clueSourceCode=10103000312%2300; user_city_id=67; sessionid=38f07071-bb7f-4a11-b703-f9ea15dde307; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_i%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22a3a69259-0007-42da-f5ef-4b623e127738%22%2C%22sessionid%22%3A%2238f07071-bb7f-4a11-b703-f9ea15dde307%22%7D; preTime=%7B%22last%22%3A1552652385%2C%22this%22%3A1552567176%2C%22pre%22%3A1552567176%7D; monitor_count=69',
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    # "Cookie": "clueSourceCode=10103000312%2300; antipas=6684zg71184410373k54O20U; uuid=38599a95-ce54-4dbe-b3ed-4ef6b7d02d26; ganji_uuid=1018921037953793342386; sessionid=73d00942-da8a-4b6d-8416-897540a76775; lg=1; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_i%22%3A%22-%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3Anull%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2238599a95-ce54-4dbe-b3ed-4ef6b7d02d26%22%2C%22sessionid%22%3A%2273d00942-da8a-4b6d-8416-897540a76775%22%7D; close_finance_popup=2018-01-30; cityDomain=xa; preTime=%7B%22last%22%3A1517307287%2C%22this%22%3A1517307276%2C%22pre%22%3A1517307276%7D",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'guaziershouche.middlewares.GuaziershoucheSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'guaziershouche.middlewares.GuaziershoucheDownloaderMiddleware': 543,
    # 'guaziershouche.middlewares.ProxyMiddleware': 400,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'guaziershouche.pipelines.DuplicatesPipeline': 300,
  'guaziershouche.pipelines.MongDBPipeline': 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MYSQL_HOST='127.0.0.1'
MYSQL_PORT=3306
MYSQL_USER='root'
MYSQL_PASSWORD=''
MYSQL_DBNAME='guazi'

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'guazi'
MONGODB_DOCNAME = 'ershouche'

PROXY_URL = 'http://ip.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&qty=1&time=1&pro=&city=&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson='
