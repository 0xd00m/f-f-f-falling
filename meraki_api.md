Checkout out the [Explore](https://developer.cisco.com/meraki/explore/) section for open source projects, or browse the [Marketplace](https://apps.meraki.io/) for partner solutions.

Sandbox Meraki [Devnet](https://devnetsandbox.cisco.com/RM/Diagram/Index/a9487767-deef-4855-b3e3-880e7f39eadc?diagramType=Topology) 

Access Details:  
The read-only Meraki sandbox network can be accessed via Meraki Cloud based dashboard at:  

-   [DevNet Always On Read Only](https://account.meraki.com/secure/login/dashboard_login)

Using the following credentials:  

-   Username: devnetmeraki@cisco.com
-   Password: Adm!n123!
-   You can also use this API key for the Dashboard API: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0

Meraki Postman collection and webhooks https://www.postman.com/meraki-api/workspace/cisco-meraki-s-public-workspace/collection/897512-42355ad3-0145-48c6-8e65-e4bb9f180939?ctx=documentation

Meraki Postman guide https://developer.cisco.com/meraki/build/meraki-postman-collection-getting-started/#!introduction

Meraki API v1 https://documenter.getpostman.com/view/897512/SzYXYfmJ

Use Meraki Dashboard API - v1.21.0.postman_collection.json file to import collection in a non postman rest client

Test with
```bash
curl https://api.meraki.com/api/v1/organizations \
  -H 'X-Cisco-Meraki-API-Key: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
  ```

Expected result 
![screenshot-1653425105](https://user-images.githubusercontent.com/42084500/170133190-71694fcd-2b81-4404-a495-3a53f4af70a5.png)


Meraki API endpoint listing and documentation https://developer.cisco.com/meraki/api-v1/


{{baseUrl}}/organizations/{organizationId}/devices

![screenshot-1653425706](https://user-images.githubusercontent.com/42084500/170133217-5c3e199f-9348-483d-8315-a77dfbd92be9.png)


{{baseUrl}}/organizations/{organizationId}/devices

![screenshot-1653426062](https://user-images.githubusercontent.com/42084500/170133245-b942329f-00ab-47db-b747-3a37ef339555.png)
