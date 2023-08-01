import json
from colorama import init, Fore, Back, Style

init()


def display_members_list():
    try:
        with open("data/members.json", "r") as file:
            members_list = json.load(file)
            print(Fore.BLUE + "Aktualna lista uczestników:" + Style.RESET_ALL)
            for idx, member in enumerate(members_list, start=1):
                print(f"{idx}. {member}")
    except FileNotFoundError:
        print(Fore.RED + "Plik z uczestnikami nie został znaleziony." + Style.RESET_ALL)
    except json.JSONDecodeError:
        print(Fore.RED + "Błąd odczytu danych." + Style.RESET_ALL)


def remove_member():
    try:
        with open("data/members.json", "r") as file:
            members_list = json.load(file)

        member_number = int(
            input(Fore.BLUE + "Podaj numer uczestnika do usunięcia: " + Style.RESET_ALL)
        )
        if 1 <= member_number <= len(members_list):
            removed_member = members_list.pop(member_number - 1)

            with open("data/members.json", "w") as file:
                json.dump(members_list, file, indent=4)

            print(f"{Fore.GREEN}Usunięto uczestnika: {removed_member}{Style.RESET_ALL}")
        else:
            print(Fore.RED + "Niepoprawny numer uczestnika." + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + "Plik z uczestnikami nie został znaleziony." + Style.REST_ALL)
    except json.JSONDecodeError:
        print(Fore.RED + "Błąd odczytu danych." + Style.REST_ALL)
    except ValueError:
        print(Fore.RED + "Niepoprawny numer uczestnika." + Style.REST_ALL)
    except Exception as e:
        print(f"{Fore.RED}Wystąpił błąd: {e}{Style.RESET_ALL}")


if __name__ == "__main__":
    display_members_list()
    remove_member()
