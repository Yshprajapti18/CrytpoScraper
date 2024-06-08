# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScrapingJob, CoinData
from .tasks import scrape_coin_data

class StartScrapingView(APIView):
    def post(self, request):
        coins = request.data.get('coins', [])
        if not coins:
            return Response({"error": "No coins provided"}, status=status.HTTP_400_BAD_REQUEST)

        job = ScrapingJob.objects.create(coins=coins)
        for coin in coins:
            scrape_coin_data.delay(job.id, coin)

        return Response({"job_id": str(job.id)}, status=status.HTTP_202_ACCEPTED)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        try:
            job = ScrapingJob.objects.get(id=job_id)
        except ScrapingJob.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

        coin_data = CoinData.objects.filter(job=job)
        data = {
            "job_id": str(job.id),
            "status": job.status,
            "coins": [
                {
                    "coin": cd.coin,
                    "output": cd.data
                } for cd in coin_data
            ]
        }
        return Response(data, status=status.HTTP_200_OK)

