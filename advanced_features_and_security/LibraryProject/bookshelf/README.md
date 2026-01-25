## Permissions and Groups Setup

This project uses Django permissions and groups to control access.

### Custom Permissions
Defined on the Book model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

### Enforcement
Permissions are enforced in views using the
@permission_required decorator with raise_exception=True.