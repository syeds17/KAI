import subprocess
import webbrowser


class Executor:

    def execute_application(self, command: str):
        try:

            if isinstance(command, str):
                subprocess.Popen(command)

            else:
                subprocess.Popen(command)

            return True

        except Exception as e:

            print(f"[Executor Error] {e}")
            return False
        
    def execute_website(self, url: str):
        webbrowser.open(url)

    def execute_folder(self, path: str):
        subprocess.Popen(["explorer", path])

    def close_process(self, process: str):
        subprocess.run(
            [
                "taskkill",
                "/F",
                "/IM",
                process
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )