import sys
try:
    from tkinter import *  # python 3
except:
    try:
        from mtTkinter import *  # for thread safety
    except:
        from Tkinter import *  # python 2
from tkinter import font as tkFont
from tkinter import messagebox



class Solution(object):
    # Estados para serem utilizados no controle do fluxo da animacao
    estado = 0
    textoStatus = "Utilize o clique esquerdo do mouse ou seta a direita para Avançar.\nSeta a esquerda para Voltar"

    ## Metodos da Questao 1
    def maxArea(self,height):
        """
        Retorna a area maxima usando forca bruta e executando
        um numero quadratico de comparacoes.
        :type height: List[int]
        :rtype: int
        """
        # Inicializando a variável resposta,
        # que ira guardar o maior valor encontrado na interacao de todas as iteracoes possiveis
        area = 0

        # bar1 sera o ponteiro da primeira barra vertical que inicializara na posicao 0 (heigth[0]) do array
        # bar2 sera o ponteiro da segunda barra vertical que inicializara na posicao 1 (heigth[bar1+1]) do array

        # Iremos iterar por forca bruta, testando todas as combinacoes de barras (bar1 x bar2) possiveis
        # Iterando sobre o array, com bar1 na primeira posicao do array heigth[0] ate bar1 na penultima posicao heigth[0]
        for bar1 in range(0, len(height)):
            # Iterando o array, com bar2 comecando na posicao 1 do array heigth[1] ate a ultima barra heigth[n]
            for bar2 in range(bar1+1, len(height)):
                # Verificando se a area do recipiente entre as barras bar1 e bar2 eh maior que a maior ja encontrada
                # Calculando a area do recipiente com bar1 e bar2 nas posicoes atuais
                areaIteracaoBar1Bar2 = min(height[bar1],height[bar2])*(bar2-bar1)
                # Se a area calculada na iteracao atual for maior que a ja encontrada, atualizar contador resposta
                if areaIteracaoBar1Bar2 > area:
                    area = areaIteracaoBar1Bar2
        # Retorna o maior valor encontrado dentre todas as iteracoes possiveis de bar1xbar2
        return area


    def maxAreaOnePass(self,height):
        """ Retorna a area maxima com um unico percurso pela lista .
        :type height: List[int]
        :rtype: int
        """
        # Inicializando a variável resposta, que ira guardar o maior valor encontrado
        area = 0

        # Sabemos que quanto maior a distancia entre as barras verticais, maior sera a area.
        # No entanto, a area eh limitada pela altura da barra vertical. Com isso, iremos iterar com uma passagem so,
        # comecando com bar1 e bar2 em cada extremos do array, deslocando a barra de menor tamanho para dentro
        # do array na proxima iteracao, e assim, sucessivamente. Quando uma barra encontrar a outra, terminaremos a iteracao

        # bar1 sera o ponteiro da primeira barra vertical que inicializara na posicao 0 (heigth[0]) do array
        # bar2 sera o ponteiro da segunda barra vertical que inicializara na ultima posicao (heigth[len(heigth)-1]) do array

        bar1 = 0
        bar2 = len(height)-1

        while bar1 < bar2:
            # Verificando se a area do recipiente entre as barras bar1 e bar2 eh maior que a maior ja encontrada
            # Calculando a area do recipiente com bar1 e bar2 nas posicoes atuais
            areaIteracaoBar1Bar2 = min(height[bar1], height[bar2]) * (bar2 - bar1)
            # Se a area calculada na iteracao atual for maior que a ja encontrada, atualizar contador resposta
            if areaIteracaoBar1Bar2 > area:
                area = areaIteracaoBar1Bar2

            # Atualizando a posicao das barras (bar1 e bar2) para a proxima iteracao
            # Se a barra1 for menor que a barra2, devemos andar com a barra1 da esquerda para direta,
            # somando 1 posicao em bar1.
            if height[bar1] < height[bar2]:
                bar1 = bar1 + 1
            # Caso contrario (barra2 menor que barra1), devemos andar com a barra2 da direita para a esquerda,
            # diminuindo uma posicao em bar2
            else:
                bar2 = bar2 - 1

        # Retorna o maior valor encontrado dentre todas as iteracoes de bar1xbar2
        return area



    ## Metodos da Questao 2
    def createInitialScreen(self):

        # Funcao para processar o evento de Avancar ou Retornar via clique do mouse ou setas do teclado
        def mousePressed(estado, c, tipo):
            if tipo=="back":
                self.estado = self.estado - 2
                estado = estado - 2
                c.delete("step1")
                c.delete("txt")

            if estado < 0:
                estado=-1
                self.estado=-1


            if estado ==-1:
                c.delete("txt")
                c.delete("step1")
                self.textoStatus = "Utilize o clique esquerdo do mouse ou seta a direita para Avançar.\nSeta a esquerda para Voltar"
                c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")
                self.estado=0

            if estado==0:
                c.delete("txt")
                c.create_rectangle(120, 335, 680, 370, fill="#f7dd72", tag="step1")
                self.textoStatus = "1.a Iteracao: Area entre Barra1 na posicao 0 e Barra 2 na posicao 8. \n Na proxima iteracao, como a Barra1 e menor que a Barra2, a Barra1 ira para direita."
                c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")
                self.estado+=1
            elif (estado==1):
                c.delete("step1")
                c.delete("txt")
                c.create_rectangle(155+40, 90+35, 680, 370, fill="#f7dd72", tag="step1")
                self.textoStatus = "2.a Iteracao: Area entre Barra1 na posicao 1 e Barra 2 na posicao 8. \n Na proxima iteracao, como a Barra2 e menor que a Barra1, a Barra2 ira para esquerda."
                c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")
                self.estado+=1
            elif (estado==2):
                c.delete("step1")
                c.delete("txt")
                c.create_rectangle(155+40, 265, 605, 370, fill="#f7dd72", tag="step1")
                self.textoStatus = "3.a Iteracao: Area entre Barra1 na posicao 1 e Barra 2 na posicao 7. \n Na proxima iteracao, como a Barra2 e menor que a Barra1, a Barra2 ira para esquerda."
                c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")
                self.estado+=1
            elif (estado==3):
                c.delete("step1")
                c.delete("txt")
                c.create_rectangle(155+40, 90, 530, 370, fill="#f7dd72", tag="step1")
                self.textoStatus = "4.a Iteracao: Area entre Barra1 na posicao 1 e Barra 2 na posicao 6. \n Na proxima iteracao, como os valores sao iguais, a Barra2 ira para esquerda."
                c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")
                self.estado+=1
            elif (estado==4):
                c.delete("step1")
                c.delete("txt")
                c.create_rectangle(155+40, 230, 455, 370, fill="#f7dd72", tag="step1")
                self.textoStatus = "5.a Iteracao: Area entre Barra1 na posicao 1 e Barra 2 na posicao 5. \n Na proxima iteracao, como a Barra2 e menor que a Barra1, a Barra2 ira para esquerda."
                c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")
                self.estado+=1
            elif (estado==5):
                c.delete("step1")
                c.delete("txt")
                c.create_rectangle(155+40, 195, 380, 370, fill="#f7dd72", tag="step1")
                self.textoStatus = "6.a Iteracao: Area entre Barra1 na posicao 1 e Barra 2 na posicao 4. \n Na proxima iteracao, como a Barra2 e menor que a Barra1, a Barra2 ira para esquerda."
                c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")
                self.estado+=1
            elif (estado==6):
                c.delete("step1")
                c.delete("txt")
                c.create_rectangle(155+40, 300, 305, 370, fill="#f7dd72", tag="step1")
                self.textoStatus = "7.a Iteracao: Area entre Barra1 na posicao 1 e Barra 2 na posicao 3. \n Na proxima iteracao, como a Barra2 e menor que a Barra1, a Barra2 ira para esquerda."
                c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")
                self.estado+=1
            elif (estado==7):
                c.delete("step1")
                c.delete("txt")
                c.create_rectangle(155+40, 160, 230, 370, fill="#f7dd72", tag="step1")
                self.textoStatus = "8.a Iteracao: Area entre Barra1 na posicao 1 e Barra 2 na posicao 2. \n Na proxima iteracao, como as Barras se encontraram, o loop e encerrado."
                c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")
                self.estado+=1
            elif (estado==8):
                c.delete("step1")
                c.delete("txt")
                self.textoStatus = "Fim do algoritmo MaxAreaOnePass. Obrigado!\nPressione Seta a Esquerda para Voltar. Avancar para sair."
                c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")
                self.estado += 1
            elif (estado==9):
                confirmaSair()



        # Subfuncoes do app
        # Instanciando os widgets
        def animar():
            # Array com as alturas de barras para animacao
            data = [1, 8, 6, 2, 5, 4, 8, 3, 7]

            # Binding eventos do mouse e do teclado
            #root.bind("<Escape>", lambda _: confirmaSair())
            root.bind("<Button-1>", lambda _: mousePressed(self.estado, c, "fwd"))
            root.bind("<Right>", lambda _: mousePressed(self.estado, c, "fwd"))
            root.bind("<Left>", lambda _: mousePressed(self.estado, c, "back"))


            # Fechando definitivamente os widgtes da tela Inicial
            playBtn.destroy()
            titulo1.destroy()
            titulo2a.destroy()
            titulo2b.destroy()
            titulo3a.destroy()


            # Criando painel superior com botão de Sair
            exitBtn = Button(text="SAIR", bg="tomato2", fg="azure", padx='15', pady='2', command=confirmaSair)
            exitBtn.pack()


            # Criando Canvas para o grafico
            c_width = 500
            c_height = 200
            c = Canvas(root, width=800, height=450, background='#5AB1BB' )
            c.pack(fill=BOTH, expand=YES)

            #Configuracoes de espacamento para as barras
            margEsq = 80
            larBarra = 40
            espEntrBarra = 35
            #Criando as barras de forma dinamica
            for pos in range(0, len(data)):
                x0 = margEsq + (((larBarra+espEntrBarra)*(pos)))
                y0 = 370-(data[pos]*35)
                x1 =  margEsq + (((larBarra+espEntrBarra)*(pos))) + larBarra
                y1 = 370
                c.create_rectangle( x0, y0,x1,y1, fill="#4E6766", tag="bar8")

            #Criando o quadro da status bar
            c.create_rectangle( 0, 386,800,450, fill="#1E152A", tag="bgStatusBar")

            #Criando as linhas inferior do quadro
            c.create_line(10, 370, 790, 370, width=2)
            # Criando o texto da barra de Status
            c.create_text(400, 416, fill="#a5c882", font="Times 12 bold", text=self.textoStatus, tag="txt")

            #Criando as tags com a posicao das Barras
            c.create_text(40, 378, fill="black", font="Times 8 bold", text="posicao", tag="pos0")
            c.create_text(100, 378, fill="black", font="Times 8 bold", text="0", tag="pos0")
            c.create_text(175, 378, fill="black", font="Times 8 bold", text="1", tag="pos1")
            c.create_text(250, 378, fill="black", font="Times 8 bold", text="2", tag="pos2")
            c.create_text(325, 378, fill="black", font="Times 8 bold", text="3", tag="pos3")
            c.create_text(400, 378, fill="black", font="Times 8 bold", text="4", tag="pos4")
            c.create_text(475, 378, fill="black", font="Times 8 bold", text="5", tag="pos5")
            c.create_text(550, 378, fill="black", font="Times 8 bold", text="6", tag="pos6")
            c.create_text(625, 378, fill="black", font="Times 8 bold", text="7", tag="pos7")
            c.create_text(700, 378, fill="black", font="Times 8 bold", text="8", tag="pos8")




        # Funcao para confirmar a saida
        def confirmaSair():
            result = messagebox.askyesno("Confirmação", "Deseja realmente sair?")
            if result:
                print("A Daniel Corporation agradeçe sua visita. Volte Sempre!")
                root.destroy()



        # Funcao principal do app
        # Create the main window
        root = Tk()

        # Add left and right margin for window first appear
        root.geometry("+250+50")

        # Setting window information
        root.title("PIG MaxAreaOnePass - APX2 2021.1 by Daniel Rocha")

        # Binding Esc keyboard press to exit game
        root.bind("<Escape>", lambda _: confirmaSair())

        # Setting text informations
        fontTitle1 = tkFont.Font(family="Times", size=22, weight="bold")
        fontTitle2 = tkFont.Font(family="Helvetica", size=14, weight="bold")
        fontTitle3 = tkFont.Font(family="Helvetica", size=10, weight="bold")

        # Add text labels
        titulo1 = Label(root, text='Coding Challenge', font=fontTitle1, fg="#1e152a")
        titulo1.pack(pady=(40, 20))
        titulo2a = Label(root, text='Container With Most Water', font=fontTitle2, fg="#4e6766")
        titulo2a.pack(ipady="5")
        titulo2b = Label(root, text='To open interactive GUI, press START button', font=fontTitle2, fg="#4e6766")
        titulo2b.pack(ipady="50", ipadx="20")
        titulo3a = Label(root, text='The algorithm results are printed to the console.', font=fontTitle3)
        titulo3a.pack(ipady="25", ipadx="20")
        playBtn = Button(text=" START ", bg="green", fg="white", padx='30', pady='10', command=animar)
        playBtn.pack(pady=(20, 100))

        # Create App menus
        menuJanela = Menu(root)
        m_jogo = Menu(menuJanela)
        m_ajuda = Menu(menuJanela)
        # Add menu Menu cascade options
        m_jogo.add_cascade(label="Sair", command=confirmaSair)
        # Add menu Ajuda cascade options
        m_ajuda.add_cascade(label="Como Usar", command=lambda: messagebox.showinfo("Manual",
                                                                                   "Para entender o algoritmo, utilize o clique esquerdo do mouse ou seta a direita para Avançar, e seta a esquerda para Voltar"))
        m_ajuda.add_cascade(label="Sobre", command=lambda: messagebox.showinfo("Sobre",
                                                                               "Programa apresentado por exigência da disciplina Programacao com Interfaces Gráficas. Have fun!"))

        # Add menus to principal
        menuJanela.add_cascade(label="Menu", menu=m_jogo)
        menuJanela.add_cascade(label="Ajuda", menu=m_ajuda)
        root.configure(menu=menuJanela)

        # Execute!
        mainloop()



## Main program for testing .
def main ():
    test = [ [1,1],
            [1,8,6,2,5,4,8,3,7],
            [4,3,2,1,4],
            [],
            [1,2,1],
            [1,2,3,4,5,6,7,8,9]
            ]
    s = Solution()

    print("Saida da Questao 1")
    for t in test :
        r1 = s.maxArea(t)
        r2 = s.maxAreaOnePass(t)
        print( "{} = {} = {}".format(t, r1,r2) )

    print()
    print("Questão 2 - Chamando a interface grafica...")
    # Chamando a interface grafica, como metodo createInitialScreen da classe Solution
    s.createInitialScreen()

if __name__=="__main__":
    sys.exit(main())

# Saida esperada
# [1 , 1] = 1 = 1
# [1 , 8 , 6 , 2 , 5 , 4 , 8 , 3 , 7] = 49 = 49
# [4 , 3 , 2 , 1 , 4] = 16 = 16
# [] = 0 = 0
# [1 , 2 , 1] = 2 = 2
# [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9] = 20 = 20
