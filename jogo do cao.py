import os

class dog: 
    def __init__(self, name):
        self.is_on = False
        self.name = name
        self.hunger = 0
        self.tire = 0

    def wake_up(self):
            if not self.is_on:
                self.is_on = True
                print (f"Você acordou o {self.name}! e ele está pronto para brincar")
            else: 
                print (f"Você já acordou o {self.name}")

    def play_dog (self):
        if self.is_on == True:
            option_play = int (input(f"O {self.name} quer brincar! Pressione 1"))
            if option_play == 1:
                    print (f"Você jogou a bola e o {self.name} buscou para você.") 
                    self.hunger += 1
                    self.tire += 1                  
                    if self.hunger == 6:
                        print ("FIM DE JOGO")
                        print (f"O {self.name} ficou com muita fome e morreu :(")
                    if self.hunger == 4:
                        print (f"Seu pet está começando a ficar com fome! Alimente ele para não morrer.")
                    if self.tire == 5:
                        print (f"O {self.name} cansou muito e dormiu.") 
                        self.tire = 0        
        else: 
            print (f"O {self.name} está dormindo, acorde ele para brincar!") 

    
    def food(self):
        fooding = int (input("Pressione 1 para poder dar um petisco para seu pet"))
        if fooding == 1:
            print(f"Você alimentou o {self.name}.")
            self.hunger -= 2        
def return_back_menu():
        return_menu = input("Deseja voltar ao menu? (s/n)").upper
        match return_menu:
            case "s" | "S" | "Sim" | "sIm" | "siM":
                return True
            case "n" | "N" | "Não" | "Nao" | "nao" | "nÃo" | "nÂo":
                print("Obrigado por jogar o Jogo do cão!")
                return False 
def menu():
    print ("""Bem vindo ao jogo do cão!
           1. Regras e dicas
           2. Crie seu pet
           3. Acordar seu pet
           4. Brincar com seu pet
           5. Alimentar seu pet 
           6. Sair
           """)
menu_loop = True
while menu_loop == True:
    menu()
    option = int (input("Escolha uma opção: "))
    match option:
        case 1:
            os.system('cls')
            print ("""Leia as regras com atenção!
                   1. Você precisa de dar um nome e indicar a raça do cachorro para poder jogar, use o menu de criação.
                   2. Fique atento com a fome do seu cachorro, cada vez que você brinca com ele, ele ganha fica com fome, ao chegar em certo ponto ele morre.
                   3. Você pode evitar a morte do seu cachorro alimentando ele na seçaõ de alimentação.1
                   """)
        case 2:
            os.system('cls')
            dog1 = dog (input("Digite o nome do seu cachorro:"))
        case 3: 
            os.system('cls')
            dog1.wake_up() 
        case 4:
            os.system('cls')
            dog1.play_dog()
            menu_loop = return_back_menu()
        case 5: 
            os.system('cls')
            dog1.food()
        

        


