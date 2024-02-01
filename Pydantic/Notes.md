# Pydantic

To learn more : https://docs.pydantic.dev/latest/concepts/models/

**1) Why using Pydantic ?**
- Type hints : 

```python
from typing import Annotated, Dict, List, Literal, Tuple
from annotated_types import Gt
from pydantic import BaseModel

class Fruit(BaseModel):
    name: str # required str field
    color: Literal['red', 'green'] # The Literal type is used to enforce that color is either 'red' or 'green'. 
    weight: Annotated[float, Gt(0)]  
    bazam: Dict[str, List[Tuple[int, bool, float]]]  # arbitrarily complex types can easily be validated

print(
    Fruit(
        name='Apple',
        color='red',
        weight=4.2,
        bazam={'foobar': [(1, True, 0.1)]},
    )
)
#> name='Apple' color='red' weight=4.2 bazam={'foobar': [(1, True, 0.1)]}
```
- Performance : 

Pydantic is among the fastest data validation libraries for Python.

- Serialization :

Pydantic provides functionality to serialize model in three ways:
1) To a Python dict made up of the associated Python objects
2) To a Python dict made up only of "jsonable" types
3) To a JSON string

- JSON Schema :

JSON Schema can be generated for any Pydantic schema — allowing self-documenting APIs and integration with a wide variety of tools which support JSON Schema.

- Strict mode and data coercion :

Some types can be automatically converted (= coerced) by Pydantic ! By default, Pydantic is tolerant to common incorrect types and coerces data to the right type — e.g. a numeric string passed to an int field will be parsed as an int.

Pydantic also has strict=True mode — also known as "Strict mode" — where types are not coerced and a validation error is raised unless the input data exactly matches the schema or type hint.

- Customisation :

Functional validators and serializers, as well as a powerful protocol for custom types, means the way Pydantic operates can be customized on a per-field or per-type basis.

- Dataclasses, TypedDicts, and more¶

Pydantic provides four ways to create schemas and perform validation and serialization:

1. BaseModel — Pydantic's own super class with many common utilities available via instance methods.
2. pydantic.dataclasses.dataclass — a wrapper around standard dataclasses which performs validation when a dataclass is initialized.
3. TypeAdapter — a general way to adapt any type for validation and serialization. This allows types like TypedDict and NampedTuple to be validated as well as simple scalar values like int or timedelta — all types supported can be used with TypeAdapter.
4. validate_call — a decorator to perform validation when calling a function.

