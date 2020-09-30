import wikipedia


def goto_wiki():
    loop=True
    while loop==True:
        choice=input("Enter your words to search:")
        if choice=='':loop=False
        else:
            try:
                items=wikipedia.search(choice,results=3)
                print(items)
                try:
                    print(wikipedia.summary(items[0],sentences=1))
                    try:
                        page= wikipedia.page(items[0])
                        print(page.title)
                        print(page.url)
                    except wikipedia.exceptions.DisambiguationError:print("Can not find it.")
                except wikipedia.exceptions.DisambiguationError:
                    print(print(wikipedia.summary(items[1],sentences=1)))
                    try:
                        page= wikipedia.page(items[1])
                        print(page.title)
                        print(page.url)
                    except wikipedia.exceptions.DisambiguationError:
                        print("Can not find it.")

            except IndexError:
                print("Can not find it.")

goto_wiki()