def     mapping_types(elem):
    map = {
        'int': int,
        'str': str,
        'bool': bool,
        'float': float
    }
    
    return map[elem]

def     create_table(tableArray:dict)-> list:#penser a gere un CREATE TABLE(juste cree la table et gere le nom de table apres la commande)
                              #ou on fait CREATE TABLE tableName(on recup largu qu'on donne)
    tableName = input("What is your table name? :")
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

def     insert_table(table:dict, elemStr:str)-> None:
    elemsArray = elemStr.split(' ')
    structElemArray = table['struct'] #on recup la liste de tupples de struct via un alias 
    data = {} #dico vide pour recevoir les datas
    for i in range(len(table['struct'])):
        elemsArray[i] = structElemArray[i][1](elemsArray[i]) #typecast via la struct de la table
        data[structElemArray[i][0]] = elemsArray[i] #on stocke chaque elem avec la clef struct de table dans le dico data
    table['data'].append(data)
        
def     main():    
    #create_table()
    #restructuring table with dicos
    tableArray = {
        'perso':
        {
            'struct': [("id", int), ("name", str), ("class", str), ("dmg", int), ("active", bool)],
            'data': []
        }
    }
    
    insert_table(tableArray['perso'], "0 ragnar warrior 100 True")
    print(tableArray)
            
if(__name__ == "__main__"):
    main()