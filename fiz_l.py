# попытка реализовать главу 3 Семейного кодекса
import datetime
import marriage
import property

class Fiz_l:
    def __init__(self, date_of_birth, sex, surname: str, name: str, fathername: str):
        self.status = {'alive': True,
                       'married': False,
                       'deesposobnost': True}
        dt = Fiz_l.to_date(date_of_birth)
        dt = datetime.date(dt[0], dt[1], dt[2])
        self.date_of_birth = dt
        # считаем разницу в годах
        today = datetime.date.today()
        temp_date = self.date_of_birth.replace(today.year) # timedelta работает с днями, поэтому вводим врем. переменную
        if temp_date > today: # если ДР в этом году еще не наступил
            self.age = datetime.date.today().year - self.date_of_birth.year - 1
        else: # если ДР уже наступил
            self.age = datetime.date.today().year - self.date_of_birth.year
        if sex == 'male' or sex == 'female':
            self.sex = sex
        else:
            raise ValueError("Мужчина - 'male', Женщина - 'female'")
        self.surname = surname
        self.name = name
        self.fathername = fathername
        self.relatives = []
        self.married = {'married_to': None,
                        'date_of_marriage': None}
        self.property = []

    def __str__(self):
        return f'{self.surname} {self.name} {self.fathername}'

    @classmethod
    def to_date(self, date_of_birth):
        l = []
        dt = date_of_birth.split('.')
        for i in dt:
            i = int(i)
            l.append(i)
        return l[0], l[1], l[2]

def to_date(date):
    l = []
    dt = date.split('.')
    for i in dt:
        i = int(i)
        l.append(i)
    return l[0], l[1], l[2]


class Actions:
    ...

if __name__ == "__main__":
    person_1 = Fiz_l(date_of_birth='1991.8.6', sex='male', surname='Коваленко', name='Евгений', fathername="Николаевич")
    person_2 = Fiz_l(date_of_birth='1990.10.28', sex='female', surname='Дуркина', name='Мария', fathername="Юрьевна")

    #marriage.marriage_func(person_1, person_2)
    #print(f'Брак с: {person_2.married["married_to"]} \n'
    #      f'Дата заключения брака: {person_2.married["date_of_marriage"]}')

    dom_1 = property.Zhiloe_pomeshenie()
    dom_1.add_sobstvennik(person_1)
    print(person_1.property[0])
    print(person_1.property[0].sobstvennik)
    print(person_1.property[0].definition)
    print(person_1.property[0].dates_of_change_owner[0])
