from ..common.db_connection import engine, Session
from ..data_model.model import Script
from typing import Any


class ScriptRepo():

    def __init__(self, session: Any) -> None:
        self.session = session


    def create_script(self, script: Script) -> Script:
        self.session.add(script)
        self.session.commit()
        self.session.close()
        return script
    
    def get_script_by_id(self, script_id: int) -> Script:
        script = self.session.query(Script).filter(Script.id == script_id).first()
        self.session.close()
        return script
    
    def update_script_by_id(self, script_id: int, set_values: dict) -> Script:
        script = self.session.query(Script).filter(Script.id == script_id).first()
        for key, value in set_values.items():
            setattr(script, key, value)
        self.session.commit()
        self.session.close()
        return script