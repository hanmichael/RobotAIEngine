#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：相声语义
  创 建 者：余菲
  创建日期：17/2/10
"""
from nlu.rule import Rule
from nlu.media.common import *
from utils.utils import attach_perperty


class Comic(object):
    """
    相声语义
    """
    # 标识是mode领域
    service = 'comic'

    show_obj = '(相声|段子)'

    # 我想听XX
    case_1 = e(me) + e(want) + e(again) + e(adverb) + see + e(tag) + e('的') + show_obj + any_w
    rule_1 = Rule(attach_perperty(case_1, {'operation': 'play', 'rule': 1}))

    # 请给我播放XX
    case_2 = e(ask) + e(give) + e(me) + tell + e(tag) + e('的') + show_obj + any_w
    rule_2 = Rule(attach_perperty(case_2, {'operation': 'play', 'rule': 2}))

    # 小忆你可以给我播放相声吗
    case_3 = e(robot) + can + e(give) + e(me) + tell + e(tag) + e('的') + show_obj + e(stop_words)
    rule_3 = Rule(attach_perperty(case_3, {'operation': 'play', 'rule': 3}))

    # 我能请你帮我打开相声吗
    case_4 = e(me) + can + e(ask) + e(robot) + e(give) + e(me) + tell + e(tag) + e('的') + show_obj + e(stop_words)
    rule_4 = Rule(attach_perperty(case_4, {'operation': 'play', 'rule': 4}))

    # 请你帮我打开相声
    case_5 = ask + robot + give + me + tell + e(tag) + e('的') + show_obj + e(stop_words)
    rule_5 = Rule(attach_perperty(case_5, {'operation': 'play', 'rule': 5}))
