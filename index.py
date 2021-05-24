from colorama import Fore, init; init()
import os, random, requests

class Console:
    def __init__(self):
        os.system('cls && title Vichy - K-Fucker')
        print(Fore.CYAN + '''       
        ██╗  ██╗     ███████╗██╗   ██╗ ██████╗██╗  ██╗███████╗██████╗ 
        ██║ ██╔╝     ██╔════╝██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
        █████╔╝█████╗█████╗  ██║   ██║██║     █████╔╝ █████╗  ██████╔╝
        ██╔═██╗╚════╝██╔══╝  ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
        ██║  ██╗     ██║     ╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
        ╚═╝  ╚═╝     ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                      
        '''.replace('█', f'{Fore.CYAN}█{Fore.WHITE}'))
    
    def Printer(self, color, past, text):
        print(f'{Fore.WHITE}[{color}{past}{Fore.WHITE}] {text}.')
        
class Kfucker:
    def __init__(self, Console, Pin):
        self.Console = Console
        self.PinCode = Pin
    
    def SendBot(self, Username):
        self.Console.Printer(Fore.YELLOW, '*', f'[{self.PinCode}] Checking pin code informations')
        PinInfo = requests.get(f'https://kahoot.it/rest/challenges/pin/{self.PinCode}', headers= {'content-type': 'application/json'})
        
        if 'error' in PinInfo.text:
            self.Console.Printer(Fore.RED, '#', f'[{self.PinCode}] Invalid Pin error: {PinInfo.json()["error"]}')
        else:
            Parsed = PinInfo.json()
            MaxPlayer = Parsed['challenge']['maxPlayers']
            self.Console.Printer(Fore.CYAN, '§', f"[{self.PinCode}] Found {Parsed['challenge']['title']} from {Parsed['challenge']['quizMaster']['username']}, sending {MaxPlayer} bot")

            for i in range(int(MaxPlayer) + 1):
                char = random.randint(1000, 9999)
                UUID = f'abf4a130-{char}-498b-80dd-12bd4b8fdd59'
                resp = requests.post(f"https://kahoot.it/rest/challenges/{Parsed['challenge']['challengeId']}/join/?nickname={Username}-{char}", headers= {'content-type': 'application/json'}, cookies= {'generated_uuid': UUID})

                if 'MAX_PLAYERS_REACHED' in resp.text:
                    self.Console.Printer(Fore.GREEN, '+', f'[{self.PinCode}] Max players reached')
                    break
                else:
                    self.Console.Printer(Fore.MAGENTA, '~', f'[{self.PinCode}] {Username}-{char} was sent, {i}/{MaxPlayer}')


Kfucker(Console(), input('Pin code: ')).SendBot(input('Bot name: '))