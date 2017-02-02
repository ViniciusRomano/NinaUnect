import json
import datetime

class toJson(object):
    """Class for json file manipulation"""

    def create(self, dict, name):
        dict['CreatedTimeThisJson'] = str(datetime.datetime.now().strftime(
            " %d %b %Y %H:%M:%S "))  # format time : ' 01 Feb 2017 13:52:26'
        with open(name + '.json', 'w') as fp:
            json.dump(dict, fp)
