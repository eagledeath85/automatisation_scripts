output_filename = "nombres.txt"

with open(output_filename, 'w', encoding='utf-8', newline='') as output_file:
    for i in range(1, 11):
        output_file.write(f"{str(i)}\n")
