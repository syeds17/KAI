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
    # Conversation Mode
    # -----------------------------------------
    active, timed_out = voice.conversation_active()
    
    if active:

        spoken_command = voice.listen()

        if not spoken_command:
            continue

        voice.refresh_conversation()
    
    elif timed_out:

        console.print("[yellow]Standing by, Chief.[/yellow]")
        voice.speak("Standing by, Chief.")
    # -----------------------------------------
    # Wake Word Mode
    # -----------------------------------------

    else:

        console.print("\n[cyan]🎤 Waiting for wake word...[/cyan]")

        if not voice.wait_for_wake_word():
            continue

        voice.start_conversation()

        spoken_command = voice.listen()

        if not spoken_command:
            continue

    spoken_command = spoken_command.lower().strip()
    
    if voice.should_exit_conversation(spoken_command):

        voice.stop_conversation()

        console.print("[yellow]Standing by, Chief.[/yellow]")

        voice.speak("Standing by, Chief.")

        continue

    if spoken_command in ["exit", "quit"]:

        console.print("[yellow]Goodbye, Chief.")
        voice.speak("Goodbye, Chief.")
        break

    response = router.route(spoken_command)

    console.print(f"[green]KAI >[/green] {response}")

    voice.speak(response)