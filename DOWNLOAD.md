Dataset **Plasmodium Falciparum from Images of Giemsa for Malaria Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTU4NV9QbGFzbW9kaXVtIEZhbGNpcGFydW0gZnJvbSBJbWFnZXMgb2YgR2llbXNhIGZvciBNYWxhcmlhIERldGVjdGlvbi9wbGFzbW9kaXVtLWZhbGNpcGFydW0tZnJvbS1pbWFnZXMtb2YtZ2llbXNhLWZvci1tYWxhcmlhLWRldGVjdGlvbi1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJNZHJxZDdXbjlyOUk0WGJDcUtYRCtBZmljdEUzVndLZzRzZkFnUmsxdldNPSJ9?response-content-disposition=attachment%3B%20filename%3D%22plasmodium-falciparum-from-images-of-giemsa-for-malaria-detection-DatasetNinja.tar%22)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Plasmodium Falciparum from Images of Giemsa for Malaria Detection', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/5bf2kmwvfn-1.zip).