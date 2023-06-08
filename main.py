import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pygame
import tkinter as tk
from tkinter import messagebox,filedialog
import shutil
def select_photo():
    # Open file dialog to select a photo
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    # Check if a photo was selected
    if file_path:
        # Create the destination directory if it doesn't exist
        destination_dir = "destination_directory"
        os.makedirs(destination_dir, exist_ok=True)

        # Get the filename from the selected file path
        filename = os.path.basename(file_path)

        # Move the selected photo to the destination directory
        destination_path = os.path.join(destination_dir, filename)
        shutil.move(file_path, destination_path)

        # Show success message
        message = f"Selected photo '{filename}' has been moved to '{destination_dir}'"
        messagebox.showinfo("Photo Selected", message)
    else:
        # Show error message if no photo was selected
        messagebox.showerror("Error", "No photo selected")
    # Open file dialog to select a photo from the destination directory
    file_path = filedialog.askopenfilename(initialdir="destination_directory", title="Select Photo to Delete",
                                           filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    # Check if a photo was selected
    if file_path:
        # Get the filename from the selected file path
        filename = os.path.basename(file_path)

        # Delete the selected photo from the destination directory
        os.remove(file_path)

        # Show success message
        message = f"Selected photo '{filename}' has been deleted from the destination directory"
        messagebox.showinfo("Photo Deleted", message)
    else:
        # Show error message if no photo was selected
        messagebox.showerror("Error", "No photo selected")

def delete_photo():
    # Open file dialog to select a photo from the destination directory
    file_path = filedialog.askopenfilename(initialdir="destination_directory", title="Select Photo to Delete",
                                           filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    # Check if a photo was selected
    if file_path:
        # Get the filename from the selected file path
        filename = os.path.basename(file_path)

        # Delete the selected photo from the destination directory
        os.remove(file_path)

        # Show success message
        message = f"Selected photo '{filename}' has been deleted from the destination directory"
        messagebox.showinfo("Photo Deleted", message)
    else:
        # Show error message if no photo was selected
        messagebox.showerror("Error", "No photo selected")

def student_management():
    def add_student():
        select_photo()
    def remove_student():
        delete_photo()

    # Create the main window
    window = tk.Tk()
    window.title("Student Management")

    # Set the window size and position it in the center of the screen
    window_width = 300
    window_height = 150
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create the buttons
    add_button = tk.Button(window, text="Add Student", font=("Arial", 14), command=add_student)
    add_button.pack(pady=10)

    remove_button = tk.Button(window, text="Remove Student", font=("Arial", 14), command=remove_student)
    remove_button.pack(pady=10)

    # Start the main window's event loop
    window.mainloop()

def login_window():
    def validate_login():
        username = username_entry.get()
        password = password_entry.get()

        # Check if the username and password are valid
        if username == "admin" and password == "admin":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            student_management()

        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    # Create the main window
    window = tk.Tk()
    window.title("Admin Login")

    # Set the window size and position it in the center of the screen
    window_width = 400
    window_height = 150
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a frame to hold the login widgets
    login_frame = tk.Frame(window, pady=20)
    login_frame.pack()

    # Create labels and entry fields for username and password
    username_label = tk.Label(login_frame, text="Username:", font=("Arial", 14))
    username_label.grid(row=0, column=0, sticky="w")

    username_entry = tk.Entry(login_frame, font=("Arial", 14))
    username_entry.grid(row=0, column=1, padx=10)

    password_label = tk.Label(login_frame, text="Password:", font=("Arial", 14))
    password_label.grid(row=1, column=0, sticky="w")

    password_entry = tk.Entry(login_frame, show="*", font=("Arial", 14))
    password_entry.grid(row=1, column=1, padx=10)

    # Create the login button
    login_button = tk.Button(window, text="Login", font=("Arial", 14), command=validate_login)
    login_button.pack(pady=10)

    # Start the main window's event loop
    window.mainloop()

# Pygame initialization
pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Face Recognition GUI")

# Face recognition initialization
path = "destination_directory"
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def encodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def attendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

encodeListKnown = encodings(images)

# Initialize the camera
cap = cv2.VideoCapture(0)
# Button properties
button_width = 50
button_height = 25
button_x = 10
button_y = 10

# Run the GUI loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_x <= event.pos[0] <= button_x + button_width and button_y <= event.pos[1] <= button_y + button_height:
                login_window()
    # Read frame from the camera
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    # Process each face in the current frame
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (74, 65, 250), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (74, 65, 250), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
            attendance(name)

    # Convert the OpenCV image to Pygame surface
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.rot90(img)
    img = pygame.surfarray.make_surface(img)

    # Display the image on the Pygame window
    window.blit(img, (0, 0))

    # Draw the "Admin" button
    pygame.draw.rect(window, (0, 0, 255), (button_x, button_y, button_width, button_height))
    admin_font = pygame.font.Font(None, 20)
    admin_text = admin_font.render("Admin", True, (255, 255, 255))
    admin_text_rect = admin_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    window.blit(admin_text, admin_text_rect)

    pygame.display.update()

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

# Release the camera and quit Pygame
cap.release()
pygame.quit()
