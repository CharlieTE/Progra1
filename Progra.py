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
    listaSimbolosPuntuacion = [',',';',':','.','?','¿','¡','!','(',')','-','*']
    for i in texto:
        if i in listaSimbolosPuntuacion :
            texto=texto.replace(i,"")    #Esto fue un problema porque no ponia que texto=texto.replace() solo texto.replace
    f=open('texto.txt','w')
    f.write(texto)
    f.close

            
def token():
    #Cambié el funcionamiento, donde en lugar de comparar en los if o elif, compara con listas creadas con los articulos, preposiciones, etc.
    #Evalúa que haya un archivo antes de tokenizar
    try:
        f=open('texto.txt','r')
        texto=f.read()
        f.close
        texto=texto+' '
        #listas
        listaArticulos=['el','la','los','las','un','una','unos','unas','lo','al','del']
        listaPreposiciones=['a','ante','bajo','cabe','con','contra','de','desde','durante','en','entre','hacia','hasta','mediante','para','por','según','sin','so','sobre','tras','versus','vía']
        listaPronombres=['yo','me','mí','conmigo','nosostros','nosotras','nos','tú','te','ti','contigo','vosotros','vosotras','vos','él','ella','se','consigo','le','les','mío','mía','míos','mías','nuestro',
                         'nuestra','nuestros','nuestras','tuyo','tuya','tuyos','vuestro','vuestra','vuestros','vuestras','suyo','suya','suyos','suyas']
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
                if palabra.lower() in listaArticulos:
                    if palabra.lower() not in arti:
                        arti=arti+[palabra]
                    
                #Preposiciones(a,ante,bajo,cabe,con,contra,de,desde,durante,en,entre,hacia,hasta,mediante,para,por,según,sin,so,sobre,tras,versus,vía) 
                elif palabra.lower() in listaPreposiciones:
                    if palabra.lower() not in prepo:
                        prepo=prepo+[palabra]
                    
                #Pronombres
                elif palabra.lower() in listaPronombres:
                    if palabra.lower() not in prono:
                        prono=prono+[palabra]

                #Verbos
                #Infinitivo
                elif palabra.lower()[len(palabra)-2:]=='ar' or palabra.lower()[len(palabra)-2:]=='er' or palabra.lower()[len(palabra)-2:]=='ir':
                    if palabra.lower() not in verbo:
                        verbo=verbo+[palabra]
                        
                #Gerundio
                elif palabra.lower()[len(palabra)-4:]=='ando' or palabra.lower()[len(palabra)-5:]=='iendo':
                    if palabra.lower() not in verbo:
                        verbo=verbo+[palabra]
                        
                #Participio
                elif palabra.lower()[len(palabra)-3:]=='ado' or palabra.lower()[len(palabra)-3:]=='ido' or palabra.lower()[len(palabra)-2:]=='to' or palabra.lower()[len(palabra)-2:]=='so' or palabra.lower()[len(palabra)-3:]=='cho':
                    if palabra.lower() not in verbo:
                        verbo=verbo+[palabra]

                #Numero
                elif palabra.isdigit():
                    if palabra.lower() not in num:
                        num=num+[palabra]
                    
                #Sin clasificador
                else:
                    if palabra!='':
                        if palabra.lower() not in tokensin:
                            tokensin=tokensin+[palabra]
                
                palabra=''
    
        #Esto es para comprobar que se tokenizan bien
        arti=ordenar(arti)
        prepo=ordenar(prepo)
        prono=ordenar(prono)
        verbo=ordenar(verbo)
        num=ordenar(num)
        tokensin=ordenar(tokensin)
        print('Articulo: ',arti)
        print('Preposicion: ',prepo)
        print('Pronombre: ',prono)
        print('Verbo: ',verbo)
        print('Numero: ',num)
        print('Token sin Clasif',tokensin)
    except:
        print('No existe archivo, realice la fase 1 para poder tokenizar.')
        
#Ordena la listas alfabéticamente sin importar que estén en mayúscula o minúscula
def ordenar(lista):
    pos = 2
    ordenado = 0
    for i in lista:
        pos = 2
        ordenado = 0
        while pos <= len(lista):
            if lista[ordenado].lower() > lista[ordenado+1].lower():
                lista.insert(pos, lista[ordenado])
                del lista[ordenado]
            else:
                pass
            pos += 1
            ordenado += 1
    return lista

#menu donde entra si se logró tokenizar, para general los diferenes tipos de archivo
def menu2():
    print ("\n**************************\n")
    print ("Generar salidas")
    print ("\n**************************\n")
    print ("1. Generar Html.")
    print ("2. Generar XML.")
    print ("3. Generar Binario.")
    opcion = int (input ("Escoja una opción: "))
    if opcion >=0 and opcion <=3:   
        if opcion == 1:
            generarHtml()
        elif opcion == 2 :
            generarXML()
        elif opcion == 3:
            generarBinario()
        else:
            return
    else:
        print ("Opción inválida, indique una opción según las opciones indicadas.")
    menu2()

#Menu que se utiliza para que el usuario indique lo que quiere realizar
def menu(tokenizo):
    print ("\n**************************\n")
    print ("TOKENIZACIÓN")
    print ("\n**************************\n")
    print ("1. Fase 1")
    print ("2. Tokenizar")
    print ("3. Generar salidas")
    print ("4. Terminar")
    opcion = int (input ("Escoja una opción: "))
    if opcion >=0 and opcion <=4:   
        if opcion == 1:
            inicia()
        elif opcion == 2 :
            desicion = 0
            while desicion != 1 and desicion!=2:
                desicion = int(input('Desea tokenizar? \n 1.Si 2.No '))
                if desicion == 1:
                    tokenizo == True
                    token()
                elif desicion == 2:
                    return menu(tokenizo)
                else:
                    print('Digite la opción correcta.')
                
        elif opcion == 3:
            print ("Genarar salidas")
            if tokenizo == True:
                menu2()
            else:
                print('Antes debe tokenizar.')
                menu(tokenizo)
        else:
            return
    else:
        print ("Opción inválida, indique una opción según las opciones indicadas.")
    menu(tokenizo)


    

#Progrma Principal
tokenizo = False #Variable que sirve para validar que se haya tokenizado, más adelante
menu(tokenizo)   




























