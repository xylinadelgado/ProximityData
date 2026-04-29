distances = [35, 22, 18, 9, 12, 40, 27]

TOO_CLOSE = 10
WARNING = 25

def classify_distance(d):
    if d <= TOO_CLOSE:
        return "TOO CLOSE"
    elif d <= WARNING:
        return "WARNING"
    else:
        return "SAFE"

print("Distance Analysis:\n")

for d in distances:
    status = classify_distance(d)
    print(f"{d} cm -> {status}")

average = sum(distances) / len(distances)

print("\nSummary:")
print(f"Average Distance: {average:.2f} cm")