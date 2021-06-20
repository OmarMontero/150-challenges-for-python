


def main():
    sentence = "No es verdad ángel de amor, que en aquella apartada orilla, si tu novio nos pilla, las hostias me las llevo yo?."
    limit = len(sentence)
    print(sentence)
    low_limit = int(input(f"Type in the low limit(between 0 and {limit}): "))
    top = int(input(f"Type in the high limit(between 0 and {limit}): "))
    print(sentence[low_limit:top])




if __name__ == '__main__':
    main()