# django-storages-migrate

Install

Add to INSTALLED_APPS

```settings.py```
```python
INSTALLED_APPS = (
    ...

    'storages',
    'storages.commands',
)
```

Using
sync_media app -m model -f field [-r]

-r - optional - Remove local file after uploading into storage
```bash
./manage.py sync_media core -m User -f logo -r
```
