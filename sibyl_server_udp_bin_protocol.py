# -*- coding: utf-8 -*-
from twisted.internet.protocol import DatagramProtocol
import struct


class SibylServerUdpBinProtocol(DatagramProtocol):
    """The class implementing the Sibyl UDP binary server protocol.

        .. note::
            You must not instantiate this class.  This is done by the code
            called by the main function.

        .. note::

            You have to implement this class.  You may add any attribute and
            method that you see fit to this class.  You must implement the
            following method (called by Twisted whenever it receives a
            datagram):
            :py:meth:`~sibyl.main.protocol.sibyl_server_udp_bin_protocol.datagramReceived`
            See the corresponding documentation below.

    This class has the following attribute:

    .. attribute:: SibylServerProxy

        The reference to the SibylServerProxy (instance of the
        :py:class:`~sibyl.main.sibyl_server_proxy.SibylServerProxy` class).

            .. warning::

                All interactions between the client protocol and the server
                *must* go through the SibylServerProxy.

    """

    def __init__(self, sibylServerProxy):
        """The implementation of the UDP server text protocol.

        Args:
            sibylServerProxy: the instance of the server proxy.
        """
        self.sibylServerProxy = sibylServerProxy


    def datagramReceived(self, datagram, host_port):
        #line="Le mode binaire, je sais pas à quoi ca sert !"
	textLen=struct.unpack("I",datagram[4:6])[0]


        liste=struct.unpack('LI%ds'%textLen,datagram[6:])

        temps=liste[0]
        buf=struct.pack('LI50s',temps,struct.calcsize('LI50s'),line.encode('utf-8'))

	answer=b"yes"
	answerBin=struct.pack("LI%ds"%len(answer),time,len(answer),answer)

        self.transport.write(buf,host_port)

        """Called by Twisted whenever a datagram is received

        Twisted calls this method whenever a datagram is received.

        Args:
            datagram (bytes): the payload of the UPD packet;
            host_port (tuple): the source host and port number.

            .. warning::
                You must implement this method.  You must not change the
                parameters, as Twisted calls it.

        """
        pass
    
