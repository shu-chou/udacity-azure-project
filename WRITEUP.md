
# Analysis

### Azure VM

With Azure Virtual Machines, we can create and use VMs in the cloud. VMs provide infrastructure as a service (IaaS) in the form of a virtualized server and can be used in many ways. Just like a physical computer, we can customize all of the software running on the VM. VMs are an ideal choice when we need:

- Total control over the operating system (OS).
- The ability to run custom software.
- To use custom hosting configurations.


An Azure VM gives us the flexibility of virtualization without having to buy and maintain the physical hardware that runs the VM. We still need to configure, update, and maintain the software that runs on the VM.


### Azure App service

App Service enables usto build and host web apps, background jobs, mobile back-ends, and RESTful APIs in the programming language of our choice without managing infrastructure. It offers automatic scaling and high availability. App Service supports Windows and Linux and enables automated deployments from GitHub, Azure DevOps, or any Git repo to support a continuous deployment model.


# Cost
At the time of writing

### Azure VM
The lowest instance in General purpose tier of VM will cost around $7.5920/month which will increase as we go up in the tier.

### Azure App Service

We pay for the Azure resources our app uses while it processes requests based on the App Service plan we choose. The App Service plan determines how much hardware is devoted to our host. For example, the plan determines whether it's dedicated or shared hardware and how much memory is reserved for it. There's even a free tier we can use to host small, low-traffic sites.


# Scalability

### Azure VM
In order to scale a VM we have two otpions available:
- Scale set 
- Azure Batch


### Azure App Service
It offers automatic scaling and high availability.


# Choice

We go with Azure App Service plan to deploy this project

# Justification
Based on the points mentioned above, since the deployed app doesnt need a full control over the OS nor does it require any legacy code to be deployed, we can safely use App Service as it provides the language of our choice and we dont have to worry about configuring the server. In App Service we have a free tier, hence it again adds to costing us less for deploying the app.



