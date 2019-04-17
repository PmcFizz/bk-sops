# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import logging

from pipeline.conf import settings
from pipeline.core.data.var import (
    SpliceVariable,
    LazyVariable,
    RegisterVariableMeta
)

logger = logging.getLogger('root')


class CommonPlainVariable(SpliceVariable):
    __metaclass__ = RegisterVariableMeta


class Input(CommonPlainVariable):
    code = 'input'
    form = '%svariables/%s.js' % (settings.STATIC_URL, code)


class Textarea(CommonPlainVariable):
    code = 'textarea'
    form = '%svariables/%s.js' % (settings.STATIC_URL, code)


class Datetime(CommonPlainVariable):
    code = 'datetime'
    form = '%svariables/%s.js' % (settings.STATIC_URL, code)


class Int(CommonPlainVariable):
    code = 'int'
    form = '%svariables/%s.js' % (settings.STATIC_URL, code)


class Password(LazyVariable):
    code = 'password'
    form = '%svariables/%s.js' % (settings.STATIC_URL, code)

    def get_value(self):
        return self.value


class Select(LazyVariable):
    code = 'select'
    form = '%svariables/%s.js' % (settings.STATIC_URL, code)

    def get_value(self):
        # multiple select
        if isinstance(self.value, list):
            return ','.join(self.value)
        # single select
        else:
            return self.value
