def count_votes(votes, candidates):
    """
    Registra los votos y detecta votos inválidos.
    Devuelve un diccionario con el conteo de votos por candidato y la cantidad de votos inválidos.
    """
    vote_counts = {candidate: 0 for candidate in candidates}
    invalid_votes = 0

    for vote in votes:
        if vote in candidates:
            vote_counts[vote] += 1
        else:
            invalid_votes += 1
            print(f"Voto inválido detectado: '{vote}'")
    return vote_counts, invalid_votes

def determine_winner(vote_counts, total_valid_votes):
    """
    Determina el ganador de la elección y su porcentaje de votos.
    """
    if not vote_counts or total_valid_votes == 0:
        return "Nadie", 0.0

    winner = None
    max_votes = -1
    tied_candidates = []

    for candidate, count in vote_counts.items():
        if count > max_votes:
            max_votes = count
            winner = candidate
            tied_candidates = [candidate]
        elif count == max_votes:
            tied_candidates.append(candidate)

    if len(tied_candidates) > 1:
        winner_message = f"Empate entre {', '.join(tied_candidates)}"
        winner_percentage = (max_votes / total_valid_votes) * 100
    else:
        winner_message = winner
        winner_percentage = (max_votes / total_valid_votes) * 100

    return winner_message, winner_percentage

# Demostración
candidatos = ["Candidato A", "Candidato B", "Candidato C"]
votos_recibidos = [
    "Candidato A", "Candidato B", "Candidato A", "Candidato C",
    "Candidato A", "Voto Nulo", "Candidato B", "Candidato A",
    "Candidato C", "Candidato B", "Candidato D", "Candidato A",
    "candidato a" # Voto inválido por capitalización
]

print(f"Candidatos: {candidatos}")
print(f"Votos recibidos: {votos_recibidos}")

votes_results, invalid_count = count_votes(votos_recibidos, candidatos)

total_valid_votes = sum(votes_results.values())

print("\n--- Resumen de Votos ---")
for candidate, count in votes_results.items():
    percentage = (count / total_valid_votes) * 100 if total_valid_votes > 0 else 0
    print(f"  {candidate}: {count} votos ({percentage:.2f}%) ")
print(f"Votos inválidos: {invalid_count}")
print(f"Total de votos válidos: {total_valid_votes}")

winner_name, winner_percentage = determine_winner(votes_results, total_valid_votes)

print("\n--- Resultado de la Elección ---")
if winner_name == "Nadie":
    print("No se pudo determinar un ganador (no hay votos válidos).")
else:
    print(f"Ganador/es: {winner_name}")
    print(f"Porcentaje del ganador: {winner_percentage:.2f}%")

# Demostración de empate
print("\n--- Demostración de Empate ---")
votos_empate = [
    "Candidato A", "Candidato A", "Candidato B", "Candidato B",
    "Candidato C", "Candidato C"
]

votes_results_empate, invalid_count_empate = count_votes(votos_empate, candidatos)
total_valid_votes_empate = sum(votes_results_empate.values())

winner_name_empate, winner_percentage_empate = determine_winner(votes_results_empate, total_valid_votes_empate)
print(f"Votos en caso de empate: {votos_empate}")
print(f"Resultado del empate: {winner_name_empate} con {winner_percentage_empate:.2f}%")
