# Generator Excela do Sprawdzania Obecności Uczestników

**Problem:** Co miesiąc potrzebny jest plik Excela z usuniętymi weekendami oraz aktualną listą uczestników ośrodka. Ten program ma za zadanie zautomatyzować tworzenie plików Excela, a w szczególności dopasowanie go do konkretnego miesiąca.

## Opis

Ten program umożliwia generowanie plików Excela do śledzenia obecności uczestników. Program automatycznie tworzy kolumny z dniami roboczymi w konkretnym miesiącu i dodaje wiersze z danymi uczestnikami. Na końcu każdej kolumny i wiersza znajduje się komórka, która sumuje obecności oznaczone przez `x`. Skrypt następnie zapisuje plik `.xslx` o nazwie odpowiadającej wybranej dacie.

## Funkcje

- Generowanie pliku Excela
- Dodawanie i usuwanie uczestników z listy

## Instrukcja Użycia

1. Uruchom program, wybierz opcję z menu:
   - **Generowanie Excela**: Wygeneruj arkusz obecności dla wybranego miesiąca.
   - **Dodawanie Uczestnika**: Dodaj nowego uczestnika do listy.
   - **Usuwanie Uczestnika**: Usuń uczestnika z listy.
   - **Zakończ program**: Wyjście z programu.
2. Postępuj zgodnie z instrukcjami programu.
3. Pliki Excela zostaną utworzone w folderze, w którym znajduje się skrypt.

## Dane uczestników

Dane uczestników przechowywane powinny być w pliku `members.json`. Ścieżka do tego pliku jest definiowana jako zmienna na początku skryptów: `add_member.py`, `create_excel.py`, `delete_members.py` jako `members_data_source`.

## Wymagania

- Python 3.x
- Biblioteka openpyxl (do obsługi plików Excela)
