<<<<<<< HEAD
**Technologies used:**
- Python/Django + Celery
- PostgreSQL
- Redis
- Nginx

---

**Local development:**

To run the project without nginx (html5 games won't work)
```text
docker-compose up -d
```

To run the project with nginx (needed for html5 games support)
```text
docker-compose -f docker-compose.dev.yml up -d
```


---

A dump of dev.engageplaywin.com exist in db_dump directory. 

You might need to set the fcm tokens per user to null, you can run the following
in python manage.py shell_plus

```python
User.objects.all().update(web_fcm_token=None, app_fcm_token=None)
```

---

**DB ERD generation:**

```text
// with docker
docker-compose exec backend python manage.py graph_models -a > output.dot

// without docker
python manage.py graph_models -a > output.dot
```
This command will generate you a .dot file, which needs to be converted to an image file (.png).
```text
dot -T png output.dot -o schema.png
```

You need to install the dot converter, on mac os you can `brew install dot`.

---

**TODO before production:**
- move the edit profile input data like DoB and countries to the frontend
- update some api endpoints to follow REST standard
- switch from threads to celery in _with class
- Refactor some of the notifications without the @notify_when decorator
- add db indexes
- check queries joins for excess unneeded queries
- Refactor some of the queries, make use of Django's model manager
=======
# Engage
Engage Source Code
>>>>>>> 261e4ae744acf5effe2f6c6570b0798b662c789a
