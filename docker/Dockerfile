FROM maven:3.9.6-amazoncorretto-21 as builder
COPY settings.xml /usr/share/maven/conf/settings.xml

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

# 修改 ENTRYPOINT 使用 exec 形式
ENTRYPOINT ["sh", "-c", "java $SERVICE_OPTS $JAVA_OPTS -jar ./target/OrionAlpha.jar $MAIN_CLASS"]
