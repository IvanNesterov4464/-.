import unittest
from datetime import datetime
# Импортируем классы из вашего модуля (убедитесь, что пути корректны)
from models import BookingManager, User, Resource

class TestBookingModule(unittest.TestCase):
    def setUp(self):
        """Настройка окружения перед каждым тестом"""
        self.manager = BookingManager()
        self.user_id = 101
        self.resource_id = 1
        self.start_time = datetime(2026, 11, 2, 14, 0)
        self.end_time = datetime(2026, 11, 2, 15, 30)

    def test_create_booking_success(self):
        """Тест успешного создания бронирования (через заглушку)"""
        booking = self.manager.create_booking(
            user_id=self.user_id,
            resource_id=self.resource_id,
            start_time=self.start_time,
            end_time=self.end_time
        )
        # Проверяем, что объект создался и данные совпадают
        self.assertIsNotNone(booking)
        self.assertEqual(booking.user_id, self.user_id)
        self.assertEqual(booking.resource_id, self.resource_id)

    def test_check_availability_stub(self):
        """Тест заглушки проверки доступности (всегда True)"""
        is_available = self.manager.check_availability(
            resource_id=self.resource_id,
            start_time=self.start_time,
            end_time=self.end_time
        )
        self.assertTrue(is_available)

if __name__ == "__main__":
    unittest.main()
