from API import API
from CSVdistance import CSV
from Mock import Mock

class Factory:
    def seleccionarServicio(self, service):
        if service == 1:
            return API()
        elif service == 2:
            return CSV()
        elif service == 3:
            return Mock()