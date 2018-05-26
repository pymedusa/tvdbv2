# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat

from six import iteritems


class BasicEpisode(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BasicEpisode - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'absolute_number': 'int',
            'aired_episode_number': 'int',
            'aired_season': 'int',
            'dvd_episode_number': 'int',
            'dvd_season': 'int',
            'episode_name': 'text_type',
            'id': 'int',
            'overview': 'text_type'
        }

        self.attribute_map = {
            'absolute_number': 'absoluteNumber',
            'aired_episode_number': 'airedEpisodeNumber',
            'aired_season': 'airedSeason',
            'dvd_episode_number': 'dvdEpisodeNumber',
            'dvd_season': 'dvdSeason',
            'episode_name': 'episodeName',
            'id': 'id',
            'overview': 'overview'
        }

        self._absolute_number = None
        self._aired_episode_number = None
        self._aired_season = None
        self._dvd_episode_number = None
        self._dvd_season = None
        self._episode_name = None
        self._id = None
        self._overview = None

    @property
    def absolute_number(self):
        """
        Gets the absolute_number of this BasicEpisode.


        :return: The absolute_number of this BasicEpisode.
        :rtype: int
        """
        return self._absolute_number

    @absolute_number.setter
    def absolute_number(self, absolute_number):
        """
        Sets the absolute_number of this BasicEpisode.


        :param absolute_number: The absolute_number of this BasicEpisode.
        :type: int
        """
        self._absolute_number = absolute_number

    @property
    def aired_episode_number(self):
        """
        Gets the aired_episode_number of this BasicEpisode.


        :return: The aired_episode_number of this BasicEpisode.
        :rtype: int
        """
        return self._aired_episode_number

    @aired_episode_number.setter
    def aired_episode_number(self, aired_episode_number):
        """
        Sets the aired_episode_number of this BasicEpisode.


        :param aired_episode_number: The aired_episode_number of this BasicEpisode.
        :type: int
        """
        self._aired_episode_number = aired_episode_number

    @property
    def aired_season(self):
        """
        Gets the aired_season of this BasicEpisode.


        :return: The aired_season of this BasicEpisode.
        :rtype: int
        """
        return self._aired_season

    @aired_season.setter
    def aired_season(self, aired_season):
        """
        Sets the aired_season of this BasicEpisode.


        :param aired_season: The aired_season of this BasicEpisode.
        :type: int
        """
        self._aired_season = aired_season

    @property
    def dvd_episode_number(self):
        """
        Gets the dvd_episode_number of this BasicEpisode.


        :return: The dvd_episode_number of this BasicEpisode.
        :rtype: int
        """
        return self._dvd_episode_number

    @dvd_episode_number.setter
    def dvd_episode_number(self, dvd_episode_number):
        """
        Sets the dvd_episode_number of this BasicEpisode.


        :param dvd_episode_number: The dvd_episode_number of this BasicEpisode.
        :type: int
        """
        self._dvd_episode_number = dvd_episode_number

    @property
    def dvd_season(self):
        """
        Gets the dvd_season of this BasicEpisode.


        :return: The dvd_season of this BasicEpisode.
        :rtype: int
        """
        return self._dvd_season

    @dvd_season.setter
    def dvd_season(self, dvd_season):
        """
        Sets the dvd_season of this BasicEpisode.


        :param dvd_season: The dvd_season of this BasicEpisode.
        :type: int
        """
        self._dvd_season = dvd_season

    @property
    def episode_name(self):
        """
        Gets the episode_name of this BasicEpisode.


        :return: The episode_name of this BasicEpisode.
        :rtype: str
        """
        return self._episode_name

    @episode_name.setter
    def episode_name(self, episode_name):
        """
        Sets the episode_name of this BasicEpisode.


        :param episode_name: The episode_name of this BasicEpisode.
        :type: str
        """
        self._episode_name = episode_name

    @property
    def id(self):
        """
        Gets the id of this BasicEpisode.


        :return: The id of this BasicEpisode.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BasicEpisode.


        :param id: The id of this BasicEpisode.
        :type: int
        """
        self._id = id

    @property
    def overview(self):
        """
        Gets the overview of this BasicEpisode.


        :return: The overview of this BasicEpisode.
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """
        Sets the overview of this BasicEpisode.


        :param overview: The overview of this BasicEpisode.
        :type: str
        """
        self._overview = overview

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
