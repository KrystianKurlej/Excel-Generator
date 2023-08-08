import subprocess
from colorama import init, Fore, Back, Style

init()


def is_input_correct(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


def take_input(question):
    while True:
        answer = input(question)
        if is_input_correct(answer):
            return int(answer)
        else:
            print(Fore.RED + "Podaj poprawną liczbę." + Style.RESET_ALL)


if __name__ == "__main__":
    while True:
        print("")
        print(Back.CYAN + Style.BRIGHT + " Wybierz opcję: " + Style.RESET_ALL)
        print("")
        print(Fore.CYAN + " 1. " + Style.RESET_ALL + "Generowanie Excela ")
        print(Fore.CYAN + " 2. " + Style.RESET_ALL + "Dodawanie uczestnika ")
        print(Fore.CYAN + " 3. " + Style.RESET_ALL + "Usuwanie uczestnika ")
        print(
            Fore.CYAN + " 4. " + Style.RESET_ALL + "Zakończ program " + Style.RESET_ALL
        )
        print("")

        choice = take_input(Fore.CYAN + "Podaj numer opcji: " + Style.RESET_ALL)

        if choice == 1:
            try:
                # Uruchomienie skryptu create_excel.py
                subprocess.run(["python3", "scripts/create_excel.py"], check=True)
            except subprocess.CalledProcessError:
                print(
                    Fore.RED
                    + "Wystąpił błąd podczas uruchamiania skryptu tworzącego arkusz."
                    + Style.RESET_ALL
                )
        elif choice == 2:
            try:
                # Uruchomienie skryptu add_member.py
                subprocess.run(["python3", "scripts/add_member.py"], check=True)
            except subprocess.CalledProcessError:
                print(
                    Fore.RED
                    + "Wystąpił błąd podczas uruchamiania skryptu dodawania uczestnika."
                    + Style.RESET_ALL
                )
        elif choice == 3:
            try:
                # Uruchomienie skryptu delete_member.py
                subprocess.run(["python3", "scripts/delete_member.py"], check=True)
            except subprocess.CalledProcessError:
                print(
                    Fore.RED
                    + "Wystąpił błąd podczas uruchamiania skryptu usuwania uczestnika."
                    + Style.RESET_ALL
                )
        elif choice == 4:
            print(Fore.GREEN + "Zamykam program." + Style.RESET_ALL)
            break
        else:
            print(
                Fore.RED
                + "Niepoprawny numer opcji. Wybierz 1, 2, 3 lub 4."
                + Style.RESET_ALL
            )
