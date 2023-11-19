.PHONY: build-docker-image
build-docker-image:
	docker build -t huawei-solar-modbus-to-mqtt:latest .
