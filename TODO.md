#Docker Build Image: gerador_relatorios
    ## Build local image no flags 
    docker build -t gerador_relatorio .
    
    ## No Cache full log on console
    docker build --no-cache --progress=plain -t gerador_relatorio .

    ## Use Cached full log on console
    docker build --progress=plain -t gerador_relatorio .



#Docker Dev containers 

docker run -it -v ./gerador_relatorio:/usr/share/gerador_relatorio gerador_relatorio sh
    
docker run -it  gerador_relatorio sh      

# Run tests on source folder (/usr/share/gerador_relatorio) 
pytest ../

