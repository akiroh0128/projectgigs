{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7995b282",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Extracted 165 articles and saved to /home/rohith-kumar/Downloads/articles.csv\n"
     ]
    }
   ],
   "source": [
    "import fitz  \n",
    "import pandas as pd\n",
    "import re\n",
    "\n",
    "def extract_text_from_pdf(pdf_path):\n",
    "    pdf_document = fitz.open(pdf_path)\n",
    "    articles = []\n",
    "\n",
    "    article_number_pattern = re.compile(r'^\\d+\\.\\d+\\.')  \n",
    "    current_article = {\"s_no\": \"\", \"article_title\": \"\", \"article_body\": \"\"}\n",
    "    collecting_body = False\n",
    "\n",
    "    for page_num in range(6,len(pdf_document)):\n",
    "        page = pdf_document[page_num]\n",
    "        text = page.get_text(\"text\").encode(\"utf-8-sig\").decode(\"utf-8-sig\")\n",
    "        lines = text.splitlines()\n",
    "\n",
    "        for line in lines:\n",
    "            line = line.strip()\n",
    "            if article_number_pattern.match(line):\n",
    "                if collecting_body and current_article[\"s_no\"]:  \n",
    "                    articles.append(current_article)\n",
    "\n",
    "                parts = line.split('.', 2)\n",
    "                current_article = {\"s_no\": f\"{parts[0]}.{parts[1]}.\", \"article_title\": parts[2].strip('\" '), \"article_body\": \"\"}\n",
    "                collecting_body = True\n",
    "            elif collecting_body:\n",
    "                if current_article[\"article_body\"]:\n",
    "                    current_article[\"article_body\"] += \"\\n\" + line\n",
    "                else:\n",
    "                    current_article[\"article_body\"] = line\n",
    "\n",
    "    if current_article[\"s_no\"]:  \n",
    "        articles.append(current_article)\n",
    "\n",
    "    return [article for article in articles if float(article['s_no'][:-1]) <= 11.11] \n",
    "\n",
    "def save_to_csv(articles, csv_path):\n",
    "    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:\n",
    "        file.write('s_no,article_title,article_body\\n')  # Write header\n",
    "        \n",
    "        for article in articles:\n",
    "            s_no = article[\"s_no\"]\n",
    "            article_title = f'\"{article[\"article_title\"].replace(\"\\\"\", \"\\\"\\\"\")}\"'  \n",
    "            article_body = f'\"{article[\"article_body\"].replace(\"\\\"\", \"\\\"\\\"\")}\"'  \n",
    "            \n",
    "            file.write(f'{s_no},{article_title},{article_body}\\n')\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    pdf_path = \"/home/rohith-kumar/Downloads/VisionIAS Monthly Current Affairs January 2024 January 2024.pdf\"  # Update this to the path of your PDF file\n",
    "    csv_path = \"/home/rohith-kumar/Downloads/articles.csv\" # Update this to the desired CSV file path\n",
    "\n",
    "    articles = extract_text_from_pdf(pdf_path)\n",
    "    save_to_csv(articles, csv_path)\n",
    "\n",
    "    print(f\"Extracted {len(articles)} articles and saved to {csv_path}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dfbbe795-1454-4053-bea5-2589e8195ffa",
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
