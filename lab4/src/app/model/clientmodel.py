from typing import Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ClientModel:
    client_id: int
    first_name: str
    last_name: str
    middle_name: Optional[str]
    birth_date: datetime
    email: Optional[str]
    phone: Optional[str]
    sex: str
    hire_date: datetime
    job_title_id: int
    department_id: int
    note: str
    image_path: str


