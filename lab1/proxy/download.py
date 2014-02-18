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
    download_data = set()
    start = None

    def __init__(self, subject, request_count):
        super(ProxyDownloader, self).__init__(subject)
        if request_count == 1:
            ProxyDownloader.start = time.time()

    def get(self, url, filename):
        ProxyDownloader.download_data.update([(url, filename)])
        if time.time() > self.start + 5:
            print 'time expired - fire the download'
            for data in ProxyDownloader.download_data:
                self.subject.get(data[0], data[1])
            download_data = ProxyDownloader.download_data
            ProxyDownloader.download_data = []
            return download_data
        return None
