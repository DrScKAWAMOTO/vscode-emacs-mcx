#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Project: My Tasks Application
# Version: 1.0
# Copyright: (C) 2023 Dr.Sc.KAWAMOTO,Takuji (Ext)
# Create: 2023/11/19 14:31:29 JST
#
'''vscode-emacs-keymap 拡張機能の keybindings.json を分析する。
'''

import os
import sys
import re
import argparse
import json
import copy

usage_message = '''%(prog)s [-h]'''
help_message = '''vscode-emacs-keymap 拡張機能の keybindings.json を分析する。
'''

parser = argparse.ArgumentParser(
    description=help_message, usage=usage_message,
    formatter_class=argparse.RawDescriptionHelpFormatter)
flags, fileargs = parser.parse_known_args()


def read_json(filename):
    lines = []
    with open(filename, 'r') as fp:
        for line in fp.readlines():
            line = line.rstrip()
            match = re.match('^(.*) +//.*$', line)
            if match is not None:
                line = match.group(1)
            lines.append(line)
    return json.loads(''.join(lines))


def check_special(keybindings):
    print('これから $special を検査します!!')
    result = []
    for keybinding in keybindings:
        if '$special' in keybinding.keys():
            print(keybinding)
        else:
            result.append(keybinding)
    print('これで $special 検査を終了します!!')
    return result


def append_mac(keybindings):
    result = []
    for keybinding in keybindings:
        if 'mac' not in keybinding.keys():
            keybinding = copy.copy(keybinding)
            keybinding['mac'] = ''
        result.append(keybinding)
    return result


def split_keys(keybindings):
    result = []
    for keybinding in keybindings:
        if 'keys' in keybinding.keys():
            keybinding = copy.copy(keybinding)
            keys = keybinding.pop('keys')
            for key in keys:
                keybinding = copy.copy(keybinding)
                keybinding['key'] = key
                result.append(keybinding)
        else:
            result.append(keybinding)
    return result


def split_whens(keybindings):
    result = []
    for keybinding in keybindings:
        if 'whens' in keybinding.keys():
            keybinding = copy.copy(keybinding)
            whens = keybinding.pop('whens')
            for when in whens:
                keybinding = copy.copy(keybinding)
                keybinding['when'] = when
                result.append(keybinding)
        else:
            result.append(keybinding)
    return result


def append_when(keybindings):
    result = []
    for keybinding in keybindings:
        if 'when' not in keybinding.keys():
            keybinding = copy.copy(keybinding)
            keybinding['when'] = ''
        result.append(keybinding)
    return result


def check_key_mac_when_command(keybindings):
    for keybinding in keybindings:
        keys = list(sorted(keybinding.keys()))
        if len(keys) == 4:
            assert keys == ['command', 'key', 'mac', 'when']
        elif len(keys) == 5:
            assert keys == ['args', 'command', 'key', 'mac', 'when']
        else:
            assert False


def gather_when(keybindings):
    result = {}
    for keybinding in keybindings:
        if 'when' in keybinding.keys():
            result[keybinding['when']] = True
    return result.keys()


def split_when(when_objs):
    splitting = True
    result = {}
    while splitting:
        splitting = False
        result = {}
        for when in when_objs:
            match = re.match('^([^&|]+) (&&|\|\|) (.+)$', when)
            if match is None:
                result[when] = True
            else:
                result[match.group(1)] = True
                result[match.group(3)] = True
                splitting = True
        when_objs = list(result.keys())
    for index in range(0, len(when_objs)):
        elem = when_objs[index]
        if len(elem) > 0 and elem[0] == '!':
            when_objs[index] = elem[1:]
    return when_objs


def keybinding_to_string(keybindings):
    result = []
    for keybinding in keybindings:
        kb_string = keybinding['key']
        kb_string += ' / ' + keybinding['mac']
        kb_string += ' / ' + keybinding['when']
        kb_string += ' / ' + keybinding['command']
        result.append(kb_string)
    return result


def main():
    '''vscode-emacs-mcx 拡張機能の keybindings.json を分析する。
    '''
    keybindings_objs = read_json('keybindings.json')
    keybindings_objs = keybindings_objs['keybindings']
    keybindings_objs = check_special(keybindings_objs)
    keybindings_objs = split_keys(keybindings_objs)
    keybindings_objs = split_whens(keybindings_objs)
    keybindings_objs = append_mac(keybindings_objs)
    keybindings_objs = append_when(keybindings_objs)
    check_key_mac_when_command(keybindings_objs)
    when_objs = gather_when(keybindings_objs)
    print('split_when()')
    when_objs = split_when(when_objs)
    print('finished')
    for when in sorted(when_objs):
        print(when)
    sys.exit(0)

    keybindings_objs = keybinding_to_string(keybindings_objs)
    keybindings_objs = sorted(keybindings_objs)
    with open('keybindings.lst', 'w') as fw:
        for line in keybindings_objs:
            print(line, file=fw)


if __name__ == '__main__':
    main()
