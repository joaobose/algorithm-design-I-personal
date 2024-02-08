# the compiler: gcc, clang for C program, define as g++, clang++ for C++
CC = clang++

# compiler flags:
#  -g     - this flag adds debugging information to the executable file
#  -Wall  - this flag is used to turn on most compiler warnings
#  -std   - specifies the std version
CFLAGS  = -g -Wall -std=c++11

# source code
SRC = src

# The remove command
RM = rm -f

# the build target executable:
TARGET = ./client
BIN = ./out

all: $(TARGET)

$(TARGET): $(BIN)/main.o
	$(CC) $(CFLAGS) -o $(TARGET) $(BIN)/main.o

$(BIN)/main.o: $(SRC)/main.cpp
	$(CC) $(CFLAGS) -c $(SRC)/main.cpp -o $(BIN)/main.o

clean:
	$(RM) $(BIN)/*.o && $(RM) $(TARGET)
