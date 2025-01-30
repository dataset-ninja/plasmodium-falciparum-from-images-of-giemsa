Dataset **Plasmodium Falciparum from Images of Giemsa for Malaria Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE1ODVfUGxhc21vZGl1bSBGYWxjaXBhcnVtIGZyb20gSW1hZ2VzIG9mIEdpZW1zYSBmb3IgTWFsYXJpYSBEZXRlY3Rpb24vcGxhc21vZGl1bS1mYWxjaXBhcnVtLWZyb20taW1hZ2VzLW9mLWdpZW1zYS1mb3ItbWFsYXJpYS1kZXRlY3Rpb24tRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiZjltbHNDMC9iRVdyaUhXVk1VTE1CTGFYRDVYVmozcDZFMVdDL2UxaWQ4MD0ifQ==)

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