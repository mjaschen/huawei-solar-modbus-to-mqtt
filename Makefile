.PHONY: build-docker-image
build-docker-image:
	docker build -t huawei-sun2000-modbus-to-mqtt:latest .
