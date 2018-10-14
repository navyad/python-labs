from contextlib import AbstractContextManager


class TaxiDriverManager(AbstractContextManager):

    def __init__(self):
        self.dialogue = "you talking to me"

    def __enter__(self):
        print("**** enterting ****")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("**** exiting ****")

    def mirror_scene(self, dialogue):
        if dialogue != self.dialogue:
            raise Exception("Please watch it again ..")
        print(dialogue)


#ErrorManager().call_me()

with TaxiDriverManager() as obj:
    random_dialogue = "this and that"
    #obj.mirror_scene(obj.dialogue)
    obj.mirror_scene(random_dialogue)
