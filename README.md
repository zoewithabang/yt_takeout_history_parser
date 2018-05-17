# Google Takeout YouTube History Parser

A Python 3 [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html) spider that lets you parse your YouTube history exported from Google Takeout as JSON instead of a giant HTML file.

To use:
- Get [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html) up and working
- In yt_takeout_history_parser/spiders/parser.py, change the "start_urls" entry to the location of your watch-history.html file
- Run `scrapy crawl parser -o out.json` in the project's top level directory

A quick example of what can be done with this JSON data can be found in `sorter.py`, counting up watched videos and dumping JSON entries of those that have been watched more than 5 times within the timeframe of the archived data.
