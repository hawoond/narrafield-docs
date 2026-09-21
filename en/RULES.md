---
title: Rules and catalogs
---

# Rules and catalogs

Create items, quests, player attributes, and initial inventory using the catalog forms. Item, quest, and attribute IDs are fixed after creation; names, descriptions, and values can change while preserving IDs. Setting an initial inventory quantity to zero removes that entry. Negative quantities and negative healing amounts are not allowed.

You cannot delete a definition referenced by scene conditions, effects, checks, expressions, or a character. Remove those references first. A successful form change is one undo step; invalid input leaves the project unchanged. Items acquired and quest progress during play are stored separately in play state.

## Conditions and expression trees

An optional expression tree (AST) can be stored in `Condition.expression`, `Effect.expression`, and `Check.expression`. Existing condition `op`, effect `value`, and check `dice` + `attribute` formats remain supported. When present, `expression` takes precedence over those fields. A check expression's result is compared with `target`. Effect expressions are supported only for `inventory`, `set`, `add`, and `hp`.

| Operation | Arguments | Result |
| --- | --- | --- |
| `int` | Integer `value` | Number |
| `ref` | Reference `ref` | Number |
| `dice` | `count`, `sides` | Number |
| `add`, `sub` | Two numbers | Number |
| `eq`, `ne`, `lt`, `le`, `gt`, `ge` | Two numbers | Boolean |
| `and`, `or` | Two booleans | Boolean |
| `not` | One boolean | Boolean |

Child arguments are stored in `args`. Supported references are `hp`, `maxHp`, `stat:<attribute ID>`, `variable:<name>`, and `inventory:<item ID>`. Attributes and items must exist in the project. An unset variable or an item not held has value zero. Integer addition or subtraction overflow is an error. Expressions do not execute general-purpose code or scripts.

Example: a `2d6 + insight` check.

```json
{
  "expression": {
    "op": "add",
    "args": [
      { "op": "dice", "count": 2, "sides": 6 },
      { "op": "ref", "ref": "stat:insight" }
    ]
  },
  "target": 10
}
```

One expression can have a maximum depth of 24, 256 nodes, and 100 dice in total. Each die supports 2–100,000 sides. Conditions must return a boolean and cannot contain dice, so repeatedly checking whether a choice is visible changes neither randomness nor game state. Use check expressions for random branches.

The entire tree is validated for types and size before evaluation. `and` and `or` short-circuit during execution. Checks and effects within game commands use stored random state, allowing reproduction after loading a save. If a later effect or scene transition fails, all state changes and random consumption for that command are rolled back. Resubmitting the same command ID does not roll again.

The current expression system works with integers and a single player state. String operations, arbitrary function calls, multiplication, division, and user code are not supported.
