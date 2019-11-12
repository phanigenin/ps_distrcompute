from concurrent.futures import ThreadPoolExecutor

class PSCMultiThreadExecutor():
    '''
    Best to be used when doing IO operations, so async processing can happen
    CPU intensive operations should use MultiProcessing

    Workers created on a queue
    ALL workers joined at exit of Python environment ( workers are daemons )

    ThreadPoolExecutor supports:


    '''
    def __init__(self,appname='default',workers=5):
        import logging
        logger             = logging.getLogger(appname)
        self.executor      = ThreadPoolExecutor(max_workers=workers)
        logger.info('Initiated %d workers for app: %s'%(workers,appname))

    def submit(self):
        '''
        returns a list of future objects
        :return:
        '''
        pass

    def map(self,func,*args,timeout=600,**kwargs):
        '''
        maps a generator to function
        waits for everyone to finish
        returns a Iterator of results, NOT future objects
        :return:
        '''
        results = self.executor.map(func,*args,**kwargs,timeout=timeout)
        return list(results)
