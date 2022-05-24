from typing import List

class _reference_c:
    def __init__(self, value=None):
        self.value = value

    def __getitem__(self, item):
        return self.value

    def __setitem__(self, key, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class _cout_c:
    def __lshift__(self, obj):
        print(obj, sep='', end='')
        return self

# пока что син вовращает строку (а должен приводить к типу)
class _cin_c:
    def __init__(self, delimiters=" \n\t"):
        self.delim = delimiters

    # TODO применить reduce тут
    def _split_by_delimiters(self, string):
        for d in self.delim:
            string = string.split(d, 1)[0]  # оставляем только первый кусок строки что был до разделителя
        return string

    def _cin_input(self):
        return self._split_by_delimiters(input())

    # тут я использую список для реализации ссылок в питоне
    def __rshift__(self, ref: _reference_c):
        ref[0] = self._cin_input()
        return self


cout = _cout_c()
cin = _cin_c()
ref = _reference_c()
endl = '\n'
