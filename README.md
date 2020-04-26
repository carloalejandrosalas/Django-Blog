# Blog made in Django
## First steps

1. Create *Virtual Environment*. Run the follow command in your terminal
```bash
virtualenv -p python3 env
```

2. Serve _Virtual environment_
```bash
source env/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure your setting.py inside (_Site folder_)  depending your Database configuration.


4. Migrate the DB
```
python manage.py migrate
```

5. Run the server
```
python manage.py runserver
```

Made with love by Carlo Salas