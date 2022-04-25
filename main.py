from pygame import mixer
import time


print("Healthy programmer service started.")
print()


mixer.init()

# The time is in second

total_working_time = 28800
start_time = time.time()


def get_current_time_str():
    sec = time.time()
    return time.ctime(sec)


def get_current_time():
    return time.time()


# append the data
def append_data(work_type):
    with open("data.txt", "a") as f:
        data = get_current_time_str() + " " + work_type
        f.write(data)
        f.write("\n")

    print("Data logged successfully!!")


# log the data
def log_data():
    with open("data.txt") as f:
        print(f.read())


log_data()


# Notify user

def eyes_exercise():
    print("Move your eyes!!!")
    mixer.music.load("eyes_mp3.mp3")
    mixer.music.play(-1)

    timeout_start = get_current_time()

    while (get_current_time() - timeout_start) <= 10:
        print("1:- To stop eyes music")
        inp = int(input())

        if inp == 1:
            break

    mixer.music.stop()

    append_data("Eye exercise")


def do_exercise():
    print("Move your legs and hands!!!")
    mixer.music.stop()
    mixer.music.load("exercise_mp3.mp3")
    mixer.music.play(-1)

    timeout_start = get_current_time()


    while (get_current_time() - timeout_start) <= 10:
        print("1:- To stop exercise music")
        inp = int(input())

        if inp == 1:
            break

    mixer.music.stop()

    append_data("Physical exercise")


def drink_water():
    print("Get up and drink water!!!")
    mixer.music.load("water_mp3.mp3")
    mixer.music.play(-1)

    timeout_start = get_current_time()

    while (get_current_time() - timeout_start) <= 10:
        print("1:- To stop drink water music")
        inp = int(input())
        if inp == 1:
            break

    mixer.music.stop()

    append_data("Water drunk")


eyes_exercise_start_time = get_current_time()
physical_exercise_start_time = get_current_time()
drink_water_start_time = get_current_time()


# Number of glasses drunk
glass_drank = 1

drinking_water_interval = 28800 / 18
# drinking_water_interval = 5


while (get_current_time() - start_time) <= total_working_time:
    if (get_current_time() - eyes_exercise_start_time) >= 1800:
        eyes_exercise_start_time = get_current_time()
        eyes_exercise()

    if (get_current_time() - physical_exercise_start_time) >= 2700:
        physical_exercise_start_time = get_current_time()
        do_exercise()

    if glass_drank <= 18 and (get_current_time() - drink_water_start_time) >= drinking_water_interval:
        glass_drank += 1
        drink_water_start_time = get_current_time()
        drink_water()



