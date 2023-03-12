{
sleep 2
echo telsvr
sleep 2
echo passwd
sleep 2
echo "echo exiting && curl http://gamesvr.netsec-docker.isi.jhu.edu:4040"
sleep 2
echo exit
} | telnet 192.168.25.127
