class CustomLogger:
    def __enter__(self):
        self.log_file = open("log.txt", "w")
        return self

    def write_log(self, log_message):
        self.log_file.write(log_message + "\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.write_log(f"An exception of type {exc_type} occurred.")
        self.log_file.close()
