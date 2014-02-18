import os.path
import time
import urllib


DOWNLOAD_TIMEOUT = 5


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
    download_data = set()
    start = None

    def __init__(self, subject, request_count):
        super(ProxyDownloader, self).__init__(subject)
        if request_count == 1:
            ProxyDownloader.start = time.time()

    def get(self, url, filename):
        ProxyDownloader.download_data.update([(url, filename)])
        if time.time() > ProxyDownloader.start + DOWNLOAD_TIMEOUT:
            for data in ProxyDownloader.download_data:
                self.subject.get(data[0], data[1])
            download_data = ProxyDownloader.download_data
            ProxyDownloader.download_data = []
            return download_data
        return None


class CachingProxyDownloader(Proxy):
    """ Caching proxy downloader class """
    download_data = set()
    start = None

    def __init__(self, subject, request_count):
        super(CachingProxyDownloader, self).__init__(subject)
        if request_count == 1:
            CachingProxyDownloader.start = time.time()       


    def get(self, url, filename):
        CachingProxyDownloader.download_data.update([(url, filename)])
        if time.time() > CachingProxyDownloader.start + DOWNLOAD_TIMEOUT:
            for data in CachingProxyDownloader.download_data:
                if not os.path.isfile(data[1]):
                    self.subject.get(data[0], data[1])
            download_data = CachingProxyDownloader.download_data
            CachingProxyDownloader.download_data = []
            return download_data
        return None
