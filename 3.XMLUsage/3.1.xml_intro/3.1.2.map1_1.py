import xmltodict


input_url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'


def download_file(url):
    import wget
    wget.download(url)


def run():
    with open('map1.osm', 'r', encoding='utf8') as fin:
        xml = fin.read()

    parsedxml = xmltodict.parse(xml)
    count = 0

    for node in parsedxml['osm']['node']:
        if 'tag' in node:
            count += 1
    print(count, len(parsedxml['osm']['node']) - count)


run()
