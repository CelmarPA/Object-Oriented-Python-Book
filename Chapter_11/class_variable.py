# class_variable.py

# Sample class
class Sample:

    n_objects: int = 0   # this is a class variable of the Sample class

    def __init__(self, name: str) -> None:
        self.name: str = name
        Sample.n_objects += 1

    @classmethod
    def how_many_objects(cls) -> None:
        print(f"There are {cls.n_objects} Sample objects")

    def __del__(self):      # Note: __del__ is not guaranteed to run immediately after 'del'
        Sample.n_objects -= 1


# Instantiate 4 objects
o_sample_1: Sample = Sample("A")
o_sample_2: Sample = Sample("B")
o_sample_3: Sample = Sample("C")
o_sample_4: Sample = Sample("D")

# Delete 1 object
del o_sample_3

# See how many we have
o_sample_1.how_many_objects()
