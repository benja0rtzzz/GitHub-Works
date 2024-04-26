#Librería de expresiones regulares
import re
#Constante de la ruta del output
htmlConst = "./output.html"
#Necesitamos compilar las expresiones regulares antes de usarlas
isDataType = re.compile(" *(int\s|float\s|bool\s|string\s|char\s|void\s) *")
isVariable = re.compile(" *[aA-zZ\d]*[^\(\!\)\+\-\*\,\;\:\>]")
isOperator = re.compile(" *(\+|\-|\*|\/|<|>|\=|\%|\{|\}|\:|return) *")
isInclude = re.compile("(#include *.*)|using namespace std")

#Para identificar que hay dentro de la función:
isFunctionOpen = re.compile(" *([aA-zZ\d])*\(")
isFunctionClose = re.compile("( *\) *)")
isLoop = re.compile(" *(while * *\() *| *(for * *\()")
isCondiOpen = re.compile(" *(if|else if|else)( *\()")
isCondiClose = re.compile("( *\) *)|(\) *)")
isComment = re.compile("( *\/\/.*)|( *\/\*([^\/\*].*\*\/) *)")

#Para identificar que hay dentro de un cout o un cin
isCoutOpen = re.compile(" *((cout *)|(cin *))")
isCloseCout = re.compile(" *<< *endl *")
#Otros
isJump = re.compile(" *\n")
isSemiColon = re.compile(" *; *")
isText = re.compile("\"([^\"]*)\"")
isComma = re.compile(" *,")

#Definición de funciones:

#Abrir el archivo y formatear las líneas en un array
def openDoc(doc, array):
    f = open(doc, 'r')
    while True:    
        line = f.readline()
        if not line:
            break
        array.insert(len(array),line)
    
    f.close()

#Inicializar el archivo con los nombres de los integrantes
def initializeHtml(html):
    f = open(html, 'w')
    f.write("<!DOCTYPE html>\n" )
    f.write("<html>\n" )
    f.write("   <body>\n" )
    f.write("<style>\n")
    f.write(".dataTypes{color: MediumOrchid;}\n")
    f.write(".variables{color: PowderBlue;}\n")
    f.write(".operators{color: Beige;}\n")
    f.write(".constants{color: turquoise;}\n")
    f.write(".conditionals{color: LightSalmon;}\n")
    f.write(".comments{color: #00A009;}\n")
    f.write(".loops{color: darkblue;}\n")
    f.write(".text{color: gold;}\n")
    f.write(".others{color: SteelBlue;}\n")
    f.write(".codeCont{width: 800px; height: auto; background-color: #333C3D;}")
    f.write(".tagsCont{width: 400px; height: auto; background-color: #333C3D;}")
    f.write(".mainCont{display: flex; justify-content: center; align-items: center; flex-direction: column; font-family: 'Trebuchet MS', sans-serif;}")
    f.write("</style>\n")
    f.write("<div class=\"mainCont\">")
    f.write("   <h1>Lexical Highlighter</h1>\n")
    f.write("   <ol><h2>\n")
    f.write("       <li>José Benjamín Ortiz Badillo A01277673</li>\n")
    f.write("       <li>Carlos Alberto Mentado Reyes A01276065</li>\n")
    f.write("       <li>Juan Yael Avalos Mayorga A01276329</li>\n")
    f.write("   </h2></ol>\n")
    f.write("<div class=\"tagsCont\">")
    f.write("<h2><font color=\"white\">Etiquetas de color:</font></h2>\n")
    f.write("<span class =\"dataTypes\"><h2>Data Types - MediumOrchid</h2></span>\n")
    f.write("<span class =\"variables\"><h2>Variables - PowderBlue</h2></span>\n")
    f.write("<span class =\"operators\"><h2>Operators - Beige</h2></span>\n")
    f.write("<span class =\"conditionals\"><h2>Conditionals - LightSalmon</h2></span>\n")
    f.write("<span class =\"comments\"><h2>Comments - Green</h2></span>\n")
    f.write("<span class =\"constants\"><h2>Constants - Turquoise</h2></span>\n")
    f.write("<span class =\"loops\"><h2>Loops - Dark Blue</h2></span>\n")
    f.write("<span class =\"text\"><h2>Text - Gold</h2></span>\n")
    f.write("<span class =\"others\"><h2>Others - SteelBlue</h2></span>\n")
    f.write("</div>")
    f.write("<h1>Código:</h1>\n")
    f.write("<div class=\"codeCont\">")
    f.write("<font size=\"4\">")

    f.close()

#Para formatear en el html
def writeWithStyle(line):
    f = open(htmlConst, 'a')
    line = line.replace("  ", "&nbsp;&nbsp;")
    f.write(line)
    f.write("</span>")
    f.close()
    
