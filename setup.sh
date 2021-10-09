wget http://www.modcoderpack.com/files/mcp940.zip

mkdir mcp

cd mcp
unzip ../mcp940.zip

wget https://launcher.mojang.com/v1/objects/909823f9c467f9934687f136bc95a667a0d19d7f/client.jar -O jars/minecraft.jar
mkdir jars/versions
mkdir jars/versions/1.12
cp jars/minecraft.jar jars/versions/1.12/1.12.jar
wget https://launchermeta.mojang.com/v1/packages/367843437acbae63de3084dd6afd3dd8bd2a7479/1.12.json -O jars/versions/1.12/1.12.json
wget https://launcher.mojang.com/v1/objects/8494e844e911ea0d63878f64da9dcc21f53a3463/server.jar -O jars/minecraft_server.jar
cd ..

pwd

cd mcp
./decompile.sh
cd ..

mkdir src
mkdir src/main
mkdir src/main/java
mkdir src/main/resources
cp -r mcp/src/minecraft_server/* src/main/java
cp -r mcp/jars/assets src/main/resources
cp -r mcp/temp/src/minecraft_server/log4j2.xml src/main/resources

python3 build.py . patches

chmod +x gradlew && ./gradlew build