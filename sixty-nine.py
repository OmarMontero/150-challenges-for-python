

def main():
    countries = ("Spain", "Uk", "France", "Portugal", "Italy")
    print(countries)
    country = input("Choose a country: ")
    final_country = country.capitalize()
    print(f"The index of {final_country} is {countries.index(final_country)}")




if __name__ == '__main__':
    main()