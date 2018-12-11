'''
All liturgical calendar magic is performed here
Thank the Lord for the Easter dateutil
'''

from datetime import datetime, date, time, timedelta
from dateutil.easter import easter

class LectionaryDateTime():
    '''
    stores all properties of the current datetime
    '''

    def __init__(self, now=datetime.now()):
        '''
        initializes the class properties
        '''
        self.now = now
        self.cycle = self.get_cycle()
        self.office = self.get_office()

    def first_sunday_advent(self):
        '''
        returns the first sunday of advent for a given year
        '''
        weeks = 4
        correction = 0
        christmas = date(self.now.year, 12, 25)
        if (christmas.weekday() != 6):
            weeks-= 1
            correction = (christmas.isoweekday())
        d = timedelta(days=(-1 * ((weeks * 7) + correction)))
        return christmas + d

    def get_cycle(self):
        '''
        returns the lectionary cycle year (1 or 2)
        '''
        cycle = None

        if self.now.year % 2 == 0:
            even_year = True
        else:
            even_year = False
        
        if even_year:
            if self.now.date() > self.first_sunday_advent():
                cycle = 1
            else:
                cycle = 2
        else:
            if self.now.date() < self.first_sunday_advent():
                cycle = 1
            else:
                cycle = 2

        return cycle

    def get_office(self):
        '''
        returns the appropriate office based on time
        '''
        office = None

        prime_diff = abs((self.now - datetime.combine(self.now.date(), time(6, 0))).total_seconds())
        sext_diff = abs((self.now - datetime.combine(self.now.date(), time(12, 0))).total_seconds())
        vespers_diff = abs((self.now - datetime.combine(self.now.date(), time(18, 0))).total_seconds())
        compline_diff = abs((self.now - datetime.combine(self.now.date(), time(21, 0))).total_seconds())

        diff_list = [prime_diff, sext_diff, vespers_diff, compline_diff]
        office_enum = diff_list.index(min(diff_list))

        if office_enum == 0:
            office = 'PRIME'
        elif office_enum == 1:
            office = 'SEXT'
        elif office_enum == 2:
            office = 'VESPERS'
        else:
            office = 'COMPLINE'

        return office

if __name__ == '__main__':
    test = LectionaryDateTime()
    print(str(test.now))
    print(str(test.cycle))
    print(str(test.office))
