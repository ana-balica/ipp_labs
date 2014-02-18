import time
import urllib


class Downloader(object):
    """ Simple downloader class """
    def get(self, url, filename):
        urllib.urlretrieve(url, filename)


class Proxy(object):
    """ Generic proxy class """
    def __init__(self, subject):
        self.subject = subject
    def __getattr__(self, name):
        return getattr(self.subject, name) 


class ProxyDownloader(Proxy):
    """ Proxy downloader class """
    start = time.time()
    download_data = []

    def get(self, url, filename):
        ProxyDownloader.download_data.extend([(url, filename)])
        if time.time() > ProxyDownloader.start + 7:
            for data in ProxyDownloader.download_data:
                self.subject.get(data[0], data[1])