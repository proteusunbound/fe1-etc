"""Skills"""
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

skill_list = {
    "Bordeaux": ["Pavise"],
    "Macbeth": ["Pavise"],
    "Chagall (Agusti)": ["Pavise"],
    "Jacobi": ["Follow-Up"],
    "Chagall (Sylvale)": ["Pavise"],
    "Myos": ["Pavise"],
    "Donovan": ["Pavise"],
    "Daccar": ["Pavise"],
    "Lombard": ["Pavise"],
    "Vaja": ["Adept"],
    "Reptor": ["Pavise"],
    "Harold": ["Pavise"],
    "Iucharba": ["Accost"],
    "Iuchar": ["Vantage"],
    "Danann": ["Pavise"],
    "Kutuzov": ["Follow-Up"],
    "Ishtore": ["Adept"],
    "Bramsel": ["Pavise"],
    "Bloom (Ulster)": ["Pavise"],
    "Bloom (Connacht)": ["Pavise"],
    "Maykov": ["Pavise"],
    "Kanatz": ["Pavise"],
    "Distler": ["Pavise"],
    "Judah": ["Follow-Up"],
    "Travant": ["Follow-Up", "Nihil", "Vantage"],
    "Hilda (Chronos)": ["Follow-Up"],
    "Riddell": ["Follow-Up", "Critical"],
    "Zagam": ["Follow-Up"],
    "Arvis": ["Nihil", "Pavise"],
    "Juphiel": ["Follow-Up"],
    "Brian": ["Follow-Up", "Accost"],
    "Hilda (Friege)": ["Follow-Up"],
    "Manfroy": ["Follow-Up", "Adept"],
    "Julius": ["Accost", "Nihil", "Wrath"],
    "Sigurd": ["Follow-Up"],
    "Naoise": ["Critical", "Accost"],
    "Alec": ["Follow-Up", "Nihil"],
    "Arden": ["Vantage"],
    "Lex": ["Vantage"],
    "Azelle": ["Follow-Up"],
    "Quan": ["Adept"],
    "Finn": ["Follow-Up", "Miracle"],
    "Ethlyn": ["Critical"],
    "Midir": ["Follow-Up", "Accost"],
    "Dew": ["Sol"],
    "Ayra": ["Follow-Up", "Nihil", "Astra"],
    "Deirdre": ["Nihil"],
    "Jamke": ["Follow-Up", "Accost", "Adept"],
    "Chulainn": ["Follow-Up", "Luna"],
    "Beowolf": ["Follow-Up", "Accost"],
    "Lewyn": ["Critical", "Adept"],
    "Silvia": ["Adept", "Miracle"],
    "Erinys": ["Follow-Up"],
    "Brigid": ["Follow-Up"],
    "Tailtiu": ["Wrath"],
    "Seliph": ["Follow-Up", "Nihil"],
    "Scathach": {
      "Chulainn": ["Follow-Up", "Nihil", "Astra", "Luna"],
      "Naoise": ["Accost", "Astra", "Critical", "Nihil", "Follow-Up"],
      "Alec": ["Astra", "Nihil", "Follow-Up"],
      "Arden": ["Astra", "Nihil", "Follow-Up", "Vantage"],
      "Azelle": ["Astra", "Nihil", "Follow-Up"],
      "Lex": ["Astra", "Nihil", "Follow-Up", "Vantage"],
      "Finn": ["Astra", "Miracle", "Nihil", "Follow-Up"],
      "Midir": ["Accost", "Astra", "Nihil", "Follow-Up"],
      "Dew": ["Astra", "Nihil", "Follow-Up", "Sol"],
      "Jamke": ["Accost", "Adept", "Astra", "Nihil", "Follow-Up"],
      "Beowolf": ["Accost", "Astra", "Nihil", "Follow-Up"],
      "Lewyn": ["Adept", "Astra", "Critical", "Nihil", "Follow-Up"],
      "Claud": ["Astra", "Nihil", "Follow-Up"]
    },
    "Dalvin": ["Follow-Up", "Vantage"],
    "Larcei": {
      "Chulainn": ["Follow-Up", "Nihil", "Astra", "Luna"],
      "Naoise": ["Accost", "Astra", "Critical", "Nihil", "Follow-Up"],
      "Alec": ["Astra", "Nihil", "Follow-Up"],
      "Arden": ["Astra", "Nihil", "Follow-Up", "Vantage"],
      "Azelle": ["Astra", "Nihil", "Follow-Up"],
      "Lex": ["Astra", "Nihil", "Follow-Up", "Vantage"],
      "Finn": ["Astra", "Miracle", "Nihil", "Follow-Up"],
      "Midir": ["Accost", "Astra", "Nihil", "Follow-Up"],
      "Dew": ["Astra", "Nihil", "Follow-Up", "Sol"],
      "Jamke": ["Accost", "Adept", "Astra", "Nihil", "Follow-Up"],
      "Beowolf": ["Accost", "Astra", "Nihil", "Follow-Up"],
      "Lewyn": ["Adept", "Astra", "Critical", "Nihil", "Follow-Up"],
      "Claud": ["Astra", "Nihil", "Follow-Up"]
    },
    "Creidne": ["Follow-Up"],
    "Lana": {
      "Jamke": ["Accost", "Adept"],
      "Naoise": ["Accost", "Critical"],
      "Alec": ["Nihil", "Follow-Up"],
      "Arden": ["Vantage"],
      "Azelle": ["Follow-Up"],
      "Lex": ["Vantage"],
      "Finn": ["Miracle", "Follow-Up"],
      "Midir": ["Accost", "Follow-Up"],
      "Dew": [],
      "Chulainn": [],
      "Beowolf": ["Accost", "Follow-Up"],
      "Lewyn": ["Adept", "Critical"],
      "Claud": []
    },
    "Diarmuid": {
      "Beowolf": ["Follow-Up", "Accost"],
      "Naoise": ["Accost", "Critical"],
      "Alec": ["Nihil", "Follow-Up"],
      "Arden": ["Vantage"],
      "Azelle": ["Follow-Up"],
      "Lex": ["Vantage"],
      "Finn": ["Miracle", "Follow-Up"],
      "Midir": ["Accost", "Follow-Up"],
      "Dew": [],
      "Jamke": ["Accost", "Adept"],
      "Chulainn": [],
      "Lewyn": ["Adept", "Critical"],
      "Claud": []
    },
    "Lester": {
      "Jamke": ["Accost", "Adept"],
      "Naoise": ["Accost", "Critical"],
      "Alec": ["Nihil", "Follow-Up"],
      "Arden": ["Vantage"],
      "Azelle": ["Follow-Up"],
      "Lex": ["Vantage"],
      "Finn": ["Miracle", "Follow-Up"],
      "Midir": ["Accost", "Follow-Up"],
      "Dew": [],
      "Chulainn": [],
      "Beowolf": ["Accost", "Follow-Up"],
      "Lewyn": ["Adept", "Critical"],
      "Claud": []
    },
    "Deimne": ["Follow-Up"],
    "Oifey": ["Follow-Up", "Critical"],
    "Julia": ["Follow-Up", "Nihil", "Adept"],
    "Fee": {
      "Lewyn": ["Follow-Up", "Critical", "Adept"],
      "Naoise": ["Accost", "Critical", "Follow-Up"],
      "Alec": ["Nihil", "Follow-Up"],
      "Arden": ["Follow-Up", "Vantage"],
      "Azelle": ["Follow-Up"],
      "Lex": ["Follow-Up", "Vantage"],
      "Finn": ["Miracle", "Follow-Up"],
      "Midir": ["Accost", "Follow-Up"],
      "Dew": ["Follow-Up"],
      "Jamke": ["Accost", "Adept", "Follow-Up"],
      "Chulainn": ["Follow-Up"],
      "Beowolf": ["Accost", "Follow-Up"],
      "Claud": ["Follow-Up"]
    },
    "Hermina": ["Adept"],
    "Arthur": {
      "Azelle": ["Follow-Up", "Wrath"],
      "Naoise": ["Accost", "Critical", "Wrath"],
      "Alec": ["Nihil", "Follow-Up", "Wrath"],
      "Arden": ["Vantage", "Wrath"],
      "Lex": ["Vantage", "Wrath"],
      "Finn": ["Miracle", "Follow-Up", "Wrath"],
      "Midir": ["Accost", "Follow-Up", "Wrath"],
      "Dew": ["Wrath"],
      "Jamke": ["Accost", "Adept", "Wrath"],
      "Chulainn": ["Wrath"],
      "Beowolf": ["Accost", "Follow-Up", "Wrath"],
      "Lewyn": ["Adept", "Critical", "Wrath"],
      "Claud": ["Wrath"]
    },
    "Amid": ["Adept"],
    "Leif": ["Critical", "Adept"],
    "Nanna": {
      "Beowolf": ["Follow-Up", "Accost"],
      "Naoise": ["Accost", "Critical"],
      "Alec": ["Nihil", "Follow-Up"],
      "Arden": ["Vantage"],
      "Azelle": ["Follow-Up"],
      "Lex": ["Vantage"],
      "Finn": ["Miracle", "Follow-Up"],
      "Midir": ["Accost", "Follow-Up"],
      "Dew": [],
      "Jamke": ["Accost", "Adept"],
      "Chulainn": [],
      "Lewyn": ["Adept", "Critical"],
      "Claud": []
    },
    "Shannan": ["Follow-Up", "Astra", "Adept"],
    "Patty": {
      "Midir": ["Follow-Up", "Accost"],
      "Naoise": ["Accost", "Critical"],
      "Alec": ["Nihil", "Follow-Up"],
      "Arden": ["Vantage"],
      "Azelle": ["Follow-Up"],
      "Lex": ["Vantage"],
      "Finn": ["Miracle", "Follow-Up"],
      "Dew": ["Sol"],
      "Jamke": ["Accost", "Adept"],
      "Chulainn": ["Luna"],
      "Beowolf": ["Accost", "Follow-Up"],
      "Lewyn": ["Adept", "Critical"],
      "Claud": []
    },
    "Daisy": ["Miracle"],
    "Ares": ["Follow-Up", "Adept", "Vantage"],
    "Lene": {
      "Claud": ["Adept", "Miracle"],
      "Naoise": ["Accost", "Adept", "Critical", "Miracle"],
      "Alec": ["Adept", "Miracle", "Nihil", "Follow-Up"],
      "Arden": ["Adept", "Miracle", "Vantage"],
      "Azelle": ["Adept", "Miracle", "Follow-Up"],
      "Lex": ["Adept", "Miracle", "Vantage"],
      "Finn": ["Adept", "Miracle", "Follow-Up"],
      "Midir": ["Accost", "Adept", "Miracle", "Follow-Up"],
      "Dew": ["Adept", "Miracle", "Sol"],
      "Jamke": ["Accost", "Adept", "Miracle"],
      "Chulainn": ["Adept", "Luna", "Miracle"],
      "Beowolf": ["Accost", "Adept", "Miracle", "Follow-Up"],
      "Lewyn": ["Adept", "Critical", "Miracle"]
    },
    "Tine": {
      "Azelle": ["Follow-Up", "Wrath"],
      "Naoise": ["Accost", "Critical", "Wrath"],
      "Alec": ["Nihil", "Follow-Up", "Wrath"],
      "Arden": ["Vantage", "Wrath"],
      "Lex": ["Vantage", "Wrath"],
      "Finn": ["Miracle", "Follow-Up", "Wrath"],
      "Midir": ["Accost", "Wrath"],
      "Dew": ["Wrath"],
      "Jamke": ["Accost", "Adept", "Wrath"],
      "Chulainn": ["Wrath"],
      "Beowolf": ["Accost", "Follow-Up", "Wrath"],
      "Lewyn": ["Adept", "Critical", "Wrath"],
      "Claud": ["Wrath"]
    },
    "Linda": ["Wrath"],
    "Febail": {
      "Midir": ["Follow-Up", "Accost"],
      "Naoise": ["Accost", "Critical", "Follow-Up"],
      "Alec": ["Nihil", "Follow-Up"],
      "Arden": ["Follow-Up", "Vantage"],
      "Azelle": ["Follow-Up"],
      "Lex": ["Follow-Up", "Vantage"],
      "Finn": ["Miracle", "Follow-Up"],
      "Dew": ["Follow-Up"],
      "Jamke": ["Accost", "Adept", "Follow-Up"],
      "Chulainn": ["Follow-Up"],
      "Beowolf": ["Accost", "Follow-Up"],
      "Lewyn": ["Adept", "Critical", "Follow-Up"],
      "Claud": ["Follow-Up"]
    },
    "Asaello": ["Follow-Up", "Accost"],
    "Ced": {
      "Lewyn": ["Follow-Up", "Critical", "Adept"],
      "Naoise": ["Accost", "Adept", "Critical", "Follow-Up"],
      "Alec": ["Adept", "Nihil", "Follow-Up"],
      "Arden": ["Adept", "Follow-Up", "Vantage"],
      "Azelle": ["Adept", "Follow-Up"],
      "Lex": ["Adept", "Follow-Up", "Vantage"],
      "Finn": ["Adept", "Miracle", "Follow-Up"],
      "Midir": ["Accost", "Adept", "Follow-Up"],
      "Dew": ["Adept", "Follow-Up"],
      "Jamke": ["Accost", "Adept", "Follow-Up"],
      "Chulainn": ["Adept", "Follow-Up"],
      "Beowolf": ["Accost", "Adept", "Follow-Up"],
      "Claud": ["Adept", "Follow-Up"]
    },
    "Hawk": ["Follow-Up", "Adept"],
    "Hannibal": ["Adept", "Vantage", "Pavise"],
    "Coirpre": {
      "Claud": ["Adept", "Miracle"],
      "Naoise": ["Accost", "Adept", "Critical", "Miracle"],
      "Alec": ["Adept", "Miracle", "Nihil", "Follow-Up"],
      "Arden": ["Adept", "Miracle", "Vantage"],
      "Azelle": ["Adept", "Miracle", "Follow-Up"],
      "Lex": ["Adept", "Miracle", "Vantage"],
      "Finn": ["Adept", "Miracle", "Follow-Up"],
      
    },
    "Altena": ["Critical", "Adept"]
}
