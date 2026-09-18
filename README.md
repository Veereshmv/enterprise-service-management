# Enterprise Service Desk – Containerized Application on Azure

## Project Overview

This project demonstrates a containerized enterprise service desk application deployed on Microsoft Azure, with a focus on Docker, Azure DevOps CI/CD, Azure Container Registry (ACR), Azure App Service, and Azure SQL Database.

The application is built using FastAPI and allows users to create service requests and incidents, while support teams can view tickets, update ticket status, and add support updates.

Docker is used to package the application, with container images stored in Azure Container Registry. Azure DevOps YAML pipelines are used for code quality checks, automated testing, dependency and container security scanning, Docker image creation, and publishing images to ACR.

A separate Azure DevOps CD pipeline is used to deploy versioned container images from ACR to Azure App Service. The deployment process supports selecting specific image versions and rolling back to a previous container image when required.

Azure Managed Identity is used for secure access to Azure resources, including pulling container images from ACR. Azure SQL Database is used for persistent application data.

Overall, the project demonstrates the practical use of FastAPI, Docker, Azure DevOps, ACR, App Service, Azure SQL, Managed Identity, CI/CD, security scanning, and container version management on Microsoft Azure.

## Screenshots

## Architecture

![Enterprise Service Desk Architecture](https://github.com/Veereshmv/enterprise-service-management/blob/main/Archi1.png?raw=true)

### Service Desk

![Enterprise Service Desk Main Page](https://github.com/Veereshmv/enterprise-service-management/blob/main/Enterprise_Service_Desk_Main_Page.png?raw=true)

![Enterprise Service Desk Main Page](https://github.com/Veereshmv/enterprise-service-management/blob/main/Enterprise_Service_Desk_Main_Page_1.png?raw=true)

### Support Team

![Enterprise Service Desk Support Page](https://github.com/Veereshmv/enterprise-service-management/blob/main/Enterprise_Service_Desk_Support_Page.png?raw=true)

![Enterprise Service Desk Support Page](https://github.com/Veereshmv/enterprise-service-management/blob/main/Enterprise_Service_Desk_Support_Page_1.png?raw=true)

![Enterprise Service Desk Support Page](https://github.com/Veereshmv/enterprise-service-management/blob/main/Enterprise_Service_Desk_Support_Page_2.png?raw=true)
