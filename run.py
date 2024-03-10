import subprocess
from twisted.internet import reactor
from twisted.protocols import basic
from twisted.internet.protocol import Factory

class RTMPProtocol(basic.LineReceiver):
    def connectionMade(self):
        print("Client connected")

    def connectionLost(self, reason):
        print("Client disconnected")

    def lineReceived(self, line):
        print("Received data:", line)

class RTMPServerFactory(Factory):
    protocol = RTMPProtocol

def start_ffmpeg():
    argset = [
        'ffmpeg',
        '-re',
        '-i', 'C:/Users/alper/Downloads/Video/tez_bilg.mp4',
        '-c:v', 'libx264',
        '-preset', 'veryfast',
        '-tune', 'zerolatency',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-f', 'flv',
        'rtmp://localhost/live/testyayini'
    ]
    subprocess.Popen(argset, shell=True)    # pass argset as a bash script

if __name__ == "__main__":
    start_ffmpeg()  # call FFmpeg subprocess for video streaming

    reactor.listenTCP(1935, RTMPServerFactory())    # Start RTMP server
    print("RTMP server listening on port 1935")

    reactor.run()
