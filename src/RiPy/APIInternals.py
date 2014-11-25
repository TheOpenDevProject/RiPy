__author__ = 'TheOpenDevProject'

class APIInternalsCore:
        APIResponse = {400: "(400)Riot API - Bad Request",
                   401: "(401)Riot API - Unauthorized (Your API key was invalid or you tried to access an invalid URL)",
                   404: "(404)Riot API - Not Found",
                   429: "(429)Riot API - Rate Limit Exceeded",
                   500: "(500)Riot API - Internal Server Error (AKA Riot swung a wrecking ball into the API server)",
                   503: "(503)Riot API - Service Unavailable"
                    }