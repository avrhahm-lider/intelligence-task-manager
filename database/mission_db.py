from db_connection import con

class MissonDB:
    def __init__(self, db_connection):
        self.connection = con
    
    def run_query(self, query, parm: tuple | None = None, is_fetch : bool = False):
        try: 
            cursor = self.connection.cursor(dictionary= True)
            cursor.execute(query, parm)
            if is_fetch:
                return cursor.fetchall()
            self.connection.connection.commit()
        except Exception as e:
            raise
        finally :   
            cursor.close()
    def create_misson(self,data: dict):
        self.run_query("insert into missons (title, description, location, difficulty, importance, risk_level) value(%s, %s, %s, %s, %s, %s)",data.values())
        return self.run_query("SELECT * FROM missons WHERE id = (SELECT MAX(id) FROM missons)")
    def get_all_missons(self):
        return self.run_query("select * from missons", is_fetch=True)
    def get_misson_by_id(self, id: int):
        return self.run_query("select * from missons wher id = %s",(id,), is_fetch=True)
    def update_misson(self,id: int, data: dict):
        for key, val in data.items():
            self.run_query(f"update missons set `{key}` = %s where id = %s",(val, id))
            return True
    def get_open_missions_by_agent(self, id):
            return self.run_query("SELECT * FROM mission WHERE status = 'ASSIGNED' or status = 'IN_PROGRESS'", is_fetch= True)

    def count_all_missions(self):
        return self.run_query("SELECT COUNT(*) FROM mission", is_fetch= True)

    def count_by_status(self, status: str):
        return self.run_query("SELECT COUNT(status) FROM mission WHERE status = %s ",(status,), True) 

    def count_open_missions(self):
        return self.run_query("SELECT COUNT(status) FROM mission WHERE status = 'ASSIGNED' or status = 'IN_PROGRESS' or status = 'NEW'",is_fetch= True)

    def count_critical_missions(self):
        return self.run_query("SELECT COUNT( risk_level) FROM mission WHERE risk_level = CRITICAL", is_fetch= True)
# לזכור לעשות כאן פונקציה שסופרת את הסוכן עם המשימות המסוימות הכי הרבה