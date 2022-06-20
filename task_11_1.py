class Date:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def take_date(cls, d_m_y):
        my_date = [int(i) for i in d_m_y.split('-')]
        return my_date

    @staticmethod
    def validation(d_m_y):
        my_date = [int(i) for i in d_m_y.split('-')]
        if my_date[0] in range(1, 31):
            print(f'Correct day')
        else:
            print(f'Incorrect day {my_date[0]}')
        if my_date[1] in range(1, 12):
            print(f'Correct month')
        else:
            print(f'Incorrect month {my_date[1]}')
        if my_date[2] in range(1900, 2023):
            print(f'Correct year')
        else:
            print(f'Incorrect year {my_date[2]}')

mc = Date('17-11-2022')
print(mc)
print(Date.take_date('11-06-2022'))
Date.validation('17-11-2022')