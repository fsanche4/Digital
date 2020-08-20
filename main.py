import json

with open('fsanche4_easy.txt', 'r', encoding='utf-8') as input_file:
    content_list = json.load(input_file)
    commma_counter = 0

    with open('fsanche4_easy.csv', 'w') as out_file:
        for num in content_list: 
            if commma_counter == 255:
                out_file.write(f"{num}, \n")
                commma_counter = 0
            else:t
                out_file.write(f"{num}, ")
                commma_counter = commma_counter + 1