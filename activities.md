---
title: "Activities"
layout: default
permalink: /activities/
---

# Kinesthetic Learning Activities

Browse our collection of hands-on computer science learning activities. Each activity is designed to help students understand CS concepts through physical engagement and interaction.

## All Activities

{% for activity in site.activities %}
<div style="border-bottom: 1px solid #eee; padding: 1rem 0;">
  <h3><a href="{{ activity.url | relative_url }}">{{ activity.title }}</a></h3>
  {% if activity.content contains 'Summary:' %}
    {% assign summary = activity.content | split: 'Summary:' | last | split: 'Learning Goals:' | first | strip %}
    <p>{{ summary | truncate: 200 }}</p>
  {% endif %}
</div>
{% endfor %}

---

[← Back to Home]({{ "/" | relative_url }})