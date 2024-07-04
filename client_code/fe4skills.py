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
    "Larcei": ["Follow-Up", "Nihil", "Astra", "Luna"],
    "Creidne": ["Follow-Up"],
    "Lana": ["Accost", "Adept"],
    "Diarmuid": ["Follow-Up", "Accost"],
    "Lester": ["Accost", "Adept"],
    "Deimne": ["Follow-Up"],
    "Oifey": ["Follow-Up", "Critical"],
    "Julia": ["Follow-Up", "Nihil", "Adept"],
    "Fee": ["Follow-Up", "Critical", "Adept"],
    "Hermina": ["Adept"],
    "Arthur": ["Follow-Up", "Wrath"],
    "Amid": ["Adept"],
    "Leif": ["Critical", "Adept"],
    "Nanna": ["Follow-Up", "Accost"],
    "Shannan": ["Follow-Up", "Astra", "Adept"],
    "Patty": ["Follow-Up", "Accost"],
    "Daisy": ["Miracle"],
    "Ares": ["Follow-Up", "Adept", "Vantage"],
    "Lene": ["Adept", "Miracle"],
    "Tine": ["Follow-Up", "Wrath"],
    "Linda": ["Wrath"],
    "Febail": ["Follow-Up", "Accost"],
    "Asaello": ["Follow-Up", "Accost"],
    "Ced": ["Follow-Up", "Critical", "Adept"],
    "Hawk": ["Follow-Up", "Adept"],
    "Hannibal": ["Adept", "Vantage", "Pavise"],
    "Coirpre": ["Adept", "Miracle"],
    "Altena": ["Critical", "Adept"]
}
