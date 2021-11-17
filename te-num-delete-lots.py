import sys
import os
import pexpect
import time

x = 410

ssh = pexpect.spawn('ssh cisco@10.225.251.6')
ssh.expect(['password', 'Password'])
ssh.sendline('cisco')
ssh.expect('[>#]')
ssh.sendline('xml echo format')
ssh.expect('[>>]')
while x < 420:
  tun = '''
<?xml version="1.0" encoding="UTF-8"?> 
<Request MajorVersion="1" MinorVersion="0">
  <Delete>
    <Configuration>
      <InterfaceConfigurationTable>
        <InterfaceConfiguration>
          <Naming>
            <Active>act</Active>
            <InterfaceName>tunnel-te%s</InterfaceName>
           </Naming>
        </InterfaceConfiguration>
      </InterfaceConfigurationTable>
    </Configuration>
  </Delete>
</Request>

''' % (x)



  ssh.sendline(tun)
  ssh.expect('[>>]')
  print("Tunnel", x,"Deleted")
  x+=1  
ssh.sendline('''
<?xml version="1.0" encoding="UTF-8"?>
<Request MajorVersion="1" MinorVersion="0">
  <Commit Mode="Atomic" Comment="MPLS-TE config update"/>
</Request>
''')
ssh.expect('[>>]')

print("COMPLETE")
