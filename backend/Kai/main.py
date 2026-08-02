from rich.console import Console

from core.startup import startup
from brain.router import Router
from voice.controller import VoiceController


console = Console()

startup()

router = Router()
voice = VoiceController()


while True:

    command = console.input(
        "\n[bold cyan]Chief > [/bold cyan]"
    ).strip()

    if command.lower() in ["exit", "quit"]:
        console.print("[yellow]Goodbye, Chief.")
        break

    if command == "":

        if not voice.wait_for_wake_word():

            console.print("[yellow]Wake word not detected.[/yellow]")

            continue

        spoken_command = voice.listen()
        
        if spoken_command and spoken_command.lower() in ["exit", "quit"]:

            console.print("[yellow]Goodbye, Chief.")
            voice.speak("Goodbye, Chief.")

            break

        if not spoken_command:
            console.print("[red]I couldn't hear you, Chief.")
            continue

        console.print(f"[cyan]Chief 🎤 >[/cyan] {spoken_command}")

        response = router.route(spoken_command)

        console.print(f"[green]KAI >[/green] {response}")

        voice.speak(response)

        continue

    response = router.route(command)

    console.print(f"[green]KAI >[/green] {response}")

    voice.speak(response)