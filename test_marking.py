def main():
    answers = [
        ["A", "B", "A", "C", "C", "D", "E", "E", "A", "D"],
        ["D", "B", "A", "B", "C", "A", "E", "E", "A", "D"],
        ["E", "D", "D", "A", "C", "B", "E", "E", "A", "D"],
        ["C", "B", "A", "E", "D", "C", "E", "E", "A", "D"],
        ["A", "B", "D", "C", "C", "D", "E", "E", "A", "D"],
        ["B", "B", "E", "C", "C", "D", "E", "E", "A", "D"],
        ["B", "B", "A", "C", "C", "D", "E", "E", "A", "D"],
        ["E", "B", "E", "C", "C", "D", "E", "E", "A", "D"]
    ]

    key = ["D", "B", "D", "C", "C", "D", "A", "E", "A", "D"]
    position = []

    for i in range(len(answers)):
        correct_count = 0
        for j in range(len(answers[i])):
            if answers[i][j] == key[j]:
                correct_count += 1
        position.append(correct_count)
        print(f"Students {i + 1}\'s correct count is {correct_count}")
    print(f"The students {position.index(max(position)) + 1} has the highest score of {max(position)}/{len(key)}")

main()