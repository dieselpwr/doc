'''
all liturgical calendar magic is performed here
thank the Lord for the Easter dateutil
'''

from datetime import datetime, date, time, timedelta
from dateutil.easter import easter

class LiturgicalTime():
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
        self.season = self.get_season()

    def epiphany(self, year):
        '''
        returns epiphany for a given year
        '''
        return date(year, 1, 6)

    def ash_wednesday(self, year):
        '''
        returns ash wednesday for a given year
        '''
        d = timedelta(days=-46)
        return easter(year)+d

    def easter_day(self, year):
        '''
        returns easter day for a given year
        '''
        return easter(year)

    def ascension_day(self, year):
        '''
        returns ascension day for a given year
        '''
        d = timedelta(days=39)
        return easter(year) + d

    def pentecost(self, year):
        '''
        returns the day of pentecost for a given year
        '''
        d = timedelta(weeks=7)
        return easter(year) + d

    def advent_sunday(self, year):
        '''
        returns the first sunday of advent for a given year
        '''
        weeks = 4
        correction = 0
        christmas = self.christmas_day(year)
        if (christmas.weekday() != 6):
            weeks-= 1
            correction = (christmas.isoweekday())
        d = timedelta(days=(-1 * ((weeks * 7) + correction)))
        return christmas + d

    def christmas_day(self, year):
        '''
        returns Christmas day for a given year
        '''
        return date(year, 12, 25)

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
            if self.now.date() > self.advent_sunday(self.now.year):
                cycle = 1
            else:
                cycle = 2
        else:
            if self.now.date() < self.advent_sunday(self.now.year):
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

    def get_season(self):
        '''
        returns the liturgical season
        '''
        season = None
        return season

if __name__ == '__main__':
    test = LiturgicalTime()
    print(str(test.now))
    print(str(test.cycle))
    print(str(test.office))
