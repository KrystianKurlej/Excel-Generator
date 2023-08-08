import json
from colorama import init, Fore, Style

init()

members_data_source = "mock_members.json"


def display_members_list():
    try:
        with open(members_data_source, "r") as file:
            members_list = json.load(file)
            print(Fore.CYAN + "Aktualna lista uczestników:" + Style.RESET_ALL)
            for idx, member in enumerate(members_list, start=1):
                print(f"{idx}. {member}")
    except FileNotFoundError:
        print(Fore.RED + "Plik z uczestnikami nie został znaleziony." + Style.RESET_ALL)
    except json.JSONDecodeError:
        print(Fore.RED + "Błąd odczytu danych." + Style.RESET_ALL)


def add_new_member():
    new_member = input(
        Fore.CYAN + "Podaj imię i nazwisko nowego uczestnika: " + Style.RESET_ALL
    )
    try:
        with open(members_data_source, "r") as file:
            members_list = json.load(file)

        members_list.append(new_member)

        with open(members_data_source, "w") as file:
            json.dump(members_list, file, indent=4)

        print(f"{Fore.GREEN}Dodano uczestnika: {new_member}{Style.RESET_ALL}")

    except FileNotFoundError:
        print(Fore.RED + "Plik z uczestnikami nie został znaleziony." + Style.RESET_ALL)
    except json.JSONDecodeError:
        print(Fore.RED + "Błąd odczytu danych." + Style.RESET_ALL)
    except Exception as e:
        print(f"{Fore.RED}Wystąpił błąd: {e}{Style.RESET_ALL}")


if __name__ == "__main__":
    display_members_list()
    add_new_member()
