from base import QuickbooksBaseObject, Ref

'''
QBO definition: The Department entity provides a way to track different segments of the business, divisions, or physical locations
such as stores, and allows another way of categorizing the entire transaction. This is in contrast to Class objects,
which are applied to individual transaction line details. Delete is achieved by setting the Active attribute to
false in an entity update request; thus, making it inactive. In this type of delete, the record is not permanently
deleted, but is hidden for display purposes. References to inactive objects are left intact.

'''
class Department(QuickbooksBaseObject):
    class_dict = {}

    qbo_object_name = "Department"

    Name = ""
    SubDepartment = False
    FullyQualifiedName = ""
    Active = True

    def __unicode__(self):
        return self.FullyQualifiedName
