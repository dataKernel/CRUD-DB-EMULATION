def     create_table()-> list:
    colTableArray = []
    
    test = ()
    tableName = input("What is your table name? :")
    colNbr = int(input("How many columns you need?: "))
    print("Registering the columns in your table now...")
    for i in range(colNbr):
        colElem = input(f"columnName[{i+1}]:")
        colTableArray.append(colElem)
        colType = input(f"columnType[{i + 1}]:")
        colTableArray.append(colType)  
        
        
    print("---debug---")
    print(f"tableName: {tableName}")
    print(f"colTableArray: {colTableArray}")
    
    return colTableArray
        
        
def     main():
    
    
    #create_table()
    #restructuring table with dicos
    tableArray = {
        "classTable":
        {
          'id': 0,
          'name': "rogue",
          'active': True  
        },
        "animalTable": 
        {
            'id': 0,
            'type': "dog",
            'color': "black"
        }
    }
    
    print(f"tableArray: {tableArray}")
    #tableArray = create_table()
    #print(f"exemple natif: {tableArray}")
    
if(__name__ == "__main__"):
    main()