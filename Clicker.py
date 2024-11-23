import keyboard
import mouse
import time
import os
from random import randrange


class Clicker:
    def __init__(self):
        self.program_is_working = 1
        self.presser_is_working = 0

        self.mainloop(self.input_settings())

    def input_settings(self):
        print('ПРИМЕЧАНИЕ: Чем меньше задержка перед включением кликера, '
              'тем больше нагрузка на систему в режиме ожидания.\n'
              'При малом значении или значении 0 задержки перед кликом задержка будет минимальной, '
              '\nно может появиться задержка перед выключением кликера или его переходом в режим ожидания.\n'
              'Все значения измеряются в секундах.')

        waiting_time, delay_time = 0.2, 0.002

        try:
            while True:
                waiting_time = float(input("\nЗадержка перед включением кликера: "))

                if 0 <= waiting_time:
                    break

        except ValueError:
            print("\nНедопустимое значение")

        try:
            while True:
                delay_time = float(input("\nЗадержка перед кликом: "))

                if 0 <= delay_time:
                    break

        except ValueError:
            print("\nНедопустимое значение")

        try:
            Key = input("\nКнопка активации / деактивации кликера: ")
            keyboard.add_hotkey(Key, self.start_and_stop_presser)

        except Exception:
            print("\nНедопустимое значение")

        print("\nКликер готов")

        return waiting_time, delay_time

    def start_and_stop_presser(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        self.presser_is_working = not self.presser_is_working

        print('\nАктивно' if self.presser_is_working else '\nОжидание')

    def stop_program(self):
        self.program_is_working = 0

    def mainloop(self, times):
        waiting_time, delay_time = times

        while self.program_is_working:
            time.sleep(waiting_time + randrange(0, 100) / 1000)
            while self.presser_is_working:
                mouse.click('left')
                time.sleep(delay_time)


if __name__ == "__main__":
    Clicker()
