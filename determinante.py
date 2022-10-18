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

  X = np.array(matriz)
  det_X = round(np.linalg.det(X))
  print("A determinante da matriz inserida é: ", det_X)

if T == 2:
  matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  for l in range(0, 3):
    for c in range(0, 3):
      matriz[l][c] = int(input(f"Digite o valor da linha {l} e coluna {c}: "))

  for l in range(0, 3):
    print(matriz[l])

  X = np.array(matriz)
  det_X = round(np.linalg.det(X))
  print("A determinante da matriz inserida é: ", det_X)

if T == 3:
  matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

  for l in range(0, 4):
    for c in range(0, 4):
      matriz[l][c] = int(input(f"Digite o valor da linha {l} e coluna {c}: "))

  for l in range(0, 4):
    print(matriz[l])

  X = np.array(matriz)
  det_X = round(np.linalg.det(X))
  print("A determinante da matriz inserida é: ", det_X)
