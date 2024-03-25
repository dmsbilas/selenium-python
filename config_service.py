class ConfigService:
    _config_file = 'config.json';
    _instance = None;


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def get_config(self):
        return self.read_config_json();

    def read_config_json(self):
        import json;
        with open(self._config_file, 'r') as file:
            # Load the JSON content from the file
            data = json.load(file);
        return data;




