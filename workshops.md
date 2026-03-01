---
title: "Workshops"
layout: default
permalink: /workshops/
---

# Workshop Collections

These are collections of materials from educational workshops, primarily from SIGCSE conferences and other computer science education venues.

## All Workshops

{% for workshop in site.workshops %}
<div style="border-bottom: 1px solid #eee; padding: 1rem 0;">
  <h3><a href="{{ workshop.url | relative_url }}">{{ workshop.title }}</a></h3>
  {% if workshop.content contains 'Summary:' or workshop.content contains 'Overview:' %}
    {% assign content_lower = workshop.content | downcase %}
    {% if content_lower contains 'summary:' %}
      {% assign summary = workshop.content | split: 'Summary:' | last | split: '\n\n' | first | strip %}
    {% elsif content_lower contains 'overview:' %}
      {% assign summary = workshop.content | split: 'Overview:' | last | split: '\n\n' | first | strip %}
    {% endif %}
    <p>{{ summary | truncate: 250 }}</p>
  {% endif %}
</div>
{% endfor %}

---

[← Back to Home]({{ "/" | relative_url }})