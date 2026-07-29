import subprocess


class Executor:

    def execute(self, application: str):

        subprocess.Popen(application)