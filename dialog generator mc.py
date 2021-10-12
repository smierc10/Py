print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#setup
dialog = []
dialog1 = []
dialog2 = []
dialog3 = []
dialog4 = []
score = str(input('Score Name:\n'))
amount = 0
x=0
odppierwszy = 0
#openfile
print("\n\n\n")
# Open file
mf = open('save.txt', "r+")


# Read all lines in the file
file_content = mf.readlines()
file_content2 = file_content

# Close opened file
mf.close()
#liczenie $
for line in file_content:
    if line[0] == "$":
        amount = amount + 1
#pozycje $
for line in file_content:
    x = x+1
    if line[0] == "$":
        dialog1.append(x)
x=0


def get_message_and_target_statement(x):
    dialog.append(file_content[x])
    dialog.append(int(file_content[x+1]))

    


def get_info(line):
    dialog2=[]
    statementnr=int(file_content[line])
    iloscodp = int(file_content[line+2])
    dialog.append(file_content[line+1])
    odppierwszy = line+3
    
    iloscodp2 = int(file_content[iloscodp])
    while iloscodp > 0:
        get_message_and_target_statement(odppierwszy)
        iloscodp = iloscodp -1
        odppierwszy = odppierwszy +2
    dialog2.append("{\"text\":\""+str(dialog[0])+"\"}")
    dialog.pop(0)
    while iloscodp2 > 0:
        iloscodp2 = iloscodp2 -1
        dialog2.append("{\"text\":\""+str(dialog[0])+"\",\"clickEvent\":{\"action\":\"run_command\",\"value\":\"/trigger "+ score +" set "+str(dialog[1])+"\"}")
        dialog.pop(0)
        dialog.pop(0)
    text = "[\"\""
    for i in dialog2:
        text = text+ ","+i
    text=text+"]"
    dialog3.append("tellraw @a[scores={"+str(score)+"="+str(statementnr)+"}] "+text)
    text = ""


def get_statement(x):
    for line in file_content:
        x = x+1
        if line[0] == "$":
            get_info(x)

get_statement(x)




for tell in dialog3:
    print(tell)

#print(dialog1)
#print(dialog)
# sprawdzic czy zaczyna sie na $ jesli tak to dodac wszytskie nastepne linijki do nastepnego $ zrobic komende dodac do glownego 