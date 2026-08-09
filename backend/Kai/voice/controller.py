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

    def listen(self, timeout=5, phrase_time_limit=10):

        return self.listener.listen(
            timeout=timeout, 
            phrase_time_limit=phrase_time_limit
        )

    def speak(self, text: str):

        self.speaker.say(text)

    def wait_for_wake_word(self):

        text = self.listen(
            timeout=3,
            phrase_time_limit=5
        )
        
        if not text:
            return None
        
        command = self.wakeword.extract_command(text)
        
        if command is None:
            
            return None
        
        self.speak("Yes, Chief.")
        
        return command
    
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