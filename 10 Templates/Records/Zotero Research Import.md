---
type: research-source
status: inbox
owner: Paul
updated: {{importDate | format("YYYY-MM-DD")}}
---
# {{title}}

## Source

- Citation key: {{citekey}}
- Authors: {% for creator in creators %}{{creator.firstName}} {{creator.lastName}}{% if not loop.last %}; {% endif %}{% endfor %}
{% if desktopURI %}- Zotero: [Open item]({{desktopURI}}){% endif %}
{% if url %}- Source URL: {{url}}{% endif %}
{% if DOI %}- DOI: {{DOI}}{% endif %}

{% persist "research-notes" %}{% if isFirstImport %}
## Research Question and Exact Location

[Question; source page/section; Bible passage and translation; actual project link.]

## Observations and Evidence

[Read the source. Distinguish your paraphrase, short quotations, and biblical observations.]

## Interpretation, Formation, and Open Questions

[Proposed synthesis and Belonging, Beholding, Becoming invitations; note uncertainty.]

## Next Handoff

[Actual Canvas or brief link, next action, and review state. Research input is not approved curriculum.]
{% endif %}{% endpersist %}
