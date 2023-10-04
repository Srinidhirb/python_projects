
import pygame
import os
import random  # Import the random module

repeat_mode = False  # Set to True for repeat mode
shuffle_mode = False 
# Initialize pygame
pygame.init()

# Define the path to your music directory
music_directory = "D:\musics"

# Get a list of all music files in the directory
music_files = [f for f in os.listdir(music_directory) if f.endswith(".mp3")]

# Initialize the pygame mixer
pygame.mixer.init()

# Function to play a selected song
def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    print("playing ",song_path,"enjoy....")

# Function to pause the currently playing song
def pause_song():
    pygame.mixer.music.pause()

# Function to unpause the paused song
def unpause_song():
    pygame.mixer.music.unpause()

# Function to stop the currently playing song
def stop_song():
    pygame.mixer.music.stop()

# Function to list available songs
def list_songs():
    for i, song in enumerate(music_files):
        print(f"{i + 1}. {song}")

# Function to play a random song
def toggle_repeat_mode():
    global repeat_mode
    repeat_mode = not repeat_mode
def toggle_shuffle_mode():
    global shuffle_mode
    shuffle_mode = not shuffle_mode
# Main loop
while True:
    print("\nPython Music Player Menu:")
    print("1. Play Song")
    print("2. Pause Song")
    print("3. Unpause Song")
    print("4. Stop Song")
    print("5. List Songs")
    print("6. Play Random Song")  # Added option for playing a random song
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        list_songs()
        song_number = int(input("Enter the song number to play: ")) - 1
        if 0 <= song_number < len(music_files):
            selected_song = os.path.join(music_directory, music_files[song_number])
            play_song(selected_song)
        else:
            print("Invalid song number!")

    elif choice == "2":
        pause_song()

    elif choice == "3":
        unpause_song()

    elif choice == "4":
        stop_song()

    elif choice == "5":
        list_songs()

    elif choice == "6":
        play_random_song()

    elif choice == "7":
        pygame.quit()
        break
    else:
        print("Invalid choice. Please try again.")
