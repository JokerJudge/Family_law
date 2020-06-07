# попытка реализовать главу 3 Семейного кодекса
import datetime

class Fiz_l:
    def __init__(self, date_of_birth, sex):
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
        self.status = []
        self.relatives = []

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
    if isinstance(person_1, Fiz_l) and isinstance(person_2, Fiz_l):
        # проверяем на мужчину и женщину
        if person_1.sex == 'male' and person_2.sex == 'female' or person_1.sex == 'female' and person_2.sex == 'male':
            print('По полу все ОК')
            # проверяем на соответствие брачному возрасту
            if marriage_age_check(person_1, person_2) == True:
                print("По брачному возрасту все ОК")
            else:
                marriage_age = marriage_age_check(person_1, person_2)[0]
                law_link = marriage_age_check(person_1, person_2)[1]
                print("Брак указанных лиц невозможен. Брачный возраст не соответствует требуемому")
                print(f'Брачный возраст: {marriage_age};\n'
                      f'Возраст первого лица: {person_1.age};\n'
                      f'Возраст второго лица: {person_2.age};\n'
                      f'Ссылка на норму: {law_link}')
        else:
            law_link = 'ч.1 ст. 12 Семейного кодекса РФ'
            print(f"Брак между лицами одного пола недопустим\n"
                  f"Ссылка на норму: {law_link}")

    else:
        raise TypeError("Аргументы должны быть из class Fiz_l")

def marriage_age_check(person_1, person_2):
    marriage_age = 18 # общий брачный возраст в РФ (ст. 13 СК РФ). Еще бы как-то метку на норму сделать, но торгда нужно новый объект создавать
    law_link = 'ч.1 ст. 13 Семейного кодекса РФ'
    # TODO
    # проверить брачный возраст нужного субъекта РФ и перезаписать, если необходимо, переменную marriage_age
    # если есть уважительные причины, признанные ЗАГСом - marriage_age = 16
    # если есть особые обстоятельства по reg_law - region_law_marriage_age
    if person_1.age >= marriage_age and person_2.age >= marriage_age:
        return True
    else:
        return (marriage_age, law_link)

def region_law_marriage_age(region):
    # TODO list of region_marriage_ages
    ...

class Actions:
    ...

if __name__ == "__main__":
    human_1 = Fiz_l('1991.8.6', 'male')
    human_2 = Fiz_l('1990.10.28', 'female')
    # print(human_1.date_of_birth)
    # print(human_1.age)
    # print(human_1.sex)
    # print('------------')
    # print(human_2.date_of_birth)
    # print(human_2.age)
    # print(human_2.sex)
    marriage(human_1, human_2)