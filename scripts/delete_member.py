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


def remove_member():
    try:
        with open("data/members.json", "r") as file:
            members_list = json.load(file)

        display_members_list()

        member_number = int(input("Podaj numer uczestnika do usunięcia: "))
        if 1 <= member_number <= len(members_list):
            removed_member = members_list.pop(member_number - 1)

            with open("data/members.json", "w") as file:
                json.dump(members_list, file, indent=4)

            print(f"Usunięto uczestnika: {removed_member}")
        else:
            print("Niepoprawny numer uczestnika.")

    except FileNotFoundError:
        print("Plik z uczestnikami nie został znaleziony.")
    except json.JSONDecodeError:
        print("Błąd odczytu danych.")
    except ValueError:
        print("Niepoprawny numer uczestnika.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    display_members_list()
    remove_member()
