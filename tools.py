import datetime
import re
import requests
from requests.exceptions import RequestException
from markdownify import markdownify
from smolagents import tool

def get_weather_report_at_coordinates(coordinates, date_time):
    # Dummy function, returns a list of [temperature in °C, risk of rain on a scale 0-1, wave height in m]
    return [28.0, 0.35, 0.85]

def convert_location_to_coordinates(location):
    # Returns dummy coordinates
    return [3.3, -42.0]


@tool
def get_weather_api(location: str, date_time: str) -> str:
    """
    Returns the weather report.

    Args:
        location: the name of the place that you want the weather for. Should be a place name, followed by possibly a city name, then a country, like "Anchor Point, Taghazout, Morocco".
        date_time: the date and time for which you want the report, formatted as '%m/%d/%y %H:%M:%S'.
    """
    lon, lat = convert_location_to_coordinates(location)
    try:
        date_time = datetime.strptime(date_time)
    except Exception as e:
        raise ValueError("Conversion of `date_time` to datetime format failed, make sure to provide a string in format '%m/%d/%y %H:%M:%S'. Full trace:" + str(e))
    temperature_celsius, risk_of_rain, wave_height = get_weather_report_at_coordinates((lon, lat), date_time)
    return f"Weather report for {location}, {date_time}: Temperature will be {temperature_celsius}°C, risk of rain is {risk_of_rain*100:.0f}%, wave height is {wave_height}m."

@tool
def visit_webpage(url: str) -> str:
    """Visits a webpage at the given URL and returns its content as a markdown string.

    Args:
        url: The URL of the webpage to visit.

    Returns:
        The content of the webpage converted to Markdown, or an error message if the request fails.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Convert the HTML content to Markdown
        markdown_content = markdownify(response.text).strip()

        # Remove multiple line breaks
        markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

        return markdown_content

    except RequestException as e:
        return f"Error fetching the webpage: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"