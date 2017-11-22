import os

# !!!!!!!!!!!!!!! ES NECESARIO ANYADIR A LA VARIABLE PATH geckodriver

os.environ['TBB_PATH'] = '/home/kiko/TFG/libraries/geckodriver/tor-browser_en-US/'
from tbselenium.tbdriver import TorBrowserDriver
script_dir = os.path.dirname(__file__)
path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/tor-browser_en-US/')

with TorBrowserDriver(path) as driver:
    driver.get('https://check.torproject.org')