# def insert_data(name,age):
def insert_data(name:str,age:int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Invalid input: age must be a non-negative integer")   
        else:
            print(f"Inserting data for {name} with age {age}")
    else:
        raise ValueError("Invalid input: name must be a string and age must be an integer")
        # raise TypeError("Invalid input: name must be a string and age must be an integer")


def update_data(name:str,age:int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Invalid input: age must be a non-negative integer")   
        else:
            print(f"Updating data for {name} with age {age}")
    else:
        raise ValueError("Invalid input: name must be a string and age must be an integer")
        # raise TypeError("Invalid input: name must be a string and age must be an integer")

insert_data("John Doe", 30)
insert_data("John Doe", "thirty")

