'''
Daily Office Companion
'''

from calendar import day_name
from dateutil.easter import easter
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from datetime import datetime, date, time

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
        name_key = 'CONFESSION_OF_ST_PETER'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Confession of Saint Peter the Apostle',
            'date': date_key,
        }

        # The Conversion of Saint Paul the Apostle
        date_key = date(year, 1, 25)
        name_key = 'CONVERSION_OF_ST_PAUL'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Conversion of Saint Paul the Apostle',
            'date': date_key,
        }

        # Saint Matthias the Apostle
        date_key = date(year, 2, 24)
        name_key = 'ST_MATTHIAS'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Matthias the Apostle',
            'date': date_key,
        }

        # Saint Joseph
        date_key = date(year, 3, 19)
        name_key = 'ST_JOSEPH'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Joseph',
            'date': date_key,
        }

        # Eve of the Annunciation
        date_key = date(year, 3, 24)
        name_key = 'EVE_OF_THE_ANNUNCIATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of the Annunciation',
            'date': date_key,
            'evening': True,
        }

        # The Annunciation of Our Lord Jesus Christ to the Blessed Virgin Mary
        date_key = date(year, 3, 25)
        name_key = 'THE_ANNUNCIATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Annunciation of Our Lord Jesus Christ to the Blessed Virgin Mary',
            'date': date_key,
        }

        # Saint Mark the Evangelist
        date_key = date(year, 4, 25)
        name_key = 'SS_PHILLIP_JAMES'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Mark the Evangelist',
            'date': date_key,
        }

        # Saint Philip and Saint James, Apostles
        date_key = date(year, 5, 1)
        name_key = 'SS_PHILIP_JAMES'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Philip and Saint James, Apostles',
            'date': date_key,
        }

        # Eve of the Visitation
        date_key = date(year, 5, 30)
        name_key = 'EVE_OF_THE_VISITATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of the Visitation',
            'date': date_key,
            'evening': True,
        }

        # The Visitation of the Blessed Virgin Mary
        date_key = date(year, 5, 31)
        name_key = 'THE_VISITATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Visitation of the Blessed Virgin Mary',
            'date': date_key,
        }

        # Saint Barnabas the Apostle
        date_key = date(year, 6, 11)
        name_key = 'ST_BARNABAS'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Barnabas the Apostle',
            'date': date_key,
        }

        # Eve of Saint John the Baptist
        date_key = date(year, 6, 23)
        name_key = 'EVE_OF_ST_JOHN_THE_BAPTIST'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of Saint John the Baptist',
            'date': date_key,
            'evening': True,
        }

        # The Nativity of Saint John the Baptist
        date_key = date(year, 6, 24)
        name_key = 'ST_JOHN_THE_BAPTIST'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Nativity of Saint John the Baptist',
            'date': date_key,
        }

        # Saint Peter and Saint Paul, Apostles
        date_key = date(year, 6, 29)
        name_key = 'SS_PETER_PAUL'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Peter and Saint Paul, Apostles',
            'date': date_key,
        }

        # Independence Day
        date_key = date(year, 7, 4)
        name_key = 'INDEPENDENCE_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Independence Day',
            'date': date_key,
        }

        # Saint Mary Magdalene
        date_key = date(year, 7, 22)
        name_key = 'ST_MARY_MAGDALENE'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Mary Magdalene',
            'date': date_key,
        }

        # Saint James the Apostle
        date_key = date(year, 7, 25)
        name_key = 'ST_JAMES'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint James the Apostle',
            'date': date_key,
        }

        # Saint Mary the Virgin, Mother of Our Lord Jesus Christ
        date_key = date(year, 8, 15)
        name_key = 'ST_MARY_THE_VIRGIN'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Mary the Virgin, Mother of Our Lord Jesus Christ',
            'date': date_key,
        }

        # Saint Bartholomew the Apostle
        date_key = date(year, 8, 24)
        name_key = 'ST_BARTHOLOMEW'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Bartholomew the Apostle',
            'date': date_key,
        }

        # Eve of Holy Cross
        date_key = date(year, 9, 13)
        name_key = 'EVE_OF_HOLY_CROSS'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of Holy Cross',
            'date': date_key,
            'evening': True,
        }

        # Holy Cross Day
        date_key = date(year, 9, 14)
        name_key = 'HOLY_CROSS_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Holy Cross Day',
            'date': date_key,
        }

        # Saint Matthew, Apostle and Evangelist
        date_key = date(year, 9, 21)
        name_key = 'ST_MATTHEW'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Matthew, Apostle and Evangelist',
            'date': date_key,
        }

        # Saint Michael and All Angels
        date_key = date(year, 9, 29)
        name_key = 'ST_MICHAEL_ALL_ANGELS'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Michael and All Angels',
            'date': date_key,
        }

        # Saint Luke the Evangelist
        date_key = date(year, 10, 18)
        name_key = 'ST_LUKE'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Luke the Evangelist',
            'date': date_key,
        }

        # Saint James of Jerusalem, Brother of Our Lord Jesus Christ, and Martyr
        date_key = date(year, 10, 23)
        name_key = 'ST_JAMES_OF_JERUSALEM'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint James of Jerusalem, Brother of Our Lord Jesus Christ, and Martyr',
            'date': date_key,
        }

        # Saint Simon and Saint Jude, Apostles
        date_key = date(year, 10, 28)
        name_key = 'SS_SIMON_JUDE'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Simon and Saint Jude, Apostles',
            'date': date_key,
        }

        # Thanksgiving Day
        date_key = date(year, 11, 1) + rd(weekday=TH(+4))
        name_key = 'THANKSGIVING_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Thanksgiving Day',
            'date': date_key,
        }

        # Saint Andrew the Apostle
        date_key = date(year, 11, 30)
        name_key = 'ST_ANDREW'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Andrew the Apostle',
            'date': date_key,
        }

        # Saint Thomas the Apostle
        date_key = date(year, 12, 21)
        name_key = 'ST_THOMAS'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Thomas the Apostle',
            'date': date_key,
        }

        # Saint Stephen, Deacon and Martyr
        date_key = date(year, 12, 26)
        name_key = 'ST_STEPHEN'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Stephen, Deacon and Martyr',
            'date': date_key,
        }

        # Saint John, Apostle and Evangelist
        date_key = date(year, 12, 27)
        name_key = 'ST_JOHN'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint John, Apostle and Evangelist',
            'date': date_key,
        }

        # The Holy Innocents
        date_key = date(year, 12, 28)
        name_key = 'HOLY_INNOCENTS'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Holy Innocents',
            'date': date_key,
        }

        #============================Tier 4============================

        # Ash Wednesday
        date_key = easter(year) - rd(days=46)
        name_key = 'ASH_WEDNESDAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Ash Wednesday',
            'date': date_key,
        }

        #============================Tier 3============================

        # First Sunday of Advent
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-4))
        name_key = 'FIRST_SUNDAY_OF_ADVENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'First Sunday of Advent',
            'date': date_key,
        }

        # Second Sunday of Advent
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-3))
        name_key = 'SECOND_SUNDAY_OF_ADVENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Second Sunday of Advent',
            'date': date_key,
        }

        # Third Sunday of Advent
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-2))
        name_key = 'THIRD_SUNDAY_OF_ADVENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Third Sunday of Advent',
            'date': date_key,
        }

        # Fourth Sunday of Advent
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-1))
        name_key = 'FOURTH_SUNDAY_OF_ADVENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Fourth Sunday of Advent',
            'date': date_key,
        }

        # First Sunday after Christmas Day
        date_key = date(year, 12, 25) + rd(days=1, weekday=SU(+1))
        name_key = 'FIRST_SUNDAY_AFTER_CHRISTMAS'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'First Sunday after Christmas Day',
            'date': date_key,
        }

        # Second Sunday after Christmas Day
        date_key = date(year, 12, 25) + rd(days=1, weekday=SU(+2))
        name_key = 'SECOND_SUNDAY_AFTER_CHRISTMAS'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Second Sunday after Christmas Day',
            'date': date_key,
        }

        # First Sunday after the Epiphany: The Baptism of our Lord
        date_key = date(year, 1, 6) + rd(days=1, weekday=SU(+1))
        if date_key >= (easter(year) - rd(days=46, weekday=SU(-1))):
            date_key = date(1970, 1, 1)
        name_key = 'FIRST_SUNDAY_AFTER_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'First Sunday after the Epiphany: The Baptism of our Lord',
            'date': date_key,
        }

        # Second Sunday after the Epiphany
        date_key = date(year, 1, 6) + rd(days=1, weekday=SU(+2))
        if date_key >= (easter(year) - rd(days=46, weekday=SU(-1))):
            date_key = date(1970, 1, 1)
        name_key = 'SECOND_SUNDAY_AFTER_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Second Sunday after the Epiphany',
            'date': date_key,
        }

        # Third Sunday after the Epiphany
        date_key = date(year, 1, 6) + rd(days=1, weekday=SU(+3))
        if date_key >= (easter(year) - rd(days=46, weekday=SU(-1))):
            date_key = date(1970, 1, 1)
        name_key = 'THIRD_SUNDAY_AFTER_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Third Sunday after the Epiphany',
            'date': date_key,
        }

        # Fourth Sunday after the Epiphany
        date_key = date(year, 1, 6) + rd(days=1, weekday=SU(+4))
        if date_key >= (easter(year) - rd(days=46, weekday=SU(-1))):
            date_key = date(1970, 1, 1)
        name_key = 'FOURTH_SUNDAY_AFTER_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Fourth Sunday after the Epiphany',
            'date': date_key,
        }

        # Fifth Sunday after the Epiphany
        date_key = date(year, 1, 6) + rd(days=1, weekday=SU(+5))
        if date_key >= (easter(year) - rd(days=46, weekday=SU(-1))):
            date_key = date(1970, 1, 1)
        name_key = 'FIFTH_SUNDAY_AFTER_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Fifth Sunday after the Epiphany',
            'date': date_key,
        }

        # Sixth Sunday after the Epiphany
        date_key = date(year, 1, 6) + rd(days=1, weekday=SU(+6))
        if date_key >= (easter(year) - rd(days=46, weekday=SU(-1))):
            date_key = date(1970, 1, 1)
        name_key = 'SIXTH_SUNDAY_AFTER_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sixth day after the Epiphany',
            'date': date_key,
        }

        # Seventh Sunday after the Epiphany
        date_key = date(year, 1, 6) + rd(days=1, weekday=SU(+7))
        if date_key >= (easter(year) - rd(days=46, weekday=SU(-1))):
            date_key = date(1970, 1, 1)
        name_key = 'SEVENTH_SUNDAY_AFTER_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Seventh Sunday after the Epiphany',
            'date': date_key,
        }

        # Eighth Sunday after the Epiphany
        date_key = date(year, 1, 6) + rd(days=1, weekday=SU(+8))
        if date_key >= (easter(year) - rd(days=46, weekday=SU(-1))):
            date_key = date(1970, 1, 1)
        name_key = 'EIGHTH_SUNDAY_AFTER_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eighth Sunday after the Epiphany',
            'date': date_key,
        }

        # Last Sunday after the Epiphany
        date_key = (easter(year) - rd(days=46, weekday=SU(-1)))
        name_key = 'LAST_SUNDAY_AFTER_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Last Sunday after the Epiphany',
            'date': date_key,
        }

        # First Sunday in Lent
        date_key = (easter(year) - rd(days=46) + rd(days=1, weekday=SU(+1)))
        name_key = 'FIRST_SUNDAY_IN_LENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'First Sunday in Lent',
            'date': date_key,
        }

        # Second Sunday in Lent
        date_key = (easter(year) - rd(days=46) + rd(days=1, weekday=SU(+2)))
        name_key = 'SECOND_SUNDAY_IN_LENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Second Sunday in Lent',
            'date': date_key,
        }

        # Third Sunday in Lent
        date_key = (easter(year) - rd(days=46) + rd(days=1, weekday=SU(+3)))
        name_key = 'THIRD_SUNDAY_IN_LENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Third Sunday in Lent',
            'date': date_key,
        }

        # Fourth Sunday in Lent
        date_key = (easter(year) - rd(days=46) + rd(days=1, weekday=SU(+4)))
        name_key = 'FOURTH_SUNDAY_IN_LENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Fourth Sunday in Lent',
            'date': date_key,
        }

        # Fifth Sunday in Lent
        date_key = (easter(year) - rd(days=46) + rd(days=1, weekday=SU(+5)))
        name_key = 'FIFTH_SUNDAY_IN_LENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Fifth Sunday in Lent',
            'date': date_key,
        }

        # The Sunday of the Passion: Palm Sunday
        date_key = easter(year) - rd(days=7)
        name_key = 'PALM_SUNDAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Sunday of the Passion: Palm Sunday',
            'date': date_key,
        }

        # Second Sunday of Easter
        date_key = easter(year) + rd(days=1, weekday=SU(+1))
        name_key = 'SECOND_SUNDAY_OF_EASTER'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Second Sunday of Easter',
            'date': date_key,
        }

        # Third Sunday of Easter
        date_key = easter(year) + rd(days=1, weekday=SU(+2))
        name_key = 'THIRD_SUNDAY_OF_EASTER'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Third Sunday of Easter',
            'date': date_key,
        }

        # Fourth Sunday of Easter
        date_key = easter(year) + rd(days=1, weekday=SU(+3))
        name_key = 'FOURTH_SUNDAY_OF_EASTER'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Fourth Sunday of Easter',
            'date': date_key,
        }

        # Fifth Sunday of Easter
        date_key = easter(year) + rd(days=1, weekday=SU(+4))
        name_key = 'FIFTH_SUNDAY_OF_EASTER'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Fifth Sunday of Easter',
            'date': date_key,
        }

        # Sixth Sunday of Easter
        date_key = easter(year) + rd(days=1, weekday=SU(+5))
        name_key = 'SIXTH_SUNDAY_OF_EASTER'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sixth Sunday of Easter',
            'date': date_key,
        }

        # Seventh Sunday of Easter
        date_key = easter(year) + rd(days=1, weekday=SU(+6))
        name_key = 'SEVENTH_SUNDAY_OF_EASTER'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Seventh Sunday of Easter',
            'date': date_key,
        }

        # Proper 3
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-31))
        if date_key <= (easter(year) + rd(days=56)):
            date_key = date(1970, 1, 1)
        name_key = 'PROPER_3'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 4
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-30))
        if date_key <= (easter(year) + rd(days=56)):
            date_key = date(1970, 1, 1)
        name_key = 'PROPER_4'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 5
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-29))
        if date_key <= (easter(year) + rd(days=56)):
            date_key = date(1970, 1, 1)
        name_key = 'PROPER_5'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 6
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-28))
        if date_key <= (easter(year) + rd(days=56)):
            date_key = date(1970, 1, 1)
        name_key = 'PROPER_6'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 7
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-27))
        if date_key <= (easter(year) + rd(days=56)):
            date_key = date(1970, 1, 1)
        name_key = 'PROPER_7'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 8
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-26))
        if date_key <= (easter(year) + rd(days=56)):
            date_key = date(1970, 1, 1)
        name_key = 'PROPER_8'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 9
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-25))
        name_key = 'PROPER_9'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 10
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-24))
        name_key = 'PROPER_10'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 11
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-23))
        name_key = 'PROPER_11'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 12
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-22))
        name_key = 'PROPER_12'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 13
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-21))
        name_key = 'PROPER_13'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 14
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-20))
        name_key = 'PROPER_14'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 15
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-19))
        name_key = 'PROPER_15'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 16
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-18))
        name_key = 'PROPER_16'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 17
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-17))
        name_key = 'PROPER_17'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper =18
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-16))
        name_key = 'PROPER_18'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 19
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-15))
        name_key = 'PROPER_19'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 20
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-14))
        name_key = 'PROPER_20'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 21
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-13))
        name_key = 'PROPER_21'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 22
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-12))
        name_key = 'PROPER_22'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 23
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-11))
        name_key = 'PROPER_23'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 24
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-10))
        name_key = 'PROPER_24'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 25
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-9))
        name_key = 'PROPER_25'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 26
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-8))
        name_key = 'PROPER_26'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 27
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-7))
        name_key = 'PROPER_27'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 28
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-6))
        name_key = 'PROPER_28'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
            'date': date_key,
        }

        # Proper 29
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-5))
        name_key = 'PROPER_29'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Sunday',
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

        # Eve of the Presentation
        date_key = date(year, 2, 1)
        name_key = 'EVE_OF_THE_PRESENTATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of the Presentation',
            'date': date_key,
            'evening': True,
        }

        # The Presentation of Our Lord Jesus Christ in the Temple
        date_key = date(year, 2, 2)
        name_key = 'THE_PRESENTATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Presentation of Our Lord Jesus Christ in the Temple',
            'date': date_key,
        }

        # Eve of the Transfiguration
        date_key = date(year, 8, 5)
        name_key = 'EVE_OF_THE_TRANSFIGURATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of the Transfiguration',
            'date': date_key,
            'evening': True,
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
            'evening': True,
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

        # Eve of Ascension Day
        date_key = easter(year) + rd(days=38)
        name_key = 'EVE_OF_ASCENSION_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of Ascension Day',
            'date': date_key,
            'evening': True,
        }

        # Ascension Day
        date_key = easter(year) + rd(days=39)
        name_key = 'ASCENSION_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Ascension Day',
            'date': date_key,
        }

        # Eve of Pentecost
        date_key = easter(year) + rd(days=48)
        name_key = 'EVE_OF_PENTECOST'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of Pentecost',
            'date': date_key,
            'evening': True,
        }

        # The Day of Pentecost: Whitsunday
        date_key = easter(year) + rd(days=49)
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

        # Eve of All Saints
        date_key = date(year, 10, 31)
        name_key = 'EVE_OF_ALL_SAINTS'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Eve of All Saints',
            'date': date_key,
            'evening': True,
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
            'evening': True,
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
            'evening': True,
        }

