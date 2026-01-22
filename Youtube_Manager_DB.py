import sqlite3

con = sqlite3.connect('youtube_database.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_all_videos():
    cursor.execute("SELECT * from videos")
    rows = cursor.fetchall()

    if not rows:
        print("\nNo videos found!")
    else:
        print(f"\n{'ID':<5} {'Name':<40} {'Time':<10}")
        print("-" * 55)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<40} {row[2]:<10}")

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name,time) VALUES (?,?)", (name, time))
    print("Video added successfully!")
    con.commit()

def update_video(vid_id, new_name, new_time):
    try:
        cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, int(vid_id)))
        con.commit()
        print("Video updated successfully!")
    except ValueError:
        print("Invalid video ID. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_video(vid_id):
    try:
        cursor.execute("DELETE FROM videos WHERE id = ?", (int(vid_id),))
        con.commit()
        print("Video deleted successfully!")
    except ValueError:
        print("Invalid video ID. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    
    while True:
        print("\n Youtube Manager(Database) | Choose an option:")
        print("1. List all videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        print("\n")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        
        elif choice == '2':
            print("\n")
            name = input("Enter video name : ")
            time = input("Enter video time : ")
            add_video(name,time)
        
        elif choice == '3':
            vid_id = input("Enter video ID to update : ")
            name = input("Enter video new name : ")
            time = input("Enter video new time : ")
            update_video(vid_id,name,time)
        
        elif choice == '4':
            vid_id = input("Enter video ID to Delete : ")
            delete_video(vid_id,)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid Choice")

    con.close()

if __name__ == "__main__":
    main()