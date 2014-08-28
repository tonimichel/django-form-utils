from form_utils.forms import BetterModelForm, BetterModelFormMetaclass

#copied wholesale from django.forms.models.modelform_factory and adapted for BetterModelForm
def modelform_factory(model, form=BetterModelForm, fieldsets=None, fields=None, exclude=None,
                       formfield_callback=None):
    # Create the inner Meta class. FIXME: ideally, we should be able to
    # construct a ModelForm without creating and passing in a temporary
    # inner class.

    # Build up a list of attributes that the Meta object will have.
    attrs = {'model': model}
    if fieldsets is not None:
        attrs['fieldsets'] = fieldsets
    if fields is not None:
        attrs['fields'] = fields
    if exclude is not None:
        attrs['exclude'] = exclude

    # If parent form class already has an inner Meta, the Meta we're
    # creating needs to inherit from the parent's inner meta.
    parent = (object,)
    if hasattr(form, 'Meta'):
        parent = (form.Meta, object)
    Meta = type('Meta', parent, attrs)

    # Give this new form class a reasonable name.
    class_name = model.__name__ + 'Form'

    # Class attributes for the new form class.
    form_class_attrs = {
        'Meta': Meta,
        'formfield_callback': formfield_callback
    }

    return BetterModelFormMetaclass(class_name, (form,), form_class_attrs)
