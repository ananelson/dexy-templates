{% for k in sorted(d) -%}
{% if "templates" in k and  k.endswith("template.html|jinja") -%}

#### {{ k }}

{{ d[k] }}

{% endif -%}{% endfor -%}

