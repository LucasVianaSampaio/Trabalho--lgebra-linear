import numpy as np

T = int(
  input("Digite 1 para matriz 2x2"
        "\nDigite 2 para a matriz 3x3"
        "\nDigite 3 para a matriz 4x4\n"))

if T == 1:
  matriz = [[0, 0], [0, 0]]

  for l in range(0, 2):
    for c in range(0, 2):
      matriz[l][c] = int(input(f"Digite o valor da linha {l} e coluna {c}: "))

  for l in range(0, 2):
    print(matriz[l])

  print()

  Z = np.array(matriz)
  det_Z = round(np.linalg.det(Z))

  if (det_Z != 0):
    f = 0
    f = matriz[-2][-2]
    matriz[-2][-2]: matriz[0] = matriz[-1][-1]
    matriz[-1][-1]: matriz[0] = f
    matriz[-2][-1]: matriz[0] = (matriz[-2][-1]) * (-1)
    matriz[-1][-2]: matriz[0] = (matriz[-1][-2]) * (-1)

    matriz[-2][-2]: matriz[0] = (matriz[-2][-2]) / (det_Z)
    matriz[-2][-1]: matriz[0] = (matriz[-2][-1]) / (det_Z)
    matriz[-1][-2]: matriz[0] = (matriz[-1][-2]) / (det_Z)
    matriz[-1][-1]: matriz[0] = (matriz[-1][-1]) / (det_Z)

    X = np.array(matriz)
    print("Inversa:", X)
  else:
    print("Matriz não é inversível!")

elif (T == 2):
  matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  for l in range(0, 3):
    for c in range(0, 3):
      matriz[l][c] = int(input(f"Digite o valor da linha {l} e coluna {c}: "))

  for l in range(0, 3):
    print(matriz[l])

  print()

  D = np.array(matriz)
  det_D = round(np.linalg.det(D))

  if (det_D != 0):
    Y = np.array(matriz)
    inv_X = np.linalg.inv(Y)
    print("A inversa da matriz inserida é: ", inv_X)
  else:
    print("Matriz não inversível!!")

elif (T == 3):
  matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

  for l in range(0, 4):
    for c in range(0, 4):
      matriz[l][c] = int(input(f"Digite o valor da linha {l} e coluna {c}: "))

  for l in range(0, 4):
    print(matriz[l])

  print()

  E = np.array(matriz)
  det_E = round(np.linalg.det(E))

  if (det_E != 0):
    W = np.array(matriz)
    inv_X = np.linalg.inv(W)
    print("A inversa da matriz inserida é: ", inv_X)
  else:
    print("Matriz não é inversível!!")
