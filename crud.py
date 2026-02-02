def     create_table()-> list:
    table = {}
    
    tableName = input("What is your table name? :")
    colNbr = int(input("How many columns you need?: "))
    table = {
        tableName: 
        {
            'struct': [],
            'data': []         
        }
    }
    print("Registering the columns in your table now...")
    for i in range(colNbr):
        colName = input(f"columnName[{i + 1}]:")
        colType = input(f"columnType[{i + 1}]:")
        #on doit convertir la string input pour le type voulu
        colType = mapping_types(colType)
        pair = (colName, colType)#tuple pour les éléments de struct à envoyer dans la liste
        table[tableName]['struct'].append(pair)#ajout du tupple dans la clef struct de la table
        
    print("---debug---")
    print(f"table: {table}")
    
    return table


def     mapping_types(elem):
    map = {
        'int': int,
        'str': str,
        'bool': bool,
        'float': float
    }
    
    return map[elem]
          
        
def     main():    
    #create_table()
    #restructuring table with dicos
    tableArray = {
    }
    
    create_table()
            
            
if(__name__ == "__main__"):
    main()