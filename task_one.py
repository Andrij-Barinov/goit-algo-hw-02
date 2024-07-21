import queue
import time
import random


class ServiceCenter:
    def __init__(self):
        # Ініціалізація черги заявок та лічильника ідентифікаторів заявок
        self.request_queue = queue.Queue()
        self.request_id = 0

    def generate_request(self):
        # Збільшуємо лічильник ідентифікаторів заявок
        self.request_id += 1
        # Формуємо дані нової заявки
        request_data = f"Заявка №{self.request_id}"
        # Додаємо нову заявку до черги
        self.request_queue.put(request_data)
        print(f"Сгенеровано нову заявку: {request_data}")

    def process_request(self):
        # Перевіряємо, чи черга не пуста
        if not self.request_queue.empty():
            # Видаляємо заявку з черги для обробки
            request_data = self.request_queue.get()
            print(f"Обробка заявки: {request_data}")
            # Симулюємо затримку обробки заявки
            time.sleep(random.uniform(0.5, 2.0))
        else:
            # Якщо черга пуста, виводимо відповідне повідомлення
            print("Черга пуста. Немає заявок для обробки.")

    def run(self):
        # Основний цикл роботи програми
        try:
            while True:
                # Симулюємо час між генерацією заявок
                time.sleep(1)

                # Випадково вирішуємо, чи генерувати нову заявку
                if random.choice([True, False]):
                    self.generate_request()

                # Випадково вирішуємо, чи обробляти заявку
                if random.choice([True, False]):
                    self.process_request()
        except KeyboardInterrupt:
            # Завершення програми користувачем
            print("\nПрограма завершена користувачем")


if __name__ == "__main__":
    # Створюємо екземпляр класу ServiceCenter
    service_center = ServiceCenter()
    # Запускаємо основний цикл роботи програми
    service_center.run()