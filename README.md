# File-hosting-trainee
File hosting with Authentication service, File service, App service.


First demo of cloud filehosting Pre-release

Application demands:
Authentication service:
Sign up. In order to signup user needs to provide a unique username, email and create a password that has at least 10 chars and contains at least 1 uppercase letter, 1 lowercase letter, 1 number and 1 special char. Server side validation required
Authorization and authentication of users using JWT. On login endpoint user enters username and password and receives access and refresh tokens which he uses to perform authentication on any endpoint that requires authentication. When access token is expired, refresh token is used on separate endpoint to receive new pair of access-refresh tokens. If refresh token is expired user needs to repeat login flow
File service:
Main purpose of file service is to handle file uploads/downloads
File format verification required:
- Supported formats: jpg, gif, tiff, png, svg, docx, xls, pdf, txt
File upload needs to be resumable - if file upload was canceled, then it must be resumed from the same spot. All not fully uploaded files needs to be deleted after one week
In order to implement resumable upload files should be divided into chunks before upload. After uploading, all chunks need to be verified and file should be build
Hash sum verification required
Before download from server file needs to be archived(.zip)
App service:
Main application that aggregates endpoints for users’ interactions.
Endpoints where users can:

    View dashboard with all uploaded files
    View details of each uploaded file
    Add and edit descriptions of each file
    Mark files as deleted
    View and edit own profile
    Change password
