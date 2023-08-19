from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
from sqlalchemy.orm import relationship

class user(Base):
    __tablename__ = "employee"

    id = Column(Integer,primary_key = True,index = True,autoincrement=True)
    name=Column(String) 
    email=Column(String) 
    password=Column(String)
    skill = Column(String,default=0)
    uid = Column(String)
    role = Column(String,default="user")
    
class job(Base):
    __tablename__ = "job"

    jid = Column(Integer, index=True, primary_key=True)
    jname = Column(String)
    jobid = Column(String, nullable=True)
    skill = Column(String,default=0)
    status = Column(Boolean, default=False)
    discription = Column(String)

# class purchase(Base):  
#     __tablename__ = "purchase info"

#     id = Column(Integer,index = True,primary_key = True)
#     pname=Column(String) 
#     pid = Column(String, nullable = True,primary_key = True)
#     puechaserd = Column(Boolean,default=False)
#     uid = Column(String, nullable = True)
#     uname = Column(String)
    