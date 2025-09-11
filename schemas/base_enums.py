from enum import StrEnum

class RichEnum(StrEnum):
    def __new__(cls, value, display_name: str):
        # The __new__ method is responsible for creating the enum member.
        # The first argument ('value') is what the member's value will be.
        # We create a string instance using the standard 'str' constructor.
        member = str.__new__(cls, value)
        
        # We then set the value and attach our custom attribute.
        member._value_ = value
        member.display = display_name
        return member

    # We define our enum members using the tuple format: (value, display_name)
    # EXAMPLES: 
    # NEWTON = ("NEWTON", "N")
    # KILOGRAM = ("KILOGRAM", "kg")