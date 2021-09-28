'''
def abrirArc():
    f=open('texto.txt','r')
    text=f.read()
    f.close
def crearArc():
    f = open ('texto.txt','w')
    f.write(texto)
    f.close()
def apenArch():
    f = open('texto.txt','a')
    f.write('\n' + 'Prueba de apendice')
    f.close()
'''

def inicia():
    texto=input('Ingrese el texto: ')
    for i in texto:
        if i == ',' or i =='.':
            texto=texto.replace(i,"")      #Esto fue un problema porque no ponia que texto=texto.replace() solo texto.replace
    f=open('texto.txt','w')
    f.write(texto)
    f.close

            
def token():
    f=open('texto.txt','r')
    texto=f.read()
    f.close
    print(texto)
    #listas
    arti=[]
    prepo=[]
    prono=[]
    verbo=[]
    num=[]
    tokensin=[]
    documento=[]
    palabra=''
    for i in texto:
        palabra=palabra+i
        print(palabra)
        if i == ' ':
            #Articulo(el,la,los,las,un,una,unos,unas,lo,al,del)
            if palabra=='el' or palabra=='la' or palabra=='los' or palabra=='las' or palabra=='un' or palabra=='una' or palabra=='unos' or palabra=='unas' or palabra=='lo' or palabra=='al' or palabra=='del': 
                arti=arti+[palabra]
                print('Articulo')
        
            #Preposiciones(a,ante,bajo,cabe,con,contra,de,desde,durante,en,entre,hacia,hasta,mediante,para,por) 
            elif palabra=='a' or palabra=='ante' or palabra=='bajo' or palabra=='cabe' or palabra=='con' or palabra=='contra' or palabra=='de' or palabra=='desde' or palabra=='durante' or palabra=='en' or palabra=='entre':
                prepo=prepo+[palabra]
                print('prepo')
            elif palabra=='hacia' or palabra=='hasta' or palabra=='mediante' or palabra=='para' or palabra=='por' or palabra=='según' or palabra=='sin' or palabra=='so' or palabra=='sobre' or palabra=='tras' or palabra=='versus' or palabra=='vía':
                prepo=prepo+[palabra]
                print('prepo')
                
            #Pronombres
            elif palabra=='yo' or palabra=='me' or palabra=='mí' or palabra=='conmigo' or palabra=='nosotros' or palabra=='nosotras' or palabra=='nos' or palabra=='tú' or palabra=='te' or palabra=='ti' or palabra=='contigo':
                prono=prono+[palabra]
                print('prono')
            elif palabra=='vosotros' or palabra=='vosotras' or palabra=='vos' or palabra=='él' or palabra=='ella' or palabra=='se' or palabra=='consigo' or palabra=='le' or palabra=='les' or palabra=='mío' or palabra=='mía':
                prono=prono+[palabra]
                print('prono')

            palabra=''

                
inicia()
token()
