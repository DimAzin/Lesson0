# 3 класса: UrTube, Video, User.
#
# Общее ТЗ:
# Реализовать классы для взаимодействия с платоформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.
#
# Подробное ТЗ:
#
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#  Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
# Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users с такмими же логином и паролем. Если такой пользователь суещствует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
# Метод log_out для сброса текущего пользователя на None.
# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же следует учитывать следущие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"

import time as t

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
#hash(password)
        log_user = User(nickname,hash(password))
        user_exists = any((user.nickname == log_user.nickname) or (user.password == log_user.password) for users in self.users)
        if user_exists:
            self.current_user = user
        # print("log_in: ", self.current_user.nickname, self.current_user.age)
        return True

    def register(self, nickname, password, age):
        new_user = User(nickname, hash(password), age)
        user_exists = any(users.nickname == new_user.nickname for users in self.users)
        if not user_exists:
            self.users.append(new_user)
            self.current_user = new_user
            # print('register: ', self.users)
            # print(self.current_user)#.nickname, self.current_user.age)
        else:
            print("Такой пользователь уже существует!")
        return True

    def log_out(self):
        UrTube.current_user = None

    def add(self, *new_videos):
        for new_video in new_videos:
            video_exists = any(video.title == new_video.title for video in self.videos)
            if not video_exists:
                self.videos.append(new_video)
                print(f"Видео {new_video.title} добавлено.")

        return True

    def get_videos(self, search_keyword):
        keyword_lower = search_keyword.lower()
        matching_videos = [video.title for video in self.videos if keyword_lower in video.title.lower()]
        return matching_videos

    def watch_video(self, video_title):
        if self.current_user is None:
            print("Войдите в аккаунт чтобы смотреть видео!")
            return

        found_video = None
        for video in self.videos:
            if video.title.lower() == video_title.lower():
                found_video = video

        if found_video:
            if self.current_user.age < 18 and found_video.adult_mode:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return

            print(f"Просмотр видео: {found_video.title}", found_video.duration)
            for second in range(0, found_video.duration):
                found_video.time_now = second
                print(f"Просмотр на {found_video.time_now} секунде.")
                t.sleep(1)
            print("Конец просмотра.")
            found_video.time_now = 0
        else:
            print("Видео не найдено.")





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
#ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')