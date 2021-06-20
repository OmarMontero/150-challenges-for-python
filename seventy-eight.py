

def main():
    tv_shows = ["seinfield", "frasier", "curb your enthusiasm", "the office"]

    for idx, i in enumerate(tv_shows):
        print(idx, i)
    new_show = input("Write another tv show: ")
    ubication = int(input("In what list´s postion do you want to insert your tv show? "))
    tv_shows.insert(ubication, new_show)
    print(tv_shows)

if __name__ == '__main__':
    main()

    #print(list(enumerate(party)))