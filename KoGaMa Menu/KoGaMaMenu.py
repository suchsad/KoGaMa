from colorama import init, Fore, Style
import os
import subprocess
import requests
import time
import shutil
import art
import subprocess
import webbrowser
import time


init(autoreset=True)

if os.path.exists('requirements.txt'):
    print(f"{Fore.LIGHTRED_EX}Installing dependencies from requirements.txt...{Style.RESET_ALL}")
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

    os.remove('requirements.txt')
    print(f"{Fore.LIGHTRED_EX}requirements.txt deleted after installation.{Style.RESET_ALL}")
print('  ')
print('  ')

username = os.getlogin()

def generate_scarecrow_ascii():
    scarecrow_ascii = art.text2art("BuGaMa", font="univers", chr_ignore=True)
    return Fore.LIGHTMAGENTA_EX + scarecrow_ascii.replace("#", Fore.BLUE + "#") + Fore.RESET




def display_menu():
    print(f"{Fore.YELLOW} Script created by{Style.RESET_ALL}{Fore.LIGHTRED_EX} Moca{Style.RESET_ALL}, {Fore.LIGHTRED_EX}Aoksu{Style.RESET_ALL} ")
    print(f"{Fore.YELLOW} KoGaMa Version: {Style.RESET_ALL}{Fore.LIGHTRED_EX}V: 2.30.59.1152 B: 2024-02-19Shaders{Style.RESET_ALL}")
    print("")
    print(Fore.YELLOW + "Launcher")
    print(Fore.LIGHTBLUE_EX + "1. Join Session")
    print(Fore.LIGHTBLUE_EX + "2. Tweak Crosshair")
    print(Fore.LIGHTBLUE_EX + "3. Clear Standalone Logs")
    print(Fore.LIGHTBLUE_EX + "4. Fix Standalone Issues")
    print(Fore.LIGHTBLUE_EX + "5. Delete KoGaMa")
    print("")
    print(Fore.YELLOW + "Misc")
    print(Fore.LIGHTBLUE_EX + "6. Socials")
    print(Fore.LIGHTBLUE_EX + "7. Quit" + Fore.RESET)
    print("")


def clear_files_in_directory(directory, extensions):
    files = [file for file in os.listdir(directory) if any(file.endswith(ext) for ext in extensions)]

    if len(files) == 0:
        print(f"No files with specified extensions found in {directory}")
        return
    
    for file in files:
        file_path = os.path.join(directory, file)
        try:
            with open(file_path, 'w') as f:
                f.truncate(0)
            print(f"Cleared content of {file} in {directory}")
        except Exception as e:
            print(f"Error clearing {file} in {directory}: {e}")

def check_folders_exist():
    return all(os.path.exists(path) for path in uninstall_path)
def download_and_replace_launcher():
    try:
        download_link = "https://github.com/Aethusx/OpenKogama_Launcher/releases/download/1.0/Launcher_Micai.exe"

        response = requests.get(download_link)
        if response.status_code == 200:
            new_launcher_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "KogamaLauncher-WWW", "Launcher", "Launcher.exe")

            # fuck off original
            if os.path.exists(new_launcher_path):
                os.remove(new_launcher_path)

            # 
            with open(new_launcher_path, "wb") as new_launcher_file:
                new_launcher_file.write(response.content)

            # make a sign that it works ffs
            with open(os.path.join(os.path.expanduser("~"), "AppData", "Local", "KogamaLauncher-WWW", "overwritten.txt"), "w") as overwritten_file:
                overwritten_file.write("File overwritten successfully.")

            print(f"{Fore.LIGHTBLUE_EX}Adjusted Launcher release")
        else:
            print(f"{Fore.RED}Error downloading KoGaMa Launcher: HTTP {response.status_code}")
    except Exception as e:
        print(f"{Fore.RED}Error downloading and replacing KoGaMa Launcher: {str(e)}") 
def install_kogama():
    try:
        response = requests.get(install_url)
        if response.status_code == 200:
            with open(installer_filename, "wb") as installer_file:
                installer_file.write(response.content)
            print(f"{Fore.GREEN}Downloaded KoGaMa Installer")

            subprocess.run([installer_filename], shell=True, check=True)
            print(f"{Fore.LIGHTYELLOW_EX}Installed KoGaMa")

            time.sleep(10)

            if not check_folders_exist():
                repair_command = ["msiexec", "/f", installer_filename]
                subprocess.run(repair_command, shell=True, check=True)
                print(f"{Fore.LIGHTCYAN_EX}Fetching repair")

                time.sleep(10)

                if not check_folders_exist():
                    print(f"{Fore.RED}Installation Try has failed.")
                else:
                    download_and_replace_launcher()
            else:
                print(f"{Fore.GREEN}Installation successful.")
                download_and_replace_launcher()

            os.remove(installer_filename)
            print(f"{Fore.GREEN}Cleaned up downloaded installer")
        else:
            print(f"{Fore.RED}Error downloading KoGaMa Installer: HTTP {response.status_code}")
    except Exception as e:
        print(f"{Fore.RED}Error installing KoGaMa: {str(e)}")

