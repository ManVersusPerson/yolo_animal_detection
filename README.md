# API-приложение для обнаружения животных 
Проект по дисциплине "Программная инженерия"

# Описание приложения
Данное приложение позволяет посредством API находить животных на картинках.

# Состав команды:
Артем Хренников - finetune модели YOLO8n на датасете Animals Detection Images Dataset , документация
Евгений Данилов - Разработка тестов, имплементация continious integration
Иван Двоеглазов - Интеграция модели в приложение, развертывание приложения в облаке

# Животные, которых классифицирует наша модель
'Spider', 'Parrot', 'Scorpion', 'Sea turtle', 'Cattle', 'Fox', 'Hedgehog', 'Turtle', 'Cheetah', 'Snake', 'Shark', 'Horse', 'Magpie', 'Hamster', 'Woodpecker', 'Eagle', 'Penguin', 'Butterfly', 'Lion', 'Otter', 'Raccoon', 'Hippopotamus', 'Bear', 'Chicken', 'Pig', 'Owl', 'Caterpillar', 'Koala', 'Polar bear', 'Squid', 'Whale', 'Harbor seal', 'Raven', 'Mouse', 'Tiger', 'Lizard', 'Ladybug', 'Red panda', 'Kangaroo', 'Starfish', 'Worm', 'Tortoise', 'Ostrich', 'Goldfish', 'Frog', 'Swan', 'Elephant', 'Sheep', 'Snail', 'Zebra', 'Moths and butterflies', 'Shrimp', 'Fish', 'Panda', 'Lynx', 'Duck', 'Jaguar', 'Goose', 'Goat', 'Rabbit', 'Giraffe', 'Crab', 'Tick', 'Monkey', 'Bull', 'Seahorse', 'Centipede', 'Mule', 'Rhinoceros', 'Canary', 'Camel', 'Brown bear', 'Sparrow', 'Squirrel', 'Leopard', 'Jellyfish', 'Crocodile', 'Deer', 'Turkey', 'Sea lion'

- Демо: http://80.89.228.14:666
- Интерактивная документация: http://80.89.228.14:666/docs#/default/get_image_image__id__get
- Использованная модель: https://github.com/ultralytics/ultralytics
- Использованный датасет: https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset?datasetId=1316317&sortBy=dateRun&tab=profile
