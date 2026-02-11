from typing import Tuple

def     mapping_types(elem):
    map = {
        'int': int,
        'str': str,
        'bool': bool,
        'float': float
    }
    
    return map[elem]

def     gen_cmd_and_table_array()-> Tuple[dict, dict]:
    tableArray = {
        'Character':
        {
            'struct': [("id", int), ("name", str), ("class", str), ("hp", int), ("dmg", int), ("active", bool)],
            'data': []
        }
    }
    cmdArray = {
        'CREATE':
        {
            'args': ["Mob"],
            'func': create_table
        },
        'INSERT':
        {
            'args': ["0 Spartacus warrior 100 230 True"],
            'func': insert_table
        },
        'DELETE':
        {
            'args': ["Mob"],
            'func': delete_table
        }
    }
    
    return (cmdArray, tableArray)

def     create_table(tableArray:dict, tableName:str)-> list:
    colNbr = int(input("How many columns you need?: "))
    table = {
        'struct': [],
        'data': []
    }
    
    print("Registering the columns in your table now...")
    for i in range(colNbr):
        colName = input(f"columnName[{i + 1}]:")
        colType = input(f"columnType[{i + 1}]:")
        #on doit convertir la string input pour le type voulu
        colType = mapping_types(colType)
        pair = (colName, colType)#tuple pour les éléments de struct à envoyer dans la liste
        table['struct'].append(pair)#ajout du tupple dans la clef struct de la table
        tableArray[tableName] = table

def     insert_table(tableArray:dict, elemStr:str)-> None:
    elemsArray = elemStr.split(' ')
    structElemArray = tableArray['struct'] #on recup la liste de tupples de struct via un alias 
    data = {} #dico vide pour recevoir les datas
    for i in range(len(tableArray['struct'])):
        elemsArray[i] = structElemArray[i][1](elemsArray[i]) #typecast via la struct de la table
        data[structElemArray[i][0]] = elemsArray[i] #on stocke chaque elem avec la clef struct de table dans le dico data
    tableArray['data'].append(data)

def     delete_table():
    pass  
        
def     main():
    cmdArray, tableArray = gen_cmd_and_table_array()
    
    print(f"cmdArray: {cmdArray}")
    print(f"tableArray: {tableArray}")

    createArg = cmdArray['CREATE']['args']
    createFunc = cmdArray['CREATE']['func']
    
    createFunc(tableArray, createArg)
    
    print(tableArray)
        
if(__name__ == "__main__"):
    main()