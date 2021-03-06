import pickle #전체적으로 예외처리 부탁드립니다.

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
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            if len(parse) != 4:
                print("잘못된 입력입니다.")
            else:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
        elif parse[0] == 'del': #db내에 순서대로 Lee, Kim이 있다고 가정하면, Kim이 있음에도 불구하고 지우지 못합니다.
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)
                else:
                    print("잘못된 입력입니다.")
                    break
        elif parse[0] == 'find':
            for p in scdb:
                if p['Name'] == parse[1]:
                    for attr in sorted(p):
                        print(attr + "=" + p[attr], end=' ')
                    print()
        elif parse[0] == 'inc': #db에 있음에도 inc업데이트를 하지 못합니다.
            for p in scdb:
                if p['Name'] == parse[1]:
                    p['Score'] = str(int(p['Score']) + int(parse[2]))
                    print(p['Name'], '의 점수는', p['Score'])
                else:
                    print('잘못된 입력입니다.')
                    break
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
