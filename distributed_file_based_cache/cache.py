from django.core.cache.backends.filebased import FileBasedCache
from serviceless_distributor.distributor import Distributor


class DistributedFileBasedCache(FileBasedCache):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for method in ["add", "set", "touch", "delete", "clear"]:
            setattr(
                self, method, Distributor.register_function()(getattr(self, method))
            )
