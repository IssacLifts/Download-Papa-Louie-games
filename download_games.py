from os import cpu_count, system
import concurrent.futures
import numpy as np
from requests import get, ConnectionError
from colorama import Fore, init
from sys import exit
from time import sleep


system('cls')
print(f"{Fore.LIGHTYELLOW_EX}{cpu_count() * 2} files can be downloaded at a time - Due to you having {cpu_count()} cpu cores...\nCores: {cpu_count()}\nThreads: {cpu_count() *2}\n")
sleep(5)

game_urls = np.array(["http://i.flipline.com/downloads/papasscooperia_102.zip",
                      "http://i.flipline.com/downloads/papassushiria_101.zip",
                      "http://i.flipline.com/downloads/papasbakeria_101.zip",
                      "http://i.flipline.com/downloads/papascheeseria_102.zip",
                      "http://i.flipline.com/downloads/papasdonuteria_102.zip",
                      "http://i.flipline.com/downloads/papaspastaria.zip",
                      "http://i.flipline.com/downloads/papascupcakeria.zip",
                      "http://i.flipline.com/downloads/papashotdoggeria.zip",
                      "http://i.flipline.com/downloads/papaswingeria.zip",
                      "http://i.flipline.com/downloads/papaspancakeria.zip",
                      "http://i.flipline.com/downloads/papasfreezeria.zip",
                      "http://i.flipline.com/downloads/papastacomia.zip",
                      "http://i.flipline.com/downloads/papasburgeria.zip",
                      "http://i.flipline.com/downloads/papaspizzeria.zip",
                      "http://i.flipline.com/downloads/papalouie3_110.zip",
                      "http://i.flipline.com/downloads/papalouie2_210.zip",
                      "http://i.flipline.com/downloads/papalouie.zip"])

def download_games(url:str) -> bool:
    game_name = url.split("/")[-1]
    game_name = game_name.replace(".zip", "")
    print(f"{Fore.LIGHTMAGENTA_EX}Downloading {game_name}...\n")
    try:
        download = get(url)
    except ConnectionError:
        print(f"{Fore.LIGHTRED_EX}You are not connected to the internet...\n{Fore.LIGHTRED_EX}Exiting...")
        exit()
    try:  
        with open(f"{game_name}.zip", "wb") as file:
            if download.status_code == 200:
                file.write(download.content)
            else:
                print(f"{Fore.LIGHTRED_EX}Status Code: {download.status_code}\n{game_name}Failed to download...")
                return False
    except FileExistsError:
        pass
    print(f"{Fore.LIGHTGREEN_EX}{download.status_code}! {Fore.RED}{game_name}{Fore.LIGHTGREEN_EX} has been downloaded!")


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_games, game_urls)
    
print(f"{Fore.LIGHTGREEN_EX}All files have been downloaded!")