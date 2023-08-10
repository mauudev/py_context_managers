import contextlib
import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(2)  # una tarea heavy
        self.end = time.time()
        print(f"Block took {self.end - self.start} seconds to execute.")


@contextlib.contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Block took {end - start} seconds to execute.")
