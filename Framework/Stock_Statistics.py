class Stock_Statistics:
    def __init__(self,sym,pchg,last,spread,list_date):
        self.sym = sym
        self.pchg = pchg
        self.last = last
        self.spread = spread
        self.list_date = list_date

    def get_sym(self):
        return self.sym

    def get_pchg(self):
        return self.pchg

    def get_last(self):
        return self.last

    def get_list_date(self):
        return self.list_date
