Dataset **Plasmodium Falciparum from Images of Giemsa for Malaria Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://www.dropbox.com/scl/fi/4yk5ge0mgiavpqo3esnr9/plasmodium-falciparum-from-images-of-giemsa-for-malaria-detection-DatasetNinja.tar?rlkey=5gtchn7snkwi8q3zi3t9ec27u&dl=1)

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