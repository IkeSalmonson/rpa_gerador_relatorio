Docker Build Image: gerador_relatorios
    docker build -t gerador_relatorios .
    
    docker build --no-cache --progress=plain -t gerador_relatorios .


Docker Dev

docker run -it -v ./gerador_relatorios:/usr/share/gerador_relatorios gerador_relatorios sh
    
    docker run -it  gerador_relatorios sh      


