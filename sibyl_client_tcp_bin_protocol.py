# -*- coding: utf-8 -*-
from twisted.internet.protocol import Protocol


import struct

print("[INFO1][client-protocol]: importing") 
print(str(Protocol))            

class SibylClientTcpBinProtocol(Protocol):
    """
    The class implementing the Sibyl TCP binary client protocol.  It has
    the following attribute:

    .. attribute:: proxy

        The reference to the SibylCientProxy (instance of the
        :py:class:`~sibyl.main.sibyl_client_proxy.SibylClientProxy` class).

        .. warning::
            All interactions between the client protocol and the user
            interface *must* go through the SibylClientProxy.  In other
            words you must call one of the methods of
            :py:class:`~sibyl.main.sibyl_client_proxy.SibylClientProxy`
            whenever you would like the user interface to do something.

    .. note::
        You must not instantiate this class.  This is done by the code
        called by the main function.

    .. note::
        You have to implement this class.  You may add any attribute and
        method that you see fit to this class.  You must implement two
        methods:
        :py:meth:`~sibyl.main.protocol.sibyl_cliend_udp_text_protocol.sendRequest`
        and
        :py:meth:`~sibyl.main.protocol.sibyl_cliend_udp_text_protocol.dataReceived`.
        See the corresponding documentation below.
    """


    print("[INFO2][client-protocol]: attribute:: proxy") 
    #print(str(proxy))
    def __init__(self, sibylProxy):
        """The implementation of the UDP Text Protocol.

        Args:
            sibylClientProxy: the instance of the client proxy,
                        this is the only way to interact with the user
                        interface;
        """
        self.clientProxy = sibylProxy
        
        print("[INFO3][client-protocol]: init") 
        print(str(sibylProxy))

    def connectionMade(self):
        """
        The Graphical User Interface (GUI) needs this function to know
        when to display the request window.

        DO NOT MODIFY IT.
        """
        self.clientProxy.connectionSuccess()

        print("[INFO3][client-protocol]: (GUI) window") 
        print(str(self.clientProxy.connectionSuccess()))

    def sendRequest(self, line):
        """Called by the controller to send the request

        The :py:class:`~sibyl.main.sibyl_client_proxy.SibylClientProxy` calls
        this method when the user clicks on the "Send Question" button.

        Args:
            line (string): the text of the question

        .. warning::
            You must implement this method.  You must not change the parameters,
            as the controller calls it.

        """
        pass
        print("[INFO4][client-protocol]: sendRequest(self, line)") 
        
        print(line)
        print(type(line))
        
        time=bytearray(4)
        print(type(time))
        
        packetLen=len(line)+6
        
       
   
        
        
        buf=bytearray(16)
        print(type(buf))
  
        
        text=line.encode('utf-8')
        
        #messageBin=time+packetLen
        
	buf=struct.pack("LH%ds"%len(text),time,len(text),text)

      
        struct.pack_into('4B',buf,0,0x4b,0x8e,0x73,0x94)

        struct.pack_into('B',buf,4,packetLen)
        struct.pack_into('8s',buf,6,text)
        struct.pack_into('2B',buf,14,13,10)
        
        self.transport.write(buf)
       
        t=b"\x41\x20\x79\x65\x61\x72"
        
        #self.transport.write(t)
        #self.transport.write(messageBin)
        
        

    def dataReceived(self, line):
        """Called by Twisted whenever a data is received

        Twisted calls this method whenever it has received at least one byte
        from the corresponding TCP connection.

        Args:
            line (bytes): the data received (can be of any length greater than
            one);

        .. warning::
            You must implement this method.  You must not change the parameters,
            as Twisted calls it.

        """
        pass
        print("[INFO5][client-protocol]: dataReceived(self, line)") 
        
        print(line)
        print(type(line))
    
