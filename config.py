# -*- coding: utf-8 -*-
'''
	LF-Portal: Configuration
	~~~~~~~~~~~~~~~~~~~~~~~~

	A video portal for Opencast Matterhorn and compatible systems.

	:copyright: 2013 by Lars Kiesow <lkiesow@uos.de>
	:license: GPL, see LICENSE for more details.
'''

# Specify the template to use for the portal.
# Templates are located in the templates/<TEMPLATE> folder.
TEMPLATE = 'uni-stuttgart'

# SEARCH_SERVICE   = 'http://player.oc-test.switch.ch/search'
# SECURITY_SERVICE = 'http://player.oc-test.switch.ch/admin-ng'
SEARCH_SERVICE   = 'https://engage.rus.uni-stuttgart.de/search/'
SECURITY_SERVICE = 'https://mh.rus.uni-stuttgart.de/j_spring_security_check'
#SEARCH_SERVICE   = 'https://nfldevocaio.rus.uni-stuttgart.de/search/'
#SECURITY_SERVICE = 'https://nfldevocaio.rus.uni-stuttgart.de/admin-ng/'

# The amount of series per page to display on /serieslist
SERIES_PER_PAGE  = 15

# The amount of series per page to display on /recordinglist
RECORDINGS_PER_PAGE  = 12

# The amount of videos displayed on the home page
NEW_EPISODES_ON_HOME    = 8
RANDOM_EPISODES_ON_HOME = 6

# The amount of recordings per search page
SEARCH_RESULTS_PER_PAGE = 12

# Plug-ins to use for the player embed HTML generation.
# The default plu-ins are:
#   simpleengage   Try to include the engage player URL by using the
#             ENGAGE_SERVICE variable and mediapackage id. Fast but reliable
#             only in some cases. Not if there are more than one engage server
#             and not if the IDs might have changed.
#   simpleembed   Try to include the embed player URL by using the
#             ENGAGE_SERVICE variable and mediapackage id. Fast but reliable
#             only in some cases. Not if there are more than one engage server
#             and not if the IDs might have changed.
# Multiple plug-ins can be defined. In that case, the next plug-in is used if
# one plug-in fails to construct the code.
PLAYER_PLUGINS = ['simpleengage']

# Set this if ENGAGE_PLUGIN is set to simpleembed or simpleengage:
# Recordings need flag "public"
#ENGAGE_SERVICE   = 'https://nfldevocaio.rus.uni-stuttgart.de/engage/'
ENGAGE_SERVICE   = 'https://engage.rus.uni-stuttgart.de/engage/'
# ENGAGE_SERVICE = 'https://engage.opencast.org/engage/'


USE_MEMCACHD     = False
MEMCACHED_HOST   = 'localhost:11211'
CACHE_TIME_SEC   = 600

# Series color generation
#SERIESCOLOR_PLUGIN        = 'sum'
SERIESCOLOR_PLUGIN        = 'stuttgart_facultycolors'
SERIESCOLOR_SUM_MAX       = [100] * 3
SERIESCOLOR_SUM_OFFSET    = [0] * 3
SERIESCOLOR_SUM_USE_TITLE = True
SERIESCOLOR_SUM_USE_ID    = False

# Configuration for built-in server only:
SERVER_DEBUG = True
SERVER_HOST  = '0.0.0.0' # Set to localhost for local access only
SERVER_PORT  = 8000
