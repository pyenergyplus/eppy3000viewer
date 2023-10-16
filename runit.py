# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
from bottle import route, run, template, view
import eppy3000
from eppy3000.dbm_functions import schemaindbm
# import schemaindbm
import pprint

@route('/')
@route('/schemaobjects')
@view('objlist_template')
def schemaobjects(alist=None):
    # print(schemaindbm.get_aschema('Version'))
    # print(schemaindbm.get_schemaversion())
    gdict = schemaindbm.get_groups()
    # =====
    alist = list(schemaindbm.get_schemakeys())
    ver = schemaindbm.get_schemaversion()
    # aschema = schemaindbm.get_aschema(b'Version')
    print(ver)
    alist.remove(b'epJSON_schema_version')
    dct = dict(ver=ver, alist=alist, gdict=gdict)
    # return dict(alist=alist)
    return dict(dct=dct)


@route('/aschemaobject/<schemakey>')
@view('aschemaobject_template')
def aschemaobject(schemakey=None):
    fieldnames = list(schemaindbm.get_props(schemakey).keys())
    aschema = schemaindbm.get_aschema(schemakey)
    aschema_keys = list(aschema.keys())
    otherfields = {k:aschema[k] for k in aschema 
                    if k not in ['patternProperties', 'legacy_idd']}
    thedict = dict(schemakey=dict(schemakey=schemakey))
    thedict['schemakey'].update(dict(otherfields=otherfields))
    thedict['schemakey'].update(dict(fieldnames=fieldnames))
    return thedict

@route('/fielddetailsof/<schemaobject>/<fieldname>')
@view('fieldname_template')
def fielddetails(schemaobject=None, fieldname=None):
    fdetails = schemaindbm.get_field(schemaobject, fieldname)
    title = {"epjobjectname":schemaobject, "fieldname":fieldname}
    # get any object list details
    objdct = dict()
    try:
        objlist = fdetails['object_list']
        for item in objlist:
            refschema = schemaindbm.get_a_refschema(item)
            refschema.pop('reflist')
            objdct.update({item:refschema})
    except KeyError as e:
        pass
    return dict(title=title, fdetails=fdetails, objdct=objdct)


run(host='localhost', port=8081, debug=True)
