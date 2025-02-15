import os

# Читаем IP-адреса из файла ips.txt
with open("ips.txt", "r") as infile:
    ip_addresses = [line.strip() for line in infile if line.strip()]

# Записываем результат в файл output.txt
with open("output.txt", "w") as outfile:
    # Записываем строки-заголовки
    outfile.write("[Bookmarks]\n")
    outfile.write("SubRep=New1\n")
    outfile.write("ImgNum=41\n")
    
    # Формируем и записываем строки с IP-адресами в нужном формате
    for ip in ip_addresses:
        formatted_line = (
            f"{ip} (root)=#109#0%{ip}%22%root%%-1%-1%%%%%0%0%0%%%-1%"
            f"0%0%0%%1080%%0%0%1%%0%%%%0%-1%-1%0#MobaFont%10%0%0%-1%"
            f"15%236,236,236%30,30,30%180,180,192%0%-1%0%%xterm%-1%"
            f"0%_Std_Colors_0_%80%24%0%1%-1%<none>%%0%0%-1%0%#0# #-1\n"
        )
        outfile.write(formatted_line)

# Переименовываем файл output.txt в "MobaXterm Sessions.mxtsessions"
os.rename("output.txt", "MobaXterm Sessions.mxtsessions")
print("Файл успешно создан и переименован в 'MobaXterm Sessions.mxtsessions'.")
