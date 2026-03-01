---
title: "QwikiSyntax"
layout: resource
---

From: Guest ()
Date: April 18, 2006, 9:49 am

Qwiki Syntax Rules:
[QwikiWiki](QwikiWiki.md) uses its own syntactical rule set.  It may seem rather terse and complex when you read it here, but it really is quite simple and natural as you do it.  For example, the text that created all this is shown at the end of this page.

## Creating Headings
Any line containing at least two words, all of which are capitalized, becomes a heading.
Any Other Line: That starts with one or more capitalized words followed by a colon becomes a sub-heading.
 Each line is intended as many times as there are spaces at the beginning.

## Creating Lists
Any line starting with a "bullet identifier" becomes a line in a list.  Bullet identifiers (including numbered and non-numbered) can be mixed-and-matched at will.  The supported bullet identifiers are as follows:
- Question Mark (?): Creates a "question item"
- Exclamation Mark (!): Creates an "action item"
- Hyphen (-): Creates a hyphenated line
- Period (.): Creates a bulleted line
1. Number: Creates a numbered line.  Any numbered line starting with one resets the list counter.  Lines starting with numbers other than one are renumbered as necessary. Likewise, the list counter is reset with every heading.

## Automatic Linking
Text in a [QwikiWiki](QwikiWiki.md) page is scanned for several patterns, which automatically produce links of the following types:
- Email addresses and DNS names become hyperlinks, as do URLs of the form xxx:/*xxx@xxx.xxx?xxx
- Any word with "![CamelBack](CamelBack.md)" capitalization (meaning "UPPERCASE lowercase UPPERCASE lowercase" etc) becomes a link to a page with its corresponding name, such as [QwikiWiki](QwikiWiki.md).
  - Note: You can disable this on a per-instance basis by prefacing the word with an exclamation point (!), or by adding the word to the `'ignoreQwikiTagArray'` variable in `_config.php`.
- Any group of words surrounded and separated by underscores (_) becomes a link to a page with its corresponding name, such as [Home](Home.md).

## Formatting Notes
- Words surrounded by asteriks (**) become **bold**.
- Words surrounded by forward-slashes (*) become *italicized*.
- Words surrounded by pound-signs (`) are shown as `code`.

## HTML Notes
- [QwikiSyntax](QwikiSyntax.md) and HTML can be freely intermixed, though care must be taken to avoid conflicting with the other automated markup rules.
  - Note: To insert HTML code that should be visible to the user, be sure to replace the '&lt;' and '&gt;' with '&amp;lt;' and '&amp;gt;', respectively,
- Text surrounded by &lt;HTML&gt; and &lt;*HTML&gt; tags will be ignored by [QwikiWiki](QwikiWiki.md) and passed to the browser without alteration.
  - Note: For security reasons, only a subset of HTML tags are allowed in [QwikiWiki](QwikiWiki.md) pages.  The specific set allowed is up to the administrator; click **Help** when editing a page to see the complete list of acceptable HTML tags.

## Attached Files And Images
If enabled by the [QwikiWiki](QwikiWiki.md) administrator, you can upload and "attach" files to each page.  Attached files are stored in a page-specific subdirectory, and can be linked to from within the page by simply typing its filename into the page text.  If the attached file is an image type (GIF, JPG, PNG), it is inserted directly rather than linked to.
  - Note: Only certain file types can be attached, as specified by [QwikiWiki](QwikiWiki.md) administrator.  Click **Help** when editing a page to see the complete list of acceptable file types.

For Example: This Page's Source
As a concrete example of how to use [QwikiSyntax](QwikiSyntax.md) to write a rich [QwikiWiki](QwikiWiki.md) page, the text that actually generates this page is shown below.  
<HTML><TABLE CLASS='QWHelpBox' ALIGN='center'><TR><TD><PRE>
Qwiki Syntax Rules:
[QwikiWiki](QwikiWiki.md) uses its own syntactical rule set.  It may seem rather terse and 
complex when you read it here, but it really is quite simple and natural as 
you do it.  For example, the text that created all this is shown at the end of 
this page.

## Creating Headings
Any line containing at least two words, all of which are capitalized, becomes 
a heading.
Any Other Line: That starts with one or more capitalized words followed by a 
colon becomes a sub-heading.
 Each line is intended as many times as there are spaces at the beginning.

## Creating Lists
Any line starting with a "bullet identifier" becomes a line in a list.  Bullet 
identifiers (including numbered and non-numbered) can be mixed-and-matched at 
will.  The supported bullet identifiers are as follows:
- Question Mark (?): Creates a "question item"
- Exclamation Mark (!): Creates an "action item"
- Hyphen (-): Creates a hyphenated line
- Period (.): Creates a bulleted line
1. Number: Creates a numbered line.  Any numbered line starting with one 
resets the list counter.  Lines starting with numbers other than one are 
renumbered as necessary. Likewise, the list counter is reset with every 
heading.

## Automatic Linking
Text in a [QwikiWiki](QwikiWiki.md) page is scanned for several patterns, which automatically 
produce links of the following types:
- Email addresses and DNS names become hyperlinks, as do URLs of the form 
xxx:**xxx@xxx.xxx?xxx
- Any word with "![CamelBack](CamelBack.md)" capitalization (meaning "UPPERCASE lowercase 
UPPERCASE lowercase" etc) becomes a link to a page with its corresponding 
name, such as [QwikiWiki](QwikiWiki.md).
  - Note: You can disable this on a per-instance basis by prefacing the word 
with an exclamation point (!), or by adding the word to the 
`'ignoreQwikiTagArray'` variable in `_config.php`.
- Any group of words surrounded and separated by underscores (_) becomes a 
link to a page with its corresponding name, such as [Home](Home.md).

## Formatting Notes
- Words surrounded by asteriks (**) become **bold**.
- Words surrounded by forward-slashes (*) become *italicized*.
- Words surrounded by pound-signs (`) are shown as `code`.

## HTML Notes
- [QwikiSyntax](QwikiSyntax.md) and HTML can be freely intermixed, though care must be taken to 
avoid conflicting with the other automated markup rules.
  - Note: To insert HTML code that should be visible to the user, be sure to 
replace the '&lt;' and '&gt;' with '&amp;lt;' and '&amp;gt;', respectively,
- Text surrounded by &lt;HTML&gt; and &lt;*HTML&gt; tags will be ignored by 
[QwikiWiki](QwikiWiki.md) and passed to the browser without alteration.
  - Note: For security reasons, only a subset of HTML tags are allowed in 
[QwikiWiki](QwikiWiki.md) pages.  The specific set allowed is up to the administrator; click 
**Help** when editing a page to see the complete list of acceptable HTML tags.

## Attached Files And Images
If enabled by the [QwikiWiki](QwikiWiki.md) administrator, you can upload and "attach" files 
to each page.  Attached files are stored in a page-specific subdirectory, and 
can be linked to from within the page by simply typing its filename into the 
page text.  If the attached file is an image type (GIF, JPG, PNG), it is 
inserted directly rather than linked to.
  - Note: Only certain file types can be attached, as specified by [QwikiWiki](QwikiWiki.md) 
administrator.  Click **Help** when editing a page to see the complete list of 
acceptable file types.
<*PRE><*TD><*TR><*TABLE><*HTML>
For even more information about how [QwikiWiki](QwikiWiki.md) converts normal text into attractive HTML, visit www.qwikiwiki.com.