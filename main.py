# попытка реализовать главу 3 Семейного кодекса
import datetime

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
        self.married = None

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



def marriage(person_1, person_2): # на вход подаются физ.лица (class Fiz_l)
    # общее правило
    if not isinstance(person_1, Fiz_l) and not isinstance(person_2, Fiz_l):
        raise TypeError("Аргументы должны быть из class Fiz_l")
    # проверка на соответствие обязательным требованиям каждого отдельного лица
    place_of_marriage = 'Saint-Petersburg' # здесь нужен input по субъекту РФ

    #проверка обоих лиц по отдельности
    person = person_1
    for i in range(2):
        # проверка на статус
        if person.status['alive'] == False:
            raise ValueError(f"{person} умер(ла). С мертвецом в браки не вступают")
        if person.status['married'] == True:
            law_link = 'абз. 2 ст. 15 Семейного кодекса РФ'
            raise ValueError(f"{person} состоит в браке. Второй брак недопустим\n Cсылка на норму: {law_link}")
        if person.status['deesposobnost'] == False:
            law_link = 'абз. 5 ст. 15 Семейного кодекса РФ'
            raise ValueError(f"{person} признан(а) недееспособным(ой). Брак с указанным лицом невозможен\n Cсылка на норму: {law_link}")
        temp = marriage_age_check(person, place_of_marriage) # проверка на брачный возраст
        if temp != True:
            marriage_age, law_link = temp[0], temp[1]
            raise ValueError(f"{person} не достиг(ла) брачного возраста - {marriage_age},\n Cсылка на норму: {law_link}")
        person = person_2

    #проверка лиц на совместную возможность пожениться
    # проверка на однополый брак
    if not (person_1.sex == 'male' and person_2.sex == 'female' or person_1.sex == 'female' and person_2.sex == 'male'):
        law_link = 'ч.1 ст. 12 Семейного кодекса РФ'
        print(f"Брак между лицами одного пола недопустим\n"
              f"Ссылка на норму: {law_link}")

    # проверка на родстввенные связи
    # TODO

    # итог + изменение статуса
    print(f"Брак между {person_1} и {person_2} возможен")
    print('===============')
    while True:
        print(f"Заключить брак между {person_1} и {person_2}?")
        print("1 - ДА")
        print("2 - НЕТ")
        choose = input("Введите ответ (1 или 2): ")
        if choose == '1':
            person_1.status['married'] = True
            person_1.married = person_2
            person_2.status['married'] = True
            person_2.married = person_1
            print(f"Брак между {person_1} и {person_2} заключен")
            break
        elif choose == '2':
            print('===============')
            print("Оставим их в покое")
            break
        else:
            print('===============')
            print("Incorrect answer. Try again.")
            print("===============")



def marriage_age_check(person, place_of_marriage):
    marriage_age = 18 # общий брачный возраст в РФ (ст. 13 СК РФ). Еще бы как-то метку на норму сделать, но торгда нужно новый объект создавать
    law_link = 'ч.1 ст. 13 Семейного кодекса РФ'
    # TODO
    # проверить брачный возраст нужного субъекта РФ и перезаписать, если необходимо, переменную marriage_age
    # если есть уважительные причины, признанные ЗАГСом - marriage_age = 16
    # если есть особые обстоятельства по reg_law - region_law_marriage_age
    if person.age >= marriage_age:
        return True
    else:
        return (marriage_age, law_link)

def region_law_marriage_age(region):
    # TODO list of region_marriage_ages
    ...

class Actions:
    ...

if __name__ == "__main__":
    human_1 = Fiz_l(date_of_birth='1991.8.6', sex='female', surname='Коваленко', name='Евгений', fathername="Николаевич")
    human_2 = Fiz_l(date_of_birth='1990.10.28', sex='male', surname='Дуркина', name='Мария', fathername="Юрьевна")
    # print(human_1.date_of_birth)
    # print(human_1.age)
    # print(human_1.sex)
    # print('------------')
    # print(human_2.date_of_birth)
    # print(human_2.age)
    # print(human_2.sex)
    marriage(human_1, human_2)
    print(f'Брак с: {human_2.married}')
    #marriage(human_1, human_2)