import json


def display_members_list():
    try:
        with open("data/members.json", "r") as file:
            members_list = json.load(file)
            print("Aktualna lista uczestników:")
            for idx, member in enumerate(members_list, start=1):
                print(f"{idx}. {member}")
    except FileNotFoundError:
        print("Plik z uczestnikami nie został znaleziony.")
    except json.JSONDecodeError:
        print("Błąd odczytu danych.")


def add_new_member():
    new_member = input("Podaj imię i nazwisko nowego uczestnika: ")
    try:
        with open("data/members.json", "r") as file:
            members_list = json.load(file)

        members_list.append(new_member)

        with open("data/members.json", "w") as file:
            json.dump(members_list, file, indent=4)

        print(f"Dodano uczestnika: {new_member}")

    except FileNotFoundError:
        print("Plik z uczestnikami nie został znaleziony.")
    except json.JSONDecodeError:
        print("Błąd odczytu danych.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    display_members_list()
    add_new_member()
