from datasources import ScotiabankWebCrawler
from os import chdir

# Change WD to projects root
chdir("..")

sw = ScotiabankWebCrawler()
sw.crawl()
