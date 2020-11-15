import argparse


def fill_table(S1, S2, n, m, T):
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                T[i][j] = 0
            elif S1[j-1] == S2[i-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])


def get_longest_subsequence(S1, S2, T, n, m):
    subsequence = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if S1[j-1] == S2[i-1]:
            subsequence += S1[j-1]
            i -= 1
            j -= 1
        else:
            max = -1
            if i - 1 > 0 and j - 1 > 0:
                if T[i-1][j] > max:
                    max = T[i-1][j]
                    i -= 1
                if T[i][j-1] > max:
                    j -= 1
            elif i - 1 == 0:
                if T[i][j-1] > max:
                    j -= 1
            elif j - 1 == 0:
                if T[i][j-1] > max:
                    i -= 1

    subsequence = subsequence[::-1]
    return subsequence


def check_longest_substring(S1, S2):
    n = len(S1)
    m = len(S2)

    T = [[-1 for i in range(n + 1)] for j in range(m + 1)]
    fill_table(S1, S2, n, m, T)
    print("La subcadena más larga es: {} --> longitud {}".format(get_longest_subsequence(S1, S2, T, n, m), T[m][n]))
    print("Porcentage de coincidencia : {} * {} / {} = {}%".format(100, T[m][n], n, 100*T[m][n]/n))

    return T[m][n]


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description='Cheque de seguridad de contraseña')
    my_parser.add_argument('-u', type=str, help='username', required=True)
    my_parser.add_argument('-n', type=str, help='nombre', required=True)
    my_parser.add_argument('-a', type=str, help='apellido', required=True)
    my_parser.add_argument('-p', type=str, help='contraseña', required=True)
    args = my_parser.parse_args()

    username = args.u
    nombre = args.n
    apelllido = args.a
    password = args.p

    c = []
    print("Para el usuario:")
    print("username: " + username)
    print("nombre: " + nombre)
    print("apellido: " + apelllido)
    print("password: " + password)
    print('\n')
    print('Comparando username "{}" con password "{}"'.format(username, password))
    c.append(check_longest_substring(username, password))
    print('\n')
    print('Comparando nombre "{}" con password "{}"'.format(username, password))
    c.append(check_longest_substring(nombre, password))
    print('\n')
    print('Comparando apellido "{}" con password "{}"'.format(username, password))
    c.append(check_longest_substring(apelllido, password))
    print('\n')
    print("Mayor longitud de coincidencia {}".format(max(c)))
    print("Longitud de la password: {}".format(len(password)))
    print("Porcentaje de originalidad: {} - {} * {} / {} = {}%".format(100, 100, max(c), len(password),
          100-100*max(c)/len(password)))

