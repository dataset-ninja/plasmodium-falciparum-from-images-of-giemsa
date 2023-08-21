Dataset **Malaria Segmentation** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/P/J/wl/XGWgwkpbI6z8erhT12apM8yHZ8DE6LysYSWNYq7rjtU1SBh3SioDvsCVXvqyeG3xsU7KbtX7BIGIhpBGV9WKet6J3LY7Z36mFLez8gLhdF7PFtK4BGC38KgqtK31.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Malaria Segmentation', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/5bf2kmwvfn-1.zip).