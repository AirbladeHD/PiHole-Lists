import wget
import sys
import os

def format_domain(url):
    list_name = url[url.rfind("/") + 1:]

    print("\n===================================================================================================")
    print("Downloade Liste {}...\n".format(list_name))
    wget.download(url)
    print("\nDownload abgeschlossen!")

    print("\nFormatiere Liste...")
    f = open(list_name, "r")
    o = open(list_name + ".new", "w")

    for l in f.readlines():
        new_line = l.replace("||", "").replace("^", "").replace("\n", "")
        o.write(new_line + "\n")

    os.remove(list_name)
    os.rename(list_name + ".new", list_name)
    sources.write("https://raw.githubusercontent.com/AirbladeHD/PiHole-Lists/master/{}\n".format(list_name))

    print("\nFormatieren von {} abgeschlossen!".format(list_name))
    print("===================================================================================================\n")

domains = open(sys.argv[1], "r")
sources = open("sources", "w")

for domain in domains.readlines():
    format_domain(domain.replace("\n", ""))