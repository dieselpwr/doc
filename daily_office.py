'''
all liturgical calendar magic is performed here
'''

from datetime import datetime, date, time, timedelta
from enum import Enum

class CanonicalHour(Enum):
    '''
    enumeration of canonical hours
    '''
    MORNING = 0
    NOONDAY = 1
    EVENING = 2
    COMPLINE = 3


class CycleYear(Enum):
    '''
    enumeration of daily office cycle years
    '''
    YEAR_ONE = 1
    YEAR_TWO = 2


class LiturgicalSeason(Enum):
    '''
    enumeration of liturgical seasons
    '''
    ADVENT = 0
    CHRISTMAS = 1
    EPIPHANY = 2
    LENT = 3
    EASTER = 4
    AFTER_PENTECOST = 5


class LiturgicalDay:
    '''
    functions returning dates from the liturgical calendar for a given
    year
    '''

    def __init__(self, year):
        '''
        initializes the class
        '''
        self.year = year
    
    #=============================Fixed Date===============================

    def epiphany(self):
        '''
        returns epiphany for a given year
        '''
        return date(self.year, 1, 6)
    
    def confession_st_peter(self):
        '''
        returns confession of St. Peter for a given year
        '''
        return date(self.year, 1, 18)
    
    def confession_st_paul(self):
        '''
        returns confession of St. Paul for a given year
        '''
        return date(self.year, 1, 25)
    
    def presentation_eve(self):
        '''
        returns the eve of the presentation for a given year
        '''
        return date(self.year, 2, 1)
    
    def presentation(self):
        '''
        returns the presentation for a given year
        '''
        return date(self.year, 2, 2)
    
    def st_matthias(self):
        '''
        returns St. Matthias' day for a given year
        '''
        return date(self.year, 2, 24)
    
    def st_joseph(self):
        '''
        returns St. Joseph's day for a given year
        '''
        return date(self.year, 3, 19)
    
    def annunciation_eve(self):
        '''
        returns the eve of the annunciation for a given year
        '''
        return date(self.year, 3, 24)
    
    def annunciation(self):
        '''
        returns the annunciation for a given year
        '''
        return date(self.year, 3, 25)

    def st_mark(self):
        '''
        returns St. Mark's day for a given year
        '''
        return date(self.year, 4, 25)
    
    def ss_phillip_james(self):
        '''
        returns St. Phillip's and St. James' Day for a given year
        '''
        return date(self.year, 5, 1)
    
    def visitation_eve(self):
        '''
        returns the eve of the visitation for a given year
        '''
        return date(self.year, 5, 30)

    def visitation(self):
        '''
        returns the visitation for a given year
        '''
        return date(self.year, 5, 31)

    def christmas(self):
        '''
        returns Christmas for a given year
        '''
        return date(self.year, 12, 25)

    #======================Calculated Date=============================

    def easter(self):
        '''
        returns easter for a given year
        '''
        y = self.year
        g = y % 19
        e = 0
        c = y//100
        h = (c - c//4 - (8*c + 13)//25 + 19*g + 15) % 30
        i = h - (h//28)*(1 - (h//28)*(29//(h + 1))*((21 - g)//11))
        j = (y + y//4 + i + 2 - c + c//4) % 7
        p = i - j + e
        d = 1 + (p + 27 + (p + 6)//40) % 31
        m = 3 + (p + 26)//30
        return date(int(y), int(m), int(d))
    
    def thanksgiving(self):
        '''
        returns thanksgiving for a given year
        '''
        y = self.year
        s = date(y, 11, 1)
        e = date(y, 11, 30)
        d = timedelta(days=1)
        t = 0
        while s <= e and t < 3:
            if(s.weekday() == 3):
                t += 1
            s += d
        return s

    #==========================Easter Dependent============================

    def ash_wednesday(self):
        '''
        returns ash wednesday for a given year
        '''
        d = timedelta(days=-46)
        return self.easter() + d

    def ascension_day(self):
        '''
        returns ascension day for a given year
        '''
        d = timedelta(days=39)
        return self.easter() + d

    def pentecost(self):
        '''
        returns the day of pentecost for a given year
        '''
        d = timedelta(weeks=7)
        return self.easter() + d

    #========================Christmas Dependent===========================

    def advent_sunday(self):
        '''
        returns the first sunday of advent for a given year
        '''
        weeks = 4
        correction = 0
        christmas = self.christmas()
        if (christmas.weekday() != 6):
            weeks-= 1
            correction = (christmas.isoweekday())
        d = timedelta(days=(-1 * ((weeks * 7) + correction)))
        return christmas + d


class LiturgicalSpan:
    '''
    functions returning boolean based on whether the given datetime is
    in a particular span/season
    '''

    def __init__(self, now=datetime.now()):
        '''
        initializes the class
        '''
        self.now = now
        self.lday = LiturgicalDay(year=now.year)


class DailyOffice:
    '''
    superclass for the individual offices
    '''

    def __init__(self, now=datetime.now()):
        '''
        initializes the class
        '''
        self.now = now
        self.lday = LiturgicalDay(year=now.year)
        self.lspan = LiturgicalSpan(now=now)
        self.cycle = self.get_cycle()
        self.hour = self.get_hour()
        # self.season = self.get_season()

    def get_cycle(self):
        '''
        returns the lectionary cycle year (1 or 2)
        '''
        if self.now.year % 2 == 0:
            even_year = True
        else:
            even_year = False
        cycle_enum = None
        if even_year:
            if self.now.date() > self.lday.advent_sunday():
                cycle_enum = 1
            else:
                cycle_enum = 2
        else:
            if self.now.date() < self.lday.advent_sunday():
                cycle_enum = 1
            else:
                cycle_enum = 2
        return CycleYear(cycle_enum)

    def get_hour(self):
        '''
        returns the appropriate cannonical hour based on time
        '''
        morning = abs((self.now - datetime.combine(self.now.date(), time(6, 0))).total_seconds())
        noonday = abs((self.now - datetime.combine(self.now.date(), time(12, 0))).total_seconds())
        evening = abs((self.now - datetime.combine(self.now.date(), time(18, 0))).total_seconds())
        compline = abs((self.now - datetime.combine(self.now.date(), time(21, 0))).total_seconds())
        diffs = (morning, noonday, evening, compline)
        hours_enum = diffs.index(min(diffs))
        return CanonicalHour(hours_enum)

if __name__ == '__main__':
    d = timedelta(hours=0)
    test = DailyOffice(now=datetime.now() + d)
    print(str(test.now))
    print(str(test.cycle.value))
    print(str(test.hour.name))
