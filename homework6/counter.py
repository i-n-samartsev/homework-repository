"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
"""
from collections import defaultdict


def instances_counter(original_class):
    """
    Decorator that adds 2 methods to the class: get_created_instances
    and reset_instances_counter
    """

    instances_counter_storage = defaultdict(int)

    @classmethod
    def get_created_instances(cls):
        return instances_counter_storage[cls]

    @classmethod
    def reset_instances_counter(cls):
        previous_number_of_instances = instances_counter_storage[cls]
        instances_counter_storage[cls] = 0
        return previous_number_of_instances

    def redefinition_of__new__(cls, *args, **kwargs):
        instances_counter_storage[cls] += 1
        instance = super(type, cls).__new__(cls)
        return instance

    original_class.__new__ = redefinition_of__new__
    original_class.get_created_instances = get_created_instances
    original_class.reset_instances_counter = reset_instances_counter
    return original_class
