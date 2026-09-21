---
title: Translation workspace
---

# Translation workspace

Use the **Translation** to edit Korean source text and English translations side by side. Save your project before applying a translation.

This feature translates the game you are making. To change the language of this guide, use the **한국어 / English** tabs at the top of the site.

## What you can translate

- World-entry names and descriptions
- Scene titles and text, and action labels
- Project titles, summaries, and relation descriptions with paired Korean and English fields
- Paired names and descriptions in items, quests, characters, abilities, factions, and other game data

Only fields that support both languages appear in the list. Each translation is linked to a field and a stable entry ID, so reordering actions does not move a translation to the wrong action. Use search and the **Missing**, **Draft**, **Reviewed**, and **Source changed** filters to find work.

## Translate an entry

1. Save the project and open the workspace.
2. Find an entry with search or a status filter.
3. Read the Korean source and enter the English translation.
4. Check placeholders and locked glossary terms, then apply the translation.
5. Save and check how the text appears in the scene.

You can leave a translation empty and return to it later; it will stay marked **Missing**. Applying translation content is one undo step.

## Exchange translations as JSON

Export a translation JSON file, edit it, and import it again. The whole file is checked before any changes are applied. An import fails if it contains:

- Unknown or duplicate string keys
- A different project or target language
- Source text or a source hash that has changed since export
- Placeholder names, counts, or types that do not match
- Violations of locked glossary terms
- Unknown JSON fields or extra data after the JSON

Files can be up to **4 MiB**. Correct the reported errors and try again. Importing translations updates the editor project; it does not update a running game.

## Placeholders and glossary terms

Placeholders can be named, such as `{actor}`, or typed, such as `{amount:int}`. Keep their names, types, and number of occurrences in the translation.

The glossary accepts an array like this:

```json
[{"source":"마라","target":"Mara","locked":true}]
```

Locked terms must appear exactly, including capitalization. Source terms cannot be empty or duplicated. Glossary edits save immediately and are not part of project undo.

## Review status and saved files

Translations are stored beside the source in the existing project fields. Games use the current English display and fallback rules.

`localization/review.json` stores source and translation hashes, review marks, and the glossary. This file is for creators and is excluded from exported games.

Changing source text marks its translation **Source changed**. Editing a translation clears its reviewed status. Review information saves immediately, but source and translation hashes are checked so undoing or discarding changes cannot leave an incorrect review mark.

## Current limits

The workspace translates from Korean to English. It does not yet support translation in the other direction, separate language catalogs, or automatic plural forms. Incomplete translations do not automatically block game export.

An available interface language does not mean all game content has been translated. Unicode, input methods, fonts, and accessibility need further testing. The workspace records your translation work; it is not an automatic translation service.

## Contract documents are separate

[Product use and game agreements](PRODUCT_TERMS.md) explains planned handling of contract regions, display languages, and accepted versions for Korea, the United States, the United Kingdom, Germany, France, Japan, and mainland China. These documents remain review drafts. Effective terms and consent features are not available yet.

Contract documents will not be changed through this workspace or runtime LLM translation. Choosing an English interface does not remove applicable regional terms. Approved originals and supporting translations remain distinct. Preparing regional documents does not add German, French, Japanese, or Chinese to the entire application interface.

## Coming later: release checks

The planned [Test and release](TEST_AND_RELEASE.md) tools will help check choices, screens, notices, and private information in each language. If source text or rules change, the new version needs another review.

**Related:** [Worlds and scenes](WORLD_BUILDING.md) · [Troubleshooting](TROUBLESHOOTING.md)
