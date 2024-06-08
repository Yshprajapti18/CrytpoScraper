# Scraping Assignment

I would have done the whole assignment but I have some work due from my college.

### A Django REST Framework API which will take in a list of crypto coin , scrape the data from the website, and return back the JSON response.

### Libraries to Use
- djangorestframework
- celery
- requests
- selenium

## API Endpoints

### 1. /api/taskmanager/start_scraping [POST]
This will take in a list payload `["Bitcoin", "Etherium", "Tether"]` which are names of the crypto coins and submit a scraping job (Celery will be used) to be run for these coins in parallel and return back a job ID.

### 2. /api/taskmanager/scraping_status/<job_id> [GET]
From the job_id received in the previous API, we can query this API and it will return the currently scraped data for that job.

### Sample Output
![Screenshot 2024-06-08 170423](https://github.com/Yshprajapti18/CrytpoScraper/assets/128960060/ac5c1d19-19e1-4f3a-938e-7476ad7e3853)
![Screenshot 2024-06-08 170359](https://github.com/Yshprajapti18/CrytpoScraper/assets/128960060/99a95e07-2596-4ecd-8758-6d3d9ccfb109)
