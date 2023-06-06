import xmltodict


input_url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'


def download_file(url):
    import wget
    wget.download(url)


with open('map1.osm', 'r', encoding='utf8') as fin:
    xml = fin.read()

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])