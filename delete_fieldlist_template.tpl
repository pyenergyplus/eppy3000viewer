<h3>Fields of EPJObject: {{schemaobject}} </h3>
<p>
%for i, fieldname in enumerate(alist):
    {{i + 1}}. <a href="../fielddetailsof/{{schemaobject}}/{{fieldname}}">{{fieldname}}</a><br>
%end
</p>