def     create_table():
    colTableArray = []
    
    test = ()
    tableName = input("What is your table name? :")
    colNbr = int(input("How many columns you need?: "))
    print("Registering the columns in your table now...")
    for i in range(colNbr):
        elem = input(f"column[{i}]:")
        colTableArray.append(elem)
        
    print("---debug---")
    print(f"tableName: {tableName}")
    print(f"colTableArray: {colTableArray}")
    
        
def     main():
    print("entry pgm...")
    
    create_table()

if(__name__ == "__main__"):
    main()