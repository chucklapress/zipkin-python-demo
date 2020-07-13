# open tracing demo with python and zipkin

demonstration code to examine zipkin as open tracing tool

## Installation
Simplest way to get Zipkin up and running is via Docker
```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```
Interesting reading on Zipkin here:
[zipkin](https://zipkin.io/)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip install requirements.txt
```

## Usage

```python
python tracingtozipkin.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
