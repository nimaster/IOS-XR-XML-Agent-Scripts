import sys
import os
import pexpect
import time

x = 1

tun = '''
<?xml version="1.0" encoding="UTF-8"?> 
<Request MajorVersion="1" MinorVersion="0">
  <Set>
    <Configuration>
      <InterfaceConfigurationTable>
        <InterfaceConfiguration>
          <Naming>
            <Active>act</Active>
            <InterfaceName>tunnel-te40%s</InterfaceName>
           </Naming>
           <InterfaceVirtual>true</InterfaceVirtual>
           <TunnelTEAttributes>
            <AutoBandwidth>
              <Enabled>true</Enabled>
                <BandwidthLimits>
                  <BandwidthMinLimit>5000</BandwidthMinLimit>
                  <BandwidthMaxLimit>5000000</BandwidthMaxLimit>
                </BandwidthLimits>
              <Overflow>
                <OverflowThresholdPercent>5</OverflowThresholdPercent>
                <OverflowThresholdValue>10000</OverflowThresholdValue>
                <OverflowThresholdLimit>5</OverflowThresholdLimit>
              </Overflow>
              <AdjustmentThreshold>
                <AdjustmentThresholdPercent>5</AdjustmentThresholdPercent>
                <AdjustmentThresholdValue>10000</AdjustmentThresholdValue>
              </AdjustmentThreshold>
              <Underflow>
                <UnderflowThresholdPercent>5</UnderflowThresholdPercent>
                <UnderflowThresholdValue>10000</UnderflowThresholdValue>
                <UnderflowThresholdLimit>10</UnderflowThresholdLimit>
              </Underflow>
              <ApplicationFrequency>30</ApplicationFrequency>
              <ResignalLastBandwidthTimeOut>2</ResignalLastBandwidthTimeOut>
            </AutoBandwidth>
            <Destination>2.2.2.2</Destination>
            <FastReroute>
              <BandwidthProtection>0</BandwidthProtection>
              <NodeProtection>0</NodeProtection>
            </FastReroute>
           </TunnelTEAttributes>                 
        </InterfaceConfiguration>
      </InterfaceConfigurationTable>
    </Configuration>
  </Set>
</Request>

''' % (x)

print(tun)

print("APPLYING CONFIG CHANGE VIA XML AGENT")

ssh = pexpect.spawn('ssh cisco@10.225.251.6')
ssh.expect(['password', 'Password'])
ssh.sendline('cisco')
ssh.expect('[>#]')
ssh.sendline('xml echo format')
ssh.expect('[>>]')
ssh.sendline(tun)
ssh.expect('[>>]')
ssh.sendline('''
<?xml version="1.0" encoding="UTF-8"?>
<Request MajorVersion="1" MinorVersion="0">
  <Commit Mode="Atomic" Comment="MPLS-TE config update"/>
</Request>
''')
ssh.expect('[>>]')


