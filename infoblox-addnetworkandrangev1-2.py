#This script adds a network and a range to the infoblox appliance
#Change the network variables (e.g. 10.3.6 to 10.2.6) in the whole script
#Replace numbers by typing :%s/10.3./10.x./g (x is replacement)
#v1-1: added telephony options and PXE options in JSON format 
#
#change: username&password, ip-address, domain name
#
import requests
import json
#ignore certificate warnings
import warnings
#importing commandline arguments
import sys
#
#defining commandline arguments
octet = (sys.argv[1])
#
#ignore certificate warnings
warnings.filterwarnings("ignore")
#
session = requests.Session()
session.auth = ('xxx', 'xxx')
session.verify = False
#
url = 'https://1.2.3.4/wapi/v2.11.1/'
#
beheernetwork ={
        'network': "10.{}.2.0/24".format(octet),
        'comment': 'beheer',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.2.1".format(octet)
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
beheern = session.post(url + 'network', json=beheernetwork)
#
beheerrange ={
        'end_addr':"10.{}.2.250".format(octet),
        'start_addr':"10.{}.2.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
beheerr = session.post(url + 'range', json=beheerrange)
#
beheern.status_code
beheerr.status_code
print("BEHEER")
print("<-- network -->")
print beheern
print("<-- range -->")
print beheerr
#
betalingnetwork ={
        'network': "10.{}.3.0/24".format(octet),
        'comment': 'betaling',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.3.1".format(octet)
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
bn = session.post(url + 'network', json=betalingnetwork)
#
betalingrange ={
        'end_addr':"10.{}.3.250".format(octet),
        'start_addr':"10.{}.3.15".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
br = session.post(url + 'range', json=betalingrange)
#
bn.status_code
br.status_code
print("BETALING")
print("<-- network -->")
print bn
print("<-- range -->")
print br
#
telefonienetwork ={
        'network': "10.{}.4.0/24".format(octet),
        'comment': 'telefonie',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.4.1".format(octet)
                },
            {
                'name':'vendor-encapsulated-options',
                'num':43,
                'value':'id:ipphone.mitel.com;sw_tftp=10.241.84.13;call_srv=10.241.84.13,10.50.4.2;l2p=6;dscp=46'
                },
            {
                'name':'vivso',
                'num':125,
                'value':'id:ipphone.mitel.com;sw_tftp=10.241.84.13;call_srv=10.241.84.13,10.50.4.2;l2p=6;dscp=46'
                },
            {
                'name':'mitel-tftp',
                'num':128,
                'value':'10.241.84.13'
                },
            {
                'name':'mitel-rtc',
                'num':129,
                'value':'10.241.84.13'
                },
            {
                'name':'mitel-ip-phone-indent',
                'num':130,
                'value':'MITEL IP PHONE'
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
tn = session.post(url + 'network', json=telefonienetwork)
#
telefonierange ={
        'end_addr':"10.{}.4.250".format(octet),
        'start_addr':"10.{}.4.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
tr = session.post(url + 'range', json=telefonierange)
#
tn.status_code
tr.status_code
print("TELEFONIE")
print("<-- network -->")
print tn
print("<-- range -->")
print tr
#
alarmnetwork ={
        'network': "10.{}.5.0/24".format(octet),
        'comment': 'alarm',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.5.1".format(octet)
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
an = session.post(url + 'network', json=alarmnetwork)
#
alarmrange ={
        'end_addr':"10.{}.5.250".format(octet),
        'start_addr':"10.{}.5.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
ar = session.post(url + 'range', json=alarmrange)
#
an.status_code
ar.status_code
print("ALARM")
print("<-- network -->")
print an
print("<-- range -->")
print ar
#
cameranetwork ={
        'network': "10.{}.6.0/24".format(octet),
        'comment': 'camera',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.6.1".format(octet)
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
cn = session.post(url + 'network', json=cameranetwork)
#
camerarange ={
        'end_addr':"10.{}.6.250".format(octet),
        'start_addr':"10.{}.6.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
cr = session.post(url + 'range', json=camerarange)
#
cn.status_code
cr.status_code
print("CAMERA")
print("<-- network -->")
print cn
print("<-- range -->")
print cr
#
medianetwork ={
        'network': "10.{}.7.0/24".format(octet),
        'comment': 'media',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.7.1".format(octet)
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
mn = session.post(url + 'network', json=medianetwork)
#
mediarange ={
        'end_addr':"10.{}.7.250".format(octet),
        'start_addr':"10.{}.7.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
mr = session.post(url + 'range', json=mediarange)
#
mn.status_code
mr.status_code
print("MEDIA")
print("<-- network -->")
print mn
print("<-- range -->")
print mr
#
printernetwork ={
        'network': "10.{}.170.0/23".format(octet),
        'comment': 'printer',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.170.1".format(octet)
                },
            {
                'name':'domain-name',
                'value':'printers.xxx.local'
                },
            {
                'name':'dhcp-lease-time',
                'value':'1814400'
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
pn = session.post(url + 'network', json=printernetwork)
#
printerrange ={
        'end_addr':"10.{}.171.250".format(octet),
        'start_addr':"10.{}.170.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
pr = session.post(url + 'range', json=printerrange)
#
pn.status_code
pr.status_code
print("PRINTER")
print("<-- network -->")
print pn
print("<-- range -->")
print pr
#
iotnetwork ={
        'network': "10.{}.194.0/23".format(octet),
        'comment': 'iot',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.194.1".format(octet)
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
iotn = session.post(url + 'network', json=iotnetwork)
#
iotrange ={
        'end_addr':"10.{}.195.250".format(octet),
        'start_addr':"10.{}.194.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
iotr = session.post(url + 'range', json=iotrange)
#
iotn.status_code
iotr.status_code
print("IOT")
print("<-- network -->")
print iotn
print("<-- range -->")
print iotr
#
b2bnetwork ={
        'network': "10.{}.220.0/23".format(octet),
        'comment': 'b2b',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.220.1".format(octet)
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
b2bn = session.post(url + 'network', json=b2bnetwork)
#
b2brange ={
        'end_addr':"10.{}.221.250".format(octet),
        'start_addr':"10.{}.220.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
b2br = session.post(url + 'range', json=b2brange)
#
b2bn.status_code
b2br.status_code
print("B2B")
print("<-- network -->")
print b2bn
print("<-- range -->")
print b2br
#
domeinnetwork ={
        'network': "10.{}.224.0/22".format(octet),
        'comment': 'domein',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.224.1".format(octet)
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
domeinn = session.post(url + 'network', json=domeinnetwork)
#
domeinrange ={
        'end_addr':"10.{}.227.250".format(octet),
        'start_addr':"10.{}.224.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
domeinr = session.post(url + 'range', json=domeinrange)
#
domeinn.status_code
domeinr.status_code
print("DOMEIN")
print("<-- network -->")
print domeinn
print("<-- range -->")
print domeinr
#
nietdomeinnetwork ={
        'network':"10.{}.240.0/20".format(octet),
        'comment': 'niet-domein',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.240.1".format(octet)
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
nietdomeinn = session.post(url + 'network', json=nietdomeinnetwork)
#
nietdomeinrange ={
        'end_addr':"10.{}.255.250".format(octet),
        'start_addr':"10.{}.240.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
nietdomeinr = session.post(url + 'range', json=nietdomeinrange)
#
nietdomeinn.status_code
nietdomeinr.status_code
print("NIET-DOMEIN")
print("<-- network -->")
print nietdomeinn
print("<-- range -->")
print nietdomeinr
#
quarantainenetwork ={
        'network': "10.{}.239.0/24".format(octet),
        'comment': 'quarantaine',
        'network_view':'default',
        'options':[
            {
                'name':'routers',
                'value':"10.{}.239.1".format(octet)
                },
            {
                'name':'vendor-class-identifier',
                'num':60,
                'value':'PXEClient'
                }
            ],
        'members': [
            {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
            ]
        }
quarantainen = session.post(url + 'network', json=quarantainenetwork)
#
quarantainerange ={
        'end_addr':"10.{}.239.250".format(octet),
        'start_addr':"10.{}.239.10".format(octet),
        'server_association_type':'MEMBER',
        'member': {
                '_struct':'dhcpmember',
                'ipv4addr':'10.241.20.233',
                'name':'infoblox.xxx.local'
            }
        }
quarantainer = session.post(url + 'range', json=quarantainerange)
#
quarantainen.status_code
quarantainer.status_code
print("QUARANTAINE")
print("<-- network -->")
print quarantainen
print("<-- range -->")
print quarantainer
#
