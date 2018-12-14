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
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # The Conversion of Saint Paul the Apostle
        date_key = date(year, 1, 25)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Conversion of Saint Paul the Apostle',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Matthias the Apostle
        date_key = date(year, 2, 24)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Matthias the Apostle',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Joseph
        date_key = date(year, 3, 19)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Joseph',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # The Annunciation of Our Lord Jesus Christ to the Blessed Virgin Mary
        date_key = date(year, 3, 25)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Annunciation of Our Lord Jesus Christ to the Blessed Virgin Mary',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Mark the Evangelist
        date_key = date(year, 4, 25)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Mark the Evangelist',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Philip and Saint James, Apostles
        date_key = date(year, 5, 1)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Philip and Saint James, Apostles',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # The Visitation of the Blessed Virgin Mary
        date_key = date(year, 5, 31)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Visitation of the Blessed Virgin Mary',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Barnabas the Apostle
        date_key = date(year, 6, 11)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Barnabas the Apostle',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # The Nativity of Saint John the Baptist
        date_key = date(year, 6, 24)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Nativity of Saint John the Baptist',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Peter and Saint Paul, Apostles
        date_key = date(year, 6, 29)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Peter and Saint Paul, Apostles',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Independence Day
        date_key = date(year, 7, 4)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Independence Day',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Mary Magdalene
        date_key = date(year, 7, 22)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Mary Magdalene',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }
        # Saint James the Apostle
        date_key = date(year, 7, 25)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint James the Apostle',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Mary the Virgin, Mother of Our Lord Jesus Christ
        date_key = date(year, 8, 15)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Mary the Virgin, Mother of Our Lord Jesus Christ',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Bartholomew the Apostle
        date_key = date(year, 8, 24)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Bartholomew the Apostle',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Holy Cross Day
        date_key = date(year, 9, 14)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Holy Cross Day',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Matthew, Apostle and Evangelist
        date_key = date(year, 9, 21)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Matthew, Apostle and Evangelist',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Michael and All Angels
        date_key = date(year, 9, 29)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Michael and All Angels',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Luke the Evangelist
        date_key = date(year, 10, 18)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Luke the Evangelist',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint James of Jerusalem, Brother of Our Lord Jesus Christ, and Martyr
        date_key = date(year, 10, 23)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint James of Jerusalem, Brother of Our Lord Jesus Christ, and Martyr',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Simon and Saint Jude, Apostles
        date_key = date(year, 10, 28)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Simon and Saint Jude, Apostles',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Thanksgiving Day
        date_key = date(year, 11, 1) + rd(weekday=TH(+4))
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Thanksgiving Day',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Andrew the Apostle
        date_key = date(year, 11, 30)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Andrew the Apostle',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Thomas the Apostle
        date_key = date(year, 12, 21)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Thomas the Apostle',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint Stephen, Deacon and Martyr
        date_key = date(year, 12, 26)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint Stephen, Deacon and Martyr',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # Saint John, Apostle and Evangelist
        date_key = date(year, 12, 27)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Saint John, Apostle and Evangelist',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        # The Holy Innocents
        date_key = date(year, 12, 28)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Holy Innocents',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm ',
            'psalm_evening': 'Psalm ',
            'reading_morning_y1': '',
            'reading_morning_y2': '',
            'reading_evening_y1': '',
            'reading_evening_y2': '',
        }

        #============================Tier 4============================

        # Ash Wednesday
        date_key = easter(year) - rd(days=46)
        name_key = ''
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Ash Wednesday',
            'date': date_key,
            'collect_traditional': 'page  under ""',
            'collect_contemporary': 'page  under ""',
            'psalm_morning': 'Psalm 95 (for invitatory), 32, 143',
            'psalm_evening': 'Psalm 102, 130',
            'reading_morning_y1': 'Jonah 3:1--4:11      Heb. 12:1-14',
            'reading_morning_y2': 'Amos 5:6-15      Heb. 12:1-14',
            'reading_evening_y1': 'Luke 18:9-14',
            'reading_evening_y2': 'Luke 18:9-14',
        }

        #============================Tier 3============================

        # The Sunday of the Passion: Palm Sunday
        date_key = easter(year) - rd(weeks=1)
        name_key = 'PALM_SUNDAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Sunday of the Passion: Palm Sunday',
            'date': date_key,
            'collect_traditional': 'page 168 under "Sunday of the Passion: Palm Sunday"',
            'collect_contemporary': 'page 219 under "Sunday of the Passion: Palm Sunday"',
            'psalm_morning': 'Psalm 24, 29',
            'psalm_evening': 'Psalm 103',
            'reading_morning_y1': 'Zech. 9:9-12      1 Tim. 6:12-16',
            'reading_morning_y2': 'Zech. 9:9-12      1 Tim. 6:12-16',
            'reading_evening_y1': 'Zech. 12:9-11, 13:1, 7-9      Matt. 21:12-17',
            'reading_evening_y2': 'Zech. 12:9-11; 13:1, 7-9      Luke 19:41-48',
        }

        # The First Sunday of Advent
        date_key = date(year, 12, 25) - rd(days=1, weekday=SU(-4))
        name_key = 'FIRST_SUNDAY_OF_ADVENT'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The First Sunday of Advent',
            'date': date_key,
            'collect_traditional': 'page 159 under "First Sunday of Advent"',
            'collect_contemporary': 'page 211 under "First Sunday of Advent"',
            'psalm_morning': 'Psalm 146 ,147',
            'psalm_evening': 'Psalm 111, 112, 113',
            'reading_morning_y1': 'Isa. 1:1-9',
            'reading_morning_y2': 'Amos 1:1-5, 13--2:8      1Thess. 5:1-11',
            'reading_evening_y1': '2 Pet. 3:1-10',
            'reading_evening_y2': 'Luke 21:5-19',
        }

        #============================Tier 2============================

        # The Holy Name of Our Lord Jesus Christ
        date_key = date(year, 1, 1)
        name_key = 'THE_HOLY_NAME'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Holy Name of Our Lord Jesus Christ',
            'date': date_key,
            'collect_traditional': 'page 162 under "The Holy Name"',
            'collect_contemporary': 'page 213 under "The Holy Name"',
            'psalm_morning': 'Psalm 103',
            'psalm_evening': 'Psalm 148',
            'reading_morning_y1': 'Gen. 17:1-12a, 15-16      Col. 2:6-12',
            'reading_morning_y2': 'Isa. 62:1-5, 10-12      Rev. 19:11-16',
            'reading_evening_y1': 'John 16:23b-30',
            'reading_evening_y2': 'Matt. 1:18-25',
        }

        # The Presentation of Our Lord Jesus Christ in the Temple
        date_key = date(year, 2, 2)
        name_key = 'THE_PRESENTATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Presentation of Our Lord Jesus Christ in the Temple',
            'date': date_key,
            'collect_traditional': 'page 187 under "The Presentation"',
            'collect_contemporary': 'page 239 under "The Presentation"',
            'psalm_morning': 'Psalm 42, 43',
            'psalm_evening': 'Psalm 48, 87',
            'reading_morning_y1': '1 Samuel 2:1-10      John 8:31-36',
            'reading_morning_y2': '1 Samuel 2:1-10      John 8:31-36',
            'reading_evening_y1': 'Haggai 2:1-9      1 John 3:1-8',
            'reading_evening_y2': 'Haggai 2:1-9      1 John 3:1-8',
        }

        # The Transfiguration of Our Lord Jesus Christ
        date_key = date(year, 8, 6)
        name_key = 'THE_TRANSFIGURATION'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Transfiguration of Our Lord Jesus Christ',
            'date': date_key,
            'collect_traditional': 'page 191 under "The Transfiguration "',
            'collect_contemporary': 'page 243 under "The Transfiguration "',
            'psalm_morning': 'Psalm 2, 24',
            'psalm_evening': 'Psalm 72',
            'reading_morning_y1': 'Exodus 24:12-18      2 Corinthians 4:1-6',
            'reading_morning_y2': 'Exodus 24:12-18      2 Corinthians 4:1-6',
            'reading_evening_y1': 'Daniel 7:9-10,13-14      John 12:27-36a',
            'reading_evening_y2': 'Daniel 7:9-10,13-14      John 12:27-36a',
        }

        #============================Tier 1============================

        # Eve of Epiphany
        date_key = date(year, 1, 5)
        name_key = 'EVE_OF_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        collect_traditional_val = 'page 161 under "First Sunday after Christmas Day"'
        collect_contemporary_val = 'page 213 under "First Sunday after Christmas Day"'
        if date_key > (date(year, 12, 25) + rd(days=1, weekday=SU(+2))):
            collect_traditional_val = 'page 162 under "Second Sunday after Christmas Day"'
            collect_contemporary_val = 'page 214 under "Second Sunday after Christmas Day"'
        self[switch_key] = {
            'name': 'Eve of Epiphany',
            'date': date_key,
            'collect_traditional': collect_traditional_val,
            'collect_contemporary': collect_contemporary_val,
            'psalm_morning': 'Psalm 2, 110:1-5(6-7)',
            'psalm_evening': 'Psalm 29, 98',
            'reading_morning_y1': 'Jonah 2:2-9      Eph. 6:10-20      John 11:17-27, 38-44',
            'reading_morning_y2': 'Joshua 1:1-9      Heb. 11:32--12:2      John 15:1-16',
            'reading_evening_y1': 'Isa. 66:18-23      Rom. 15:7-13',
            'reading_evening_y2': 'Isa. 66:18-23      Rom. 15:7-13',
        }

        # The Epiphany of Our Lord Jesus Christ
        date_key = date(year, 1, 6)
        name_key = 'THE_EPIPHANY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The Epiphany of Our Lord Jesus Christ',
            'date': date_key,
            'collect_traditional': 'page 162 under "The Epiphany"',
            'collect_contemporary': 'page 214 under "The Epiphany"',
            'psalm_morning': 'Psalm 46, 97',
            'psalm_evening': 'Psalm 96, 100',
            'reading_morning_y1': 'Isa. 52:7-10      Rev. 21:22-27',
            'reading_morning_y2': 'Isa. 49:1-7      Rev. 21:22-27',
            'reading_evening_y1': 'Matt. 12:14-21',
            'reading_evening_y2': 'Matt. 12-14-21',
        }

        # The Sunday of the Resurrection, or Easter Day
        date_key = easter(year)
        name_key = 'EASTER_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        collect_traditional_val = choice([
            'page 170 under "Easter Day" first selection',
            'page 170 under "Easter Day" second selection',
            'page 170 under "Easter Day" third selection'
        ])
        collect_contemporary_val = choice([
            'page 170 under "Easter Day" first selection',
            'page 170 under "Easter Day" second selection',
            'page 170 under "Easter Day" third selection'
        ])
        psalm_evening_val = choice([
            'Psalm 113, 114',
            'Psalm 113, 118'
        ])
        reading_evening_val = choice([
            'Isa. 51:9-11      Luke 24:13-35',
            'Isa. 51:9-11      John 20:19-23',
        ])
        self[switch_key] = {
            'name': 'The Sunday of the Resurrection, or Easter Day',
            'date': date_key,
            'collect_traditional': collect_traditional_val,
            'collect_contemporary': collect_contemporary_val,
            'psalm_morning': 'Psalm 148, 149, 150',
            'psalm_evening': psalm_evening_val,
            'reading_morning_y1': 'Exod. 12:1-14      John 1:1-18',
            'reading_morning_y2': 'Exod. 12:1-14      John 1:1-18',
            'reading_evening_y1': reading_evening_val,
            'reading_evening_y2': reading_evening_val,
        }

        # Ascension Day
        date_key = easter(year) + rd(days=39)
        name_key = 'ASCENSION_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        collect_traditional_val = choice([
            'page 174 under "Ascension Day" first selection',
            'page 174 under "Ascension Day" second selection'
        ])
        collect_contemporary_val = choice([
            'page 226 under "Ascension Day" first selection',
            'page 226 under "Ascension Day" second selection'
        ])
        self[switch_key] = {
            'name': 'Ascension Day',
            'date': date_key,
            'collect_traditional': collect_traditional_val,
            'collect_contemporary': collect_contemporary_val,
            'psalm_morning': 'Psalm 8, 47',
            'psalm_evening': 'Psalm 24, 96',
            'reading_morning_y1': 'Ezek. 1:14, 24-28b      Heb. 2:5-18',
            'reading_morning_y2': 'Dan. 7:9-14      Heb. 2:5-18',
            'reading_evening_y1': 'Matt. 28:16-20',
            'reading_evening_y2': 'Matt. 28:16-20',
        }

        # The Day of Pentecost: Whitsunday
        date_key = easter(year) + rd(weeks=7)
        name_key = 'WHITSUNDAY'
        switch_key = self.key_switcher(date_key, name_key)
        collect_traditional_val = choice([
            'page 175 under "The Day of Pentecost: Whitsunday" first selection',
            'page 175 under "The Day of Pentecost: Whitsunday" second selection'
        ])
        collect_contemporary_val = choice([
            'page 227 under "The Day of Pentecost: Whitsunday" first selection',
            'page 227 under "The Day of Pentecost: Whitsunday" second selection'
        ])
        self[switch_key] = {
            'name': 'The Day of Pentecost: Whitsunday',
            'date': date_key,
            'collect_traditional': collect_traditional_val,
            'collect_contemporary': collect_contemporary_val,
            'psalm_morning': 'Psalm 118',
            'psalm_evening': 'Psalm 145',
            'reading_morning_y1': 'Isa. 11:1-9      1 Cor. 2:1-13',
            'reading_morning_y2': 'Deut. 16:9-12      Acts 4:18-21, 23-33',
            'reading_evening_y1': 'John 14:21-29',
            'reading_evening_y2': 'John 4:19-26',
        }

        # The First Sunday after Pentecost: Trinity Sunday
        date_key = easter(year) + rd(days=56)
        name_key = 'TRINITY_SUNDAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'The First Sunday after Pentecost: Trinity Sunday',
            'date': date_key,
            'collect_traditional': 'page 176 under "The First Sunday after Pentecost: Trinity Sunday"',
            'collect_contemporary': 'page 228 under "The First Sunday after Pentecost: Trinity Sunday"',
            'psalm_morning': 'Psalm 146, 147',
            'psalm_evening': 'Psalm 111, 112, 113',
            'reading_morning_y1': 'Ecclus. 43:1-12(27-33)      Eph. 4:1-16',
            'reading_morning_y2': 'Job 38:1-11, 42:1-5      Rev. 19:4-16',
            'reading_evening_y1': 'John 1:1-18',
            'reading_evening_y2': 'John 1:29-34',
        }

        # All Saint's Day
        date_key = date(year, 11, 1)
        name_key = 'ALL_SAINTS_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'All Saints Day',
            'date': date_key,
            'collect_traditional': 'page 194 under "All Saints Day"',
            'collect_contemporary': 'page 245 under "All Saints Day"',
            'psalm_morning': 'Psalm 111, 112',
            'psalm_evening': 'Psalm 148, 150',
            'reading_morning_y1': '2 Esdras 2:42-47      Hebrews 11:32--12:2',
            'reading_morning_y2': '2 Esdras 2:42-47      Hebrews 11:32--12:2',
            'reading_evening_y1': 'Wisdom 5:1-5,14-16      Revelation 21:1-4,22--22:5',
            'reading_evening_y2': 'Wisdom 5:1-5,14-16      Revelation 21:1-4,22--22:5',
        }

        # Christmas Eve
        date_key = date(year, 12, 24)
        name_key = 'CHRISTMAS_EVE'
        switch_key = self.key_switcher(date_key, name_key)
        self[switch_key] = {
            'name': 'Christmas Eve',
            'date': date_key,
            'collect_traditional': 'page 160 under "Fourth Sunday of Advent"',
            'collect_contemporary': 'page 212 under "Fourth Sunday of Advent"',
            'psalm_morning': 'Psalm 45, 46',
            'psalm_evening': 'Psalm 89:1-29',
            'reading_morning_y1': 'Isa. 35:1-10      Rev. 22:12-17, 21      Luke 1:67-80',
            'reading_morning_y2': 'Baruch 4:36--5:9      Mat. 1:18-25',
            'reading_evening_y1': 'Baruch 4:36--5:9      Gal. 3:23--4:7      Mat. 1:18-25',
            'reading_evening_y2': 'Isa. 59:15b-21      Phil. 2:5-11',
        }

        # The Nativity of Our Lord Jesus Christ
        date_key = date(year, 12, 25)
        name_key = 'CHRISTMAS_DAY'
        switch_key = self.key_switcher(date_key, name_key)
        collect_traditional_val = choice([
            'page 160 under "The Nativity of Our Lord: Christmas Day" first selection',
            'page 161 under "The Nativity of Our Lord: Christmas Day" second selection',
            'page 161 under "The Nativity of Our Lord: Christmas Day" third selection'
        ])
        collect_contemporary_val = choice([
            'page 212 under "The Nativity of Our Lord: Christmas Day" first selection',
            'page 212 under "The Nativity of Our Lord: Christmas Day" second selection',
            'page 213 under "The Nativity of Our Lord: Christmas Day" third selection'
        ])
        self[switch_key] = {
            'name': 'The Nativity of Our Lord Jesus Christ',
            'date': date_key,
            'collect_traditional': collect_traditional_val,
            'collect_contemporary': collect_contemporary_val,
            'psalm_morning': 'Psalm 2, 85',
            'psalm_evening': 'Psalm 110:1-5(6-7), 132',
            'reading_morning_y1': 'Zech. 2:10-13      1 John 4:7-16',
            'reading_morning_y2': 'Micah 4:1-5; 5:2-4      1 John 4:7-16',
            'reading_evening_y1': 'John 3:31-36',
            'reading_evening_y2': 'John 3:31-36',
        }

        # Eve of Holy Name
        date_key = date(year, 12, 31)
        name_key = 'EVE_OF_THE_HOLY_NAME'
        switch_key = self.key_switcher(date_key, name_key)
        collect_traditional_val = 'page 161 under "First Sunday after Christmas Day"'
        collect_contemporary_val = 'page 213 under "First Sunday after Christmas Day"'
        if date_key < (date(year, 12, 25) + rd(days=1, weekday=SU(+1))):
            collect_traditional_val = choice([
                'page 160 under "The Nativity of Our Lord: Christmas Day" first selection',
                'page 161 under "The Nativity of Our Lord: Christmas Day" second selection',
                'page 161 under "The Nativity of Our Lord: Christmas Day" third selection'
            ])
            collect_contemporary_val = choice([
                'page 212 under "The Nativity of Our Lord: Christmas Day" first selection',
                'page 212 under "The Nativity of Our Lord: Christmas Day" second selection',
                'page 213 under "The Nativity of Our Lord: Christmas Day" third selection'
            ])
        self[switch_key] = {
            'name': 'Eve of Holy Name',
            'date': date_key,
            'collect_traditional': collect_traditional_val,
            'collect_contemporary': collect_contemporary_val,
            'psalm_morning': 'Psalm 46, 48',
            'psalm_evening': 'Psalm 90',
            'reading_morning_y1': 'Isa. 26:1-9      2 Cor. 5:16--6:2      John 8:12-19',
            'reading_morning_y2': 'Isa. 49:1-7      Rev. 21:22-27',
            'reading_evening_y1': '1 kings 3:5-14      James 4:13-17; 5:7-11      John 5:1-15',
            'reading_evening_y2': 'Isa. 65:15b-25      Rev. 21:1-6',
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
