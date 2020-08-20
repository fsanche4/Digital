import json

with open('fsanche4_easy2.txt', 'r', encoding='utf-8') as input_file:
    content_list = json.load(input_file)
    height = 512
    width = 512

    stackIntensities = []

    with open('fsanche4_easy2.csv', 'w') as
    for i in range(0, width * height, i + width):
            if commma_counter == 511:

                out_file.write(f"{num}, \n")
                commma_counter = 0
            else:
                out_file.write(f"{num}, ")
                commma_counter = commma_counter + 1
