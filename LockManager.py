import threading


class LockManager:
    def __init__(self):
        self.resource_locks = {}

    def acquire_lock(self, resource_name):
        if resource_name not in self.resource_locks:
            self.resource_locks[resource_name] = threading.Lock()
        self.resource_locks[resource_name].acquire()

    def release_lock(self, resource_name):
        if resource_name in self.resource_locks:
            self.resource_locks[resource_name].release()
