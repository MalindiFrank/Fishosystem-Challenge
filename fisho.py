from clear import clear
import random, time

# try:
#     while True:
#         grounds = [[random.choices([" ", ">", "#"], [25, 2, 1])[0] for i in range(20)] for j in range(20)]
#         clear()
#         for row in grounds:
#             print(row)
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Thank you!")

fishosys = [[random.choices([" ", ">", "#"], [25, 2, 1])[0] for i in range(10)] for j in range(10)]

def fish_noticer(fishosys = fishosys):

    for row_index, row in enumerate(fishosys):
        for col_index, cell in enumerate(row):
            if cell == ">":
                return row_index, col_index

def shark_noticer(fishosys = fishosys):

    for row_index, row in enumerate(fishosys):
        for col_index, cell in enumerate(row):
            if cell == ">":
                return row_index, col_index
            
def space(fishosys = fishosys):

    for y, row in enumerate(fishosys):
        for x, object in enumerate(row):
            if object == " ":
                return x, y





if __name__ == "__main__":
    print(fish_noticer())