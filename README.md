# Web Archive Analysis

Part of [Open Source Intelligence](https://en.wikipedia.org/wiki/Open-source_intelligence) (OSINT) for [collective, or public intelligence]https://en.wikipedia.org/wiki/Collective_intelligence) purposes.

## Fetching data from Commom Crawl 

[Common crawl](http://commoncrawl.org/)

Option 1:

- [using-python-to-mine-common-crawl](https://www.bellingcat.com/resources/2015/08/13/using-python-to-mine-common-crawl/)
 - parse, search and download pages
 - Extracts links from html
 - log to console and store as csv the results
 - libs: requests, argparse, json, String IO, gzip, csv ...


Initial code: the following error happens: IOError: Not a gzipped file – details below.

Traceback (most recent call last):
File “commoncrawler.py”, line 123, in
html_content = download_page(record)
File “commoncrawler.py”, line 80, in download_page
data = f.read()
File “C:\Python27\lib\gzip.py”, line 261, in read
self._read(readsize)
File “C:\Python27\lib\gzip.py”, line 303, in _read
self._read_gzip_header()
File “C:\Python27\lib\gzip.py”, line 197, in _read_gzip_header
raise IOError, ‘Not a gzipped file’
IOError: Not a gzipped file

Change the prefix variable in the download_page helper function.

prefix = ‘https://aws-publicdatasets.s3.amazonaws.com/’
to
prefix = ‘https://commoncrawl.s3.amazonaws.com/’


Option 2: 

- [common-crawl-python](https://dmorgan.info/posts/common-crawl-python/)
 - Explains the relationship between WARC, WAT, and WET files
 - Download and search throuh warc files
 - libs: warc, requests

Option 3: using Mr Job library.

- Python and Hadoop, locally and in the cloud: [MrJob's Documentation](https://pythonhosted.org/mrjob/)
- [mr job starter kit](https://github.com/Smerity/cc-mrjob)'s github repository.


##  web archival replay tools:

[PyWB](https://github.com/ikreymer/pywb)
