<p> 
    <a href="./schemaobjects">HOME</a> | <a href="./schemaobjects">HOME</a>
</p>

<H3>EPJ Objects</H3>
Schema Version = {{dct['ver']}}

<p>
%for i, group in enumerate(dct['gdict']):
    <H4>{{i + 1}}. {{group}}</H4>
    <p style="margin-left: 40px">
    %for j, epjobject in enumerate(dct["gdict"][group]):
        {{j + 1}}. <a href="aschemaobject/{{epjobject}}">{{epjobject}}</a><br>
    %end
    </p>
%end
</p>

