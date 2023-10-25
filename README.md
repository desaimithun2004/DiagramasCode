# DiagramasCode

# The Diagrams package
Diagrams is a Python package that can be used for creating cloud system architecture diagrams and supports six major Cloud Providers including Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), Kubernetes, Alibaba Cloud and Oracle Cloud. Additionally, it also supports other commonly used technologies such as specific programming languages, frameworks, chat systems and many more nodes. At the same time, you also have the option to create custom nodes in order to serve your specific use-cases.

# Getting started with diagrams
## Prerequisite
You need Python 3.6 or higher installed on your machine
It uses [Graphviz] to render the diagram, so you need to [install Graphviz] to use diagrams.

[Graphviz]: https://www.graphviz.org/
[install Graphviz]: https://graphviz.gitlab.io/download/

```PowerShell
# On Windows using Chocolatey 
choco install graphviz
```

## Installing diagrams

```python
# using pip (pip3)
$ pip install diagrams
```

## Quick Start

```python
# diagram.py

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("aws basic", show=False):
    ELB("lb") >> EC2("web") >> RDS("db")
```

Run python diagram.py -> It will generate below diagram

![alt text][sample]

[sample]: https://github.com/desaimithun2004/DiagramasCode/blob/main/Images/sample.png

## Lets use this to generate data pipeline on GCP

```python
python DiagramasCode.py
```

![GCP architecture][gcp-datapipeline]

[gcp-datapipeline]: https://github.com/desaimithun2004/DiagramasCode/blob/main/data_pipeline_example_using_diagram_as_code.png


