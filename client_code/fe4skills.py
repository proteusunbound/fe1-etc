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
    "Dalvin": ["Follow-Up", "Vantage"],
    "Creidne": ["Follow-Up"],
    "Deimne": ["Follow-Up"],
    "Oifey": ["Follow-Up", "Critical"],
    "Julia": ["Follow-Up", "Nihil", "Adept"],
    "Hermina": ["Adept"],
    "Amid": ["Adept"],
    "Leif": ["Critical", "Adept"],
    "Shannan": ["Follow-Up", "Astra", "Adept"],
    "Daisy": ["Miracle"],
    "Ares": ["Follow-Up", "Adept", "Vantage"],
    "Linda": ["Wrath"],
    "Asaello": ["Follow-Up", "Accost"],
    "Hawk": ["Follow-Up", "Adept"],
    "Hannibal": ["Adept", "Vantage", "Pavise"],
    "Altena": ["Critical", "Adept"]
}
