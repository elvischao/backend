import typing as t
from pydantic import BaseModel

from app.db.schemas.user import UserOut
from app.db.schemas.port_usage import PortUsageOut
from app.db.schemas.port_forward import PortForwardRuleOut

class PortUserConfig(BaseModel):
    pass

class PortUserBase(BaseModel):
    user_id: int


class PortUserOut(PortUserBase):
    port_id: int
    config: PortUserConfig

    class Config:
        orm_mode = True


class PortUserOpsOut(PortUserBase):
    port_id: int
    user: UserOut
    config: PortUserConfig

    class Config:
        orm_mode = True


class PortUserEdit(PortUserBase):
    config: t.Optional[PortUserConfig]
    
    class Config:
        orm_mode = True


class PortConfig(BaseModel):
    egress_limit: t.Optional[int]
    ingress_limit: t.Optional[int]


class PortBase(BaseModel):
    external_num: int = None
    num: int
    server_id: int
    config: PortConfig


class PortOut(PortBase):
    id: int
    usage: t.Optional[PortUsageOut]
    forward_rule: t.Optional[PortForwardRuleOut]

    class Config:
        orm_mode = True


class PortOpsOut(PortBase):
    id: int
    is_active: bool
    forward_rule: t.Optional[PortForwardRuleOut]
    allowed_users: t.List[PortUserOpsOut]

    class Config:
        orm_mode = True


class PortCreate(BaseModel):
    num: int
    external_num: t.Optional[int] = None
    config: t.Optional[PortConfig]
    is_active: t.Optional[bool] = True

    class Config:
        orm_mode = True


class PortEdit(BaseModel):
    external_num: t.Optional[int]
    is_active: t.Optional[bool]
    config: t.Optional[PortConfig]

    class Config:
        orm_mode = True

