# CRUD and HTTP Methods

**CRUD** is an acronym used to describe the four basic operations performed on data:

- **Create**
- **Read**
- **Update**
- **Delete**

These operations correspond directly to HTTP methods commonly used in RESTful APIs:

| CRUD Operation | HTTP Method | Description                                         |
|----------------|-------------|-----------------------------------------------------|
| Create         | `POST`      | Used to create a new resource                      |
| Read           | `GET`       | Used to retrieve or read an existing resource      |
| Update         | `PATCH`     | Used to update parts of an existing resource       |
| Delete         | `DELETE`    | Used to remove a resource                          |

### Examples

- Sending a `GET` request to `/users` should return a list of users.
- Sending a `POST` request to `/users` should create a new user.
- Sending a `PATCH` request to `/users/5` should update user #5.
- Sending a `DELETE` request to `/users/5` should delete user #5.

Understanding how CRUD maps to HTTP methods is foundational when working with web APIs.
