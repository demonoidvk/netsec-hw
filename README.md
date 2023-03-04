#Setting up targetVM 

Setup targetVM as per instructions: NwSec/targetVm-README.md at master · jhu-information-security-institute/NwSec · GitHub 

$ wget https://raw.githubusercontent.com/jhu-information-security-institute/NwSec/master/applications/termsvr/termsvr_UbuntuServerX86-64.sh 
$ chmod +x termsvr_UbuntuServerX86-64.sh 
$ ./termsvr_UbuntuServerX86-64.sh 

cd Downloads/termsvr/applications/termsvr/UbuntuServerX86-64/ 

TODO: make a repository of the docker containers and their config files 

docker build -t tgamesvr . 

sudo docker run -d --name gamesvr --hostname gamesvr.netsec-docker.isi.jhu.edu --add-host gamesvr.netsec-docker.isi.jhu.edu:127.0.1.2 --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --security-opt seccomp=unconfined --cgroup-parent=docker.slice --cgroupns private --tmpfs /tmp --tmpfs /run --tmpfs /run/lock --network host -p 2323:23 -p 2222:22 -p 4040:8080 --cpus=1 tgamesvr:latest 

docker exec -it gamesvr bash 

docker build -t tapisvr . 

docker run -d --name apisvr --hostname apisvr.netsec-docker.isi.jhu.edu --add-host apisvr.netsec-docker.isi.jhu.edu:127.0.1.1 --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --security-opt seccomp=unconfined --cgroup-parent=docker.slice --cgroupns private --tmpfs /tmp --tmpfs /run --tmpfs /run/lock --network host -p 2300:23 -p 2200:22 -p 5050:8080 --cpus=1 tapisvr:latest 

docker exec -it apisvr bash 

docker build -t ttelnetsvr . 

docker run -d --name telnetsvr --hostname telnetsvr.netsec-docker.isi.jhu.edu --add-host telnetsvr.netsec-docker.isi.jhu.edu:127.0.1.1 --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --security-opt seccomp=unconfined --cgroup-parent=docker.slice --cgroupns private --tmpfs /tmp --tmpfs /run --tmpfs /run/lock --network host -p 2303:23 -p 2202:22 --cpus=1 ttelnetsvr:latest 

docker exec -it telnetsvr bash 
