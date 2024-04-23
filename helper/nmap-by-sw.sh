#!bin/bash
clear

# Function to print text in different colors
print() {
    # Reset text color at the end
    local RESET='\e[0m'

    case $2 in
        red)    local COLOR='\e[1;31m';;
        green)  local COLOR='\e[1;32m';;
        blue)   local COLOR='\e[1;34m';;
        yellow) local COLOR='\e[1;33m';;
        cyan)   local COLOR='\e[1;36m';;
        purple) local COLOR='\e[1;35m';;
        *)      local COLOR='\e[0m';;
    esac

    echo -e "${COLOR}$1${RESET}"
}

# Display the tool name and author in a way that catches the eye
print "888b    888 888b     d888        d8888 8888888b•" | lolcat
print "8888b   888 8888b   d8888       d88888 888   Y88b" | lolcat
print "88888b  888 88888b.d88888      d88P888 888    888" | lolcat
print "888Y88b 888 888Y88888P888     d88P 888 888   d88P" | lolcat
print "888 Y88b888 888 Y888P 888    d88P  888 8888888P•" | lolcat
print "888  Y88888 888  Y8P  888   d88P   888 888" | lolcat
print "888   Y8888 888   •   888  d8888888888 888" | lolcat
print "888    Y888 888       888 d88P     888 888" | lolcat
print "-----------------------v=1.0----------------------" "red"

echo -e -n "\e[1;32m••••••••••••••~~  B"
sleep 0.1
echo -n "y"
sleep 0.1
echo -n " "
sleep 0.1
echo -n "S"
sleep 0.1
echo -n "U"
sleep 0.1
echo -n "D"
sleep 0.1
echo -n "O"
sleep 0.1
echo -n " "
sleep 0.1
echo -n "W"
sleep 0.1
echo -n "O"
sleep 0.1
echo -n "R"
sleep 0.1
echo -n "L"
sleep 0.1
echo -e -n "D ~~•••••••••••••••\e[0m\n"
print "-------------------------------------------------" "red"
sleep 1
echo
echo

