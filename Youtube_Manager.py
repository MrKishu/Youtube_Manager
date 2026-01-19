import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)


def list_all_videos(videos):
    if not videos:
        print("No videos found.")
        return

    print("\nYour Videos:")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['Name']} ({video['Length']})")


def search_video(videos, vid_name):
    name = vid_name.lower()
    return [v for v in videos if name in v["Name"].lower()]


def add_video(videos):
    vid_name = input("Enter video name: ").strip()
    vid_len = input("Enter video length: ").strip()

    if not vid_name or not vid_len:
        print("Video name and length cannot be empty.")
        return

    videos.append({
        'Name': vid_name,
        'Length': vid_len
    })

    save_data_helper(videos)
    print("Video added successfully.")


def update_video(videos):
    if not videos:
        print("No videos to update.")
        return

    list_all_videos(videos)

    try:
        index = int(input("\n\nEnter video number to update: "))
        if index < 1 or index > len(videos):
            print("Invalid video number.")
            return

        new_name = input("Enter new video name: ").strip()
        new_length = input("Enter new video length: ").strip()

        if not new_name or not new_length:
            print("Fields cannot be empty.")
            return

        videos[index - 1]['Name'] = new_name
        videos[index - 1]['Length'] = new_length

        save_data_helper(videos)
        print("Video updated successfully.")

    except ValueError:
        print("Please enter a valid number.")


def delete_video(videos):
    if not videos:
        print("No videos to delete.")
        return

    list_all_videos(videos)

    try:
        index = int(input("Enter video number to delete: "))
        if index < 1 or index > len(videos):
            print("Invalid video number.")
            return

        confirm = input("Are you sure you want to delete this video? (y/n): ").lower()
        if confirm != 'y':
            print("Delete cancelled.")
            return

        deleted = videos.pop(index - 1)
        save_data_helper(videos)
        print(f"Deleted video: {deleted['Name']}")

    except ValueError:
        print("Please enter a valid number.")


def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an option:")
        print("1. List all videos")
        print("2. Add a youtube video")
        print("3. Search youtube video")
        print("4. Update a youtube video")
        print("5. Delete a youtube video")
        print("6. Exit the app")
        print("\n")
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                list_all_videos(videos)

            case '2':
                add_video(videos)

            case '3':
                search_name = input("Enter video name to search: ").strip()
                if not search_name:
                    print("Search term cannot be empty.")
                    continue

                results = search_video(videos, search_name)
                if not results:
                    print("No matching videos found.")
                else:
                    print("\nSearch Results:")
                    for index, video in enumerate(results, start=1):
                        print(f"{index}. {video['Name']} ({video['Length']})")

            case '4':
                update_video(videos)

            case '5':
                delete_video(videos)

            case '6':
                print("Exiting app.")
                break

            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
