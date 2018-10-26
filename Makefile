#
# Makefile for gerating Splunk App package
#
VERSION = $(shell git describe --tags)
PREFIX = $(shell basename `pwd`)
TARGET = $(PREFIX).$(VERSION).zip

.PHONY: dist
dist: $(TARGET)

.PHONY: test
test:
	PYTHONPATH=bin py.test

$(TARGET):
	git archive --worktree-attributes --prefix=$(PREFIX)/ --format=zip --output=$@ HEAD

