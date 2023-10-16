<p> 
    <a href="../../schemaobjects">HOME</a> | <a href="../../schemaobjects">HOME</a>
</p>

<h3>Field details of:</h3>
<p> the field <b>{{title['fieldname']}}</b> in EPJObject <b>{{title['epjobjectname']}}</b></p>
%for key in fdetails:
    %if isinstance(fdetails[key], list):
        <strong>{{key}}</strong> : 
        <ul>
        %for item in fdetails[key]:
            %if key == 'object_list':
                <li>{{item}} -> are from following EPJObjects
                    <ul>
                        %for epjname in objdct[item]['objlist']:
                        <li><a href="../../aschemaobject/{{epjname}}">{{epjname}}</a></li>
                        %end
                    </ul>
                </li>
            %else:
                <li>{{item}}
                </li>
            %end
        %end
        </ul>
    %elif isinstance(fdetails[key], dict):
       <strong>{{key}}</strong> : 
        <ul>
        %for key in fdetails[key]['properties']:
            <li>{{key}}</li>
        %end
        </ul>
    %else:
        <strong>{{key}}</strong> : {{fdetails[key]}}
    %end
    <br>
%end
