class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: "Customer") -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
    
class CinemaHall:
    def __init__(self, hall_number: int):
        self.hall_number = hall_number
    
    def movie_session(self, 
                      movie_name: str, 
                      customers: list["Customer"], 
                      cleaning_staff: "Cleaner") -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.hall_number)
    
class Customer:
    def __init__(self, name: str, food: str):
        self.name = name
        self.food = food
    
    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')
        
class Cleaner:
    def __init__(self, name: str):
        self.name = name
    
    def clean_hall(self, hall_number: int) -> None:
        print(f'Cleaner {self.name} is cleaning hall number {hall_number}.')
