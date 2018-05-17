import ConfigParser
import traceback
import time
import sys

if __name__== "main":
 print 'Argyments :',sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
 resList=[]
 URL = sys.argv[1]
 username = sys.argv[2]
 password = sys.argv[3]
 sname = sys.argv[4]
 try:
    connect(username,password,URL)
    try:
     domainConfig()
     serverList=cmo.getServers();
     domainRuntime()
     cd('/ServerLifeCycleRuntimes/')
     for server in serverList:
          name=server.getName()
          cd(name)
          serverState=cmo.getState()
          resList.append('SVR:'+name +':'+serverState)
          cd('..')
    except Exception, e:
     traceback.print_exc()
     resList.append( server+':UNABLE_TO_CONNECT')
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
              resList.append('APP:'+appName.getName()+':'+curstate4)
    except Exception, e:
     traceback.print_exc()
     resList.append( 'APP:EXCEPTION:UNABLE_TO_CONNECT')
    disconnect()
 except Exception, e:
  resList.append( 'SVR'+ sname +':UNABLE_TO_CONNECT')
 print 'STARTCAPTURE'
 for p in resList: print p
 print 'ENDCAPTURE'
