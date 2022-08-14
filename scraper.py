import sys


def run():
    print("\n░█▀▀░█▀▀░█▀▄░█▀█░█▀█░█▀▀░█▀▄\n░▀▀█░█░░░█▀▄░█▀█░█▀▀░█▀▀░█▀▄\n░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░░░▀▀▀░▀░▀")
    sites = []
    choicescreen(sites)


def choicescreen(sites):
    done = False
    print("\n1. Add site to list"
          "\n2. Start scraping"
          "\n3. Exit")

    choice = input("\nEnter your choice: ")
    if choice == "1":
        while not done:
            site = input("\nEnter site to add: ")
            sites.append(site)
            done = input("\nDone? (y/n): ") == "y"
        choicescreen(sites)
    elif choice == "2":
        scrape(sites)
    elif choice == "3":
        sys.exit()


def scrape(sites):
    pass


if __name__ == "__main__":
    run()
