import xmltodict


input_url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'


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
    with open('map1.osm', 'r', encoding='utf8') as fin:
        xml = fin.read()
    print_result(xmltodict.parse(xml))


run()
