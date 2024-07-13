from django.apps import AppConfig

class SellerPageConfig(AppConfig):
    name = 'seller_page'  # Ensure this matches your app name

    def ready(self):
        import seller_page.signals  # Ensure this matches your app name