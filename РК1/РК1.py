from operator import itemgetter

class comp:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class McPr:
    """Микропроцессор"""
    def __init__( self,id,model_name,manufacturer,number_of_cores,frequency,comp_id):
        self.id = id
        self.model_name = model_name
        self.manufacturer = manufacturer
        self.number_of_cores = number_of_cores
        self.frequency = frequency
        self.comp_id=comp_id

class MсPrComp:
    """'Микропроцессоры пк' для реализации связи многие-ко-многим"""
    def __init__(self, mcpr_id, comp_id):
        self.mcpr_id = mcpr_id
        self.comp_id = comp_id

# Микропроцессоры
processors=[
    McPr( 1,"Threadripper","AMD", 64, 3.1, 5),
    McPr( 2,"Ryzen 3","AMD", 4, 3.5, 1),
    McPr( 3,"Core i3","Intel", 2, 3.9, 3),
    McPr( 4,"Core i5","Intel", 4, 3.6, 2),
    McPr( 5,"Core i9","Intel", 8, 3.1, 1),
    McPr( 6,"Pentium","Intel", 2, 3.3, 3),
    McPr( 7,"Ryzen 7","AMD", 8, 3.2, 4),
]

# Компьютеры
computers=[
    comp(1,"Компьютер директора"),
    comp(2,"Компьютер секретаря"),
    comp(3,"Компьютер сотрудника"),
    comp(4,"Компьютер студента"),
    comp(5,"Компьютер школьника"),
]

McPr_Comp =[
    MсPrComp(1,5),
    MсPrComp(1,4),
    MсPrComp(2,1),
    MсPrComp(3,3),
    MсPrComp(3,2),
    MсPrComp(4,2),
    MсPrComp(4,1),
    MсPrComp(5,1),
    MсPrComp(6,3),
    MсPrComp(7,4),
    MсPrComp(7,5),
]

def main():
    """Основная функция"""

    #Соединение данных  один-ко-многим
    one_to_many =[(p.model_name, p.number_of_cores, c.name)
                  for c in computers
                  for p in processors
                  if p.comp_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, pc.mcpr_id, pc.comp_id)
                         for c in computers
                         for pc in McPr_Comp
                         if c.id == pc.comp_id]

    many_to_many = [(p.model_name, p.number_of_cores, comp_name)
                    for comp_name, comp_id, mcpr_id in many_to_many_temp
                    for p in processors if p.id == mcpr_id]

    print('Задание В1')
    res_11 = list(filter(lambda x: x[0].startswith('C'),one_to_many))
    print(res_11)

    print('\nЗадание B2')
    res_12_unsorted = []

    for c in computers:
        c_mcpr=list(filter(lambda i: i[2]==c.name, one_to_many))
        if len(c_mcpr) > 0:
            c_number_of_cores = [number_of_cores for _,number_of_cores,_ in c_mcpr]
            c_number_of_cores_min = min(c_number_of_cores)
            res_12_unsorted.append((c.name, c_number_of_cores_min))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=False)
    print(res_12)

    print('\nЗадание B3')
    res_13 = sorted(many_to_many, key=itemgetter(0))
    print(res_13)

if __name__ == '__main__':
    main()
