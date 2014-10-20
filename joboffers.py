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
careerjet_ict = 'http://rss.careerjet.it/rss?l=Italia&lid=41162&c=informatica-telecomunicazioni'
monster_ict = 'http://rss.jobsearch.monster.com/rssquery.ashx?rad_units=km&cy=IT&pp=25&sort=rv.di.dt&occ=660.11904&occ=660.11772&occ=660.11970&occ=660.11979&occ=660.11969&occ=660.11996&occ=660.11787&occ=660.11771&occ=660.12005&occ=660.11774&occ=660.11841&occ=660.11848&occ=660.11754&occ=660.11882&occ=660.11987&baseurl=offerte-lavoro.monster.it'

urls = [careerjet_ict, monster_ict]

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
