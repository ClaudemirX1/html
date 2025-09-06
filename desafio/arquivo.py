import json
import os

# Arquivo onde vamos salvar os dados
ARQUIVO = "treinos.json"

# Exercícios cadastrados por grupo muscular
EXERCICIOS = {
    "Peito": ["Supino reto", "Supino inclinado", "Crucifixo"],
    "Costas": ["Puxada frontal", "Remada baixa", "Barra fixa"],
    "Bíceps": ["Rosca direta", "Rosca alternada", "Rosca inclinada"],
    "Tríceps": ["Tríceps corda", "Tríceps testa", "Mergulho"],
    "Pernas": ["Agachamento livre", "Leg press", "Cadeira extensora"],
    "Ombro": ["Desenvolvimento militar", "Elevação lateral", "Arnold press"]
}

# Carregar dados salvos
def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return {}

# Salvar dados
def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def escolher_opcao(lista):
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")
    escolha = int(input("Escolha uma opção: "))
    return lista[escolha - 1]

def main():
    dados = carregar_dados()

    print("\n--- Programa de Treino ---")
    print("Escolha o grupo muscular:")
    grupo = escolher_opcao(list(EXERCICIOS.keys()))

    print(f"\nExercícios de {grupo}:")
    exercicio = escolher_opcao(EXERCICIOS[grupo])

    # Ver peso atual
    peso_atual = dados.get(exercicio, 0)
    print(f"\nPeso atual em {exercicio}: {peso_atual} kg")

    # Perguntar se quer atualizar
    opc = input("Deseja atualizar o peso? (s/n): ").lower()
    if opc == "s":
        novo_peso = int(input("Digite o novo peso (kg): "))
        dados[exercicio] = novo_peso
        salvar_dados(dados)
        print(f"Peso atualizado! Agora você levanta {novo_peso} kg em {exercicio}.")
    else:
        print("Beleza! Nada alterado.")

if _name_ == "_main_":
    main()