def delete_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"{Fore.GREEN}Deleted folder:{Style.RESET_ALL} {Fore.BLUE}{path}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Folder not found:{Style.RESET_ALL} {Fore.BLUE}{path}{Style.RESET_ALL}")

def delete_specific_folders():
    user_home = os.path.expanduser("~")
    appdata_local_path = os.path.join(user_home, "AppData", "Local")
    appdata_locallow_path = os.path.join(user_home, "AppData", "LocalLow")

    folders_to_delete = [
        "KogamaLauncher-WWW",
        "Multiverse ApS"
    ]

    for folder in folders_to_delete:
        folder_path = os.path.join(appdata_local_path, folder)
        delete_folder(folder_path)

    for folder in folders_to_delete:
        folder_path = os.path.join(appdata_locallow_path, folder)
        delete_folder(folder_path)

def download_and_overwrite(username, url):
    original_filename = os.path.basename(url)
    home_directory = os.path.expanduser('~')

    destination_path = os.path.join(home_directory, f"AppData\\Local\\KogamaLauncher-WWW\\Launcher\\Standalone\\kogama_Data\\{original_filename}")
    original_file_path = os.path.join(home_directory, f"AppData\\Local\\KogamaLauncher-WWW\\Launcher\\Standalone\\kogama_Data\\sharedassets1.assets")

    if os.path.exists(original_file_path):
        os.remove(original_file_path)
        print(f"{Fore.GREEN}Deleted the original sharedassets1.assets.{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Original sharedassets1.assets not found.{Style.RESET_ALL}")

    response = requests.get(url)

    if response.status_code == 200:
        with open(destination_path, 'wb') as file:
            file.write(response.content)
        
        print(f"{Fore.GREEN}Successfully downloaded and overwritten {original_filename}.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Failed to download file from {url}.{Style.RESET_ALL}")

url_to_watch = "https://kogama.com" 
browser_processes = ["Brave.exe", "chrome.exe", "firefox.exe", "edge.exe", "opera.exe"]

def join_session_submenu():
    print("")
    print(Fore.RED + "Join Session:")
    print("")
    print(Fore.LIGHTBLUE_EX + "1. > WAR 4 < ")
    print(Fore.LIGHTBLUE_EX +  "2. Ultimate Hard Parkour")
    print(Fore.LIGHTBLUE_EX +  "3. LOL Cube Gun 35!!")
    print("")

    session_id_mapping = {
        "> WAR 4 < ": "2593313",
        "Ultimate Hard Parkour": "4388322",
        "LOL Cube Gun 35!!": "10370845",
    }

    try:
        choice = int(input("Enter the number of the session: "))
        session_names = list(session_id_mapping.keys())
        selected_session_name = session_names[choice - 1]

        session_id = session_id_mapping[selected_session_name]
        session_url = f"https://www.kogama.com/games/play/{session_id}/?standalone=2"

        webbrowser.open(session_url)
        time.sleep(4) # close after this amount of time, seems pretty balanced by test given so far

        while True:
            if webbrowser.open(url_to_watch):
                for browser in browser_processes:
                 subprocess.call(["taskkill", "/IM", browser, "/F"])
                break

    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number.")

def tweak_crosshair_submenu():
    print("Choose one of the following options:")
    print(f"{Fore.LIGHTRED_EX}1. Heart")
    print(f"{Fore.LIGHTMAGENTA_EX}2. Star")
    print(f"{Fore.LIGHTYELLOW_EX}3. Dot")
    print(f"{Fore.LIGHTCYAN_EX}4. Plus Sign")
    print(f"{Fore.LIGHTWHITE_EX}5. Plus Sign V2" + Fore.RESET)
    print("")
