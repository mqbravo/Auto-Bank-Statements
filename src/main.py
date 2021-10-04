from os import chdir

# Change WD to projects root
chdir("..")

from datasources import ScotiabankWebCrawler

sw = ScotiabankWebCrawler()
df = sw.extract()
print(df)

sw.upload()
