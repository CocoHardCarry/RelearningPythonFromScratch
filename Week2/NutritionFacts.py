def main():
    fruits = {"apple" : 130,
              "banana" : 100,
              "avocado" : 50,
              "cantaloupe" : 50,
              "grapefruit" : 60,
              "grapes" : 90,
              "honeydew melon" : 50,
              "kiwifruit" : 90,
              "lemom" : 15,
              "lime" : 20,
              "nectarine" : 60,
              "orange" : 80,
              "peach" : 60,
              "pear"  : 100,
              "pineapple" : 50,
              "plums" : 70,
              "strawberries" : 50,
              "sweet cherries" : 100,
              "tangerine" : 50,
              "watermelon" : 80}

    item = input("Item: ").lower()
    if item in fruits:
        print("Calories:", fruits[item])

main()