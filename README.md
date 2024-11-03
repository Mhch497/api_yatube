<h1 align="center">CRUD для Yatube</h1>

<h2>Оглавление</h2>

1. [Об авторе](#me)

1. [О программе](#programm)

1. [Как установить](#install)


## <a name="me">Об авторе</a>

<h3>Привет! Меня зовут Мария</h3>
<p>Я занимаюсь программированием уже больше 4 лет. В моем арсенале:</p>
<div>
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/lua-%232C2D72.svg?style=for-the-badge&logo=lua&logoColor=white">
<img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E">
<img src="https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white">
<img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white">
<img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
<img src="https://github.com/Mhch497/the_snake/assets/55291670/cb8309ba-5a85-40c1-ae28-291713f0609d" width="35px" height="35px">
</div>
<p>Я также являюсь преподавателем программирования в международной школе математики и программирования Алгоритмика</p>
<img src="https://static.tildacdn.com/tild6661-3330-4861-b630-663534303033/Logo1.svg"  height="35px"/>

## <a name="programm">О программе</a>

<p><b>Yatube</b> — это платформа для блогов, чем-то похожая на Блогикум. Все блоги чем-то похожи друг на друга: любой блог-сервис предполагает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.</p>

<h3>Эндпоинты:</h3>
<ul>
  <li>api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.</li>
  <li>api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.</li>
  <li>api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост с идентификатором{post_id}.</li>
  <li>api/v1/groups/ (GET): получаем список всех групп.</li>
  <li>api/v1/groups/{group_id}/ (GET): получаем информацию о группе с идентификатором {group_id}.</li>
  <li>api/v1/posts/{post_id}/comments/
<ol type="square">
  <li>(GET): получаем список всех комментариев поста с идентификатором post_id</li>
  <li>(POST): создаём новый комментарий для поста с идентификатором {post_id}.</li></ol></li>
  <li>api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий с идентификатором {comment_id} в посте с id=post_id.</li>
</ul>

## <a name="install">Как установить</a>

<p>Клонировать репозиторий</p>

`git clone https://github.com/Mhch497/api_yatube.git`

<p>Перейти в папку</p>

`cd .\api_yatube\`

<p>Установить зависимости</p>

`pip install -r requirements.txt`

<p>Выполнить миграции:</p>

`python3 manage.py migrate`

<p>Запустить проект:</p>

`python3 manage.py runserver`
