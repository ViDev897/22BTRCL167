# To run the FastAPI URL Shortener microservice:
# 1. Open a terminal in this backend folder.
# 2. Run the following command:
#
# uvicorn main:app --reload
#
# The API will be available at http://127.0.0.1:8000
#
# Example usage:
# POST http://127.0.0.1:8000/shorten with JSON {"url": "https://example.com"}
# GET http://127.0.0.1:8000/{short_code} to redirect.
