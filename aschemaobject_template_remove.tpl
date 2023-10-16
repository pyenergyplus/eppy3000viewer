<p> 
    <a href="../schemaobjects">HOME</a> | <a href="../schemaobjects">HOME</a>
</p>

<h3>This is the details of an EPJObject : {{schemakey['schemakey']}}</h3>

%if 'name' in schemakey:
    <h4>Attributes of name</h4>
    <dl>
    %for key in schemakey['name']:
        %if not isinstance(schemakey['name'][key], list):
            <dt><b>{{key}}:</b></dt>
            <dd>{{schemakey['name'][key]}}</dd>
        %else:
            <dt><b>{{key}}:</b></dt>
            %for item in schemakey['name'][key]:
                <dd>{{item}}</dd>
            %end
        %end
    %end
%else:
    This epjobject does not have a name
%end
</dl>

<h4>Field Names of {{schemakey['schemakey']}}</h4>
<ul type = "circle">
%for fieldname in schemakey['fieldnames']:
        <li>
             <a href="../fielddetailsof/{{schemakey['schemakey']}}/{{fieldname}}">{{fieldname}}</a>
        </li>
%end
</ul>
