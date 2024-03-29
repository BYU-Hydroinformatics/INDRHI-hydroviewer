from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting


class IndrhiHydroviewer(TethysAppBase):
    """
    Tethys app class for Indrhi Hydroviewer.
    """

    name = 'Indrhi Hydroviewer'
    index = 'indrhi_hydroviewer:home'
    icon = 'indrhi_hydroviewer/images/Dominican-Republic-Map-Flag.png'
    package = 'indrhi_hydroviewer'
    root_url = 'indrhi-hydroviewer'
    color = '#f39c12'
    description = 'This is a Hydroviewer for INDRHI'
    tags = '"Hydrology", "DR", "BYU", "Hydroviewer"'
    enable_feedback = False
    feedback_emails = []


    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='indrhi-hydroviewer',
                controller='indrhi_hydroviewer.controllers.home'
            ),
            UrlMap(
                name='get-available-dates',
                url='get-available-dates',
                controller='indrhi_hydroviewer.controllers.get_available_dates'),
            UrlMap(
                name='get-time-series',
                url='get-time-series',
                controller='indrhi_hydroviewer.controllers.get_time_series'),
            UrlMap(
                name='get-return-periods',
                url='get-return-periods',
                controller='indrhi_hydroviewer.controllers.get_return_periods'),
            UrlMap(
                name='get-historic-data',
                url='get-historic-data',
                controller='indrhi_hydroviewer.controllers.get_historic_data'),
            UrlMap(
                name='get_dailyAverages',
                url='get-dailyAverages',
                controller='indrhi_hydroviewer.controllers.get_dailyAverages'),
            UrlMap(
                name='get_monthlyAverages',
                url='get-monthlyAverages',
                controller='indrhi_hydroviewer.controllers.get_monthlyAverages'),
            UrlMap(
                name='get-flow-duration-curve',
                url='get-flow-duration-curve',
                controller='indrhi_hydroviewer.controllers.get_flow_duration_curve'),
            UrlMap(
                name='get_historic_data_csv',
                url='get-historic-data-csv',
                controller='indrhi_hydroviewer.controllers.get_historic_data_csv'),
            UrlMap(
                name='get_forecast_data_csv',
                url='get-forecast-data-csv',
                controller='indrhi_hydroviewer.controllers.get_forecast_data_csv'),
            UrlMap(
                name='forecastpercent',
                url='forecastpercent',
                controller='indrhi_hydroviewer.controllers.forecastpercent'),
            UrlMap(
                name='getModelData',
                url='getModelData',
                controller='indrhi_hydroviewer.controllers.retrieve_models'),
            UrlMap(
                name='getModelDataIn',
                url='getModelDataIn',
                controller='indrhi_hydroviewer.controllers.retrieve_models_in'),
        )

        return url_maps
    def custom_settings(self):
        return (
            CustomSetting(
                name='endpoint',
                type=CustomSetting.TYPE_STRING,
                description='Endpoint for the Geoserver service',
                required=True,
            ),
            CustomSetting(
                name='workspace',
                type=CustomSetting.TYPE_STRING,
                description='Workspace within Geoserver where web service is',
                required=True,
            ),
        )
