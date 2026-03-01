---
title: "Resources"
layout: default
permalink: /resources/
---

# Resources

Templates, design patterns, research papers, and supporting materials for creating and implementing kinesthetic learning activities.

## Design & Implementation

{% for resource in site.resources %}
  {% if resource.title contains 'Template' or resource.title contains 'Design' or resource.title contains 'Heuristics' or resource.title contains 'Building Blocks' %}
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
  {% endif %}
{% endfor %}

## Research & Background

{% for resource in site.resources %}
  {% if resource.title contains 'Paper' or resource.title contains 'Background' or resource.title contains 'Philosophy' or resource.title contains 'Paradigm' %}
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
  {% endif %}
{% endfor %}

## Other Resources

{% for resource in site.resources %}
  {% if resource.title contains 'KLAs' or resource.title contains 'Links' or resource.title contains 'Props' or resource.title contains 'Notes' or resource.title contains 'Home' or resource.title contains 'QwikiSyntax' or resource.title contains 'QwikiWiki' %}
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
  {% endif %}
{% endfor %}

---

[← Back to Home]({{ "/" | relative_url }})