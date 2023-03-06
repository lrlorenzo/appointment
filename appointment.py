
class Appointment:
    def __init__(self, resource_id, resource_name, task_id, task, start_date, end_date, status, pct):
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.task_id = task_id
        self.task = task
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.pct = pct

    def to_dict(self):
        return {
            'resource_id': self.resource_id,
            'resource_name': self.resource_name,
            'task_id': self.task_id,
            'task': self.task,
            'start_date': self.start_date,
            'end_date':self.end_date,
            'status': self.status,
            'pct': self.pct
        }
