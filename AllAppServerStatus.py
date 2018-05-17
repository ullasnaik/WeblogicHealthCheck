import ConfigParser
import traceback
import time

if __name__== "main":
 sections=['host','ui','soa','o2o', 'odi','documaker','bip','oid_internal']
 print sections
 for sec in sections:
   config = ConfigParser.ConfigParser()
   config.read('envdtls.cfg')
   URL = config.get(sec,sec+'_url')
   username = config.get(sec,sec+'_username')
   password = config.get(sec,sec+'_password')
   sname=config.get(sec,sec+'_name')
   try:
      connect(username,password,URL)
      try:
       domainConfig()
       serverList=cmo.getServers();
       domainRuntime()
       cd('/ServerLifeCycleRuntimes/')
       print 'STARTCAPTURE'
       for server in serverList:
            name=server.getName()
            cd(name)
            serverState=cmo.getState()
            print  name +':'+serverState
            cd('..')
       print 'ENDCAPTURE'
      except Exception, e:
       traceback.print_exc()
       print 'STARTCAPTURE'
       print server+':UNABLE_TO_CONNECT'
       print 'ENDCAPTURE'
       continue
      cd('/')
      try:
       serverConfig()
       cd ('AppDeployments')
       myapps=cmo.getAppDeployments() 
       for appName in myapps:
          domainConfig()
          cd ('/AppDeployments/'+appName.getName()+'/Targets')
          mytargets = ls(returnMap='true')
          domainRuntime()
          cd('AppRuntimeStateRuntime')
          cd('AppRuntimeStateRuntime')
          for targetinst in mytargets:
             App=appName.getName();
             curstate4=cmo.getCurrentState(appName.getName(),targetinst)
             if App.startswith("obp") or App=="em" or App=="wsm-pm" or App=="oraclediagent":
                print 'STARTCAPTURE'
                print 'SVRAPPDTLS:',appName.getName(),':',curstate4
                print 'ENDCAPTURE'
      except Exception, e:
       traceback.print_exc()
       print 'STARTCAPTURE'
       print 'EXCEPTION:UNABLE_TO_CONNECT'
       print 'ENDCAPTURE'
       continue
      print 'STARTCAPTURE'
      print  'ENVNAME:'+sname
      print 'ENDCAPTURE'
      disconnect()
   except Exception, e:
    print 'STARTCAPTURE'
    print  sec+':UNABLE_TO_CONNECT'
    print  'ENVNAME:'+sname
    print 'ENDCAPTURE'






