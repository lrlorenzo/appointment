import appointment_dao
from database import engine
from datetime import timezone, datetime
from LockManager import LockManager

lock_manager = LockManager()


def add_appointments(appointments):
    with engine.begin() as conn:
        for a in appointments:
            try:
                resource_name = a.resource_name
                lock_manager.acquire_lock(resource_name)
                print(resource_name, a.start_date, a.end_date)
                appointment_dao.has_conflict(conn, resource_name, a.start_date, a.end_date)
                appointment_id = appointment_dao.create_appointment(conn, a)
                print(appointment_id)
            finally:
                lock_manager.release_lock(resource_name)


def find_all():
    with engine.begin() as conn:
        customer = appointment_dao.find_all(conn)
        return customer


def find(appointment_id):
    with engine.begin() as conn:
        appointment = appointment_dao.find(conn, appointment_id)
        return appointment
