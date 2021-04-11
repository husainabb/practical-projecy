# Prize
This project is a basic application that uses docker to containerise and jenkins to deploy. The application had 4 services to it. one frontend and three backend.
The frontend communicates with the other services and displays the result, where as service 2&3 generates a random number and letter respectively. Fianlly service 4 collects the data from service 2&3

## Requirements
1. An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
2. This could also provide a record of any issues or risks that you faced creating your project.
3. An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
4. If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
5. The project must follow the Service-oriented architecture that has been asked for.
6. The project must be deployed using containerisation and an orchestration tool.
7. As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
8. The project must make use of a reverse proxy to make your application accessible to the user.