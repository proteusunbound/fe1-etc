"""Supports"""
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

supportlist = {
  "Leif": {"Nanna": 10, "None": 0},
  "Finn": {"Leif": 10, "Nanna": 10},
  "Osian": {"Eyvel": 10, "Tanya": 10},
  "Halvan": {"Eyvel": 10, "None": 0},
  "Eyvel": {"Leif": 10, "Mareeta": 10},
  "Dagdar": {"Eyvel": 10, "Tanya": 10},
  "Tanya": {"Osian": 10, "None": 0},
  "Marty": {"Dagdar": 10, "None": 0},
  "Ronan": {"Leif": 10, "None": 0},
  "Safy": {"Leif": 10, "Tina": 10},
  "Lifis": {"Safy": 10, "None": 0},
  "Machyua": {"Ced": 10, "None": 0},
  "Brighton": {"Machyua": 10, "None": 0},
  "Lara": {"Perne": 10, "None": 0},
  "Fergus": {"Karin": 10, "None": 0},
  "Karin": {"Fergus": 10, "Ced": 10},
  "Dalsin": {"Leif": 10, "None": 0},
  "Asbel": {"Leif": 10, "Ced": 10},
  "Nanna": {"Leif": 10, "Diarmuid": 10},
  "Hicks": {"Leif": 10, "None": 0},
  "Shiva": {"Safy": 10, "None": 0},
  "Carrion": {"Leif": 10, "Selphina": 10},
  "Selphina": {"Leif": 10, "Glade": 10},
  "Cain": {"Selphina": 10, "Glade": 10},
  "Alva": {"Selphina": 10, "Glade": 10},
  "Robert": {"Selphina": 10, "Glade": 10},
  "Fred": {"Olwen": 10, "None": 0},
  "Olwen": {"Leif": 10, "None": 0},
  "Mareeta": {"Eyvel": 10, "Galzus": 10},
  "Salem": {"Perne": 10, "Sara": 10},
  "Perne": {"Lara": 10, "None": 0},
  "Troude": {"Perne": 10, "None": 0},
  "Tina": {"Leif": 10, "Safy": 10},
  "Glade": {"Selphina": 20, "None": 0},
  "Deen": {"Eda": 10, "Linoan": 20},
  "Eda": {"Deen": 10, "None": 10},
  "Homer": {"Nanna": 10, "None": 0},
  "Linoan": {"Leif": 10, "Deen": 10},
  "Misha": {"Karin": 10, "None": 0},
  "Sara": {"Leif": 10, "None": 0},
  "Miranda": {"Leif": 10, "None": 0},
  "Xavier": {"Leif": 10, "None": 0},
  "Conomor": {"Miranda": 20, "None": 0},
  "Diarmuid": {"Nanna": 10, "None": 0},
  "Galzus": {"Mareeta": 20, "None": 0}
}
