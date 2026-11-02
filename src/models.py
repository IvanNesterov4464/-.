# src/booking.py

class Resource:
    """Заглушка класса Ресурса (аудитории или оборудования)"""
    def __init__(self, resource_id: int, name: str, resource_type: str):
        self.id = resource_id
        self.name = name
        self.type = resource_type  # 'аудитория' или 'техника'
        self.status = "доступен"


class BookingManager:
    """Менеджер управления бронированием"""
    def __init__(self):
        # Временное хранилище броней внутри оперативной памяти
        self.bookings = []

    def check_availability(self, resource_id: int, start_time: str, end_time: str) -> bool:
        """
        Минимальная реализация проверки доступности.
        В рамках первого цикла всегда возвращает True (свободно).
        """
        print(f"[Заглушка] Проверка доступности ресурса {resource_id} с {start_time} по {end_time}")
        return True
