import requests
import pandas as pd

from config import config


class NewPost:

    def __init__(self):
        """
        The constructor initializes the NewPost instance with the API key and base URL, which are obtained from the
        config module.
        """
        self.api_key = config.API_KEY
        self.base_url = config.BASE_URL

    def payload(self, model_name, called_method, area_ref=None, city_ref=None):
        """
        This method generates the payload required for the API request.
        :param model_name: The API model name
        :param called_method: The specific method to call within the model
        :param area_ref: The reference for the area
        :param city_ref: The reference for the city
        :return:
        """
        payload = {
            "apiKey": self.api_key,
            "modelName": model_name,
            "calledMethod": called_method,
            "methodProperties": {
                "AreaRef": area_ref,
                "CityRef": city_ref,
            }
        }
        return payload

    def get_areas(self):
        """
        This method fetches all available areas from the Nova Poshta API.
        :return:
        """
        payload = self.payload(model_name="AddressGeneral", called_method="getAreas")
        response = requests.post(url=self.base_url, json=payload)
        for city in response.json()['data']:
            yield city

    def get_cities(self, area_ref: str = None):
        """
        This method fetches all cities for a given area using the area reference.
        :param area_ref: A reference for the area.
        :return:
        """
        payload = self.payload(model_name="AddressGeneral",
                               called_method="getCities",
                               area_ref=area_ref)

        response = requests.post(url=self.base_url, json=payload)
        for city in response.json()['data']:
            yield city

    def get_warehouses(self, city_ref: str):
        """
        This method fetches all warehouses for a given city using the city reference.
        :param city_ref: A reference for the city.
        :return:
        """
        payload = self.payload(model_name="AddressGeneral",
                               called_method="getWarehouses",
                               city_ref=city_ref)
        response = requests.post(url=self.base_url, json=payload)
        for city in response.json()['data']:
            yield city

    def result_collection(self):
        """
        Collecting the area name, city name, and warehouse name into a list.
        :return:
        """
        result = []
        areas = self.get_areas()

        for area in areas:
            area_name = area['Description']
            area_ref = area['Ref']
            cities = self.get_cities(area_ref)

            for city in cities:
                city_name = city['Description']
                city_ref = city['Ref']
                warehouses = self.get_warehouses(city_ref)

                for warehouse in warehouses:
                    warehouse_name = warehouse['Description']
                    result.append([area_name, city_name, warehouse_name])
                    print(result[-1])

        self.save_to_db(result)

    @staticmethod
    def save_to_db(data):
        """
        This static method saves the given data into an Excel file
        :param data: A list of lists, where each sublist contains the area, city, and warehouse names.
        :return:
        """
        df = pd.DataFrame(data=data, columns=['Область', 'Місто', 'Відділення'])
        df.to_excel('./new_post.xlsx', index=False)


if __name__ == "__main__":
    new_post_instance = NewPost()
    new_post_instance.result_collection()
