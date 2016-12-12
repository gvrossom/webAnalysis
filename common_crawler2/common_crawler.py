import warc
import requests
from contextlib import closing
from StringIO import StringIO

def get_partial_warc_file(url, num_bytes=1024 * 10):
    """
    Download the first part of a WARC file and return a warc.WARCFile instance.

    url: the url of a gzipped WARC file
    num_bytes: the number of bytes to download. Default is 10KB

    return: warc.WARCFile instance
    """
    with closing(requests.get(url, stream=True)) as r:
        buf = StringIO(r.raw.read(num_bytes))
    return warc.WARCFile(fileobj=buf, compress=True)

urls = {
    'warc': 'https://aws-publicdatasets.s3.amazonaws.com/common-crawl/crawl-data/CC-MAIN-2016-07/segments/1454701145519.33/warc/CC-MAIN-20160205193905-00000-ip-10-236-182-209.ec2.internal.warc.gz',
    'wat':  'https://aws-publicdatasets.s3.amazonaws.com/common-crawl/crawl-data/CC-MAIN-2016-07/segments/1454701145519.33/wat/CC-MAIN-20160205193905-00000-ip-10-236-182-209.ec2.internal.warc.wat.gz',
    'wet':  'https://aws-publicdatasets.s3.amazonaws.com/common-crawl/crawl-data/CC-MAIN-2016-07/segments/1454701145519.33/wet/CC-MAIN-20160205193905-00000-ip-10-236-182-209.ec2.internal.warc.wet.gz'
}

files = {file_type: get_partial_warc_file(url=url) for file_type, url in urls.items()}
# this line can be used if you want to download the whole file
# files = {file_type: warc.open(url) for file_type, url in urls.items()}


def get_record_with_header(warc_file, header, value):
    for record, _, _ in warc_file.browse():
        if record.header.get(header) == value:
            return record

warc_record = get_record_with_header(
    files['warc'],
    header='WARC-Type',
    value='response'
)
wat_record = get_record_with_header(
    files['wat'],
    header='WARC-Refers-To',
    value=warc_record.header['WARC-Record-ID']
)
wet_record = get_record_with_header(
    files['wet'],
    header='WARC-Refers-To',
    value=warc_record.header['WARC-Record-ID']
)

print(warc_record.header)
print(wat_record.header)
print(wet_record.header)

import json

print(warc_record.payload.read())
print(json.dumps(json.loads(wat_record.payload.read()), indent=2))
print(wet_record.payload.read())