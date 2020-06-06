# Suraksha
A web app for women safety and empowerment. It features women related news articles to highlight current women issues, and crimes against women, has an emergency button for connecting woman in need to their trusted ones, various maps features and awareness about women rights and laws.

Run instructions:

After clonning repository open a terminal from the repository folder,
install all the requirements from requirements.txt by running a command in terminal/cmd: 

For linux/macOS users:
1) Check for virtual env:
python3 -m pip install virtualenv
2) Create virtual env with name suraksha
python3 -m venv suraksha
3) Activate virtual env
source suraksha/bin/activate
4) Install required dependicies
pip install -r requirements.txt
5) Run the webapp server:
./run.sh 

For windows users:
1) Check for virtual env:
py -m pip install --user virtualenv
2) Create virtual env with name suraksha
py -m venv suraksha
3) Activate virtual env
.\suraksha\Scripts\activate
4) Install required dependicies
pip install -r requirements.txt
5) Change directory to website 
cd website
6) Run Project Server
python manage.py runserver