#Función para manejar cout
def examineCout(line):
    f = open(htmlConst, 'a')
    if(isComment.match(line)):
        m = isComment.match(line)
        f.write("\n<span class=\"comments\">")
        f.close()
        writeWithStyle(m.group()+"</br>")    
        examineCout(remove(line, m.start(), m.end()))
    elif(isOperator.match(line)):
        m = isOperator.match(line)
        f.write("\n<span class=\"operators\">")
        f.close()
        writeWithStyle(m.group())        
        examineCout(remove(line, m.start(), m.end()))
    elif(isText.match(line)):
        m = isText.match(line)
        f.write("\n<span class=\"text\">")
        f.close()
        writeWithStyle(m.group())    
        examineCout(remove(line, m.start(), m.end()))
    elif(isCloseCout.match(line)):
        m = isCloseCout.match(line)
        f.write("\n<span class=\"couts\">")
        f.close()
        writeWithStyle(m.group())    
        examine(remove(line, m.start(), m.end()))
    elif(isSemiColon.match(line)):
        m = isSemiColon.match(line)
        f.write("\n<span class=\"others\">")
        f.close()
        writeWithStyle(m.group())    
        examineCout(remove(line, m.start(), m.end()))
    elif(isJump.match(line)):
        m = isJump.match(line)
        f.write("</br>")
        f.close
    elif(isVariable.match(line)):
        m = isVariable.match(line)
        f.write("\n<span class=\"variables\">")
        f.close()
        writeWithStyle(m.group())    
        examineCout(remove(line, m.start(), m.end()))
    else:
        return   

#Función para manejar funciones
def examineFunction(line):
    f = open(htmlConst, 'a')
    if(isComment.match(line)):
        m = isComment.match(line)
        f.write("\n<span class=\"comments\">")
        f.close()
        writeWithStyle(m.group()+"</br>")    
        examineFunction(remove(line, m.start(), m.end()))
    elif(isOperator.match(line)):
        m = isOperator.match(line)
        f.write("\n<span class=\"operators\">")
        f.close()
        writeWithStyle(m.group())    
        examineFunction(remove(line, m.start(), m.end()))
    elif(isComma.match(line)):
        m = isComma.match(line)
        f.write("\n<span class=\"others\">")
        f.close()
        writeWithStyle(m.group())    
        examineFunction(remove(line, m.start(), m.end()))
    elif(isDataType.match(line)):
        m = isDataType.match(line)
        f.write("\n<span class=\"dataTypes\">")
        f.close()
        writeWithStyle(m.group())    
        examineFunction(remove(line, m.start(), m.end()-1))
    elif(isJump.match(line)):
        m = isJump.match(line)
        f.write("</br>")
        f.close
    elif(isSemiColon.match(line)):
        m = isSemiColon.match(line)
        f.write("\n<span class=\"others\">")
        f.close()
        writeWithStyle(m.group())    
        examineFunction(remove(line, m.start(), m.end()))
    elif(isVariable.match(line)):
        m = isVariable.match(line)
        f.write("\n<span class=\"variables\">")
        f.close()
        writeWithStyle(m.group())    
        examineFunction(remove(line, m.start(), m.end()))
    elif(isFunctionClose.match(line)):
        m = isFunctionClose.match(line)
        f.write("\n<span class=\"others\">")
        f.close()
        writeWithStyle(m.group())
        examine(remove(line, m.start(), m.end()))
    else:
        return

#Función para examinar contenido de los loops
def examineLoops(line):
    f = open(htmlConst, 'a')
    if(isComment.match(line)):
        m = isComment.match(line)
        f.write("\n<span class=\"comments\">")
        f.close()
        writeWithStyle(m.group()+"</br>")    
        examineLoops(remove(line, m.start(), m.end()))
    elif(isDataType.match(line)):
        m = isDataType.match(line)
        f.write("\n<span class=\"dataTypes\">")
        f.close()
        writeWithStyle(m.group())    
        examineLoops(remove(line, m.start(), m.end()-1))
    elif(isSemiColon.match(line)):
        m = isSemiColon.match(line)
        f.write("\n<span class=\"others\">")
        f.close()
        writeWithStyle(m.group())    
        examineLoops(remove(line, m.start(), m.end()))
    elif(isOperator.match(line)):
        m = isOperator.match(line)
        f.write("\n<span class=\"operators\">")
        f.close()
        writeWithStyle(m.group())    
        examineLoops(remove(line, m.start(), m.end()))
    elif(isFunctionClose.match(line)):
        m = isFunctionClose.match(line)
        f.write("\n<span class=\"loops\">")
        f.close()
        writeWithStyle(m.group())    
        examine(remove(line, m.start(), m.end()))
    elif(isJump.match(line)):
        m = isJump.match(line)
        f.write("</br>")
        f.close
    elif(isVariable.match(line)):
        m = isVariable.match(line)
        f.write("\n<span class=\"variables\">")
        f.close()
        writeWithStyle(m.group())    
        examineLoops(remove(line, m.start(), m.end()))
    else:
        return

