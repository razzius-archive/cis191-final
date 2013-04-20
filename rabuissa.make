CC=gcc
CFLAGS=-g -Wall

EXEC=rabuissa.o

all: $(EXEC)

$(EXEC): rabuissa.c
	$(CC) $(CFLAGS) -o $(EXEC) rabuissa.c

clean:
	echo "I should clean up all output files"
