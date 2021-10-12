import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        
        try:
            if inputstr == "": continue
            parse = inputstr.split(" ")
        
            if parse[0] == 'add':
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            
           
            elif parse[0]=='del': #Del all same name 
	            i=len(scdb)-1
	            whilei>=0:
		            if scdb[i]["Name"]==parse[1]:
			           delscdb[i]
				       i-=1
                    
            elif parse[0] == 'show':
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
                
            elif parse[0]=="find": #find given name
	            for i in scdb:
		            if parse[1] == i["Name"]:
			            for v in sorted(i):
				            print(v + "=" + str(i[v]), end=' ')
				            print()
                    
            elif parse[0]=="inc": #amount score given name
	            for i in scdb:
		            if parse[1] == i["Name"]:
			            i["Score"] += int(parse[2])
		            else:
			            print("Invalid command: "+parse[0])

            elif parse[0] == 'quit':
                break

            else:
                print("Invalid command: " + parse[0])
                
        except:
            print("error")


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
