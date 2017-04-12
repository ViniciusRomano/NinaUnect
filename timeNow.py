# -*- coding: utf-8 -*-

import requests


class timeNow(object):
    """ Classe feita para obter um json com o horário atual(São Paulo) """

    def __init__(self):
        r = requests.get('https://script.googleusercontent.com/macros/echo?user_content_key=tPcPix-8NgC1BNhgCZNL_XE9GK_JvQDnFqpL6aQyHoWQeyaXbzLTwtEtmWoSDkCRvnoFWcwNZTCWuJqcwchKgP6I3SmPcPeSm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnJ9GRkcRevgjTvo8Dc32iw_BLJPcPfRdVKhJT5HNzQuXEeN3QFwl2n0M6ZmO-h7C6bwVq0tbM60-_IQDS8gp7-wwK7XAnp4CU0ajkDCYtjwe&lib=MwxUjRcLr2qLlnVOLh12wSNkqcO1Ikdrk')
        self.json = r.json()

    def getTime(self):
        # retorna no json apenas o horário atual
        return self.json['fulldate'].split(',')[1].split('-')[0]
