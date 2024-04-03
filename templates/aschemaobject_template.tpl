<p> 
    <a href="../schemaobjects">HOME</a> | <a href="../schemaobjects">HOME</a>
</p>

<h3>This is the details of an EPJObject : {{schemakey['schemakey']}}</h3>


%for otherfield in schemakey['otherfields']:
     <b>{{otherfield}}:</b> {{schemakey['otherfields'][otherfield]}}<br>
%end


<h4>Field Names of {{schemakey['schemakey']}}</h4>
<ul type = "circle">
%for fieldname in schemakey['fieldnames']:
        <li>
             <a href="../fielddetailsof/{{schemakey['schemakey']}}/{{fieldname}}">{{fieldname}}</a>
        </li>
%end
</ul>
