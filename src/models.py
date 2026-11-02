from datetime import datetime
from typing import List, Optional

# =====================================================================
# Задача: Создать заготовку класса пользователя (User stub)
# =====================================================================
class User:
    def __init__(self, user_id: int, name: str, role: str):
        self.user_id = user_id
        self.name = name
        self.role = role  # Например: "Преподаватель", "Студент"


# =====================================================================
# Задача: Реализовать базовую модель ресурса и аудитории (Resource stub)
# =====================================================================
class Resource:
    def __init__(self, resource_id: int, name: str, resource_type: str):
        self.resource_id = resource_id
        self.name = name  # Например: "Аудитория 401" или "Проектор Epson"
        self.resource_type = resource_type  # "Аудитория" или "Оборудование"


# =====================================================================
# Класс сущности бронирования для внутренней логики
# =====================================================================
class Booking:
    def __init__(self, booking_id: int, user_id: int, resource_id: int, start_time: datetime, end_time: datetime):
        self.booking_id = booking_id
        self.user_id = user_id
        self.resource_id = resource_id
        self.start_time = start_time
        self.end_time = end_time


# =====================================================================
# Бизнес-логика модуля бронирования
# =====================================================================
class BookingManager:
    def __init__(self):
        # Имитация временной базы данных в памяти
        self._bookings: List[Booking] = []
        self._booking_id_counter = 1

    # =================================================================
    # Задача: Добавить функцию-заглушку для проверки доступности (check_availability stub)
    # =================================================================
    def check_availability(self, resource_id: int, start_time: datetime, end_time: datetime) -> bool:
        """
        Проверяет, свободен ли ресурс на указанный промежуток времени.
        Временная заглушка всегда возвращает True (ресурс свободен).
        """
        # TODO: Реализовать проверку пересечения временных интервалов (коллизий)
        return True

    # =================================================================
    # Задача: Написать структуру логики создания бронирования (create_booking stub)
    # =================================================================
    def create_booking(self, user_id: int, resource_id: int, start_time: datetime, end_time: datetime) -> Optional[Booking]:
        """
        Создает бронирование, если ресурс доступен по времени.
        """
        # Использование функции проверки доступности
        if self.check_availability(resource_id, start_time, end_time):
            new_booking = Booking(
                booking_id=self._booking_id_counter,
                user_id=user_id,
                resource_id=resource_id,
                start_time=start_time,
                end_time=end_time
            )
            self._bookings.append(new_booking)
            self._booking_id_counter += 1
            print(f"[STUB] Бронирование #{new_booking.booking_id} для пользователя {user_id} успешно создано.")
            return new_booking
        
        print(f"[STUB] Ошибка: Ресурс {resource_id} занят на выбранное время.")
        return None

    # =====================================================================
# Блок проверки работы заглушек (добавьте в конец файла)
# =====================================================================
if __name__ == "__main__":
    print("--- Старт проверки модуля бронирования ---")
    
    # 1. Инициализируем менеджер бронирования
    manager = BookingManager()
    
    # 2. Создаем тестовых пользователей (User stub)
    teacher = User(user_id=101, name="Иван Иванов", role="Преподаватель")
    print(f"Создан пользователь: {teacher.name} ({teacher.role})")
    
    # 3. Создаем тестовые ресурсы (Resource stub)
    room = Resource(resource_id=1, name="Аудитория 401", resource_type="Аудитория")
    projector = Resource(resource_id=2, name="Проектор Epson", resource_type="Оборудование")
    print(f"Созданы ресурсы: {room.name}, {projector.name}")
    
    # 4. Проверяем структуру логики создания бронирования (create_booking stub)
    start = datetime(2026, 11, 2, 12, 0)
    end = datetime(2026, 11, 2, 13, 30)
    
    print("\nПопытка создания бронирования...")
    booking = manager.create_booking(
        user_id=teacher.user_id, 
        resource_id=room.resource_id, 
        start_time=start, 
        end_time=end
    )
    
    print("--- Проверка завершена ---")

