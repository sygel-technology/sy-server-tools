To use this module, you need to:

Create another module that inherits this module and uses the 3 provided mixin models to:
- Create a requirement rule record. Use the confirmation_requirement_rule_mixin for that.
- Link the requirement rule to a 'type' record. Use the requirement_rule_type_mixin for that.
- Apply the requirements to a record that has the 'type' above. Use the confirmation_requirement_mixin for that.

See sale_type_confirmation_requirement_rules of sy-sale-workflow an example
