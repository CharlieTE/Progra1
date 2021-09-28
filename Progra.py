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
            texto=texto.replace(i,"")    #Esto fue un problema porque no ponia que texto=texto.replace() solo texto.replace
    f=open('texto.txt','w')
    f.write(texto)
    f.close

            
def token():
    f=open('texto.txt','r')
    texto=f.read()
    f.close
    texto=texto+' '
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
        #print(palabra)
        if i == ' ':
            palabra=palabra.replace(' ','')
            #Articulo(el,la,los,las,un,una,unos,unas,lo,al,del)
            if palabra=='el' or palabra=='la' or palabra=='los' or palabra=='las' or palabra=='un' or palabra=='una' or palabra=='unos' or palabra=='unas' or palabra=='lo' or palabra=='al' or palabra=='del': 
                arti=arti+[palabra]
                print('Articulo')
        
            #Preposiciones(a,ante,bajo,cabe,con,contra,de,desde,durante,en,entre,hacia,hasta,mediante,para,por,según,sin,so,sobre,tras,versus,vía) 
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
            elif palabra=='míos' or palabra=='mías' or palabra=='nuestro' or palabra=='nuestra' or palabra=='nuestros' or palabra=='nuestras' or palabra=='tuyo' or palabra=='tuya' or palabra=='tuyos' or palabra=='vuestro' or palabra=='vuestra':
                prono=prono+[palabra]
                print('prono')
            elif palabra=='vuestros' or palabra=='vuestras' or palabra=='suyo' or palabra=='suya' or palabra=='suyos' or palabra=='suyas':
                prono=prono+[palabra]
                print('prono')

            #Verbos
            #Infinitivo
            elif palabra[len(palabra)-2:]=='ar' or palabra[len(palabra)-2:]=='er' or palabra[len(palabra)-2:]=='ir':
                verbo=verbo+[palabra]
            #Gerundio
            elif palabra[len(palabra)-4:]=='ando' or palabra[len(palabra)-5:]=='iendo':
                verbo=verbo+[palabra]
            #Participio
            elif palabra[len(palabra)-3:]=='ado' or palabra[len(palabra)-3:]=='ido' or palabra[len(palabra)-2:]=='to' or palabra[len(palabra)-2:]=='so' or palabra[len(palabra)-3:]=='cho':
                verbo=verbo+[palabra]

            #Numero
            elif palabra.isdigit():
                num=num+[palabra]
                
            #Sin clasificador
            else:
                tokensin=tokensin+[palabra]
            
            palabra=''
            
    #Esto es para comprobar que se tokenizan bien        
    print('Articulo: ',arti)
    print('Preposicion: ',prepo)
    print('Pronombre: ',prono)
    print('Verbo: ',verbo)
    print('Numero: ',num)
    print('Token sin Clasif',tokensin)





inicia()
token()    
