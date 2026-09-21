---
title: Relations
description: Create relationships between people, places and organizations, then arrange, search and share the graph.
---

# Relations

**Relations** connects world entries: a person belongs to a guild, lives at a place, or witnesses an event.

{% include screenshot.html file="relations.png" alt="Membership, residence and event relations between Mara, the keepers' guild and places" caption="Read connections through their direction and relationship type." %}

## Create a relationship

1. Create both entries in [World](WORLD_BUILDING.md).
2. Choose **Relations → + Add relation**.
3. Set **From**, **To**, **Type**, and a description.
4. Select **Directed** for a relationship that points from one entry to another.
5. Set visibility, **Apply**, and **Save**.

For example, connect Mara to the keepers' guild with a membership label. To manage actual joining, reputation, and roles as game rules, use [Factions](FACTION_GUIDE.md).

## Organize a larger graph

Search by name, type, or tag. Zoom and pan to inspect an area. Drag nodes or adjust their positions through the position entries. Review a type-based arrangement before applying it.

Use **Reset view** to regain your bearings and **Undo layout** to revert a recent arrangement. Moving a node changes its display position; editing a relation changes its meaning.

## Personal arrangement and team views

Use **Save team view** to share an arrangement and **Load team view** to use the stored layout. Sharing the project files with collaborators is covered in [Git collaboration](COLLABORATION.md).

## Check public visibility

After setting visibility, inspect **Player view**. Older builds may label it **Public data preview**. This read-only view helps check that hidden entries and their relations are not exposed.

Unlock values entered in preview are test inputs. To reveal conditional lore during actual play, connect an appropriate scene or ability effect.

## Check the result

- Direction and endpoints match the intended relationship.
- Clearing search reveals the wider graph.
- Private information stays hidden in player view.
- Removing a relation is not confused with deleting the underlying world entry.

**Related:** [World building](WORLD_BUILDING.md) · [Factions](FACTION_GUIDE.md) · [Maps](MAPS.md)
