"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(original_class):
    """
    Decorator that adds 2 methods to the class: get_created_instances
    and reset_instances_counter
    """

    number_of_instances = 0

    @classmethod
    def get_created_instances(cls):
        return number_of_instances

    @classmethod
    def reset_instances_counter(cls):
        nonlocal number_of_instances
        previous_number_of_instances = number_of_instances
        number_of_instances = 0
        return previous_number_of_instances

    def redefinition_of__new__(cls, *args, **kwargs):
        nonlocal number_of_instances
        number_of_instances += 1
        instance = super(cls, cls).__new__(cls)
        return instance

    original_class.__new__ = redefinition_of__new__
    original_class.get_created_instances = get_created_instances
    original_class.reset_instances_counter = reset_instances_counter
    return original_class


@instances_counter
class User:
    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(1, 2), User(1, 2), User(1, 2)
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
    print(user.get_created_instances())  # 0
    print(user.a)  # 1
