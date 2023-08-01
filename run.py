import subprocess


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
            print("Podaj poprawną liczbę.")


if __name__ == "__main__":
    while True:
        print("Wybierz opcję:")
        print("1. Generowanie Excela")
        print("2. Dodawanie uczestnika")
        print("3. Usuwanie uczestnika")
        print("4. Zakończ program")

        choice = take_input("Podaj numer opcji: ")

        if choice == 1:
            try:
                # Uruchomienie skryptu create_excel.py
                subprocess.run(["python3", "scripts/create_excel.py"], check=True)
            except subprocess.CalledProcessError:
                print("Wystąpił błąd podczas uruchamiania skryptu tworzącego arkusz.")
        elif choice == 2:
            try:
                # Uruchomienie skryptu add_member.py
                subprocess.run(["python3", "scripts/add_member.py"], check=True)
            except subprocess.CalledProcessError:
                print(
                    "Wystąpił błąd podczas uruchamiania skryptu dodawania uczestnika."
                )
        elif choice == 3:
            try:
                # Uruchomienie skryptu delete_member.py
                subprocess.run(["python3", "scripts/delete_member.py"], check=True)
            except subprocess.CalledProcessError:
                print("Wystąpił błąd podczas uruchamiania skryptu usuwania uczestnika.")
        elif choice == 4:
            print("Zamykam program.")
            break
        else:
            print("Niepoprawny numer opcji. Wybierz 1, 2, 3 lub 4.")
