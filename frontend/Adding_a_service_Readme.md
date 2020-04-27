## <div align="center">How to add a service to the forntend<br /><br /></div>


### How to add service to database, Service table:
1. If a admin logs in, the admin user will have access to "Add a service" page.
2. Here all the details of the serice can be filled into the form and pushed to databases.
3. Once data for new service is added to the database, the dropdown menu in each page will be automatically populated.
4. However, the information for this new service has to be manually added to the page that the user sees after login. This is an improvmeent that can be made, so that this gets automatically populated from database like the dropdown. However, we have the setup ready for this to be integrated.

### Adding service to services.py
Two functions has to be added for each service:
  - one for rendering the page for the service: which renders the HTML page, that is the form to take user inputs for using the service, and has details regaridn the service.
  - one method for making the call to API endpoint of the service: Here the API end point can be pulled form the database. But method has to be written to call the API, and rendering the page with output from service or any error message.
  This method has try-exception case, so that in case any error "THere is a issue with service, contact admin."
  - For both of these methods, methods of existing services in services.py can be used.
  - Existing templates for any other services can be used and modfied for new se

### Adding HTML page that is service specific:
1. There is a page specific to each service. This page is used for taking user inputs, button for calling the service, description of the service and the API details.
2. A template of any page of existing service page can be used to be modified and used. 
