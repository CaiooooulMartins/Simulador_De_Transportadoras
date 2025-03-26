import customtkinter as ctk
from tkinter import messagebox

# Configuração do tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class Transportadora:
    def __init__(self, nome, veiculo, frete_total, detalhes):
        self.nome = nome
        self.veiculo = veiculo
        self.frete_total = frete_total
        self.detalhes = detalhes

def calculo_Transportadora_n1(valorNF, pallets):
    try:
        if pallets in range(1, 10):
            fretepeso = 4694.99
            veiculo = "Toco"
        elif pallets in range(10, 16):
            fretepeso = 4945.24
            veiculo = "Truck"
        elif pallets in range(17, 28):
            fretepeso = 6375.18
            veiculo = "Carreta"
        else:
            return None
            
        # Aplicar escolta apenas se NF > 3.5 milhões
        escolta = 2900 if valorNF > 3500000 else 0
        advfixa = 0.0007 * 100
        adv = 0.0007 * valorNF
        icms = 0.12
        
        fretePuro = fretepeso + adv
        frete_com_impostos = fretePuro + (fretePuro * icms) / 0.88
        frete_total = frete_com_impostos + escolta
        
        detalhes = (
            f"• Veículo: {veiculo}\n"
            f"• Frete peso: R${fretepeso:,.2f}\n"
            f"• Advalorem: {advfixa:.4f}% (R${adv:,.2f})\n"
            f"• ICMS: {icms*100:.0f}%\n"
            f"• Escolta: {'R$2.900,00 (obrigatório)' if valorNF > 3500000 else 'Não necessário'}\n"
            f"• Total: R${frete_total:,.2f}"
        )
        
        return Transportadora("Transportadora N1", veiculo, frete_total, detalhes)
    
    except Exception as e:
        print(f"Erro no cálculo da Transportadora N1: {e}")
        return None

def calculo_Transportadora_n2(valorNF, pallets):
    try:
        if pallets in range(1, 10):
            fretepeso = 4350
            veiculo = "Toco"
        elif pallets in range(10, 16):
            fretepeso = 4350
            veiculo = "Truck"
        else:
            return None
            
        # Aplicar escolta apenas se NF > 3.5 milhões
        escolta = 2900 if valorNF > 3500000 else 0
        advfixo = 0.001 * 100
        adv = valorNF * 0.001
        icms = 0.12
        
        fretePuro = fretepeso + adv
        frete_com_impostos = fretePuro + (fretePuro / (1 - icms) * icms)
        frete_total = frete_com_impostos + escolta
        
        detalhes = (
            f"• Veículo: {veiculo}\n"
            f"• Frete peso: R${fretepeso:,.2f}\n"
            f"• Advalorem: {advfixo:.4f}% (R${adv:,.2f})\n"
            f"• ICMS: {icms*100:.0f}%\n"
            f"• Escolta: {'R$2.900,00 (obrigatório)' if valorNF > 3500000 else 'Não necessário'}\n"
            f"• Total: R${frete_total:,.2f}"
        )
        
        return Transportadora("Transportadora N2", veiculo, frete_total, detalhes)
    
    except Exception as e:
        print(f"Erro no cálculo da Transportadora N2: {e}")
        return None

