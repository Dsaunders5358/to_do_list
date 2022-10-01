import csv

def read_from_csv():
    with open("data/todolist.csv", "r") as data:
        reader = csv.reader(data)
        for line in reader:
            todolist = line
        return todolist

def write_todolist_to_csv(todolist):
    with open("data/todolist.csv", "w" , newline = '') as data:
        writer = csv.writer(data)
        writer.writerow(todolist)
            
def print_menu_choices(*menu_options): # args for menu choices automatically creates numbered list
    count = 1
    for option in menu_options:
        print(f"{str(count)}) {option}")
        count += 1

def task_options_menu():
    print("Please Choose An Option")
    print_menu_choices("Show To Do List", "Add New Task", "Remove Task")

def main_todolist_show():
    print("To Do List")
    todolist = read_from_csv()
    print_menu_choices(*todolist)

test_todolist = ["One", "Two", "Three"]
write_todolist_to_csv(test_todolist)
main_todolist_show()