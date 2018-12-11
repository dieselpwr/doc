'''
All liturgical calendar magic is performed here
Thank the Lord for the Easter dateutil
'''

from datetime import datetime, date, timedelta
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
        self.year = self.get_cycle_year()

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

    def get_cycle_year(self):
        '''
        returns the lectionary cycle year (1 or 2)
        '''
        cycle_year = None

        if self.now.year % 2 == 0:
            even_year = True
        else:
            even_year = False
        
        if even_year:
            if self.now.date() > self.first_sunday_advent():
                cycle_year = 1
            else:
                cycle_year = 2
        else:
            if self.now.date() < self.first_sunday_advent():
                cycle_year = 1
            else:
                cycle_year = 2

        return cycle_year

if __name__ == '__main__':
    test = LectionaryDateTime(now=datetime.now())
    print(str(test.cycle_year))