class DailyOffice:
    '''
    superclass for the individual offices
    '''

    def __init__(self, now=datetime.now()):
        '''
        initializes the class
        '''
        self.now = now
        self.ldate = LiturgicalDay(year=now.year, switch=False)
        self.lday = LiturgicalDay(year=now.year, switch=True)
        self.cycle = self.get_cycle()
        self.season = self.get_season()
        self.week = self.get_week()
        self.day = self.get_day()
        self.hour = self.get_hour()

    def get_cycle(self):
        '''
        returns the lectionary cycle year (1 or 2)
        '''
        if self.now.year % 2 == 0:
            even_year = True
        else:
            even_year = False
        if even_year:
            if self.now.date() > self.lday.get('first sunday of advent')['date']:
                cycle_year = 'Daily Office Year One'
            else:
                cycle_year = 'Daily Office Year Two'
        else:
            if self.now.date() < self.lday.get('first sunday of advent')['date']:
                cycle_year = 'Daily Office Year One'
            else:
                cycle_year = 'Daily Office Year Two'
        return cycle_year

    def get_first_proper(self):
        '''
        first proper after Trinity Sunday
        '''
        if self.lday.get('PROPER_3')['date'] > date(1970, 1, 1):
            first_proper = 3
        elif self.lday.get('PROPER_4')['date'] > date(1970, 1, 1):
            first_proper = 4
        elif self.lday.get('PROPER_5')['date'] > date(1970, 1, 1):
            first_proper = 5
        elif self.lday.get('PROPER_6')['date'] > date(1970, 1, 1):
            first_proper = 6
        elif self.lday.get('PROPER_7')['date'] > date(1970, 1, 1):
            first_proper = 7
        else:
            first_proper = 8
        return first_proper

    def get_season(self):
        '''
        returns the current season
        '''
        evening = self.now.time() > time(18, 0)
        if bool(evening) and self.now.date() == self.lday.get('CHRISTMAS_EVE')['date']:
            liturgical_season = 'Christmas Season'
        elif bool(evening) and self.now.date() == self.lday.get('EVE_OF_EPIPHANY')['date']:
            liturgical_season = 'Epiphany Season'
        elif self.lday.get('FIRST_SUNDAY_OF_ADVENT')['date'] <= self.now.date() < self.lday.get('CHRISTMAS_DAY')['date']:
            liturgical_season = 'Advent Season'
        elif self.now.date() >= self.lday.get('CHRISTMAS_DAY')['date'] or self.now.date() < self.lday.get('THE_EPIPHANY')['date']:
            liturgical_season = 'Christmas Season'
        elif self.lday.get('THE_EPIPHANY')['date'] <= self.now.date() < self.lday.get('ASH_WEDNESDAY')['date']:
            liturgical_season = 'Epiphany Season'
        elif self.lday.get('ASH_WEDNESDAY')['date'] <= self.now.date() < self.lday.get('EASTER_DAY')['date']:
            liturgical_season = 'The Lenten Season'
        elif self.lday.get('EASTER_DAY')['date'] <= self.now.date() <= self.lday.get('TRINITY_SUNDAY')['date']:
            liturgical_season = 'Easter'
        else:
            liturgical_season = 'The Season after Pentecost'
        return liturgical_season

    def get_week(self):
        '''
        returns the current week
        '''
        proper = self.get_first_proper()
        if self.lday.get('FIRST_SUNDAY_OF_ADVENT')['date'] <= self.now.date() < self.lday.get('SECOND_SUNDAY_OF_ADVENT')['date']:
            week = 'Week of 1 Advent'
        elif self.lday.get('SECOND_SUNDAY_OF_ADVENT')['date'] <= self.now.date() < self.lday.get('THIRD_SUNDAY_OF_ADVENT')['date']:
            week = 'Week of 2 Advent'
        elif self.lday.get('THIRD_SUNDAY_OF_ADVENT')['date'] <= self.now.date() < self.lday.get('FOURTH_SUNDAY_OF_ADVENT')['date']:
            week = 'Week of 3 Advent'
        elif self.lday.get('FOURTH_SUNDAY_OF_ADVENT')['date'] <= self.now.date() < self.lday.get('CHRISTMAS_DAY')['date']:
            week = 'Week of 4 Advent'
        elif self.now.date() >= self.lday.get('CHRISTMAS_DAY')['date'] or self.now.date() < self.lday.get('THE_EPIPHANY')['date']:
            week = 'Christmas Day and Following'
        elif self.lday.get('THE_EPIPHANY')['date'] <= self.now.date() < self.lday.get('FIRST_SUNDAY_AFTER_EPIPHANY')['date']:
            week = 'The Epiphany and Following'
        elif self.lday.get('FIRST_SUNDAY_AFTER_EPIPHANY')['date'] <= self.now.date() < self.lday.get('SECOND_SUNDAY_AFTER_EPIPHANY')['date']:
            week = 'Week of 1 Epiphany'
        elif self.lday.get('SECOND_SUNDAY_AFTER_EPIPHANY')['date'] <= self.now.date() < self.lday.get('THIRD_SUNDAY_AFTER_EPIPHANY')['date']:
            week = 'Week of 2 Epiphany'
        elif self.lday.get('THIRD_SUNDAY_AFTER_EPIPHANY')['date'] <= self.now.date() < self.lday.get('FOURTH_SUNDAY_AFTER_EPIPHANY')['date']:
            week = 'Week of 3 Epiphany'
        elif self.lday.get('FOURTH_SUNDAY_AFTER_EPIPHANY')['date'] <= self.now.date() < self.lday.get('FIFTH_SUNDAY_AFTER_EPIPHANY')['date']:
            week = 'Week of 4 Epiphany'
        elif self.lday.get('FIFTH_SUNDAY_AFTER_EPIPHANY')['date'] <= self.now.date() < self.lday.get('SIXTH_SUNDAY_AFTER_EPIPHANY')['date']:
            week = 'Week of 5 Epiphany'
        elif self.lday.get('SIXTH_SUNDAY_AFTER_EPIPHANY')['date'] <= self.now.date() < self.lday.get('SEVENTH_SUNDAY_AFTER_EPIPHANY')['date']:
            week = 'Week of 6 Epiphany'
        elif self.lday.get('SEVENTH_SUNDAY_AFTER_EPIPHANY')['date'] <= self.now.date() < self.lday.get('EIGHTH_SUNDAY_AFTER_EPIPHANY')['date']:
            week = 'Week of 7 Epiphany'
        elif self.lday.get('EIGHTH_SUNDAY_AFTER_EPIPHANY')['date'] <= self.now.date() < self.lday.get('LAST_SUNDAY_AFTER_EPIPHANY')['date']:
            week = 'Week of 8 Epiphany'
        elif self.lday.get('LAST_SUNDAY_AFTER_EPIPHANY')['date'] <= self.now.date() < self.lday.get('FIRST_SUNDAY_IN_LENT')['date']:
            week = 'Week of Last Epiphany'
        elif self.lday.get('FIRST_SUNDAY_IN_LENT')['date'] <= self.now.date() < self.lday.get('SECOND_SUNDAY_IN_LENT')['date']:
            week = 'Week of 1 Lent'
        elif self.lday.get('SECOND_SUNDAY_IN_LENT')['date'] <= self.now.date() < self.lday.get('THIRD_SUNDAY_IN_LENT')['date']:
            week = 'Week of 2 Lent'
        elif self.lday.get('THIRD_SUNDAY_IN_LENT')['date'] <= self.now.date() < self.lday.get('FOURTH_SUNDAY_IN_LENT')['date']:
            week = 'Week of 3 Lent'
        elif self.lday.get('FOURTH_SUNDAY_IN_LENT')['date'] <= self.now.date() < self.lday.get('FIFTH_SUNDAY_IN_LENT')['date']:
            week = 'Week of 4 Lent'
        elif self.lday.get('FIFTH_SUNDAY_IN_LENT')['date'] <= self.now.date() < self.lday.get('PALM_SUNDAY')['date']:
            week = 'Week of 5 Lent'
        elif self.lday.get('PALM_SUNDAY')['date'] <= self.now.date() < self.lday.get('EASTER_DAY')['date']:
            week = 'Holy Week'
        elif self.lday.get('EASTER_DAY')['date'] <= self.now.date() < self.lday.get('SECOND_SUNDAY_OF_EASTER')['date']:
            week = 'Easter Week'
        elif self.lday.get('SECOND_SUNDAY_OF_EASTER')['date'] <= self.now.date() < self.lday.get('THIRD_SUNDAY_OF_EASTER')['date']:
            week = 'Week of 2 Easter'
        elif self.lday.get('THIRD_SUNDAY_OF_EASTER')['date'] <= self.now.date() < self.lday.get('FOURTH_SUNDAY_OF_EASTER')['date']:
            week = 'Week of 3 Easter'
        elif self.lday.get('FOURTH_SUNDAY_OF_EASTER')['date'] <= self.now.date() < self.lday.get('FIFTH_SUNDAY_OF_EASTER')['date']:
            week = 'Week of 4 Easter'
        elif self.lday.get('FIFTH_SUNDAY_OF_EASTER')['date'] <= self.now.date() < self.lday.get('SIXTH_SUNDAY_OF_EASTER')['date']:
            week = 'Week of 5 Easter'
        elif self.lday.get('SIXTH_SUNDAY_OF_EASTER')['date'] <= self.now.date() < self.lday.get('SEVENTH_SUNDAY_OF_EASTER')['date']:
            week = 'Week of 6 Easter'
        elif self.lday.get('SEVENTH_SUNDAY_OF_EASTER')['date'] <= self.now.date() < self.lday.get('WHITSUNDAY')['date']:
            week = 'Week of 7 Easter'
        elif self.lday.get('WHITSUNDAY')['date'] <= self.now.date() < self.lday.get('TRINITY_SUNDAY')['date']:
            week = 'Week of Proper ' + str(proper-2)
        elif self.lday.get('TRINITY_SUNDAY')['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper))['date']:
            week = 'Week of Proper ' + str(proper-1)
        elif self.lday.get('PROPER_' + str(proper))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+1))['date']:
            week = 'Week of Proper ' + str(proper)
        elif self.lday.get('PROPER_' + str(proper+1))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+2))['date']:
            week = 'Week of Proper ' + str(proper+1)
        elif self.lday.get('PROPER_' + str(proper+2))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+3))['date']:
            week = 'Week of Proper ' + str(proper+2)
        elif self.lday.get('PROPER_' + str(proper+3))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+4))['date']:
            week = 'Week of Proper ' + str(proper+3)
        elif self.lday.get('PROPER_' + str(proper+4))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+5))['date']:
            week = 'Week of Proper ' + str(proper+4)
        elif self.lday.get('PROPER_' + str(proper+5))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+6))['date']:
            week = 'Week of Proper ' + str(proper+5)
        elif self.lday.get('PROPER_' + str(proper+6))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+7))['date']:
            week = 'Week of Proper ' + str(proper+6)
        elif self.lday.get('PROPER_' + str(proper+7))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+8))['date']:
            week = 'Week of Proper ' + str(proper+7)
        elif self.lday.get('PROPER_' + str(proper+8))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+9))['date']:
            week = 'Week of Proper ' + str(proper+8)
        elif self.lday.get('PROPER_' + str(proper+9))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+10))['date']:
            week = 'Week of Proper ' + str(proper+9)
        elif self.lday.get('PROPER_' + str(proper+10))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+11))['date']:
            week = 'Week of Proper ' + str(proper+10)
        elif self.lday.get('PROPER_' + str(proper+11))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+12))['date']:
            week = 'Week of Proper ' + str(proper+11)
        elif self.lday.get('PROPER_' + str(proper+12))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+13))['date']:
            week = 'Week of Proper ' + str(proper+12)
        elif self.lday.get('PROPER_' + str(proper+13))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+14))['date']:
            week = 'Week of Proper ' + str(proper+13)
        elif self.lday.get('PROPER_' + str(proper+14))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+15))['date']:
            week = 'Week of Proper ' + str(proper+14)
        elif self.lday.get('PROPER_' + str(proper+15))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+16))['date']:
            week = 'Week of Proper ' + str(proper+15)
        elif self.lday.get('PROPER_' + str(proper+16))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+17))['date']:
            week = 'Week of Proper ' + str(proper+16)
        elif self.lday.get('PROPER_' + str(proper+17))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+18))['date']:
            week = 'Week of Proper ' + str(proper+17)
        elif self.lday.get('PROPER_' + str(proper+18))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+19))['date']:
            week = 'Week of Proper ' + str(proper+18)
        elif self.lday.get('PROPER_' + str(proper+19))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+20))['date']:
            week = 'Week of Proper ' + str(proper+19)
        elif self.lday.get('PROPER_' + str(proper+20))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+21))['date']:
            week = 'Week of Proper ' + str(proper+20)
        elif self.lday.get('PROPER_' + str(proper+21))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+22))['date']:
            week = 'Week of Proper ' + str(proper+21)
        elif self.lday.get('PROPER_' + str(proper+22))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+23))['date']:
            week = 'Week of Proper ' + str(proper+22)
        elif self.lday.get('PROPER_' + str(proper+23))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+24))['date']:
            week = 'Week of Proper ' + str(proper+23)
        elif self.lday.get('PROPER_' + str(proper+24))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+25))['date']:
            week = 'Week of Proper ' + str(proper+24)
        elif self.lday.get('PROPER_' + str(proper+25))['date'] <= self.now.date() < self.lday.get('PROPER_' + str(proper+26))['date']:
            week = 'Week of Proper ' + str(proper+25)
        return week

    def get_day(self):
        '''
        returns relevant holy date or day of week name
        '''
        evening = self.now.time() > time(18, 0)
        if self.now.date() in self.ldate:
            day_dict = self.ldate.get(self.now.date())
            if evening:
                day = day_dict['name']
            elif 'evening' not in day_dict:
                day = day_dict['name']
            else:
                day = day_name[self.now.date().weekday()]
        else:
            day = day_name[self.now.date().weekday()]
        return day

    def get_hour(self):
        '''
        returns the appropriate cannonical hour based on time
        '''
        test_now = self.now.replace(year=1970, month=1, day=1, tzinfo=None)
        morning = abs((test_now - datetime(1970, 1, 1, 6, 0)).total_seconds())
        noonday = abs((test_now - datetime(1970, 1, 1, 12, 0)).total_seconds())
        evening = abs((test_now - datetime(1970, 1, 1, 18, 0)).total_seconds())
        compline = abs((test_now - datetime(1970, 1, 1, 21, 0)).total_seconds())
        diffs = (morning, noonday, evening, compline)
        hours_enum = diffs.index(min(diffs))
        if hours_enum == 0:
            canonical_hour = 'Daily Morning Prayer'
        elif hours_enum == 1:
            canonical_hour = 'An Order of Service for Noonday'
        elif hours_enum == 2:
            canonical_hour = 'Daily Evening Prayer'
        elif hours_enum == 3:
            canonical_hour = 'An Order for Compline'
        return canonical_hour


if __name__ == '__main__':
    d = rd(days=0)
    test = DailyOffice(now=datetime.now() + d)
    print(test.cycle)
    print(test.season)
    print(test.week)
    print(test.day)
    print(test.hour)
