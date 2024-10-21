import random


def generate_jazz_chord(min=0, max=20):
    if min < 0:
        raise ValueError("min must be greater than or equal to 0")

    if max <= 2:
        raise ValueError("max must be greater than 2")

    if min > max:
        raise ValueError("min must be less than or equal to max")

    if min >= 20:
        raise ValueError("min must be less than 20")

    roots = [
        "C",
        "C#",
        "Db",
        "D",
        "D#",
        "Eb",
        "E",
        "F",
        "F#",
        "Gb",
        "G",
        "G#",
        "Ab",
        "A",
        "A#",
        "Bb",
        "B",
    ]
    qualities = ["maj", "m", "dim", "aug", "sus"]
    extensions = ["6", "7", "9", "11", "13"]
    alterations = ["#5", "b5", "#9", "b9", "#11", "b13", "b9", "#9"]
    additions = ["add9", "add13", "add11", "add#11"]
    bass_notes = ["/" + root for root in roots]

    # Decide whether to add alterations, additions, and bass notes
    decision = [True, False]

    # If min is greater than 19, all decisions are True
    if min > 19:
        decision = [True]

    while True:
        chord = random.choice(roots)
        chord += random.choice(qualities)
        chord += random.choice(extensions)

        if random.choice(decision):
            chord += random.choice(alterations)

        if random.choice(decision):
            chord += random.choice(additions)

        if random.choice(decision):
            chord += random.choice(bass_notes)

        if min <= len(chord) <= max:
            return chord


def generate_jazz_chords(n, min=0, max=20):
    return [generate_jazz_chord(min, max) for _ in range(n)]


if __name__ == "__main__":
    # Generate and print 10 random jazz chord names
    chords = generate_jazz_chords(10, max=3)
    for chord in chords:
        print(chord)
