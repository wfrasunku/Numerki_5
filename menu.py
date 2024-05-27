import functions


def functions_menu():
    functions_list: list = []
    functions_amount = 0
    while True:
        try:
            print(' 0) zakończ listę\n', '1) wielomian\n', '2) sinus\n', '3) cosinus\n', '4) tangens\n',
                  '5) cotanges\n', '6) moduł')
            functions_amount += 1
            equation = int(input(f'Dodaj równanie nr {functions_amount}: '))
            if 0 <= equation <= 6:
                match equation:
                    case 0:
                        if functions_amount > 1:
                            break
                        print('Najpierw musisz dodać funkcje! \n')
                        functions_amount -= 1
                    case 1:
                        while True:
                            factors_list: list = []
                            try:
                                i = int(input('\nPodaj najwyższą potęgę wielomianu: '))
                                for i in range(i + 1, 0, -1):
                                    x = float(input(f'Wartość x^{i - 1}: '))
                                    factors_list.append(x)
                                equation = functions.Polynomial(factors_list)
                                functions_list.append(equation)
                                break
                            except ValueError:
                                print('Niepoprawna wartość!')
                    case 2:
                        equation = functions.Sinus()
                        functions_list.append(equation)
                    case 3:
                        equation = functions.Cosinus()
                        functions_list.append(equation)
                    case 4:
                        equation = functions.Tangens()
                        functions_list.append(equation)
                    case 5:
                        equation = functions.Cotangens()
                        functions_list.append(equation)
                    case 6:
                        equation = functions.Abs()
                        functions_list.append(equation)
            else:
                print('Niepoprawna wartość!\n')
                functions_amount -= 1
        except ValueError:
            print('Niepoprawna wartość!\n')
            functions_amount -= 1

    return functions_list


def precision_menu():
    try:
        precision = float(input("Wprowadź dokładność: "))
        if precision > 0:
            return precision
        else:
            print("dokładność musi być większy niż 0!")
            return precision_menu()
    except ValueError:
        print("Niepoprawna dokładność!")
        return precision_menu()

def interval_menu():
    while True:
        try:
            left_boundary = float(input('\nPodaj lewą granicę przedziału: '))
            right_boundary = float(input('Podaj prawą granicę przedziału: '))

            if right_boundary <= left_boundary:
                print('Prawa granica przedziału musi być większa od lewej granicy!')
            else:
                break
        except ValueError:
            print('Niepoprawna wartość!')

    return left_boundary, right_boundary

def nodes_menu():
    while True:
        try:
            nodes_value = int(input('\nPodaj ilość węzłów Czebyszewa: '))

            if nodes_value < 2 or nodes_value > 99:
                print('Ilość węzłów poza przedziałem!')
            else:
                break
        except ValueError:
            print('Niepoprawna wartość!')

    return nodes_value

def approximation_menu():
    while True:
        try:
            approx = int(input('\nPodaj stopień aproksymacji wielomianu: '))

            if approx < 0:
                print('Stopień musi być >= 0!')
            else:
                break
        except ValueError:
            print('Niepoprawna wartość!')

    return approx


def read_data(file_path, n):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        found_n = False

        for line in lines:
            if line.startswith(f"n = {n}"):
                found_n = True
                continue

            if found_n:
                if not line.strip():
                    break

                values = line.strip().split()
                data.append((float(values[0]), float(values[1])))

    return data
