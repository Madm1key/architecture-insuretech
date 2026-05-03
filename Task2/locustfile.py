import logging
from locust import HttpUser, between, task
from locust.contrib.fasthttp import FastHttpUser

logger = logging.getLogger(__name__)


class WebsiteUser(FastHttpUser):
    """Load testing user that simulates real user behavior."""

    wait_time = between(1, 5)
    host = "http://scaletestapp:8080"

    @task
    def index(self) -> None:
        """Test GET request to the root endpoint."""
        try:
            response = self.client.get("/", timeout=5)
            if response.status_code != 200:
                logger.warning(f"Unexpected status code: {response.status_code}")
        except Exception as e:
            logger.error(f"Request failed: {e}")
