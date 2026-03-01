---
title: "Resources"
layout: default
permalink: /resources/
---

# Resources

Templates, design patterns, research papers, and supporting materials for creating and implementing kinesthetic learning activities.

## Design & Implementation

{% assign design_resources = site.resources | where_exp: "item", "item.title contains 'Template' or item.title contains 'Design' or item.title contains 'Heuristics' or item.title contains 'Building Blocks'" %}

{% for resource in design_resources %}
<div style="border-bottom: 1px solid #eee; padding: 1rem 0;">
  <h3><a href="{{ resource.url | relative_url }}">{{ resource.title }}</a></h3>
  {% if resource.content contains 'Summary:' or resource.content contains 'Overview:' %}
    {% assign content_lower = resource.content | downcase %}
    {% if content_lower contains 'summary:' %}
      {% assign summary = resource.content | split: 'Summary:' | last | split: '\n\n' | first | strip %}
    {% elsif content_lower contains 'overview:' %}  
      {% assign summary = resource.content | split: 'Overview:' | last | split: '\n\n' | first | strip %}
    {% endif %}
    <p>{{ summary | truncate: 200 }}</p>
  {% endif %}
</div>
{% endfor %}

## Research & Background

{% assign research_resources = site.resources | where_exp: "item", "item.title contains 'Paper' or item.title contains 'Background' or item.title contains 'Philosophy' or item.title contains 'Paradigm'" %}

{% for resource in research_resources %}
<div style="border-bottom: 1px solid #eee; padding: 1rem 0;">
  <h3><a href="{{ resource.url | relative_url }}">{{ resource.title }}</a></h3>
  {% if resource.content contains 'Summary:' or resource.content contains 'Overview:' %}
    {% assign content_lower = resource.content | downcase %}
    {% if content_lower contains 'summary:' %}
      {% assign summary = resource.content | split: 'Summary:' | last | split: '\n\n' | first | strip %}
    {% elsif content_lower contains 'overview:' %}
      {% assign summary = resource.content | split: 'Overview:' | last | split: '\n\n' | first | strip %}
    {% endif %}
    <p>{{ summary | truncate: 200 }}</p>
  {% endif %}
</div>
{% endfor %}

## Other Resources

{% assign other_resources = site.resources | where_exp: "item", "item.title contains 'KLAs' or item.title contains 'Links' or item.title contains 'Props' or item.title contains 'Notes' or item.title contains 'Home' or item.title contains 'QwikiSyntax' or item.title contains 'QwikiWiki'" %}

{% for resource in other_resources %}
<div style="border-bottom: 1px solid #eee; padding: 1rem 0;">
  <h3><a href="{{ resource.url | relative_url }}">{{ resource.title }}</a></h3>
  {% if resource.content contains 'Summary:' or resource.content contains 'Overview:' %}
    {% assign content_lower = resource.content | downcase %}
    {% if content_lower contains 'summary:' %}
      {% assign summary = resource.content | split: 'Summary:' | last | split: '\n\n' | first | strip %}
    {% elsif content_lower contains 'overview:' %}
      {% assign summary = resource.content | split: 'Overview:' | last | split: '\n\n' | first | strip %}
    {% endif %}
    <p>{{ summary | truncate: 200 }}</p>
  {% endif %}
</div>
{% endfor %}

---

[← Back to Home]({{ "/" | relative_url }})