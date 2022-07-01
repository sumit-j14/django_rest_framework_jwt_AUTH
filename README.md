# django_rest_framework_jwt_AUTH
user can be alloted with a jwt token upon Email verifications, Otp verification and login  
this token is embedded in request header each time that user is communicating with servers  
this token gets stored in servers and keeps refreshing after given time interval  
# new token gets allotted to the user  
![new_token](https://user-images.githubusercontent.com/72104547/176961240-cf5492a8-2c8e-43a8-aec2-63f456ca709d.png)  
# no response without this token added in bearer token header  
![no response](https://user-images.githubusercontent.com/72104547/176961363-a3e93de1-0183-4a3a-accf-804522f05998.png)  
# Response given after jwt authentication success  
![Screenshot from 2022-07-02 01-18-30](https://user-images.githubusercontent.com/72104547/176961453-8017a24a-ec4f-4896-b001-b17a340725b9.png)
