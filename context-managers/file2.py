from contextlib import AbstractContextManager, ContextDecorator


class TaxiDriverManager(AbstractContextManager):

    def __init__(self):
        self.dialogue = "you talking to me"

    def __enter__(self):
        print("**** enterting ****")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("**** exiting ****")
        return False

    def mirror_scene(self, dialogue):
        if dialogue != self.dialogue:
            raise Exception("Please watch it again ..")
        print(dialogue)


with TaxiDriverManager() as obj:
    random_dialogue = "this and that"
    #obj.mirror_scene(random_dialogue)





"""
ContextDecorator:
    1. can be used as a decorator
    2. can be used 'with' statement
"""
class director(ContextDecorator):

    def __enter__(self):
        print("**** director: enterting ****")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("**** director: exiting ****")
        return False



# #: Use: 1
@director()
def movie_director():
    print("director: martin")

movie_director()


#Use: 2
with director() as dir:
    print("director: martin")
