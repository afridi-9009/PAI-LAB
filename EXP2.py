from collections import defaultdict
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
aim = int(input("Enter target amount: "))
visited = defaultdict(lambda: False)
def waterJugSolver(amt1, amt2):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True
    if not visited[(amt1, amt2)]:
        print(amt1, amt2)
        visited[(amt1, amt2)] = True
        return (
            waterJugSolver(0, amt2) or
            waterJugSolver(amt1, 0) or
            waterJugSolver(jug1, amt2) or
            waterJugSolver(amt1, jug2) or
            waterJugSolver(
                amt1 + min(amt2, jug1 - amt1),
                amt2 - min(amt2, jug1 - amt1)
            ) or
            waterJugSolver(
                amt1 - min(amt1, jug2 - amt2),
                amt2 + min(amt1, jug2 - amt2)
            )
        )
    return False

print("Steps:")
if not waterJugSolver(0, 0):
    print("No solution possible.")

