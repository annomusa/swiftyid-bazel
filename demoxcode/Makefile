.PHONY : run

ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

PRODUCT := xchammer.app
XCHAMMER_BIN := $(ROOT_DIR)/$(PRODUCT)/Contents/MacOS/XCHammer

PREFIX := /usr/local

SAMPLE ?= texture-example

run:
	$(XCHAMMER_BIN) generate \
	    $(ROOT_DIR)/$(SAMPLE)/XCHammer.yaml \
	    --workspace_root $(ROOT_DIR)/$(SAMPLE) \
	    --bazel $(ROOT_DIR)/$(SAMPLE)/tools/bazelwrapper

build: build-debug

build-debug: BAZELFLAGS = --announce_rc \
	--disk_cache=$(HOME)/Library/Caches/Bazel
build-debug: build-impl
build-impl:
	$(ROOT_DIR)/tools/bazelwrapper build \
		$(BAZELFLAGS) xchammer
	@rm -rf $(ROOT_DIR)/xchammer.app
	@unzip -q $(ROOT_DIR)/bazel-bin/xchammer.zip
