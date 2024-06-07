import keyboard
import mouse
import time
import os


class Clicker:
    def __init__(self):
        keyboard.add_hotkey('esc', self.stop_app)

        self.AppWork = 1
        self.ClickerWork = 0

        self.mainloop(self.input_settings())

    def input_settings(self):
        print('ПРИМЕЧАНИЕ: Чем меньше задержка перед включением кликера, '
              'тем больше нагрузка на систему в режиме ожидания.\n'
              'При малом значении или значении 0 задержки перед кликом задержка будет минимальной, '
              '\nно может появиться задержка перед выключением кликера или его переходом в режим ожидания.\n'
              'Все значения измеряются в секундах.')

        try:
            while True:
                CheckTime = float(input("\nЗадержка перед включением кликера: "))

                if 0 <= CheckTime:
                    break

        except ValueError:
            print("\nНедопустимое значение")

        try:
            while True:
                ClickTime = float(input("\nЗадержка перед кликом: "))

                if 0 <= ClickTime:
                    break

        except ValueError:
            print("\nНедопустимое значение")

        try:
            Key = input("\nКнопка активации / деактивации кликера: ")
            keyboard.add_hotkey(Key, self.start_and_stop_clicker)

        except Exception:
            print("\nНедопустимое значение")

        print("\nКликер готов")

        return CheckTime, ClickTime

    def start_and_stop_clicker(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.ClickerWork = not self.ClickerWork
        print('\nАктивно' if self.ClickerWork else '\nОжидание')

    def stop_app(self):
        self.AppWork = 0

    def mainloop(self, Times):
        while self.AppWork:
            time.sleep(Times[0])
            while self.ClickerWork:
                mouse.click('left')
                time.sleep(Times[1])


if __name__ == "__main__":
    Clicker()
