"""
    Copyright 2022 bitValence, Inc.
    All Rights Reserved.

    This program is free software; you can modify and/or redistribute it
    under the terms of the GNU Affero General Public License
    as published by the Free Software Foundation; version 3 with
    attribution addendums as found in the LICENSE.txt.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    Purpose:
        Module initialization file

"""
import sys
sys.path.append("..")

import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# PySimpleGUI_License must be defined prior to import PySimpleGUI. This is an Open STEMware distribution key.
PySimpleGUI_License = 'e1ygJ1MkaOW0NTl0b2nJNylRVlH4ltwGZXSfIF6aIikCRCpBcs3GRRywaCWHJp1qdXGFlkvGbjiwIGsII5k3xkpTYF2tVuu4cS2WV6JARpCtIi6cMRTBc1wHOlD6cV4BO7TqIS40N4SbwCiMTKGilqjaZnWP5hztZhU7RelGc1G9x1v8eDWR1fl1bTnxRXWIZVXDJbztaaW09VuaIJjDokiyN0Se4ZwDIai0wwi2TvmJFktAZ3ULZxp6clnWNQ00IVjRoaimRiG6FM2WauWPQEiyLpC3JtOUYyWQ1DlUTSGYFBzKd2CdIc6CIOkK1cjfQH2I94tFY1X0M6ihLcCGJKDRbq2q1jweYyWs5U5QIrjcoiiPT23oBplPbuiTBuTqVEEgVTNvdN2cFwyIZmSfBrGFbK3gV3ujZfGJFa05a0Wo9kuTIMimw8ihQ53PVnzxdSGy93tGZsXCJvJzROCFID69IhjfI2ylNcz9AIiQLIC7JIEDY0XIRelLStX5NszxdOW6VukUIejPoNiYMMjQAvyHNGCB0EwnMeiJ0RyhNDCvItsiIokRRqhJdeGFVaFVewHbBQpic6mtVezkIjjKoJiHMyjsAtyrN7Sx0PwHMBiI0qxiNIyqIosyIpkyVltrYSWOlMstQ7WYRukHcKmBVAzScmytIj6QIvm59CwnZ7W64guzcD3XROl4bTXKdWhGcqmkVxASZO2V1fhGaIWAwJulYY2o9vtQIDi5wiiIS7VIBfBPZ3GaR2ydZIX5N6zwI5jxoAidNRjXkJuQMLTrMl4ALvjHgL2sLgjWIG0rNOCKJm9Z13e4cb89bc91311cec486e2df03057a632976e481d4b4c0aa1a8827431a10069df9cbb625a3708a4e191184ec193e0afe6ec5eadc6d0376c800d82d28eaa75e36f73d3e556da16f75f70d0b05859216b797892a5e5578d868851ba1491675ff0d35930d6fde89f5ebd33675f579b4e4e538afea815a34d2caaf3449101a185fa8f34f48937a341dd0e8bbb1345b267c97e5ed115a839181163c5c6e5be2cbe95bd5d29c0932729c937783fa133bc0002a356a06ab2c81204942435fbc82e2b4b2efaff2e29812cf47de50ea9d6325846c5effee94182eb1f935dbc3b811d0d42ce7a5bc43bd08b8c9f7ac77ec58ae83a1c18667df1d906ffc62efdbc5d87c8521a17f2f9c574de196430cbe9685f9f4dbcbd183a27c2eaedff73fc8bc079cf5839c30b7463ad53a5f3cec471cfc5a390566a2fab82f84636264b220b720d4e51269430cf3cbfb59014f3b93637170a39840fa338eda8c11be76b3de642da51ec379f803de4cd00e9c90d876e15c45633bd57d944278a4b5d8ef5b36ef765b7955aa6f649599378fdb4b8c7a0de1754abe81be2b241f1cc9b163a3239b34b1110d1a40020b0094107ca3a203a67c1c24de0847264f72a3c834f8ca884c5463b3fd937f67112b491b4f0383c0f27c2904d90610a3be2d2447bae0693e98f69270370e06415f0477dee8269ef61dc537a5bf3d3fde4085199b1dbed5986e838c419'

from .appcodetutorial import ManageCodeTutorials
from .appstore import AppStore, AppSpec, ManageUsrApps
from .apptemplate import CreateApp
from .eds import CfeTopicIds, AppEds
from .jsonfile import JsonTblTopicMap
from .pdfviewer import PdfViewer
from .tutorial import ManageTutorials
from .texteditor import TextEditor
from .utils import *

