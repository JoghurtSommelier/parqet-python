from loguru import logger
import requests
import json

class Portfolio:
    """
    A class representing a portfolio object.

    Attributes:
    - pId (str): The ID  or the Link of the portfolio.
    - response (dict): The JSON response from the API.

    Methods:
    - __init__(self, pId): Initializes the Portfolio object and retrieves the portfolio information from the API.
    - get_name(self): Returns the name of the portfolio.
    - get_value(self): Returns the current value of the portfolio.
    - get_total_gain_gross(self): Returns the total gross gain of the portfolio.
    - get_total_invested(self): Returns the total amount invested in the portfolio.
    - get_total_gain_net(self): Returns the total net gain of the portfolio.
    - get_total_return_gross(self): Returns the total gross return of the portfolio.
    - get_total_return_net(self): Returns the total net return of the portfolio.
    - get_fees(self): Returns the total fees paid for the portfolio.
    - get_activities(self): Returns the activities associated with the portfolio.
    - get_holdings(self): Returns the holdings associated with the portfolio.
    """

    def __init__(self, pId):
        """
        Initializes the Portfolio object and retrieves the portfolio information from the API.

        Args:
        - pId (str): The ID of the portfolio.
        """

        # Check if pId is a URL or the ID itself
        if "https://" in pId:
            if "https://app.parqet.com/p/" in pId:
                pId = pId.strip("https://app.parqet.com/p/")
            else:
                logger.error("Invalid URL: Either pass the Portfolio ID or the URL in the format https://app.parqet.com/p/XXXXXXX")
                return

        url = f"https://api.parqet.com/v1/portfolios/{pId}"
        try:
            response = requests.get(url)
            json_response = json.loads(response.text)
        except Exception as e:
            logger.error(e)
        if response.status_code != 200:
            logger.error(f"Error getting Portfolio Info (ID: {pId})")
            logger.error(f"Status Code: {response.status_code}")
            logger.error(f"Response: {response.text}")
        else:
            logger.success(f"Got Portfolio Info (ID: {pId})")
            self.response = json_response

    def get_name(self):
        """
        Returns the name of the portfolio.

        Returns:
        - float: The name of the portfolio.
        """
        return(self.response["portfolio"]["name"])

    def get_value(self):
        """
        Returns the current value of the portfolio.

        Returns:
        - float: The current value of the portfolio.
        """
        return(self.response['performance']["value"])

    def get_total_gain_gross(self):
        """
        Returns the total gross gain of the portfolio.

        Returns:
        - float: The total gross gain of the portfolio.
        """
        return(self.response['performance']["gainGross"])
    
    def get_total_invested(self):
        """
        Returns the total amount invested in the portfolio.

        Returns:
        - float: The total amount invested in the portfolio.
        """
        return(self.response['performance']["invested"])
    
    def get_total_gain_net(self):
        """
        Returns the total net gain of the portfolio.

        Returns:
        - float: The total net gain of the portfolio.
        """
        return(self.response['performance']["totalGainNet"])
    
    def get_total_return_gross(self):
        """
        Returns the total gross return of the portfolio.

        Returns:
        - float: The total gross return of the portfolio.
        """
        return(self.response['performance']["totalReturnGross"])
    
    def get_total_return_net(self):
        """
        Returns the total net return of the portfolio.

        Returns:
        - float: The total net return of the portfolio.
        """
        return(self.response['performance']["totalReturnNet"])
    
    def get_fees(self):
        """
        Returns the total fees paid for the portfolio.

        Returns:
        - float: The total fees paid for the portfolio.
        """
        return(self.response['performance']["fees"])
    
    def get_activities(self):
        """
        Returns the activities associated with the portfolio.

        Returns:
        - list: The activities associated with the portfolio.
        """
        return(self.response['activities'])
    
    def get_holdings(self):
        """
        Returns the holdings associated with the portfolio.

        Returns:
        - list: The holdings associated with the portfolio.
        """
        return(self.response['holdings'])
    
    def get_created_at(self):
        """
        Returns the date and time the portfolio was created.

        Returns:
        - str: The date and time the portfolio was created.
        """
        return(self.response['portfolio']['createdAt'])