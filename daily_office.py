'''
Daily Office Companion
'''

from enum import Enum
from random import choice
from dateutil.easter import easter
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from datetime import datetime, date, time

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


class LiturgicalRite(Enum):
    '''
    enumeration or liturgical rites
    '''
    RITE_ONE = 1
    RITE_TWO = 2


class LiturgicalDay(dict):
    '''
    represents days from the liturgical calendar with associated
    collects, psalms, and readings
    '''

    def __init__(self, year, switch=False):
        '''
        initializes the class
        '''
        self.switch = switch
        self._populate(year)

    def __keytransform__(self, key):
        if bool(self.switch):
            if isinstance(key, str):
                key = '_'.join(key.split()).upper()
            else:
                raise TypeError('Cannot handle non-string type {} in switched mode.'.format(str(type(key))))
        else:
            if isinstance(key, datetime):
                key = key.date()
            elif isinstance(key, date):
                key = key
            elif isinstance(key, int) or isinstance(key, float):
                key = datetime.utcfromtimestamp(key).date()
            elif isinstance(key, str):
                try:
                    key = parse(key).date()
                except (ValueError, OverflowError):
                    raise ValueError('Cannot parse date from string {}'.format(str(key)))
            else:
                raise TypeError('Cannot convert type {} to date.'.format(str(type(key))))
        return key

    def __contains__(self, key):
        return dict.__contains__(self, self.__keytransform__(key))

    def __getitem__(self, key):
        return dict.__getitem__(self, self.__keytransform__(key))

    def get(self, key, default=None):
        return dict.get(self, self.__keytransform__(key), default)

    def pop(self, key, default=None):
        if default is None:
            return dict.pop(self, self.__keytransform__(key))
        return dict.pop(self, self.__keytransform__(key), default)

    def __eq__(self, other):
        return dict.__eq__(self, other) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return dict.__ne__(self, other) or self.__dict__ != other.__dict__

    def key_switcher(self, date_key, name_key):
        switch_key = date_key
        if bool(self.switch):
            switch_key = name_key
        return switch_key

    def _populate(self, year):
        '''
        populates with liturgical days
        '''

        #============================Tier 6============================



        #============================Tier 5============================

        # The Confession of Saint Peter the Apostle
        date_key = date(year, 1, 18)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Confession of Saint Peter the Apostle',
            'date': date_key,
        }

        # The Conversion of Saint Paul the Apostle
        date_key = date(year, 1, 25)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Conversion of Saint Paul the Apostle',
            'date': date_key,
        }

        # Saint Matthias the Apostle
        date_key = date(year, 2, 24)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Matthias the Apostle',
            'date': date_key,
        }

        # Saint Joseph
        date_key = date(year, 3, 19)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Joseph',
            'date': date_key,
        }

        # The Annunciation of Our Lord Jesus Christ to the Blessed Virgin Mary
        date_key = date(year, 3, 25)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Annunciation of Our Lord Jesus Christ to the Blessed Virgin Mary',
            'date': date_key,
        }

        # Saint Mark the Evangelist
        date_key = date(year, 4, 25)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Mark the Evangelist',
            'date': date_key,
        }

        # Saint Philip and Saint James, Apostles
        date_key = date(year, 5, 1)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Philip and Saint James, Apostles',
            'date': date_key,
        }

        # The Visitation of the Blessed Virgin Mary
        date_key = date(year, 5, 31)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Visitation of the Blessed Virgin Mary',
            'date': date_key,
        }

        # Saint Barnabas the Apostle
        date_key = date(year, 6, 11)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Barnabas the Apostle',
            'date': date_key,
        }

        # The Nativity of Saint John the Baptist
        date_key = date(year, 6, 24)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Nativity of Saint John the Baptist',
            'date': date_key,
        }

        # Saint Peter and Saint Paul, Apostles
        date_key = date(year, 6, 29)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Peter and Saint Paul, Apostles',
            'date': date_key,
        }

        # Independence Day
        date_key = date(year, 7, 4)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Independence Day',
            'date': date_key,
        }

        # Saint Mary Magdalene
        date_key = date(year, 7, 22)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Mary Magdalene',
            'date': date_key,
        }

        # Saint James the Apostle
        date_key = date(year, 7, 25)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint James the Apostle',
            'date': date_key,
        }

        # Saint Mary the Virgin, Mother of Our Lord Jesus Christ
        date_key = date(year, 8, 15)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Mary the Virgin, Mother of Our Lord Jesus Christ',
            'date': date_key,
        }

        # Saint Bartholomew the Apostle
        date_key = date(year, 8, 24)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Bartholomew the Apostle',
            'date': date_key,
        }

        # Holy Cross Day
        date_key = date(year, 9, 14)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Holy Cross Day',
            'date': date_key,
        }

        # Saint Matthew, Apostle and Evangelist
        date_key = date(year, 9, 21)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Matthew, Apostle and Evangelist',
            'date': date_key,
        }

        # Saint Michael and All Angels
        date_key = date(year, 9, 29)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Michael and All Angels',
            'date': date_key,
        }

        # Saint Luke the Evangelist
        date_key = date(year, 10, 18)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Luke the Evangelist',
            'date': date_key,
        }

        # Saint James of Jerusalem, Brother of Our Lord Jesus Christ, and Martyr
        date_key = date(year, 10, 23)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint James of Jerusalem, Brother of Our Lord Jesus Christ, and Martyr',
            'date': date_key,
        }

        # Saint Simon and Saint Jude, Apostles
        date_key = date(year, 10, 28)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Simon and Saint Jude, Apostles',
            'date': date_key,
        }

        # Thanksgiving Day
        date_key = date(year, 11, 1) + rd(weekday=TH(+4))
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Thanksgiving Day',
            'date': date_key,
        }

        # Saint Andrew the Apostle
        date_key = date(year, 11, 30)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Andrew the Apostle',
            'date': date_key,
        }

        # Saint Thomas the Apostle
        date_key = date(year, 12, 21)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Thomas the Apostle',
            'date': date_key,
        }

        # Saint Stephen, Deacon and Martyr
        date_key = date(year, 12, 26)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Stephen, Deacon and Martyr',
            'date': date_key,
        }

        # Saint John, Apostle and Evangelist
        date_key = date(year, 12, 27)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint John, Apostle and Evangelist',
            'date': date_key,
        }

        # The Holy Innocents
        date_key = date(year, 12, 28)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Holy Innocents',
            'date': date_key,
        }

        #============================Tier 4============================

        # Ash Wednesday
        date_key = easter(year) - rd(days=46)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Ash Wednesday',
            'date': date_key,
        }

        #============================Tier 3============================

        # The Sunday of the Passion: Palm Sunday
        date_key = easter(year) - rd(weeks=1)
        name_key = 'PALM_SUNDAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Sunday of the Passion: Palm Sunday',
            'date': date_key,
        }

        # The First Sunday of Advent
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-4))
        name_key = 'FIRST_SUNDAY_OF_ADVENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The First Sunday of Advent',
            'date': date_key,
        }

        #============================Tier 2============================

        # The Holy Name of Our Lord Jesus Christ
        date_key = date(year, 1, 1)
        name_key = 'THE_HOLY_NAME'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Holy Name of Our Lord Jesus Christ',
            'date': date_key,
        }

        # The Presentation of Our Lord Jesus Christ in the Temple
        date_key = date(year, 2, 2)
        name_key = 'THE_PRESENTATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Presentation of Our Lord Jesus Christ in the Temple',
            'date': date_key,
        }

        # The Transfiguration of Our Lord Jesus Christ
        date_key = date(year, 8, 6)
        name_key = 'THE_TRANSFIGURATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Transfiguration of Our Lord Jesus Christ',
            'date': date_key,
        }

        #============================Tier 1============================

        # Eve of Epiphany
        date_key = date(year, 1, 5)
        name_key = 'EVE_OF_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of Epiphany',
            'date': date_key,
        }

        # The Epiphany of Our Lord Jesus Christ
        date_key = date(year, 1, 6)
        name_key = 'THE_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Epiphany of Our Lord Jesus Christ',
            'date': date_key,
        }

        # The Sunday of the Resurrection, or Easter Day
        date_key = easter(year)
        name_key = 'EASTER_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Sunday of the Resurrection, or Easter Day',
            'date': date_key,
        }

        # Ascension Day
        date_key = easter(year) + rd(days=39)
        name_key = 'ASCENSION_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Ascension Day',
            'date': date_key,
        }

        # The Day of Pentecost: Whitsunday
        date_key = easter(year) + rd(weeks=7)
        name_key = 'WHITSUNDAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Day of Pentecost: Whitsunday',
            'date': date_key,
        }

        # The First Sunday after Pentecost: Trinity Sunday
        date_key = easter(year) + rd(days=56)
        name_key = 'TRINITY_SUNDAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The First Sunday after Pentecost: Trinity Sunday',
            'date': date_key,
        }

        # All Saint's Day
        date_key = date(year, 11, 1)
        name_key = 'ALL_SAINTS_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'All Saints Day',
            'date': date_key,
        }

        # Christmas Eve
        date_key = date(year, 12, 24)
        name_key = 'CHRISTMAS_EVE'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Christmas Eve',
            'date': date_key,
        }

        # The Nativity of Our Lord Jesus Christ
        date_key = date(year, 12, 25)
        name_key = 'CHRISTMAS_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Nativity of Our Lord Jesus Christ',
            'date': date_key,
        }

        # Eve of Holy Name
        date_key = date(year, 12, 31)
        name_key = 'EVE_OF_THE_HOLY_NAME'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of Holy Name',
            'date': date_key,
        }


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
        self.lday = LiturgicalDay(year=now.year, switch=True)


class DailyOffice:
    '''
    superclass for the individual offices
    '''

    def __init__(self, now=datetime.now()):
        '''
        initializes the class
        '''
        self.now = now
        self.lday = LiturgicalDay(year=now.year, switch=True)
        self.lspan = LiturgicalSpan(now=now)
        self.cycle = self.get_cycle()
        self.hour = self.get_hour()

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
            if self.now.date() > self.lday.get('first sunday of advent')['date']:
                cycle_enum = 1
            else:
                cycle_enum = 2
        else:
            if self.now.date() < self.lday.get('first sunday of advent')['date']:
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
    d = rd(hours=0)
    test = DailyOffice(now=datetime.now() + d)
    print(str(test.now))
    print(str(test.cycle.value))
    print(str(test.hour.name))
