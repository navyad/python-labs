from contextlib import AbstractContextManager



# class ManagerABC(AbstractContextManager):
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#     def call_me(self):
#         print("call_me")
#
#
# with ManagerABC() as obj:
#     obj.call_me()
#


# class ManagerException(AbstractContextManager):
#     """
#     exit without True or False: raise Exception
#     """
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#     def call_me(self):
#         raise Exception("poi")
#         print("call_me")
#
#
# with ManagerException() as obj:
#     obj.call_me()



class ManagerSuppressException(AbstractContextManager):
    """
    suppress exception
    """

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

    def call_me(self):
        raise Exception("poi")
        print("call_me")


with ManagerSuppressException() as obj:
    obj.call_me()
    print("after call")



# class ManagerRaiseException(AbstractContextManager):
#     """
#     raise exception
#     """
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return False
#
#     def call_me(self):
#         raise Exception("poi")
#         print("call_me")
#
#
# with ManagerRaiseException() as obj:
#     obj.call_me()