#Función para examinar los condicionales
def examineCond(line):
    f = open(htmlConst, 'a')
    if(isComment.match(line)):
        m = isComment.match(line)
        f.write("\n<span class=\"comments\">")
        f.close()
        writeWithStyle(m.group()+"</br>")    
        examineCond(remove(line, m.start(), m.end()))
    elif(isOperator.match(line)):
        m = isOperator.match(line)
        f.write("\n<span class=\"operators\">")
        f.close()
        writeWithStyle(m.group())    
        examineCond(remove(line, m.start(), m.end()))
    elif(isCondiClose.match(line)):
        m = isCondiClose.match(line)
        f.write("\n<span class=\"conditionals\">")
        f.close()
        writeWithStyle(m.group())    
        examineCond(remove(line, m.start(), m.end()))
    elif(isJump.match(line)):
        m = isJump.match(line)
        f.write("</br>")
        f.close()
    elif(isVariable.match(line)):
        m = isVariable.match(line)
        f.write("\n<span class=\"variables\">")
        f.close()
        writeWithStyle(m.group())    
        examineCond(remove(line, m.start(), m.end()-1))
    else:
        return
    
#Función de comparación general
def examine(line):
    f = open(htmlConst, 'a')
    if(isInclude.match(line)):
        m = isInclude.match(line)
        f.write("\n<span class=\"comments\">")
        f.close()
        writeWithStyle(m.group()+"</br>")
    elif(isComment.match(line)):
        m = isComment.match(line)
        f.write("\n<span class=\"comments\">")
        f.close()
        writeWithStyle(m.group()+"</br>")    
    elif(isOperator.match(line)):
        m = isOperator.match(line)
        f.write("\n<span class=\"operators\">")
        f.close()
        writeWithStyle(m.group())    
        examine(remove(line, m.start(), m.end()))
    elif(isCoutOpen.match(line)):
        m = isCoutOpen.match(line)
        f.write("\n<span class=\"others\">")
        f.close()
        writeWithStyle(m.group())        
        examineCout(remove(line, m.start(), m.end()-1))
    elif(isLoop.match(line)):
        m = isLoop.match(line)
        f.write("\n<span class=\"loops\">")
        f.close()
        writeWithStyle(m.group())    
        examineLoops(remove(line, m.start(), m.end()))
    elif(isCondiOpen.match(line)):
        m = isCondiOpen.match(line)
        f.write("\n<span class=\"conditionals\">")
        f.close()
        writeWithStyle(m.group())    
        examineCond(remove(line, m.start(), m.end()))
    elif(isDataType.match(line)):
        m = isDataType.match(line)
        f.write("\n<span class=\"dataTypes\">")
        f.close()
        writeWithStyle(m.group())    
        examine(remove(line, m.start(), m.end()-1))
    elif(isFunctionOpen.match(line)):
        m = isFunctionOpen.match(line)
        f.write("\n<span class=\"others\">")
        f.close()
        writeWithStyle(m.group())    
        examineFunction(remove(line, m.start(), m.end()))
    elif(isSemiColon.match(line)):
        m = isSemiColon.match(line)
        f.write("\n<span class=\"others\">")
        f.close()
        writeWithStyle(m.group())    
        examine(remove(line, m.start(), m.end()))
    elif(isComma.match(line)):
        m = isComma.match(line)
        f.write("\n<span class=\"others\">")
        f.close()
        writeWithStyle(m.group())    
        examine(remove(line, m.start(), m.end()))
    elif(isJump.match(line)):
        m = isJump.match(line)
        f.write("</br>")
        f.close
    elif(isFunctionClose.match(line)):
        m = isFunctionClose.match(line)
        f.write("\n<span class=\"others\">")
        f.close()
        writeWithStyle(m.group())    
        examine(remove(line, m.start(), m.end()))
    elif(isText.match(line)):
        m = isText.match(line)
        f.write("\n<span class=\"text\">")
        f.close()
        writeWithStyle(m.group())    
        examine(remove(line, m.start(), m.end()))
    elif(isVariable.match(line)):
        m = isVariable.match(line)
        f.write("\n<span class=\"variables\">")
        f.close()
        writeWithStyle(m.group())    
        examine(remove(line, m.start(), m.end()))
    else:
        return

#Función para completar el html y cerrar el documento
def closeHtml(html):
    f = open(html, 'a')
    f.write("</font>")
    f.write("</div>")
    f.write("</div>")
    f.write("   </body>\n" )
    f.write("</html>\n" )
    f.close()   

#Esta la utilizaremos para quitar los elementos de la línea que ya inspeccionamos
def remove(line, start, end):
    if(end == 0): end = 1
    range = [(start, end)]
    res = ""
    for idx, chr in enumerate(line):
        for strt_idx, end_idx in range:
            if strt_idx <= idx + 1 <= end_idx: 
                break
        else:
            res += chr
    return res


#Función para el formato en html, cada array pasará con un id, y con eso se pondrán de distintos colores

#Programa principal
#Declaración de variables
mainArray = []
i = 0

#Inicialización del array principal (contiene el txt segmentado línea por línea)
openDoc("./program.txt", mainArray)

#Inicializar el html que contendrá lo demás
initializeHtml("./output.html")

#Código
for i in range(len(mainArray)):
    examine(mainArray[i])


#Cerrar el html que contendrá lo demás
closeHtml("./output.html")


