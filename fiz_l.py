# попытка реализовать главу 3 Семейного кодекса
import datetime
import marriage
import property


class Fiz_l:
    def __init__(self, date_of_birth, sex, surname: str, name: str, fathername: str):
        self.date_of_birth = to_date(date_of_birth)
        self.age = to_age(self.date_of_birth)
        if sex == 'male' or sex == 'female':
            self.sex = sex
        else:
            raise ValueError("Мужчина - 'male', Женщина - 'female'")
        self.surname = surname
        self.name = name
        self.fathername = fathername
        self.relatives = []
        self.status = {'live': {'alive': True},
                       'marriage': {'married': False,
                                    'married_to': None,
                                    'date_of_marriage': None,
                                    'duration_of_marriage': None},
                       'capacity': {'full_deesposobnost': True if self.age >= 18 else False,
                                    'ogranicheniya': False}}
        self.property = []

    def __str__(self):
        return f'{self.surname} {self.name} {self.fathername}'

    def __repr__(self):
        return f'{self.surname} {self.name} {self.fathername}'

def to_date(date):
    l = []
    dt = date.split('.')
    for i in dt:
        i = int(i)
        l.append(i)
    dt = datetime.date(l[0], l[1], l[2])
    return dt

def to_age(date_of_birth):
    # считаем разницу в годах
    today = datetime.date.today()
    temp_date = date_of_birth.replace(today.year)  # timedelta работает с днями, поэтому вводим врем. переменную
    if temp_date > today:  # если ДР в этом году еще не наступил
        return today.year - date_of_birth.year - 1
    else:  # если ДР уже наступил
        return today.year - date_of_birth.year

class Actions:
    ...

if __name__ == "__main__":
    person_1 = Fiz_l(date_of_birth='1991.8.6', sex='male', surname='Коваленко', name='Евгений', fathername="Николаевич")
    person_2 = Fiz_l(date_of_birth='1990.10.28', sex='female', surname='Дуркина', name='Мария', fathername="Юрьевна")

    # проверка модуля marriage
    # marriage.marriage_func(person_1, person_2)
    # print(f'Брак с: {person_2.status["marriage"]["married_to"]} \n'
    #       f'Дата заключения брака: {person_2.status["marriage"]["date_of_marriage"]}')


    #temp
    person_1.status["marriage"]['married'] = True
    person_1.status["marriage"]['married_to'] = person_2
    person_1.status["marriage"]['date_of_marriage'] = to_date('2015.10.1')
    person_2.status["marriage"]['married'] = True
    person_2.status["marriage"]['married_to'] = person_1
    person_2.status["marriage"]['date_of_marriage'] = person_1.status["marriage"]['date_of_marriage']

    #TODO

    dom_1 = property.Zhiloe_pomeshenie()
    dom_1.add_sobstvennik(person_1)

    print(f'Список имущества {person_1}: {person_1.property}')
    print(person_1.property[0])
    print(f'Список собственников {person_1.property[0]}: {person_1.property[0].sobstvennik}')
    print(f'Дата получения права собственности на {person_1.property[0]}: {person_1.property[0].dates_of_change_owner[-1]}')
    print(f'Список собственников {dom_1}: {dom_1.sobstvennik}')
