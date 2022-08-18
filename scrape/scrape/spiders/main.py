import sys, generic_spider


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
            with open("urls.txt", "a") as f:
                f.write(site+"\n")
            done = input("\nDone? (y/n): ") == "y"
            if done:
                f.close()
        choicescreen(sites)

    elif choice == "2":
        spider = generic_spider.spider()
        spider.parse()

    elif choice == "3":
        with open("urls.txt", "w") as f:
            f.truncate()
        f.close()
        sys.exit()


if __name__ == "__main__":
    run()
