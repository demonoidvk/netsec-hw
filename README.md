Setting up targetVM 

Setup targetVM as per instructions: NwSec/targetVm-README.md at master · jhu-information-security-institute/NwSec · GitHub 

Create 3 different network-adapters, and make sure to re-generate the mac-addresses for each adapter 

On targetvm, also run: sudo apt update, sudo apt install python3-pip 

$ cd Downloads/ && mkdir servers && cd servers 

$ git clone https://github.com/demonoidvk/netsec-hw.git 

$ unzip apiserver.zip

$ cp -r Tetris-AI/ gamesvr/. && cd gamesvr 

$ docker build -t tgamesvr . 

$ sudo docker run -d --name gamesvr --hostname gamesvr.netsec-docker.isi.jhu.edu --add-host gamesvr.netsec-docker.isi.jhu.edu:127.0.1.2 --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --security-opt seccomp=unconfined --cgroup-parent=docker.slice --cgroupns private --tmpfs /tmp --tmpfs /run --tmpfs /run/lock --network host -p 2323:23 -p 2222:22 -p 4040:8080 --cpus=1 tgamesvr:latest 

$ cd .. && cp -r apiserver/ apisvr/. && cd apisvr 

$ docker build -t tapisvr . 

$ docker run -d --name apisvr --hostname apisvr.netsec-docker.isi.jhu.edu --add-host apisvr.netsec-docker.isi.jhu.edu:127.0.1.1 --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --security-opt seccomp=unconfined --cgroup-parent=docker.slice --cgroupns private --tmpfs /tmp --tmpfs /run --tmpfs /run/lock --network host -p 2300:23 -p 2200:22 -p 5050:8080 --cpus=1 tapisvr:latest 

$ cd ../telnetsvr 

$ docker build -t ttelnetsvr . 

$ docker run -d --name telnetsvr --hostname telnetsvr.netsec-docker.isi.jhu.edu --add-host telnetsvr.netsec-docker.isi.jhu.edu:127.0.1.1 --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --security-opt seccomp=unconfined --cgroup-parent=docker.slice --cgroupns private --tmpfs /tmp --tmpfs /run --tmpfs /run/lock --network host -p 2303:23 -p 2202:22 --cpus=1 ttelnetsvr:latest 

$ cd ../telnetclient 

$ docker build -t ttelnetclt . 

$ docker run -d --name telnetclt --hostname telnetclt.netsec-docker.isi.jhu.edu --add-host telnetclt.netsec-docker.isi.jhu.edu:127.0.1.1 --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --security-opt seccomp=unconfined --cgroup-parent=docker.slice --cgroupns private --tmpfs /tmp --tmpfs /run --tmpfs /run/lock --network host -p 2305:23 -p 2204:22 --cpus=1 ttelnetclt:latest 
