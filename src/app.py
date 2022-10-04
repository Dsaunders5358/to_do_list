from csv import reader, writer

def read_from_csv(): # Reads Current to do list from CSV
    with open("data/todolist.csv", "r") as data:
        readercur = reader(data)
        for line in readercur:
            todolist = line
        return todolist

def write_todolist_to_csv(todolist): # writes current to do list to csv
    with open("data/todolist.csv", "w" , newline = '') as data:
        writercur = writer(data)
        writercur.writerow(todolist)
            
def print_numbered_list(*menu_options): # print numbered list of args
    count = 1
    for option in menu_options:
        print(f"{str(count)}) {option}")
        count += 1

def task_options_menu_main(): # menu to interact with task list
    format_title_with_stars("Please Choose An Option")
    print_numbered_list("Add New Task", "Remove Task", "Empty List", "Exit")

def format_title_with_stars(title_message): # formats title to include stars based on length
    star_line = ""
    for c in title_message:
        star_line += "*"
    print(star_line)
    print(title_message)
    print(star_line)
        
def main_todolist_show():
    format_title_with_stars("To Do list")
    if len(todolist) <= 0:
        print("No items in list, add items to populate list")
    else:
        print_numbered_list(*todolist)
    task_options_menu_main()

def add_task_to_list(task_message):
    todolist.append(task_message)

def remove_task_from_list(index):
    todolist.pop(index - 1)
todolist = read_from_csv()
add_task_to_list("Test Message")
remove_task_from_list(5)
main_todolist_show()