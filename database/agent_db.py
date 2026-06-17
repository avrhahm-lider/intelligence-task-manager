from db_connection import con

class AgentDB:
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
    def create_agent(self,data: dict):
        self.run_query("insert into agents (name, specialty, agent_rank) value(%s, %s, %s)",data.values())
        return self.run_query("SELECT * FROM agents WHERE id = (SELECT MAX(id) FROM agents)")
    def get_all_agents(self):
        return self.run_query("select * from agents", is_fetch=True)
    def get_agent_by_id(self, id: int):
        return self.run_query("select * from agents wher id = %s",(id,), is_fetch=True)
    def update_agent(self,id: int, data: dict):
        for key, val in data.items():
            self.run_query(f"update agents set `{key}` = %s where id = %s",(val, id))
            return True
    def deactivate_agent(self, id):
            self.run_query(f"update books set is_active = false where id = %s",(id,))
            return True
    def increment_completed(self, id: int):
        self.run_query(f"update books set completed_missions = completed_missions + 1 where id = %s",(id,))
        return True
    def increment_failed(self, id: int):
        self.run_query(f"update books set failed_missions = failed_missions + 1 where id = %s",(id,)) 
        return True
    def get_agent_performance(self, id: int):
         completed = self.run_query("select completed_missions from agents wher id = %s", (id,), True)
         failed = self.run_query("select failed_missions from agents wher id = %s", (id,), True)
         total = completed + failed
         success_rate = (completed / total) * 100 
         return{
             "completed" : completed,
             "failed" : failed,
             "total" : total,
             "success_rate" : success_rate
         }
    def count_active_agent(self):
        return self.run_query(" SELECT COUNT(*) FROM agents where is_active = true", is_fetch= True)