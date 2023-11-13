Dataset **Plasmodium Falciparum from Images of Giemsa for Malaria Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/8/m/2F/NuBw7bIkv26zkz1IKjQepH0ur3CXkPWRylTUzmvJ4F2SxaLzPPF36ohhNmiOuXfp7JaFyO8arglnZLpr4BBH1cyaxnPEi8mmJ7k5dyPoPeUVkS4c8L0etOZWBuBy.tar)

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