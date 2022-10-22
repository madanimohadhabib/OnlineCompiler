from django.shortcuts import render
import sys
# Create your views here.

#create index fuction
file_path=''

def index(request):
    return render(request, 'index.html')

def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt','w') #change the standerd output to the file we created

            #execute code

            exec(codeareadata) 

            sys.stdout.close()

            sys.stdout = original_stdout #reset the standard output to its value

            #finally read out put from file and save in output variable

            output = open ('file.txt', 'r').read()
        except Exception as e:
            #to return error in the code
            sys.stdout = original_stdout
            output = e
    #finally return and render indexpage and send codedata and output to show on page

    return render(request,'index.html',{"code":codeareadata, "output":output})

