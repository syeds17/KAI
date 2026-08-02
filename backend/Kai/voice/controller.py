from .listener import Listener
from .speaker import Speaker
from .wakeword import WakeWordDetector
from .conversation import ConversationManager
from .commands import EXIT_CONVERSATION


class VoiceController:

    def __init__(self):

        self.listener = Listener()
        self.speaker = Speaker()
        self.wakeword = WakeWordDetector()
        self.conversation = ConversationManager()

    def listen(self):

        return self.listener.listen()

    def speak(self, text: str):

        self.speaker.say(text)

    def wait_for_wake_word(self):

        text = self.listen()

        if self.wakeword.detected(text):

            self.speak("Yes, Chief.")

            return True

        return False
    
    def conversation_active(self):

        return self.conversation.is_active()


    def start_conversation(self):

        self.conversation.start()


    def refresh_conversation(self):

        self.conversation.refresh()


    def stop_conversation(self):

        self.conversation.stop()
        
    def should_exit_conversation(self, text: str):

        if not text:
            return False

        text = text.lower().strip()

        return text in EXIT_CONVERSATION