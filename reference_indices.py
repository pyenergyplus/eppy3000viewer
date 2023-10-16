# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""create the indices for the references"""

import dbm
import json
import dbm.dumb
import pprint


def db_in_memory(fname=None):
    """get the dbm in memory"""
    if not fname:
        fname = '../eppy3000/eppy3000/resources/schema/V9_3/Energy+.schema.epJSON'
    d = json.load(open(fname, 'r'))
    db = dict()
    for key in d['properties']:
        db[key] = json.dumps(d['properties'][key])
    return db
    


def main(key):
    try:
        key = key.encode()
    except AttributeError as e:
        pass
    with dbm.dumb.open('schema', 'r') as db:
        print(db[key])
                
        
def get_schemakeys(fname=None):
    """get all the schema keys"""
    if fname:
        with dbm.dumb.open(fname, 'r') as db:
            return db.keys()
    else:
        with dbm.dumb.open('../eppy3000/schema', 'r') as db:
            return db.keys()

def get_aschema(key):
    """gets a schema"""
    try:
        key = key.encode()
    except AttributeError as e:
        pass
    with dbm.dumb.open('../eppy3000/schema', 'r') as db:
        dt = json.loads(db[key])
        return dt
        
def get_name(key, aschema=None):
    """get the name field of the schema"""
    if aschema:
        dt = aschema
    else:
        dt = get_aschema(key)
    try:
        return dt['name']
    except KeyError as e:
        return None
    
def get_props(key, aschema=None):
    """gets the properties of a schema
    if already have aschema, it avoids disk access"""
    if aschema:
        dt = aschema
    else:
        dt = get_aschema(key)
    # props = dt['patternProperties']['^.*\\S.*$']['properties']
    for pkey in dt['patternProperties']:
        props = dt['patternProperties'][pkey]['properties'] 
        break
    return props

def get_field(key, fieldname, aschema=None):
    """get the field of a schema
    if already have aschema, it avoids disk access"""
    dt = get_props(key, aschema)
    return dt[fieldname]
    
def get_arrayfieldnames(key, fieldname, aschema=None):
    """get the array fieldnames of a field"""
    field = get_field(key, fieldname, aschema=aschema)
    try:
        return [arrayfield for arrayfield in field['items']['properties']]
    except KeyError as e:
        return list()
        
def get_arrayfield(key, fieldname, arrayfieldname, aschema=None):
    """get the array field of a field"""
    field = get_field(key, fieldname, aschema=aschema)
    return field['items']['properties'][arrayfieldname]

if __name__ == '__main__':
    fname = "../eppy3000/eppy3000/resources/schema/V9_3/Energy+.schema.epJSON"
    db = db_in_memory(fname)
    dt = dict()
    for key in db.keys():
        aschema = json.loads(db[key])
        try:
            name = get_name(key, aschema=aschema)
            refs = name['reference']
            for ref in refs:
                objlist = dt.setdefault(ref, {'objlist':list()})['objlist']
                objlist.append(key)
        except (TypeError, KeyError) as e:
            pass

    for key in db.keys():
        aschema = json.loads(db[key])
        name = get_name(key, aschema=aschema)
        # get reflist from name
        try:
            object_list = name['object_list']
            for object_item in object_list:
                for object_item in object_list:
                    dt[object_item].setdefault('reflist', list()).append(f'{key}.name')
        except (TypeError, KeyError) as e:
            pass
        fieldnames = get_props(key, aschema=aschema).keys()
        for fieldname in fieldnames:
            # get reflist from fieldname
            field = get_field(key, fieldname, aschema=aschema)
            try:
                object_list = field['object_list']
                for object_item in object_list:
                    dt[object_item].setdefault('reflist', list()).append(f'{key}.{fieldname}')
            except KeyError as e:
                pass
            # get reflist from field array
            for arrayfieldname in get_arrayfieldnames(key, fieldname, aschema=aschema):
                arrayfield = get_arrayfield(key, fieldname, arrayfieldname, aschema=aschema)
                try:
                    object_list = arrayfield['object_list']
                    for object_item in object_list:
                        dt[object_item].setdefault('reflist', list()).append(f'{key}.{fieldname}.{arrayfieldname}')
                except KeyError as e:
                    object_list = list()
                print(f'{key}')
                print(f'    -> {fieldname}')
                print(f'         -> {arrayfieldname}')
                print(f'             -> {object_list}')
                

    # for key, vals in dt.items():
    #     print(key)
    #     for val in vals['objlist']:
    #         print(f'   {val}')
    #     print('---')

    for key, vals in dt.items():
        # print(key)
        try:
            for val in vals['reflist']:
                print(f'   {val}')
        except KeyError as e:
            print(f'**** {key} **** is an orphaned reference')
            # for val in vals:
            #     print(val)
            # print('---')
        # print('---')
        
    # save the indice dict in dbm
    
    with dbm.dumb.open('schema_ref', 'c') as thedb:
        for key in dt:
            thedb[key] = json.dumps(dt[key])
    

