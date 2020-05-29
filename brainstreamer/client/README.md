
## Client

The client is available as brainstreamer.client and exposes the following API:

```pycon
>>> from brainstreamer.client import upload_sample
>>> upload_sample(host= '127.0.0.1' , port= 8000 , num_of_snaps_to_read=20 , sample_path= 'sample.mind.gz' )
… # upload 20 snapshots from path to host : port
```

And the following CLI:

```
$ python -m brainstreamer.client upload-sample \
-h/--host '127.0.0.1' \
-p/--port 8000 \
'snapshot.mind.gz'
…
```

### Note:
If not necessary, try to use small values for the  ```num_of_snaps_to_read``` parameter to ensure a smooth and fast flow.
