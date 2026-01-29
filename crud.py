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
        'classTable':
        {
            'struct': ["id", "name", "active"],
            'data': [
                {
                    'id': 0, 
                    'name': "rogue", 
                    'active': True
                },
                {
                    'id': 1, 
                    'name': "warrior", 
                    'active': False
                }
            ]
        },
        'animalTable': 
        {
            'struct': ["id", "type", "color", "playful"],
            'data': [
                {
                    'id': 0, 
                    'type': "cat", 
                    'color': "white", 
                    'playful': True
                }
            ]
        }
    
    
    print(f"tableArray:{tableArray}")
    print(f"classTable:{tableArray['classTable']}")
    for tableName in tableArray:
        print(f"tableName:{tableName}")
    for tableName in tableArray:
        print(f"elems from struct: {tableName}")
        print("-------------------------------")
        for elem in tableArray[tableName]['struct']:
            print(f"elem:{elem}")
            
            
if(__name__ == "__main__"):
    main()