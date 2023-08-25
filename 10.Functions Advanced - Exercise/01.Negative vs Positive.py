def negative_vs_positive(*args):
    negative = sum([int(i) for i in args[0] if int(i) < 0])
    positive = sum([int(i) for i in args[0] if int(i) > 0])

    print(negative)
    print(positive)
    print("The negatives are stronger than the positives" if abs(negative) > abs(positive)
          else "The positives are stronger than the negatives")


negative_vs_positive(input().split())