#!/usr/bin/env bash

# testing the armadillo implementation inside cpp only
g++ -std=c++17 -O2 -o scripts/cpp_test \
	scripts/cpp_test.cpp \
	src/core/irls.cpp \
	-larmadillo \
	-Isrc/core
