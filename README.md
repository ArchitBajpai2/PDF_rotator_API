The api request is given in json format which has a file path, page number, and angel of rotation and it returns the edited pdf which has that specific page rotated with that particular angle.
The API and the main logic function are both in main.py.
To test the API follow theses steps in your code editor
first upload a sample pdf int the input folder or anywhere just change the path accordingly
Open a new terminal and activate the virtual environment by typing <env/Scripts/activate> in the terminal.
Open main.py, install all the rquirements using the requirements file by typing <pip install -r requirements.txt> in the terminal.
Open main.py and just run it. Copy the local host link by default it should be localhost:5000 and add a "/" to it and copy that link to the postman bar, Link should be <localhost:5000/>
Choose the method "Post", go to body, choose "raw" and pass "json" in the following format- {
    "file_path": "C:/Users/ARCHIT/Desktop/Rotate_Pdf-main/input_pdf/test.pdf",
    "page_number": "3",
    "angle_of_rotation": "90"
}
Just remember to change the file path according to your computer.