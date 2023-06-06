import xmltodict


input_url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'


def download_file(url):
    import wget
    wget.download(url)


def count_string(nodes, string):
    return len(list(filter(lambda x: string in x, nodes)))


def count_no_string(nodes, string):
    return len(list(filter(lambda x: string not in x, nodes)))


def print_result(parsed_xml):
    print(count_string(parsed_xml['osm']['node'], 'tag'),
          count_no_string(parsed_xml['osm']['node'], 'tag'))


def run():
    with open('map2.osm', 'r', encoding='utf8') as fin:
        xml = fin.read()

    parsed_xml = xmltodict.parse(xml)

    count = 0
    for node in parsed_xml['osm']['node']:
        found = False
        if 'tag' in node:
            tags = node['tag']
            if isinstance(tags, list):
                for tag in tags:
                    if len(dict(tag).keys()) == 2 and '@k' in tag and '@v' in \
                            tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                        found = True
            else:
                if len(dict(tags).keys()) == 2 and '@k' in tags and '@v' in \
                        tags and tags['@k'] == 'amenity' and tags['@v'] == 'fuel':
                    found = True

        if found:
            count += 1

    print(count)


run()
