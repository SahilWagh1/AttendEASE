# AttendEASE - Face Detection Attendance System with Admin Panel
![AttendEASE Logo](https://github.com/SahilWagh1/DeskMateAi/blob/24899f77e084a81b33ed7d8055c74c77834e9872/deskmateai-low-resolution-logo-transparent%20(1).png)
AttendEASE is an AI-based attendance system that leverages face detection and recognition techniques to seamlessly track attendance. This project is built using Python and features an admin panel with login functionality. Administrators can easily manage and maintain the system by adding or deleting photos of employees or students.

## Dependencies
To run this project, you need to have the following dependencies installed:

* OpenCV **(cv2)**
* NumPy **(numpy)**
* face_recognition
* pygame
* tkinter

You can install these dependencies using pip by running the following command:

```bash
pip install opencv-python numpy face_recognition pygame tkinter
```

## Getting Started

1. Clone the repository to your local machine or download the source code as a ZIP file.
2. Make sure you have the necessary dependencies installed.
3. Open the project in your preferred Python IDE or text editor.

## Usage

1. Run the **'main.py'** file to start the AttendEASE attendance system.
2. The system will utilize your webcam to detect and recognize faces in real-time.
3. When a recognized face is detected, the system will mark the attendance with the current date and time.
4. Attendance details will be stored in a CSV file named **'attendance.csv'**.
5. To access the admin panel, click on the "Admin" button.
6. You will be prompted to enter your login credentials.
7. Once logged in, you can add or delete photos of employees or students.
8. To add a photo, click on the "Add Photo" button and select the image file.
9. To delete a photo, select the photo from the list and click on the "Delete Photo" button.
10. The system will update the face recognition model and remove the corresponding data from the attendance records.

## Contributors

* [Sahil Wagh](https://github.com/SahilWagh1)

## License
This project is licensed under the MIT License.
