def split_integer(value: int, number_of_parts: int) -> list[int]:
    base = value // number_of_parts
    remainder = value % number_of_parts

    # Najpierw ustawiamy wszystkie części na base
    parts = [base] * number_of_parts

    # Rozdajemy resztę - po jednym do ostatnich elementów
    for i in range(remainder):
        parts[-1 - i] += 1

    # Sortujemy rosnąco
    parts.sort()
    return parts
