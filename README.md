# "intelligence-task-manager".

## רקע

יחידת מודיעין בשם ShadowNet זקוקה למערכת לניהול סוכנים ומשימות. המשימה שלך היום: לבנות את שכבת
הנתונים המלאה — חיבור ל-MySQL, יצירת טבלאות, ומחלקות OOP לניהול הנתונים


## מבנה תיקיות

```
intelligence-task-manager/
├── database/
│ ├── db_connection.py
│ ├── agent_db.py
│ └── mission_db.py
├── README.md
├── requirements.txt
└── .gitignore
```

## טבלת agents


type | field
|--|--|
id | INT, AUTO_INCREMENT, PK
name | VARCHAR
specialty | VARCHAR
is_active | BOOLEAN
completed_missions| INT
failed_missions | INT
agent_rank | Junior / Senior / Commander ENUM / VARCHAR
|


## טבלת missions
tipe | filed 
|--|--|
id | INT, AUTO_INCREMENT, PK
title | VARCHAR 
description | TEXT
location | VARCHAR
difficulty | INT
importance | INT
status | VARCHAR
level_risk | VARCHAR
assigned_agent_id | INT
|

## מחלקה AgentBB

תפקיד | מתודה
|--|--|
(data(agent_create | יוצרת סוכן חדש ומחזירה את האובייקט של הסוכן 
()agents_all_get | מחזירה רשימה של כל הסוכנים
get_agent_by_id(id) | None או ,ID לפי אחד סוכן מחזירה
update_agent(id, data) | )id לשנות אפשרות אין )השורה לכל UPDATE
(id(agent_deactivate | מגדירה מצב סוכן ללא פעיל 
(id(completed_increment | מעדכן את כמות המשימות שהושלמו 
(id(failed_increment | מעדכן את כמות המשימות שנכשלו 
get_agent_performance(id) | completed, failed, total,האלוהמפתחותעםמילוןמחזירהsuccess_rate)שימו לב לחשב את הערך הזה rate_success - כמה באחוזים משימותהסתיימו בהצלחה מתוך הסך הכולל(| 
count_active_agent()| מחזירה את מספר הסוכנים הפעילים 

## מתודות MissionDB

תפקיד|  מתודה
|--|--|
(data(mission_create | יצירת משימה חדשה ומחזירה את כל האובייקט 
()missions_all_get | מחזירה את כל המשימות
get_mission_by_id(id) | מחזירה משימה אחת לפי ID או None
assign_mission(m_id, a_id) | משייכת משימה לסוכן
update_mission_status(id, status) | משמשת לכל שינוי סטטוס
get_open_missions_by_agent(id) | מחזירה משימות ASSIGNED/IN_PROGRESS של סוכן
()missions_all_count | סה"כ משימות
(status(status_by_count | סופרת לפי סטטוס מסוים 
()missions_open_count | סופרת משימות פתוחות 
count_critical_missions() | סופרת משימות CRITICAL
get_top_agent() | הסוכן ביותר הגבוה completed_missions עם 
|


## חוקי הבסיס נתונים 
מספר |חוק
|--|--|
1 | rank חייב להיות Commander / Senior / Junior — כל ערך אחר זורק שגיאה.
2 | difficulty ו-importance חייבים להיות בין 1 ל10- — אחרת שגיאה.
3 | level_risk מחושב אוטומטית בעת יצירת משימה — המשתמש לא שולח אותו.
4 | סוכן עם False=active_is לא יכול לקבל משימות.
5 | סוכן לא יכול להחזיק יותר מ3- משימות פתוחות )PROGRESS_IN / ASSIGNED )במקביל.
6 | אם CRITICAL=level_risk — רק סוכן בדרגת Commander יכול לקבל את המשימה.
7 | ניתן לשייך רק משימה בסטטוס NEW. לאחר שיוך: ASSIGNED=status.
8 | ניתן להתחיל רק משימה בסטטוס ASSIGNED. לאחר: PROGRESS_IN=status.
9 | ניתן לסיים רק משימה. PROGRESS_IN ולשנות לסטטוס completed or failed
10 |ניתן לבטל רק משימה בסטטוס NEW או ASSIGNED — אחרת שגיאה


## הרצת התוכנית 

### להורדת הפרויקט

`git clone https://github.com/avrhahm-lider/intelligence-task-manager.git`

### יש להריץ את הפקודות בשורה אחת ולהוריד את `\`

```
docker run -d --name intelligence-mysql \
-e MYSQL_ROOT_PASSWORD=1234 \
-e MYSQL_DATABASE=Intelligence_db \
-p 3306:3306  \ 
-v mysql_data_intelligence:/var/lib/mysql \
-d mysql:latest
```
### בסביבה שמשתמשים להתחבר ל Imege 

```
user = root
password = 1234
port = 3306
host = הIP HOST

```

## להוריד את קובץ ה `requirements.txt`

`pip install -r requirements.txt `
## הרצת ה `main`
`python main.py`

