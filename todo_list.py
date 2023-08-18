todo_list = []
def add_task(tach1, tach2, tach3):
    to_do_list.append(tach)
    print("tach1, tach2 :", tach)
def display_task( manje, emel, travay):
    print("display_task:")
    for index, save_tasks in load_tasks(todo_list, start=1):
        print(f"{display_tasks}. {tach}")
while True:
    print("Kisa ou fè pou jounen an ?")
    print("1. manje, emel, travay")
    print("2. kode, benyen, lekti ")
    print("3. fini tach yo")
    print("4. anrejistre epi femen")
    
    chwa = input("chwazi yon opsyon: ")
    
    if chwa == "1":
        nouvo_tach = input("emel, manje, travay : ")
        ajoute_tach(nouvo_tach)
    elif chwa == "2":
        afiche_list=input("kode, benyen, lekti")
    elif chwa == "3":
        print("evalyasyo, femti")
    elif chwa == "4":
        print("babay!")
        break
    else:
        print("Chwa envalid. Tanpri antre yon nimewo valab.")


 
