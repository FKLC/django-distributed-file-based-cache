# Django Distributed File Based Cache
The Django Distributed File Based Cache is a library that I developed for myself to use in my small projects.

## How it works?
Thanks to my other library([Django Serviceless Distributor](https://github.com/FKLC/django-serviceless-distributor)) I can distribute any functions easily across nodes so I wrote a cache backend if you wonder how it works you should definitely see [Django Serviceless Distributor](https://github.com/FKLC/django-serviceless-distributor)

## Is it efficient to use?
The answer is depends on how many nodes you have in your environment. If it is over 5 that maybe useless because you know if you can pay for 5 why not 1 for the cache. Also replicating data across request processing servers not the best approach.

## Quick Start
Install library
```bash
pip install django-distributed-file-based-cache
```

Configure your `urls.py`
```py
  ....
  path("", include("distributed_file_based_cache.urls")),
  ....
```

Configure your `settings.py`
```py
# Set as cache backend
CACHES = {
    "default": {
        "BACKEND": "distributed_file_based_cache.cache.DistributedFileBasedCache",
        "LOCATION": "cache",
    }
}

# Nodes IPs (Do not use load balancer IP, we couldn't know
# if all nodes affected if you use load balancer IP)
SERVICELESS_DISTRIBUTOR_NODES = ["http://10.0.0.0", "http://10.0.0.1", ...]
```


### (Not) Frequently Asked Questions
Most of the answers can be found on [Django Serviceless Distributor](https://github.com/FKLC/django-serviceless-distributor) but I'll update if I'll receive specific question about this library.
