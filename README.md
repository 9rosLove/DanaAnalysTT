# Python Data Scraping and Processing Projects
This repository contains three Python projects focusing on data scraping and processing tasks using various libraries and tools.

## 🔧 Installing using GitHub
1. Clone the repository from GitHub:
    ```bash
    git clone htthps://github.com/9rosLove/DanaAnalysTT.git
    cd social-network
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate a virtual enviroment:
    - For Windows🪟:
    ```bash
    .\venv\Scripts\activate
    ```
    - For Linux🐧 and MacOS🍏:
    ```bash
    source venv/bin/activate
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set the environment variables:
    
   - For Linux🐧 and MacOS🍏
   ```bash
    export GOOGLE_APPLICATION_CREDENTIALS=<path to google credentials>
    export EMAIL=<your email>
                    ...
    ```
    - For Windows🪟
    ```shell
    set GOOGLE_APPLICATION_CREDENTIALS=<path to google credentials>
    set EMAIL=<your email>
                    ...
    ```
5. Move "credentials.json" into the project folder.

## Task 1: Image Extension Parser
**Description:** This task involves building a Python script to parse image extensions from a webpage and set it to the spreadsheet.

***[Solution](https://docs.google.com/spreadsheets/d/1aY7jnhUV1HI6PkzyXcXnBlec9bSrNGoLdzl9YPip6cY/edit?gid=1902149593#gid=1902149593)***

## Task 2: Concurrent Data Transfer Pipeline
**Description:**
This project implements a simple concurrent data transfer pipeline in Python. It involves:
- Concurrently querying Google Analytics API to retrieve selective data.
- Merging the retrieved data into a single DataFrame.
- Grouping and aggregating the data into multiple DataFrames.
- Concurrently writing the DataFrames to Google Sheets, each on a separate sheet.

***[Solution](https://docs.google.com/spreadsheets/d/16X7iiNj3CZTcI5mMbLrjtsMY8vklBswNIlo7YWWjYRo/edit?gid=2017030212#gid=2017030212)***
 
## Task 3: Selenium Web Scraping
**Description:**
This project demonstrates web scraping using Selenium, focusing on extracting real estate listings from the OLX catalog. It scrapes data such as price, floor, storey count, locality, and area. The extracted data is structured and written to a Google Sheet.

***[Solution](https://docs.google.com/spreadsheets/d/1-sqtZ5RA717Xqt4yW5iRuDZa17-ZNjwRVSGPinOyYbs/edit?gid=1448728758#gid=1448728758)***