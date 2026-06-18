from database.db_connection import con

class AgentDB:
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
        ids = self.run_query("select id from agents",is_fetch= True)
        return len(list(filter(lambda x : x["id"] == id, ids))) != 0
    
    def create_agent(self,data: dict):
        self.run_query("insert into agents (name, specialty, agent_rank) value(%s, %s, %s)",tuple(data.values()))
        return self.run_query("SELECT * FROM agents WHERE id = (SELECT MAX(id) FROM agents)", is_fetch=True)
    def get_all_agents(self):
        return self.run_query("select * from agents", is_fetch=True)
    def get_agent_by_id(self, id: int):
        return self.run_query("select * from agents where id = %s",(id,), is_fetch=True)
    def update_agent(self, id: int, data: dict):
        for key, val in data.items():
            self.run_query(f"update agents set `{key}` = %s where id = %s", (val, id))
        return True
    def deactivate_agent(self, id):
            self.run_query(f"update agents set is_active = false where id = %s",(id,))
            return True
    def increment_completed(self, id: int):
        self.run_query(f"update agents set completed_missions = completed_missions + 1 where id = %s",(id,))
        return True
    def increment_failed(self, id: int):
        self.run_query(f"update agents set failed_missions = failed_missions + 1 where id = %s",(id,)) 
        return True
    def get_agent_performance(self, id: int):
        result = self.run_query("select completed_missions, failed_missions from agents where id = %s", (id,), True)
        if not result:
            return {"completed": 0, "failed": 0, "total": 0, "success_rate": 0}
        completed = result[0]["completed_missions"]
        failed = result[0]["failed_missions"]
        total = completed + failed
        success_rate = (completed / total) * 100 if total > 0 else 0
        return {
            "completed": completed,
            "failed": failed,
            "total": total,
            "success_rate": success_rate
        }
    def count_active_agent(self):
        return self.run_query(" SELECT COUNT(*) FROM agents where is_active = true", is_fetch= True)
    
    def is_agent_active(self, id: int):
        return self.run_query("select is_active from agents where id = %s", (id,), True)
    
    def is_commender(self, id: int):
        return len(self.run_query("select * FROM agents where agent_rank = 'Commander' and id = %s", (id,), True))