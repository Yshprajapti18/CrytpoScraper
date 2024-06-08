from celery import shared_task
from .scraper import CoinMarketCap
from .models import ScrapingJob, CoinData

@shared_task
def scrape_coin_data(job_id, coin_name):
    job = ScrapingJob.objects.get(id=job_id)
    scraper = CoinMarketCap(coin_name)
    try:
        data = scraper.scrape()
        CoinData.objects.create(
            job=job,
            coin=coin_name,
            data=data
        )
    except Exception as e:
        job.status = 'failed'
        job.save()
        raise e
    job.status = 'completed'
    job.save()

