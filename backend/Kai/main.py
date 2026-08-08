from rich.console import Console

from core.startup import startup
from brain.router import Router
from voice.controller import VoiceController


console = Console()

startup()

router = Router()
voice = VoiceController()


while True:

    # -----------------------------------------
    # WAKE WORD MODE
    # -----------------------------------------

    if not voice.conversation_active()[0]:

        console.print("\n[cyan]🎤 Waiting for wake word...[/cyan]")

        spoken_command = voice.wait_for_wake_word()

        if spoken_command is None:
            continue

        voice.start_conversation()

        # Wake word only
        if not spoken_command:

            spoken_command = voice.listen()

            if not spoken_command:
                continue

    # -----------------------------------------
    # CONVERSATION MODE
    # -----------------------------------------

    else:

        active, timed_out = voice.conversation_active()

        if timed_out:

            console.print("[yellow]Standing by, Chief.[/yellow]")
            voice.speak("Standing by, Chief.")
            continue

        spoken_command = voice.listen()

        if not spoken_command:
            continue

        spoken_command = spoken_command.lower().strip()

        if voice.should_exit_conversation(spoken_command):

            voice.stop_conversation()

            console.print("[yellow]Standing by, Chief.[/yellow]")
            voice.speak("Standing by, Chief.")

            continue

        voice.refresh_conversation()

    # -----------------------------------------
    # GLOBAL EXIT
    # -----------------------------------------

    spoken_command = spoken_command.lower().strip()

    if spoken_command == "exit":

        voice.stop_conversation()

        console.print("[yellow]Goodbye, Chief.[/yellow]")
        voice.speak("Goodbye, Chief.")

        break

    # -----------------------------------------
    # ROUTER
    # -----------------------------------------

    response = router.route(spoken_command)

    console.print(f"[green]KAI >[/green] {response}")

    voice.speak(response)