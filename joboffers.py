# -*- coding: utf-8 -*-
"""

job offers RSS feed parser
Multi websites scraper

"""

import feedparser
from datetime import datetime
import os

#specify directory where output is saved. Default is working dir.
os.chdir('.')

#modify links with own RSS feed
rss_feed_1 = 'your_rss_feed_url'
rss_feed_2 = 'your_other_rss_feed_url'

urls = [rss_feed_1, rss_feed_2]

#output saved as JobALERT-datetime.txt
fileOut = 'JobALERT-'+str(datetime.now().strftime('%d-%m-%Y-%H-%M'))+'.txt'

with open(fileOut, 'w') as f:

    f.write(datetime.now().strftime("%d-%m-%Y %H:%M"))

    for url in urls:
        RSSfeed = feedparser.parse(url)
        listJobs = []
        for feed in RSSfeed.entries:
            listJobs.append(str(feed.title+' : '+feed.description+' '+feed.link))


        f.write('\n')
        f.write('Number of job ads retrieved: '+str(len(listJobs)))
        f.write('\n')
        f.write('\n')
        for el in listJobs:
            f.write(el+'\n')

f.close()
