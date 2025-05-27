class Car:
    def __init__(self, brand):
        self.brand = brand              
        self.__engine_status = "Off"   

    def display_engine_status(self):
        print(f"Engine status: {self.__engine_status}")

    def __start_the_engine(self):       
        self.__engine_status = "Running"
        print("Engine has started.")

    def start_the_car(self):            
        self.__start_the_engine()


# EXAMPLE USAGE

if __name__ == "__main__":
    my_car = Car("Toyota")
    print("Brand:", my_car.brand) 