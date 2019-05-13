import json
import requests

class SpaceX:
    """
    A base class for interacting with the SpaceX API
    """

    def get(self, url):
        """
        Perform an HTTP GET request and return the JSON data in the response.
        """
        url = "https://api.spacexdata.com/v3" + url
        data = requests.get(url).json()
        return data


class UpcomingLaunches(SpaceX):
    """
    A class for representing SpaceX Launches
    """

    def __init__(self):
        """
        The constructor 
        """


    def get_upcoming_launches(self):
        """
        Returns a JSON of launches
        """
    
        launch_ext = '/launches/upcoming'
        launches = self.get(launch_ext) 
        return launches


    def get_payloads(self, launches):
        """
        Returns a dictionary mapping of launch names to their payloads 
        """ 

        final_payloads = []

        for flight in launches:
            rocket = flight["rocket"]
            second_stage = rocket["second_stage"]
            payloads = second_stage["payloads"]

            for payload in payloads:
                item = payload["payload_type"]
                final_payloads.append(item)

        return final_payloads



    def get_payload_count(self, payloads):
        """
        Returns a count of how frequently the payloads appear
        """ 

        payload_count = {}

        for payload in payloads:
            if payload in payload_count:
                payload_count[payload] = payload_count[payload] + 1
            else:
                payload_count[payload] = 1

        return payload_count

        






