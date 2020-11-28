import requests
import os
from bs4 import BeautifulSoup
import time


def download_latest_cones_from_noaa(base_url, resource, target_directory):
    page = requests.get(base_url + resource)
    soup = BeautifulSoup(page.content, 'html.parser')
    resources = find_all_cones_of_uncertainty_resources(soup)
    if len(resources) > 0:
        download_cones_of_uncertainty_to_directory(
            base_url, resources, target_directory)


def find_all_cones_of_uncertainty_resources(soup):
    resources = []
    for a in soup.findAll('a'):
        if a.get_text() == 'Cone':
            resources.append(a.get('href'))
    return resources


def download_cones_of_uncertainty_to_directory(base_url, cones_of_uncertainty_resources, target_directory):
    for resource in cones_of_uncertainty_resources:
        response = requests.get(base_url + resource, allow_redirects=True)
        new_file_name = resource.split('/')[3]
        if not any(new_file_name == file_name for file_name in os.listdir(target_directory)):
            open(target_directory + new_file_name, 'wb').write(response.content)


if __name__ == "__main__":
    base_url = "https://www.nhc.noaa.gov"
    resource = "/gis"
    target_directory = "/data"
    download_latest_cones_from_noaa(base_url, resource, target_directory)