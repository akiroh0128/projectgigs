{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "58265b7b-06e6-4924-a40d-6333b002b036",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import selenium\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "from time import sleep\n",
    "driver_path=\"/usr/bin.chromedriver\"\n",
    "driver=webdriver.Chrome()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1bc6210a-69cc-4e91-8e0e-ff1a2ad4b4ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "articles=[]\n",
    "def scrapper(start_index,element):\n",
    "    continue_scraping = True\n",
    "    while(True):\n",
    "        print(len(articles))\n",
    "        driver.get(\"https://indianexpress.com/section/business/?utm_source=google&utm_medium=paid&utm_campaign=allaccess&gad_source=1&gclid=CjwKCAjwmYCzBhA6EiwAxFwfgMwWQPSaQ3-_mIij5ghNYh-md2dTiHT8vUoPzu7rbtVkYLsU67HU8hoCLcQQAvD_BwE\")\n",
    "        sleep(4)\n",
    "        try:\n",
    "            temp = {}\n",
    "            driver.find_element(by=By.XPATH, value=f'/html/body/div[{element}]/div[5]/div/div/div[3]/div[3]/div[{3+start_index}]/div[2]/h2/a').click()\n",
    "            sleep(2)\n",
    "            temp[\"title\"] = driver.find_element(by=By.XPATH, value=f'/html/body/div[2]/div[5]/div/div[1]/div/h1').text\n",
    "            temp[\"Published\"] = driver.find_element(by=By.XPATH, value=f'/html/body/div[2]/div[5]/div/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/span').text\n",
    "            temp[\"Author\"] = driver.find_element(by=By.XPATH, value=f'/html/body/div[2]/div[5]/div/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a').text\n",
    "            temp[\"Context\"] = driver.find_element(by=By.XPATH, value=f'/html/body/div[2]/div[5]/div/div[2]/div[1]/div/div/div/div/div[2]/p[1]').text\n",
    "            articles.append(temp)\n",
    "            start_index += 1\n",
    "            continue_scraping = True\n",
    "\n",
    "        except:\n",
    "            try:\n",
    "                temp[\"title\"] = driver.find_element(by=By.XPATH, value=f'/html/body/div[3]/div[5]/div/div[1]/div/h1').text\n",
    "                temp[\"Published\"] = driver.find_element(by=By.XPATH, value=f'/html/body/div[3]/div[5]/div/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/span').text\n",
    "                temp[\"Author\"] = driver.find_element(by=By.XPATH, value=f'/html/body/div[3]/div[5]/div/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a').text\n",
    "                temp[\"Context\"] = driver.find_element(by=By.XPATH, value=f'/html/body/div[3]/div[5]/div/div[2]/div[1]/div/div/div/div/div[2]/p[1]').text\n",
    "                articles.append(temp)\n",
    "                start_index += 1\n",
    "                continue_scraping = True\n",
    "            except:\n",
    "                start_index += 1\n",
    "                if(not continue_scraping):\n",
    "                    return \n",
    "                continue_scraping = False\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cdfd33a0-27c5-4c20-a8d3-7143fd99c9f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "3\n",
      "4\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "scrapper(0,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "2c56cc32-f114-4bce-bed5-97d8ed3edaf9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Market rebounds: Sensex rises 3.2%, Nifty closes above 22,600',\n",
       "  'Published': 'June 5, 2024 21:42 IST',\n",
       "  'Author': 'Hitesh Vyas',\n",
       "  'Context': 'A day after witnessing the worst trading session in four years, benchmark indices, the Sensex and the Nifty recovered nearly half of their losses on Wednesday after they rose over 3 per cent.'},\n",
       " {'title': 'Big Mac battle: McDonald’s loses European Union trademark fight with Irish rival Supermac’s',\n",
       "  'Published': 'Updated: June 5, 2024 21:40 IST',\n",
       "  'Author': 'AP',\n",
       "  'Context': 'McDonald’s lost a European Union trademark dispute over the Big Mac name after a top European Union court sided Wednesday with Irish fast food rival Supermac’s in a long-running legal battle.'},\n",
       " {'title': 'Market rebounds: Sensex rises 3.2%, Nifty closes above 22,600',\n",
       "  'Published': 'June 5, 2024 21:42 IST',\n",
       "  'Author': 'Hitesh Vyas',\n",
       "  'Context': 'A day after witnessing the worst trading session in four years, benchmark indices, the Sensex and the Nifty recovered nearly half of their losses on Wednesday after they rose over 3 per cent.'},\n",
       " {'title': 'Big Mac battle: McDonald’s loses European Union trademark fight with Irish rival Supermac’s',\n",
       "  'Published': 'Updated: June 5, 2024 21:40 IST',\n",
       "  'Author': 'AP',\n",
       "  'Context': 'McDonald’s lost a European Union trademark dispute over the Big Mac name after a top European Union court sided Wednesday with Irish fast food rival Supermac’s in a long-running legal battle.'},\n",
       " {'title': 'Indian carrier Akasa Air expects Boeing 737 MAX 10 deliveries by 2027',\n",
       "  'Published': 'Updated: June 5, 2024 20:22 IST',\n",
       "  'Author': 'Reuters',\n",
       "  'Context': 'Indian carrier Akasa Air expects deliveries of Boeing’s 737 MAX 10 planes by the summer of 2027, Akasa’s chief executive officer Vinay Dube told Reuters on the sidelines of an industry event on Wednesday.'},\n",
       " {'title': 'Air India Express to operate 28 weekly flights from Ghaziabad’s Hindon airport from August',\n",
       "  'Published': 'June 5, 2024 17:18 IST',\n",
       "  'Author': 'Sukalp Sharma',\n",
       "  'Context': 'Air India Express on Wednesday announced that it will start flights from Ghaziabad’s Hindon Airport, which will make it the only carrier to operate from two airports in the National Capital Region (NCR). The airline, which is a subsidiary of Air India, will operate a total of 28 direct flights between Hindon and Bengaluru, Goa, and Kolkata from August 1, the carrier said in a release.'},\n",
       " {'title': 'Sensex inches 2.46% higher, Nifty gains 560 points in morning trade',\n",
       "  'Published': 'Updated: June 5, 2024 14:13 IST',\n",
       "  'Author': 'Hitesh Vyas',\n",
       "  'Context': 'A day after the announcement of the Lok Sabha elections, domestic stock market indices Sensex and Nifty, which opened nearly 1 per cent higher on Wednesday (May 5), extended gains in the morning trade.'}]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "articles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "79dc715b-6eb1-4153-a9fd-fe21292da3d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "48f42b65-ed25-4a02-8761-6aed5b0d8f9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x76cea759ac40>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "connection = sqlite3.connect('articles.db')\n",
    "cursor = connection.cursor()\n",
    "cursor.execute(\"CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,author TEXT,publication_date TEXT NOT NULL,content TEXT NOT NULL)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6ec7ec06-da84-4acd-856f-cda6f5a0eb64",
   "metadata": {},
   "outputs": [],
   "source": [
    "for article in articles:\n",
    "    cursor.execute('''\n",
    "            INSERT INTO articles (title, author, publication_date, content)\n",
    "            VALUES (?, ?, ?, ?)\n",
    "        ''', (article[\"title\"], article[\"Author\"], article[\"Published\"], article[\"Context\"]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "372f583d-15de-40f2-a972-9ec573b76c4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "connection.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5a56200b-5e31-425a-abee-ab037053fd78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 'Markets extend winning momentum to 2nd day running', 'PTI', 'June 6, 2024 11:57 IST', 'Benchmark equity indices Sensex and Nifty began the trade on a buoyant note on Thursday, continuing to rally for the second day running, after leaders of the BJP-led National Democratic Alliance (NDA) unanimously elected Narendra Modi as their leader.')\n",
      "(2, 'Markets extend winning momentum to 2nd day running', 'PTI', 'June 6, 2024 11:57 IST', 'Benchmark equity indices Sensex and Nifty began the trade on a buoyant note on Thursday, continuing to rally for the second day running, after leaders of the BJP-led National Democratic Alliance (NDA) unanimously elected Narendra Modi as their leader.')\n",
      "(3, 'India’s tech manufacturing map may get a makeover with TDP as key NDA player', 'Soumyarendra Barik', 'Updated: June 6, 2024 08:42 IST', 'He is known to be a man invested in technology, and is widely credited for turning Hyderabad into a technology hub. Even in his party’s largely welfare-oriented manifesto, there were mentions of encouraging artificial intelligence in a largely agrarian state. And in 2024, N Chandrababu Naidu and his Telugu Desam Party (TDP) could have one more tryst with technology – with the coastal state of Andhra Pradesh potentially emerging as a new manufacturing destination.')\n",
      "(4, 'BJP’s vote share shrinks in most states with low growth rates in per capita income', 'Sukalp Sharma', 'Updated: June 6, 2024 12:25 IST', 'The Bharatiya Janata Party’s (BJP’s) vote share in the 2024 general election contracted in most of the states and union territories (UTs) that had relatively low rates of growth in per capita income since the previous Lok Sabha polls in 2019, shows an analysis of Election Commission of India (ECI) data and per capita net state domestic product (NSDP) data from states. NSDP per capita is taken as the per capita income of a state and is counted among states’ key economic indicators.')\n",
      "(5, 'Tier-II cities continue to witness consistent growth in hiring activities: Report', 'PTI', 'June 5, 2024 21:59 IST', 'Hiring in tier-II cities showed consistent growth trends compared to metropolitan areas during May, mainly led by cities such as Kochi, Coimbatore, and Jaipur, which have emerged as key hiring locations, a report said on Wednesday.')\n",
      "(6, 'Big Mac battle: McDonald’s loses European Union trademark fight with Irish rival Supermac’s', 'AP', 'Updated: June 5, 2024 21:40 IST', 'McDonald’s lost a European Union trademark dispute over the Big Mac name after a top European Union court sided Wednesday with Irish fast food rival Supermac’s in a long-running legal battle.')\n",
      "(7, 'Indian carrier Akasa Air expects Boeing 737 MAX 10 deliveries by 2027', 'Reuters', 'Updated: June 5, 2024 20:22 IST', 'Indian carrier Akasa Air expects deliveries of Boeing’s 737 MAX 10 planes by the summer of 2027, Akasa’s chief executive officer Vinay Dube told Reuters on the sidelines of an industry event on Wednesday.')\n",
      "(8, 'Air India Express to operate 28 weekly flights from Ghaziabad’s Hindon airport from August', 'Sukalp Sharma', 'June 5, 2024 17:18 IST', 'Air India Express on Wednesday announced that it will start flights from Ghaziabad’s Hindon Airport, which will make it the only carrier to operate from two airports in the National Capital Region (NCR). The airline, which is a subsidiary of Air India, will operate a total of 28 direct flights between Hindon and Bengaluru, Goa, and Kolkata from August 1, the carrier said in a release.')\n",
      "(9, 'Sensex inches 2.46% higher, Nifty gains 560 points in morning trade', 'Hitesh Vyas', 'Updated: June 5, 2024 14:13 IST', 'A day after the announcement of the Lok Sabha elections, domestic stock market indices Sensex and Nifty, which opened nearly 1 per cent higher on Wednesday (May 5), extended gains in the morning trade.')\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"SELECT * FROM articles\")\n",
    "rows = cursor.fetchall()\n",
    "for row in rows:\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d820617-de5f-4680-a705-1acbf6a8aa32",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
