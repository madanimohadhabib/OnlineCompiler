from django.shortcuts import render
import sys

#Créez vos vues ici.
#créer une fonction d’indexation

file_path=''

def index(request):
    return render(request, 'index.html')

def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST['codearea']
        input_part = request.POST['input']
        inp =  input_part
        input_part =  input_part.replace("\n"," ").split(" ")
        def input():
            a =  input_part[0]
            del  input_part[0]
            return a

        try:
            #Enregistrer la référence de sortie du standard d’origine
            original_stdout = sys.stdout
            sys.stdout = open('file.txt','w') #modifier la sortie du standerd au fichier que nous avons créé
            #execute code
            exec(codeareadata) 
           
            sys.stdout.close()
            sys.stdout = original_stdout #reset the standard output to its value
            #enfin lire sorti du fichier et enregistrer dans la variable de sortie
            output = open ('file.txt', 'r').read()
        except Exception as e:
            #pour renvoyer l’erreur dans le code
            sys.stdout = original_stdout
            output = e
    #enfin retourner et rendre indexpage et envoyer code et sortie pour afficher sur la page
    return render(request,'index.html',{"code":codeareadata,"input":inp, "output":output})

