# To-Do List Sederhana

tasks = []

def show_menu():
    print("\n== TO-DO LIST ==")
    print("1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

def list_tasks():
    if not tasks:
        print("Belum ada tugas.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Masukkan tugas: ")
    tasks.append(task)
    print("Tugas berhasil ditambahkan!")

def delete_task():
    list_tasks()
    try:
        task_num = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Tugas '{removed}' dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

while True:
    show_menu()
    choice = input("Pilih menu (1-4): ")
    if choice == '1':
        list_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Terima kasih, sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid.")
