import os
import re

# Function to validate IP address
def is_valid_ip(ip):
    ip_regex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    return re.match(ip_regex, ip) is not None

# Function to validate domain name
def is_valid_domain(domain):
    domain_regex = r'^[a-zA-Z0-9][a-zA-Z0-9.-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$'
    return re.match(domain_regex, domain) is not None


colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'black': '\033[30m',
    'reset': '\033[0m'
}

def load():
    os.system("bash /helper/nmap-by-sw.sh")

def banner():
    print("Welcome to the Interactive Menu!")
    print("Choose an option:")
    print("1. Automatic Scanning")
    print("2. Learning")
    print("3. About Us")
    print("4. Update")
    print("5. Exit")

def update():
    print("\033[96mthe tool is up to date . No update needed")
    print("Thanks for using this tool\033[0m")


def automatic_scanning():
    #ip = input("Enter victim ip / domain : ")
    import os

def automatic_scanning():
    print("\033[95m\n\nWHAT DO YOU WANT TO DO\033[0m ")
    print("\n\033[93m1) Ping IP\n2) Quick/Normal scan\n3) Normal scan with version\n4) Deep scan\n5) Aggressive scan\n6) OS scan\n7) All ports scan\n8) TCP scan\n9) UDP scan\n10) Script scan\n11) SYN scan\n12) ACK scan\n13) FIN scan\n14) Window scan\n15) Multiple target scan\n99) Exit\033[0m ")

    inp = input("choose option to perform scan [1-15,99] : ")
    if inp == '1':
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f"\033[91mpinging {ip}........")
        print("\n\nPress ctrl+c to stop pinging\n")
        os.system(f"ping {ip}")
       
    elif inp == "2":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running normal scan using command :
        nmap {ip}''' )
        os.system(f"nmap {ip}")

    elif inp == "3":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Runnning normal scan with version scan using command:
        nmap -sV {ip}''')
        os.system(f"nmap -sV {ip}")

    elif inp == "4":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running deep scan using command :
        nmap -sV -p- {ip}''')
        os.system(f"nmap -sV -p- {ip}") 
    elif inp == "5":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running Agressive scan using command : 
        nmap -sA {ip}''')
        os.system(f"nmap -A {ip}")
    elif inp == "6":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Runnning OS detection scan using command :
        nmap -O {ip}''')
        os.system(f"nmap -O {ip}")
    elif inp == "7":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running all port scan using command :
        nmap -p- {ip}''')
        os.system(f"nmap -p- {ip}")
    elif inp == "8":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running TCP scan using command : 
        nmap -sT {ip}''')
        os.system(f"nmap -sT {ip} ")
    elif inp == "9":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running UDP scan using command :
        nmap -sU {ip}''')
        os.system(f"nmap -sU {ip}")
    elif inp == "10":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running Script scan using command :
        nmap -sC {ip}''')
        os.system(f"nmap -sC {ip}")
    elif inp == "11":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running SYN scan using command :
        nmap -sS {ip}''')
        os.system(f"nmap -sS {ip}")
    elif inp == "12":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running ACK scan using command :
        nmap -sA {ip}''')
        os.system(f"nmap -sA {ip}")
    elif inp == "13":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running FIN scan using command :
        nmap -sF {ip}''')
        os.system(f"nmap -sF {ip}")
    elif inp == "14":
        ip = input("Enter victim ip / domain : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        print(f'''Running Window scan using command :
        nmap -sW {ip}''')
        os.system(f"nmap -sW {ip}")
    elif inp == "15":
        
        print("input ip separated by commas")
        ip = input("Enter victim ip / domain [e.g: 192.168.1.1,192.168.1.2,.....]  : ")
        while not is_valid_ip(ip) and not is_valid_domain(ip):
            print(f"{colors['red']}Invalid input. Please enter a valid IP address or domain name.{colors['reset']}")
            ip = input(f"{colors['blue']}Enter victim IP / domain: {colors['reset']}")
        
        os.system(f"nmap {ip}")
    elif inp == "99":
        print("\033[95m\nExiting script. SEE YOU SOON.....\033[0m")
        exit()
    else:
        print("invalid option\n choose between 1-14,99")    


    #os.system("chmod +x nmap-auto.sh && ./nmap-auto.sh")

    

def learning():
    print("Learning Mode:")
    with open('learning.txt', 'r') as file:
        for line in file:
            print(line.strip())

def about_us():
   print("\033[97m\nAbout Us:\n")

   print("\033[93mTitle: The Sudo World Hacking Group: A Collective of Specialized Hackers Pushing Boundaries\n\033[0m")

   print("\033[93mIntroduction: \nThe Sudo World Hacking Group represents a dynamic collective of skilled individuals passionate about exploring the depths of cybersecurity through ethical hacking. Founded by Shoeb, with Tanmoy as the co-founder and Hitesh and Scorpion Yug as key developers, this group has emerged as a powerhouse within the hacking community. Each member brings their unique expertise to the table, forming a well-rounded team capable of tackling a diverse range of challenges.\n\033[0m")

   print("\033[96mShoeb: The Master of Web Hacking\nAs the founder of the Sudo World Hacking Group, Shoeb serves as the guiding force behind its operations. With a specialization in web hacking, Shoeb possesses an unparalleled understanding of vulnerabilities that lurk within the intricate structures of online platforms. His expertise lies in identifying and exploiting weaknesses in web applications, making him a formidable force in the realm of cybersecurity.\n")

   print("Tanmoy: The Wizard of Wi-Fi Hacking and Programming\nTanmoy, the co-founder of the group, brings a wealth of knowledge in both Wi-Fi hacking and programming to the table. His prowess extends beyond mere exploitation of wireless networks; Tanmoy is also a proficient programmer, capable of crafting intricate scripts and tools to streamline the hacking process. His expertise in programming languages complements his skills in hacking, making him a versatile asset to the team.\n")

   print("Hitesh: The Python Maestro and Android Pentesting Expert\nHitesh's mastery of Python programming and Android pentesting adds another layer of depth to the Sudo World Hacking Group. With a keen understanding of Python's capabilities, Hitesh develops sophisticated tools and scripts to automate hacking processes and enhance efficiency. His proficiency in Android pentesting further solidifies the group's capabilities, allowing them to explore vulnerabilities within the increasingly prevalent mobile ecosystem.\n")

   print("Scorpion Yug: The Crackling Genius in Web Exploitation\nScorpion Yug's expertise in web hacking and crackling techniques elevates the group's capabilities to new heights. With an innate ability to uncover vulnerabilities and exploit them to gain unauthorized access, Scorpion Yug is a force to be reckoned with in the world of cybersecurity. His contributions have been instrumental in propelling the Sudo World Hacking Group to the forefront of the hacking community.\n\033[0m")

   print("\033[95mCollaborative Synergy:\nWhile each member of the Sudo World Hacking Group brings our own specialized skills to the table, it is our collaborative synergy that truly sets them apart. By leveraging our individual strengths and expertise, they are able to tackle complex challenges with finesse and precision. Whether it's conducting penetration tests, developing custom tools, or exploring emerging security threats, the group operates as a cohesive unit, pushing the boundaries of ethical hacking.\n")

   print("Impact and Contributions:\nThe contributions of the Sudo World Hacking Group extend far beyond our individual exploits. Through our Telegram group and other channels, we actively share our knowledge and expertise with aspiring hackers, fostering a community of learning and collaboration. our open-source tools and resources, hosted on platforms like GitHub, serve as valuable assets to the broader cybersecurity community, empowering others to enhance their skills and contribute to the field.\n")

   print("Conclusion:\nThe Sudo World Hacking Group stands as a testament to the power of collaboration and expertise in the realm of cybersecurity. With Shoeb, Tanmoy, Hitesh, and Scorpion Yug at the helm, the group continues to push the boundaries of ethical hacking, uncovering vulnerabilities, developing innovative solutions, and sharing our knowledge with the world. As we forge ahead, our impact on the cybersecurity landscape is sure to be felt for years to come.\n\033[0m")

def exit_program():
    print("Exiting the Interactive Menu. Goodbye!")

def main():
    load()
    banner()
    choice = input("Enter your choice: ")

    if choice == '1':
        automatic_scanning()
    elif choice == '2':
        learning()
    elif choice == '3':
        about_us()
    elif choice == '4':
        update()    
    elif choice == '5':
        exit_program()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

