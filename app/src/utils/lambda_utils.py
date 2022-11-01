from src.utils.enums.env_var import EnvVar


class LambdaUtils:

    @staticmethod
    def get_url_base_api_imdb() -> str:
        return EnvVar.URL_BASE_API_IMDB.value

    @staticmethod
    def get_api_key() -> str:
        return EnvVar.API_KEY.value
