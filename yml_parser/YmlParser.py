import yaml


class YmlParser:

    def __init__(self):
        self.parsed ={}

    def load_file(self, filename):
        try:
            file = open(filename)
            self.parsed = yaml.load(file)
            file.close()
        except (yaml.YAMLError, IOError) as ex:
            print("Error {0} is occurred, when {1} file is loaded".format(ex, filename))

    def get_values(self, key):
        return self.parsed.get(key)
