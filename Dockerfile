# docker build -t python-ifc-it .
# docker run -it python-ifc-it 
FROM continuumio/miniconda3

RUN conda install -c conda-forge ifcopenshell

ADD ifc.py .

ADD Duplex_A.ifc .

CMD ["python", "ifc.py"]