# API-приложение для обнаружения животных 
Проект по дисциплине "Программная инженерия"

# Описание приложения
Данное приложение позволяет посредством API находить животных на картинках.

# Состав команды:

- Артем Хренников - finetune модели YOLO8n на датасете Animals Detection Images Dataset , документация

- Евгений Данилов - Разработка тестов, имплементация continuous integration

- Иван Двоеглазов - Интеграция модели в приложение, развертывание приложения в облаке

# Возможности

1. Получить картинку с предсказаниями

По адресу /predict/image отправляется POST-запрос, в теле сообщения отправляется файл формата jpg. 
![image width="100" height="100"](https://github.com/ManVersusPerson/yolo_animal_detection/assets/105095657/db1cf8b3-ef75-40d5-ae3a-b6c70c1818e9)

Нейросеть выполняет predict по картинке и ответ получаем:
<img src="https://github.com/ManVersusPerson/yolo_animal_detection/assets/105095657/229f9c46-9ead-4512-9c05-7d072ee2e62b.png" width="800" height="660" />

2. Получить json с предсказанными животными

По адресу /predict/image отправляется POST-запрос, в теле сообщения отправляется файл формата jpg. 
Нейросеть выполняет predict по картинке и ответ получаем:
![image](https://github.com/ManVersusPerson/yolo_animal_detection/assets/105095657/debe0019-e7d9-4df1-92cf-818b85a33a44)

3. Получить уже предсказанную картинку

По адресу /image/{id} отправляется GET-запрос, id можно получить из json из второго пункта по ключу "img_url".
Получаем уже предсказанную картинку:
![image](https://github.com/ManVersusPerson/yolo_animal_detection/assets/105095657/fe2a4819-5d0f-4122-8496-c09a9a45b383)

# Животные, которых классифицирует наша модель
'Spider', 'Parrot', 'Scorpion', 'Sea turtle', 'Cattle', 'Fox', 'Hedgehog', 'Turtle', 'Cheetah', 'Snake', 'Shark', 'Horse', 'Magpie', 'Hamster', 'Woodpecker', 'Eagle', 'Penguin', 'Butterfly', 'Lion', 'Otter', 'Raccoon', 'Hippopotamus', 'Bear', 'Chicken', 'Pig', 'Owl', 'Caterpillar', 'Koala', 'Polar bear', 'Squid', 'Whale', 'Harbor seal', 'Raven', 'Mouse', 'Tiger', 'Lizard', 'Ladybug', 'Red panda', 'Kangaroo', 'Starfish', 'Worm', 'Tortoise', 'Ostrich', 'Goldfish', 'Frog', 'Swan', 'Elephant', 'Sheep', 'Snail', 'Zebra', 'Moths and butterflies', 'Shrimp', 'Fish', 'Panda', 'Lynx', 'Duck', 'Jaguar', 'Goose', 'Goat', 'Rabbit', 'Giraffe', 'Crab', 'Tick', 'Monkey', 'Bull', 'Seahorse', 'Centipede', 'Mule', 'Rhinoceros', 'Canary', 'Camel', 'Brown bear', 'Sparrow', 'Squirrel', 'Leopard', 'Jellyfish', 'Crocodile', 'Deer', 'Turkey', 'Sea lion'


- Демо: http://80.89.228.14:666
- Интерактивная документация: http://80.89.228.14:666/docs
- Использованная модель: https://github.com/ultralytics/ultralytics
- Использованный датасет: https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset?datasetId=1316317&sortBy=dateRun&tab=profile
