#LABEL authors="sjy0727"
#
##ENTRYPOINT ["top", "-b"]
#
## 基础镜像
#FROM openjdk:11-jre-slim
#
## 复制项目文件到镜像中
#COPY . /app
#
## 复制 launch_login.sh 脚本到镜像中
#COPY launch_login.sh /app/launch_login.sh
#
## 赋予脚本执行权限
#RUN chmod +x /app/launch_login.sh
#
## 设置工作目录
#WORKDIR /app
#
## 执行脚本启动应用
#ENTRYPOINT ["/app/launch_login.sh"]

LABEL authors="sjy0727"

FROM maven:3.9.6-amazoncorretto-21 as builder

WORKDIR /opt/server

COPY ./pom.xml ./pom.xml
COPY ./src ./src

RUN mvn clean package -U

FROM eclipse-temurin:21.0.4_7-jre-alpine

WORKDIR /opt/server

RUN mkdir -p ./target

COPY --from=builder /opt/server/target/OrionAlpha.jar ./target

EXPOSE 8383 8484 8585 8686 8787 8888

ENV CLASSPATH=.:/target/OrionAlpha.jar

# 设置公共的 JVM 启动参数
ENV JAVA_OPTS="-Dio.netty.leakDetection.level=advanced -Xmx500m -XX:NewRatio=50 -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:+HeapDumpOnOutOfMemoryError -XX:-DisableExplicitGC -Xnoclassgc -XX:+UseNUMA -XX:ReservedCodeCacheSize=48m -XX:MaxGCPauseMillis=300 -XX:GCPauseIntervalMillis=400 -XX:+UseTLAB -XX:+AlwaysPreTouch"

#java -Xmx600m -DgameID=0 -Dwzpath=data/ -Dio.netty.leakDetection.level=advanced -XX:NewRatio=50 -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:+HeapDumpOnOutOfMemoryError -XX:-DisableExplicitGC -Xnoclassgc -XX:+UseNUMA -XX:ReservedCodeCacheSize=48m -XX:MaxGCPauseMillis=300 -XX:GCPauseIntervalMillis=400 -XX:+UseTLAB -XX:+AlwaysPreTouch game.GameApp

ENTRYPOINT ["java","$SERVICE_OPTS","$JAVA_OPTS","-jar","./target/OrionAlpha.jar","$MAIN_CLASS"]

