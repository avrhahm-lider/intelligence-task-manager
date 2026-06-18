from database.db_connection import con

class MissionDB:
    def __init__(self, db_connection):
        self.connection = con
    
    def run_query(self, query, parm: tuple | None = None, is_fetch : bool = False):
        try: 
            cursor = self.connection.cursor(dictionary= True)
            cursor.execute(query, parm)
            if is_fetch:
                return cursor.fetchall()
            self.connection.commit()
        except Exception as e:
            raise
        finally :   
            cursor.close()
    
    def is_id(self, id: int):
        ids = self.run_query("select id from missions",is_fetch= True)
        return len(list(filter(lambda x : x["id"] == id, ids))) != 0
    
    def create_mission(self,data: dict):
        self.run_query("insert into missions (title, description, location, difficulty, importance, risk_level) value(%s, %s, %s, %s, %s, %s)",tuple(data.values()))
        return self.run_query("SELECT * FROM missions WHERE id = (SELECT MAX(id) FROM missions)", is_fetch= True)
    def get_all_missions(self):
        return self.run_query("select * from missions", is_fetch=True)
    def get_mission_by_id(self, id: int):
        return self.run_query("select * from missions where id = %s",(id,), is_fetch=True)

    def assign_mission(self, m_id: int, a_id: int):
        self.run_query("update missions set assigned_agent_id = %s where id = %s",(a_id, m_id))
        return True   
    def update_mission_status(self,id: int, status: dict):
            self.run_query("update missions set status = %s where id = %s",(status, id))
            return True
    def get_open_missions_by_agent(self, id):
            return self.run_query("SELECT * FROM missions WHERE (status = 'ASSIGNED' OR status = 'IN_PROGRESS') AND assigned_agent_id = %s", (id,), is_fetch=True)

    def count_all_missions(self):
        return self.run_query("SELECT COUNT(*) FROM missions", is_fetch= True)

    def count_by_status(self, status: str):
        return self.run_query("SELECT COUNT(status) FROM missions WHERE status = %s ",(status,), True) 

    def count_open_missions(self):
        return self.run_query("SELECT COUNT(status) FROM missions WHERE status = 'ASSIGNED'",is_fetch= True)

    def count_critical_missions(self):
        return self.run_query("SELECT COUNT(risk_level) FROM missions WHERE risk_level = 'CRITICAL'", is_fetch=True)
# לזכור לעשות כאן פונקציה שסופרת את הסוכן עם המשימות המסוימות הכי הרבה