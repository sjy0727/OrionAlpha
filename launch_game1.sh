#!/bin/bash

# define color
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[1;36m'
NC='\033[0m' # No Color

# Set the terminal window title
echo -ne "${CYAN}
 ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄       ▄▄ ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░▌     ▐░░▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀▐░█▀▀▀▀▀▀▀█░▐░▌░▌   ▐░▐░▐░█▀▀▀▀▀▀▀▀▀
▐░▌         ▐░▌       ▐░▐░▌▐░▌ ▐░▌▐░▐░▌
▐░▌ ▄▄▄▄▄▄▄▄▐░█▄▄▄▄▄▄▄█░▐░▌ ▐░▐░▌ ▐░▐░█▄▄▄▄▄▄▄▄▄
▐░▌▐░░░░░░░░▐░░░░░░░░░░░▐░▌  ▐░▌  ▐░▐░░░░░░░░░░░▌
▐░▌ ▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀█░▐░▌   ▀   ▐░▐░█▀▀▀▀▀▀▀▀▀
▐░▌       ▐░▐░▌       ▐░▐░▌       ▐░▐░▌
▐░█▄▄▄▄▄▄▄█░▐░▌       ▐░▐░▌       ▐░▐░█▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▐░▌       ▐░▐░▌       ▐░▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ ▀         ▀ ▀         ▀ ▀▀▀▀▀▀▀▀▀▀▀
              ** OrionAlpha - GameServer **
${NC}\n"

# Set the classpath
export CLASSPATH=.:target/OrionAlpha.jar

# Run the Java application
java -Xmx600m -DgameID=1 -Dwzpath=data/ -Dio.netty.leakDetection.level=advanced -XX:NewRatio=50 -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:+HeapDumpOnOutOfMemoryError -XX:-DisableExplicitGC -Xnoclassgc -XX:+UseNUMA -XX:ReservedCodeCacheSize=48m -XX:MaxGCPauseMillis=300 -XX:GCPauseIntervalMillis=400 -XX:+UseTLAB -XX:+AlwaysPreTouch game.GameApp
