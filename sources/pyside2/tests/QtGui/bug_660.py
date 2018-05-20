#############################################################################
##
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the test suite of Qt for Python.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

import unittest
import py3kcompat as py3k
from PySide2.QtGui import QStandardItemModel, QStandardItem

class MyItemModel(QStandardItemModel):
    def __init__(self,parent=None):
        super(MyItemModel,self).__init__(parent)
        self.appendRow([QStandardItem('Item 1'),])

    def mimeTypes(self):
        mtypes = super(MyItemModel,self).mimeTypes()
        mtypes.append(py3k.unicode_('application/my-form'))
        return mtypes

    def mimeData(self,indexes):
        self.__mimedata = super(MyItemModel,self).mimeData(indexes)
        self.__mimedata.setData(py3k.unicode_('application/my-form'), py3k.b('hi'))
        return self.__mimedata

class TestBug660(unittest.TestCase):
    '''QMimeData type deleted prematurely when overriding mime-type in QStandardItemModel drag and drop'''
    def testIt(self):
        model = MyItemModel()
        model.mimeData([model.index(0, 0)]) # if it doesn't raise an exception it's all right!

if __name__ == '__main__':
    unittest.main()
