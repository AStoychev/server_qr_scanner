## Simple server for QR code scanner

Server create admins and users. Users have counter for visited places and list containing all visited places. When user scan QR code couter of visited places is equal to 0 and list with all visited places is empty list = []


## How to run

1. Clone the repo `https://github.com/AStoychev/server_qr_scanner.git`

2. Install the packages with command: `pip install -r requirements.txt`

3. Good practice is: 
    * To create a Virtual Environment with command: `python -m venv myenv`
    * Activate Virtual Environment with command:
        - For Windows: `myenv\Scripts\activate`
        - For macOS/Linux: `source myenv/bin/activate`

4. Create: 
    * **.env** file in root directory of the project;
    * Add in **.env** file:
        - **PORT**=**YOUR PORT**
        - **MONGODB_URI**=**YOUR MONDODB URI**
        - **DATABASE_NAME**=**YOUR DATABASE NAME**
        - **SECRET_KEY**=**YOUR SECRET KEY**
        
5. Go to **app** foldet and start command: `uvicorn main:app --reload`