import os
import sys
# Ensure parent directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from template_player import TemplatePlayer
import random

class CautiousPlayer(TemplatePlayer):
    def handle_hit_stay(self, msg):
        # Extract number cards and decide: stay if sum is at least 20, else hit.
        numbers = [int(c[1]) for c in msg.get('hand', []) if isinstance(c, list) and c[0] == 'number']
        if sum(numbers) >= 20:
            self.send("stay")
        else:
            self.send("hit")

    # Use default freeze and flip_three logic from TemplatePlayer.
    
    # Ignore the print statements in handle_information
    def handle_information(self, msg):
        pass

if __name__ == "__main__":
    player = CautiousPlayer(name='Cautious' + str(random.randint(1, 1000)))
    player.play()