def calcular():
    try:
        # Obter e validar valores de entrada
        valor_texto = entry_valorNF.get().replace(".", "").replace(",", ".")
        if not valor_texto.replace(".", "").isdigit():
            raise ValueError("Valor da NF inválido")
            
        valorNF = float(valor_texto)
        pallets = int(entry_pallets.get())
        
        if valorNF <= 0 or pallets <= 0:
            raise ValueError("Valores devem ser positivos")
        
        # Calcula os fretes
        transp_n1 = calculo_Transportadora_n1(valorNF, pallets)
        transp_n2 = calculo_Transportadora_n2(valorNF, pallets)
        
        # Filtra resultados válidos
        resultados = [t for t in [transp_n1, transp_n2] if t is not None]
        
        if not resultados:
            messagebox.showerror("Erro", "Nenhuma transportadora suporta essa quantidade de pallets.")
            return
        
        # Determina a melhor opção
        melhor_opcao = min(resultados, key=lambda x: x.frete_total)
        
        # Cria janela de resultados
        result_window = ctk.CTkToplevel(root)
        result_window.title("Resultados da Simulação")
        result_window.geometry("900x650")
        
        # Frame principal
        main_frame = ctk.CTkFrame(result_window)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Título com valor da NF e pallets
        info_text = f"Simulação para NF de R${valorNF:,.2f} e {pallets} pallets"
        ctk.CTkLabel(main_frame, text=info_text, 
                     font=("Arial", 14)).pack(pady=(5,10))
        
        # Adiciona alerta se necessário escolta
        if valorNF > 3500000:
            ctk.CTkLabel(main_frame, 
                        text="ATENÇÃO: NF acima de R$3.5M - Escolta obrigatória!",
                        text_color="#f8d030",
                        font=("Arial", 12, "bold")).pack(pady=5)
        
        # Frame para os resultados
        results_frame = ctk.CTkFrame(main_frame)
        results_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Exibe cada resultado
        for i, transp in enumerate(resultados):
            frame_transp = ctk.CTkFrame(results_frame, border_width=2,
                                      border_color="#1f6aa5" if transp == melhor_opcao else "gray")
            frame_transp.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
            
            results_frame.grid_columnconfigure(i, weight=1)
            
            # Título com destaque para a melhor opção
            title_color = "#2fa572" if transp == melhor_opcao else "white"
            ctk.CTkLabel(frame_transp, text=transp.nome, 
                        font=("Arial", 14, "bold"), 
                        text_color=title_color).pack(pady=(10,5))
            
            # Detalhes
            textbox = ctk.CTkTextbox(frame_transp, width=300, height=220,
                                   wrap="word", font=("Arial", 12))
            textbox.pack(padx=10, pady=5, fill="both", expand=True)
            textbox.insert("1.0", transp.detalhes)
            textbox.configure(state="disabled")
        
        # Melhor opção
        ctk.CTkLabel(main_frame, 
                    text=f"★ MELHOR OPÇÃO: {melhor_opcao.nome} - R${melhor_opcao.frete_total:,.2f} ★",
                    font=("Arial", 14, "bold"), 
                    text_color="#2fa572").pack(pady=10)
        
        # Botão de fechar
        ctk.CTkButton(main_frame, text="Fechar", 
                      command=result_window.destroy).pack(pady=10)
        
    except ValueError as ve:
        messagebox.showerror("Erro de Validação", f"Dados inválidos:\n{str(ve)}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado:\n{str(e)}")

# Interface principal
root = ctk.CTk()
root.title("Simulador de Transportadoras")
root.geometry("500x350")

# Frame principal
main_frame = ctk.CTkFrame(root)
main_frame.pack(pady=30, padx=30, fill="both", expand=True)

# Título
ctk.CTkLabel(main_frame, text="Simulador de Frete", 
             font=("Arial", 18, "bold")).pack(pady=(10,20))

# Campos de entrada
input_frame = ctk.CTkFrame(main_frame)
input_frame.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(input_frame, text="Valor da NF (R$):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_valorNF = ctk.CTkEntry(input_frame, placeholder_text="Ex: 1000000 ou 3.500.000")
entry_valorNF.grid(row=0, column=1, padx=5, pady=5)

ctk.CTkLabel(input_frame, text="Quantidade de Pallets:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_pallets = ctk.CTkEntry(input_frame, placeholder_text="Ex: 12")
entry_pallets.grid(row=1, column=1, padx=5, pady=5)

# Botão de cálculo
btn_frame = ctk.CTkFrame(main_frame)
btn_frame.pack(pady=20)

ctk.CTkButton(btn_frame, text="Calcular Frete", 
              command=calcular, width=200, height=40,
              font=("Arial", 14)).pack()

root.mainloop()