import logging
from dataclasses import dataclass
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from config import BASE_URL


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@dataclass
class Apartment:
    # title: str
    price: int
    currency: str
    floor: int
    floors: int
    area_sqm: float
    location: str
    url: str


def get_max_pages(driver: webdriver.Firefox) -> int:
    if pages := driver.find_elements(By.CLASS_NAME, "css-1mi714g"):
        num_pages = int(pages[-1].text)

        return num_pages

    return 1


def get_num_apartments(driver: webdriver.Firefox) -> tuple[bool, int | str]:
    apartments_num_message = driver.find_element(
        By.CLASS_NAME,
        "css-7ddzao"
    ).text.split(" ")

    if len(apartments_num_message) < 6:
        if num := int(apartments_num_message[-2]) > 0:
            return True, num

        raise Exception("No apartments found")

    return True, "More than 1000"


def get_apartments_urls(driver: webdriver, num_pages: int) -> set:
    apartment_urls = []

    parsed_url = urlparse(BASE_URL)
    query_params = parse_qs(parsed_url.query)

    for page_num in range(1, num_pages + 1):
        query_params["page"] = page_num
        updated_query = urlencode(query_params, doseq=True)
        updated_url = urlunparse(parsed_url._replace(query=updated_query))

        logger.info(f"Getting page: {updated_url}")

        driver.get(updated_url)
        apartment_urls.extend(
            element.get_attribute("href")
            for element in driver.find_elements(By.CLASS_NAME, "css-z3gu2d")
        )

    return set(apartment_urls)


def parse_extra_info(driver: webdriver) -> dict:
    return {
        element.text.split(": ")[0]: element.text.split(": ")[1]
        for element in driver.find_elements(
            By.CSS_SELECTOR, ".css-b5m1rv.er34gjf0"
        )
        if ":" in element.text
    }


def parse_integer(input_text: str | list) -> int:
    modified_input = (
        "".join(input_text)
        if isinstance(input_text, list)
        else input_text.replace(" ", "")
    )

    if "." in modified_input:
        modified_input = float(modified_input)

    return int(modified_input)


def parse_single_apartment(driver: webdriver, apartment_url: str, num: int) -> Apartment:
    logger.info(f"Parsing apartment number {num}: {apartment_url}")

    driver.get(apartment_url)

    extra_info = parse_extra_info(driver)

    return Apartment(
        # title=driver.find_element(By.CSS_SELECTOR, ".css-1juynto").text,
        price=parse_integer(
            driver.find_element(
                By.CSS_SELECTOR,
                ".css-12vqlj3").text.split(" ")[:-1]
        ),
        currency=driver.find_element(
            By.CSS_SELECTOR,
            ".css-12vqlj3"
        ).text.split(" ")[-1],
        floor=parse_integer(extra_info.get("Поверх")),
        floors=parse_integer(extra_info.get("Поверховість")),
        area_sqm=float(extra_info.get("Загальна площа").split(" ")[0]),
        location=driver.find_element(
            By.CSS_SELECTOR,
            ".css-1cju8pu.er34gjf0"
        ).text,
        url=apartment_url
    )


def parse_all_apartments(
    driver: webdriver, apartment_urls: set[str]
) -> list[Apartment]:
    logging.info(f"Parsing {len(apartment_urls)} apartments")

    apartments = [
        parse_single_apartment(driver, url, num + 1)
        for num, url in enumerate(apartment_urls)
    ]

    return apartments


def get_all_apartments(num_pages: int = None) -> list[Apartment]:
    options = Options()
    options.add_argument("--headless")

    logger.info("Getting webdriver...")

    with webdriver.Firefox(options=options) as driver:
        driver.get(BASE_URL)
        is_success, msg = get_num_apartments(driver)

        logging.info(f"Apartments found: {msg}")

        max_pages = get_max_pages(driver)
        logger.info(f"Pages found: {max_pages}")

        if not num_pages:
            num_pages = max_pages

        if max_pages < num_pages < 1:
            raise ValueError(
                f"Number of pages must be in range from 1 to {max_pages}"
            )

        apartment_urls = get_apartments_urls(driver, num_pages)
        apartments = parse_all_apartments(driver, apartment_urls)

        logger.info("Done!")

    return apartments


if __name__ == "__main__":
    res = get_all_apartments()
