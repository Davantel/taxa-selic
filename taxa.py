import tkinter as tk
import customtkinter as tkc
from PIL import Image

def calcular_valor_futuro():
    try:
        # obtém os valores dos campos de entrada
        investimento_inicial = float(valor_investimento_inicial.get())
        aporte_mensal = float(valor_aporte_mensal.get())
        taxa_selic_anual = float(valor_taxa_selic_anual.get()) / 100

        # define o número de anos e o número de períodos de composição de juros
        anos = int(opcao_anos.get())
        periodos = 12

        # calcula a taxa mensal de juros com base na taxa anual
        taxa_juros_mensal = (1 + taxa_selic_anual)**(1/periodos) - 1

        # calcula o valor futuro do investimento após o número de anos selecionado
        valor_futuro = investimento_inicial * (1 + taxa_juros_mensal)**(anos*periodos)
        for i in range(1, anos*periodos + 1):
            valor_futuro += aporte_mensal * (1 + taxa_juros_mensal)**(anos*periodos - i)
        
        rentabilidade = valor_futuro - (investimento_inicial + aporte_mensal * (anos * periodos))
        

        # exibe o valor futuro do investimento após o número de anos selecionado
        label_resultado.configure(text=f"O valor futuro do investimento após {anos} anos é de\nR${valor_futuro:,.2f}\n\nSua rentabilidade foi R${rentabilidade:,.2f}", text_color='#43A519')
        

    except ValueError:
        label_resultado.configure(text=f"Os campos de entrada devem receber valores numéricos.", text_color='#c20b21')


# cria a janela principal

tkc.set_appearance_mode("System")
tkc.set_default_color_theme("blue")
app = tkc.CTk()
app.geometry('500x540')
app.title('Selic')

imagem = tkc.CTkImage(dark_image=Image.open('retorno.png'), size=(45, 45))
logo = tkc.CTkLabel(app, text="", height=10, image=imagem)
logo.place(x=150,y=12)

#texto intro
intro = tkc.CTkLabel(app, text="Taxa Selic", font=('Ivy', 28, 'bold'), text_color='#43A519', height=10)
intro.place(x=210,y=18)

linha = tkc.CTkLabel(app, text="", width=750, height=1, font=('Ivy', 1), fg_color=('#43A519'))
linha.place(x=0,y=70)

# cria os widgets da interface
label_investimento_inicial = tkc.CTkLabel(app, text="Investimento inicial:", font=('Ivy', 15, 'bold'), text_color='#F9BA55')
valor_investimento_inicial = tkc.CTkEntry(app, text_color='#43A519', font=('Ivy', 14, 'bold'), corner_radius= 15, border_color='#F9BA55')
valor_investimento_inicial.focus_force()
label_aporte_mensal = tkc.CTkLabel(app, text="Aporte mensal:", font=('Ivy', 15, 'bold'), text_color='#F9BA55')
valor_aporte_mensal = tkc.CTkEntry(app, text_color='#43A519', font=('Ivy', 14, 'bold'), corner_radius= 15, border_color='#F9BA55')
label_taxa_selic_anual = tkc.CTkLabel(app, text="Taxa Selic anual (%):", font=('Ivy', 15, 'bold'), text_color='#F9BA55')
valor_taxa_selic_anual = tkc.CTkEntry(app, text_color='#43A519', font=('Ivy', 14, 'bold'), corner_radius= 15, border_color='#F9BA55')
valor_taxa_selic_anual.insert(0, "13.75")
label_anos = tkc.CTkLabel(app, text="Selecione o número de anos", font=('Ivy', 15, 'bold'), text_color='#F9BA55')
opcao_anos = tkc.StringVar(value="1")
opcao_1_ano = tkc.CTkRadioButton(app, text="1 ano", variable=opcao_anos, value="1", text_color='#F9BA55', hover_color='#43A519', border_color='#F9BA55', fg_color='#43A519')
opcao_5_anos = tkc.CTkRadioButton(app, text="5 anos", variable=opcao_anos, value="5", text_color='#F9BA55', hover_color='#43A519', border_color='#F9BA55', fg_color='#43A519')
opcao_10_anos = tkc.CTkRadioButton(app, text="10 anos", variable=opcao_anos, value="10", text_color='#F9BA55', hover_color='#43A519', border_color='#F9BA55', fg_color='#43A519')
botao_calcular = tkc.CTkButton(app, text="Calcular", font=('Ivy', 15, 'bold'), command=calcular_valor_futuro, fg_color='#F9BA55', hover_color='#43A519', corner_radius= 15 )
label_resultado = tkc.CTkLabel(app, text="", font=('Ivy', 15, 'bold'), text_color='#43A519', width=460, height=90, pady=5, padx=5, fg_color=('black', '#323232'), corner_radius=8)

# posiciona os widgets na app
label_investimento_inicial.place(x=90, y=100)
valor_investimento_inicial.place(x=260, y=100)
label_aporte_mensal.place(x=90, y=150)
valor_aporte_mensal.place(x=260, y=150)
label_taxa_selic_anual.place(x=90, y=200)
valor_taxa_selic_anual.place(x=260, y=200)
label_anos.place(x=140, y=250)
opcao_1_ano.place(x=120, y=290)
opcao_5_anos.place(x=200, y=290)
opcao_10_anos.place(x=280, y=290)
botao_calcular.place(x=180, y=360)
label_resultado.place(x=20, y=420)


# inicia o loop de eventos da app
app.mainloop()

