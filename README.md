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

## Trello board
![image](https://user-images.githubusercontent.com/79215061/114325462-367b9d00-9b28-11eb-886c-ddacaf6356e1.png)
This is my Trello board after completion

## Development Pipeline
![image](https://user-images.githubusercontent.com/79215061/114325711-6e371480-9b29-11eb-9cbc-03d7fd23972a.png)
Heres a basic diagram i made to show how the development pipeline is connected

## Testing
here is where i tested my application to see if it works, to make sure i have not made any errors in my code.

unfortunely, my vscode had some sort glitch and wouldn't run pytest --cov=app properly
![image](https://user-images.githubusercontent.com/79215061/114325884-2b297100-9b2a-11eb-8a5e-703b225ddd59.png)
All I can show is that tests ran and successed.

## Risk Assessment 
![image](https://user-images.githubusercontent.com/79215061/114326152-447eed00-9b2b-11eb-8a69-7c3b57c62faa.png)

## Errors
unfortunetly, this project was riddled with many errors that may of had a simple solution. It ate away a lot of my time and I couldn't the soultions in time.
I have completed my ansible and my jenkins pipline should work properly without this error
![image](https://user-images.githubusercontent.com/79215061/114326292-00401c80-9b2c-11eb-89eb-9d577ff58c5f.png)

## Reference 
Everything i learned from my trainners and my fellow cohort, without them, I wouldn't have gotten this far
My resources came from qa community, google and youtube.
 


