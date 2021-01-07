class MyClass:
    def __init__(self, name:str):
        self.name = name
    def show(self) -> None:
        print(self.name)       
    def get_name(self) -> str:
        return self.name