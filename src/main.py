from datasources import ScotiabankWebCrawler
from os import chdir

# Change WD to projects root
chdir("..")

sw = ScotiabankWebCrawler()
df = sw.extract()
print(df)
