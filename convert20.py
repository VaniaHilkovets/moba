import os

CHUNK_SIZE = 20  # количество IP-адресов в каждом файле

# Читаем IP-адреса из файла ips.txt
with open("ips.txt", "r", encoding="utf-8") as infile:
    ip_addresses = [line.strip() for line in infile if line.strip()]

# Делим IP-адреса на группы по 20 в каждой
for i in range(0, len(ip_addresses), CHUNK_SIZE):
    chunk = ip_addresses[i : i + CHUNK_SIZE]  # текущая "порция" IP
    chunk_number = (i // CHUNK_SIZE) + 1      # номер текущей группы (1, 2, 3, ...)

    # Формируем имя выходного файла для данной группы
    output_filename = f"MobaXterm Sessions Part{chunk_number}.mxtsessions"

    # Открываем файл для записи
    with open(output_filename, "w", encoding="utf-8") as outfile:
        # Записываем строки-заголовки
        outfile.write("[Bookmarks]\n")
        outfile.write(f"SubRep=New{chunk_number}\n")  # уникальное название папки
        outfile.write("ImgNum=41\n")
        
        # Формируем и записываем строки с IP-адресами в нужном формате
        for ip in chunk:
            formatted_line = (
                f"{ip} (root)=#109#0%{ip}%22%root%%-1%-1%%%%%0%0%0%%%-1%"
                f"0%0%0%%1080%%0%0%1%%0%%%%0%-1%-1%0#MobaFont%10%0%0%-1%"
                f"15%236,236,236%30,30,30%180,180,192%0%-1%0%%xterm%-1%"
                f"0%_Std_Colors_0_%80%24%0%1%-1%<none>%%0%0%-1%0%#0# #-1\n"
            )
            outfile.write(formatted_line)

    print(f"Файл '{output_filename}' успешно создан.")
