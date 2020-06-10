from abc import ABC, abstractmethod
import fiz_l
import marriage

#ABC - когда запрещено создавать экземпляр класса - нужно создавать наследника

class Property(ABC):
    def __init__(self):
        self.definition = 'Имуществом признаются материальные и нематериальные объекты, которые могут быть предметами владения, пользования или распоряжения'
        self.owner = None # владелец
        self.price = None
        self.description = None
        self.list_of_owners = []
        self.dates_of_change_owner = []
        self.time_in_possession = None


# проверить порядок наследования
class Vesh(Property, ABC):
    def __init__(self):
        super().__init__()
        self.definition = 'осязаемый, материальный предмет, представляющий имущественную ценность'
        self.sobstvennik = None
        self.owner = None

    def add_sobstvennik(self, person):
        '''
        Добавление собственника
        :param person:
        :return:
        '''
        print("Введите дату приобретения имущества (дата государственной регистрации перехода права собственности (выписка из ЕГРН)): ")
        date = input()
        date_of_ownership = fiz_l.to_date(date)
        date_of_ownership = fiz_l.datetime.date(date_of_ownership[0], date_of_ownership[1], date_of_ownership[2])
        self.dates_of_change_owner.append(date_of_ownership)
        # проверка на наличие брака
        if not marriage.marriage_property_check(person.married['date_of_marriage'], date_of_ownership): # если нет
            self.list_of_owners.append(person)
            person.property.append(self)
            self.sobstvennik = person
            self.owner = person
        # если приобретено в браке
        else:
            self.list_of_owners.append((person, person.married['married_to']))
        # TODO нужна метка о виде собственности (совместная)
            person.property.append(self)
            person.married['married_to'].property.append(self)
            self.sobstvennik = (person, person.married['married_to'])
            self.owner = (person, person.married['married_to'])

# проверить порядок наследования
class Nedvizhimost(Vesh, ABC):
    def __init__(self):
        super().__init__()
        self.definition = 'все, что прочно связано с землей, то есть объекты, перемещение которых без несоразмерного ущерба их назначению невозможно, в том числе здания, сооружения, объекты незавершенного строительства'

'''
Ниже - описание видов недвижимости
'''
class Zhiloe_pomeshenie(Nedvizhimost):
    def __init__(self):
        super().__init__()
        self.definition = 'изолированное помещение, которое является недвижимым имуществом и пригодно для постоянного проживания граждан'
        self.ploshad = None
        self.address = None
        self.date_of_ownership = None

    def __str__(self):
        return f'Жилое помещение - адрес: {self.address}'

    def __repr__(self):
        return f'Жилое помещение - адрес: {self.address}'

# проверить порядок наследования
class Dvizhimie_veshi(Vesh, ABC):
    def __init__(self):
        super().__init__()
        self.definition = 'все вещи, которые не относятся к недвижимости'


class Dengi_nalichnie(Dvizhimie_veshi):
    def __init__(self):
        super().__init__()
        self.definition = 'особый вид универсального товара, используемого в качестве всеобщего эквивалента, посредством которого выражается стоимость всех других товаров'

class Tsennie_bumagi_dokumentarnie(Dvizhimie_veshi):
    def __init__(self):
        super().__init__()
        self.definition = 'ценная бумага на физическом носителе (бумаге)'

class Inoe_imushestvo(Property):
    def __init__(self):
        super().__init__()
        self.definition = ''

class Imushestvennie_prava(Inoe_imushestvo):
    def __init__(self):
        super().__init__()
        self.definition = ''

class Denigi_beznalichnie(Imushestvennie_prava):
    def __init__(self):
        super().__init__()
        self.definition = ''

class Tsennie_bumagi_bezdokumentarnie(Imushestvennie_prava):
    def __init__(self):
        super().__init__()
        self.definition = 'ценная бумага без физического носителя'

class Tsifrovie_prava(Imushestvennie_prava):
    def __init__(self):
        super().__init__()
        self.definition = ''

class Rezultati_rabot_uslug(Property):
    def __init__(self):
        super().__init__()
        self.definition = ''

class Rezultati_intellektualnoi_deyatelnosti():
    def __init__(self):
        super().__init__()
        self.definition = ''

class Nematerialnie_blaga():
    def __init__(self):
        super().__init__()
        self.definition = ''


# def add_sobstvennik(vesh, person):
#     vesh.sobstvennik = person
#     print("Введите дату приобретения (дата государственной регистрации перехода права собственности (выписка из ЕГРН)): ")
#     date = input()
#     date_of_ownership = Fiz_l.to_date(date)
#     date_of_ownership = datetime.date(date_of_ownership[0], date_of_ownership[1], date_of_ownership[2])
#     vesh.dates_of_change_owner.append(date_of_ownership)
#     vesh.list_of_owners.append(person)
#     person.property.append(vesh)
