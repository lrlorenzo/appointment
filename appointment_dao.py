from sqlalchemy.exc import NoResultFound

from appointment import Appointment
from sqlalchemy import text, create_engine, MetaData, Table, Column, BigInteger, Integer, Float, DateTime, String, \
    Date, ForeignKey, select, func

from appointment_exception import AppointmentException

metadata_obj = MetaData()

task_schedule = Table(
    "task_schedule",
    metadata_obj,
    Column("id", BigInteger, primary_key=True),
    Column("resource_id", String(50), nullable=False),
    Column("resource_name", String(100), nullable=False),
    Column("task_id", BigInteger, nullable=False),
    Column("task", String(100), nullable=False),
    Column("status", String(10), nullable=False),
    Column("start_date", DateTime, nullable=False),
    Column("end_date", DateTime, nullable=False),
    Column("pct", Float, nullable=False),
)


def create_appointment(conn, a):
    stmt = task_schedule.insert().values(resource_id=a.resource_id, resource_name=a.resource_name,
                                         task_id=a.task_id, task=a.task, start_date=a.start_date, end_date=a.end_date,
                                         status=a.status, pct=a.pct)
    result = conn.execute(stmt)
    return result.inserted_primary_key[0]


def has_conflict(conn, resource_name, start_date, end_date):
    stmt = select(func.count()). \
        select_from(task_schedule). \
        where(task_schedule.c.resource_name == resource_name,
              task_schedule.c.start_date < end_date,
              task_schedule.c.end_date > start_date)

    result = conn.execute(stmt).fetchone()
    print(result.count_1)
    if result.count_1 > 0:
        raise NoResultFound(f"Appointment conflict for resource")

    return False


def find_all(conn):
    stmt = select(task_schedule.c.resource_id, task_schedule.c.resource_name, task_schedule.c.task_id,
                  task_schedule.c.task, task_schedule.c.status, task_schedule.c.pct). \
        select_from(task_schedule)

    result = conn.execute(stmt)

    appointment_list = []
    for i, r in enumerate(result):
        resource_id = r.resource_id
        resource_name = r.resource_name
        task_id = r.task_id
        task = r.task
        start_date = r.start_date
        end_date = r.end_date
        status = r.status
        pct = r.pct
        appointment_list.append(Appointment(resource_id, resource_name, task_id, task, start_date, end_date,
                                            status, pct))

    return appointment_list
