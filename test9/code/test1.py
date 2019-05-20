class PrintableMixin:
    def print(self):
        print(self.content, 'mixin')

class SuperPrintableMixin(PrintableMixin):
    def print(self):
        print('`'*20)
        super().print()
        print('---'*20)
