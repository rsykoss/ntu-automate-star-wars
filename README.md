# ntu-automate-star-wars
This script automates adding of courses into new NTU Stars system (so called star wars). Stars is based on first come first serve basis however more slots open up within the 3 hours as well. This script will ease your star wars. 
*Developed by Ko Seoyoon in 2020 June*

## Functionality
* **Automatically logs in and register courses**
* When STARs log you out, it will automatically quit and log in again 
* Continously clicks until registration begins
* Only works for Cores or prescribed and NOT UE at this point of time since it will not choose but just add

It will stop running only when all the courses have been registered (There are no courses saying "no more vacancies")

## Warning
Please do prepare backup in cases there are failures and use at your own risk. Please do not blame here for failure in getting courses. **Recommended to start using this like 15 minutes into STARs and there are no more vacancies at that point of time. But it can also be used from the start** This was developed in a very short time during my own STARs and it was an impulse decision to create this and it is not perfect at all.

## prerequisites
* python
* pip
* **MUST DO:** Kake sure all the cores or ger core or major pe that you need are **saved to plan 1 as default**. Try to remove UEs (Those need to choose ranks) 

## set up
1. Clone or Fork or download this github
2. Go to chrome settings and go to about chrome. Check chrome version
3. Go [here](https://chromedriver.chromium.org/downloads) and download chrome driver with correct version
4. Unzip the downloaded chromedriver and copy the directory it is saved in
5. In the `config.txt` file fill DRIVE directory, USERNAME and PASSWORD used for intu in the corresponding fields and save:
```
DRIVE = C:/Users/xxx/Downloads/chromedriver.exe
USERNAME = ET0001
PASSWORD = xxxx
```
*no quotation is required

## Run 
There are 2 ways to run. 
#### A) Use batch file
double click automateStars.bat file to run

#### B) use cmd
```
pip install -r requirements.txt
python automateStars.py
```
To run this **without opening up chrome physically** (virtually carried out), append argument `-bg` like shown below
```
python automateStars.py -bg
```