def generate_choice_prompt(start_color, end_color):
    prompt_text = "Enter your choice: "


    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))


    gradient_prompt = f"\033[38;2;{start_rgb[0]};{start_rgb[1]};{start_rgb[2]}m" \
                      f"\033[38;2;{end_rgb[0]};{end_rgb[1]};{end_rgb[2]}m{prompt_text}\033[0m"

    return gradient_prompt

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(generate_scarecrow_ascii())

    display_menu()

    start_color = "#BF89EC"
    end_color = "#EBCBE6"
    choice_prompt = generate_choice_prompt(start_color, end_color)

    choice = input(choice_prompt)

    if choice == '1':
        join_session_submenu()

    elif choice == '2':
        tweak_crosshair_submenu()
        crosshair_choice = input("Pick your crosshair: ")
        crosshair_choices = {
        '1': ('heart', 'https://raw.githubusercontent.com/suchsad/KoGaMa/main/KoGaMa%20Menu/Crosshairs/heart/sharedassets1.assets'),
        '2': ('star', 'https://raw.githubusercontent.com/suchsad/KoGaMa/main/KoGaMa%20Menu/Crosshairs/star/sharedassets1.assets'),
        '3': ('dot', 'https://raw.githubusercontent.com/suchsad/KoGaMa/main/KoGaMa%20Menu/Crosshairs/dot/sharedassets1.assets'),
        '4': ('plus_sign', 'https://raw.githubusercontent.com/suchsad/KoGaMa/main/KoGaMa%20Menu/Crosshairs/plus_sign/sharedassets1.assets'),
         '5': ('plus_sign_v2', 'https://raw.githubusercontent.com/suchsad/KoGaMa/main/KoGaMa%20Menu/Crosshairs/plus_sign2/sharedassets1.assets')
        }
                 # I will have so much fun fixing it every update.
        crosshair_choice_info = crosshair_choices.get(crosshair_choice)

        if crosshair_choice_info is not None:
            crosshair_file_name, crosshair_file_url = crosshair_choice_info

            crosshair_color = {
                'heart': Fore.LIGHTRED_EX,
                'star': Fore.LIGHTMAGENTA_EX,
                'dot': Fore.LIGHTYELLOW_EX,
                'plus_sign': Fore.LIGHTCYAN_EX,
                'plus_sign_v2': Fore.LIGHTWHITE_EX
            }

            print(f"{crosshair_color[crosshair_file_name]}You chose {crosshair_file_name}.{Style.RESET_ALL}")
            download_and_overwrite(crosshair_file_name, crosshair_file_url)
        else:
            print(f"{Fore.RED}Invalid choice. Please choose a number from 1 to 5.{Style.RESET_ALL}")

    elif choice == '3':
        print(Fore.LIGHTGREEN_EX + "Clearing Standalone Logs...")
        directories = [
            f'C:\\Users\\{username}\\AppData\\LocalLow\\Multiverse ApS\\KoGaMa',
            f'C:\\Users\\{username}\\AppData\\Local\\KogamaLauncher-WWW\\log',
            f'C:\\Users\\{username}\\AppData\\Local\\KogamaLauncher-WWW\\Launcher\\log'
        ]
        file_extensions = ['.txt', '.log']

        for directory in directories:
            if os.path.exists(directory):
                clear_files_in_directory(directory, file_extensions)
            else:
                print(f"Directory not found: {directory}")

        print(Fore.LIGHTGREEN_EX + "Standalone Logs cleared.")
    elif choice == '4':
        print(Fore.YELLOW + "Fixing Standalone Issues...")
        user_home = os.path.expanduser("~")
        uninstall_path = [
        os.path.join(user_home, "AppData", "Local", "KogamaLauncher-WWW"),
        os.path.join(user_home, "AppData", "LocalLow", "Multiverse ApS")
    ]
        install_url = "https://www-gamelauncher.kogstatic.com/www/KogamaLauncher.msi?_t=1437643420"
        installer_filename = "KogamaLauncher.msi"
        check_folders_exist()
        install_kogama()
        print(Fore.YELLOW + "Standalone Issues fixed.")

    elif choice == '5':
        print(Fore.RED + "Deleting KoGaMa...")
        user_home = os.path.expanduser("~")
        appdata_local_path = os.path.join(user_home, "AppData", "Local")
        appdata_locallow_path = os.path.join(user_home, "AppData", "LocalLow")

        folders_to_delete = [
            "KogamaLauncher-WWW",
            "Multiverse ApS"
        ]

        for folder in folders_to_delete:
            folder_path = os.path.join(appdata_local_path, folder)
            delete_folder(folder_path)

        for folder in folders_to_delete:
            folder_path = os.path.join(appdata_locallow_path, folder)
            delete_folder(folder_path)

        print(Fore.RED + "KoGaMa deleted.")

    elif choice == '6':
        print("")
        print(Fore.MAGENTA + "Main Developer")
        print("")
        print(Fore.YELLOW + "Discord Server: https://discord.gg/SkyqDFezZn")
        print(Fore.YELLOW + "Discord: @mocababe")
        print(Fore.YELLOW + "KoGaMa WWW: PID/17769289")
        print(Fore.YELLOW + "Youtube: @yovrgoth")
        print(Fore.YELLOW + "Github: @suchsad")
        print("")
        print(Fore.MAGENTA + "Affiliated Support")
        print("")
        print(Fore.YELLOW + "AOKSU") # < = = I don't care you are being added anyways 



    elif choice == '7':
        print(Fore.RESET + "Exiting program. Adios!")
        break
    else:
        print(Fore.RED + "Invalid choice. Please enter a valid option (1-5).")

    input("\nPress Enter to continue...")
