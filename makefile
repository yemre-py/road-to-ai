run-sorting:
	@cd cs-grind/algorithms/sorting && \
	gcc bubble.c -o bubble && \
	./bubble && \
	rm -rf bubble

run-linealg:
	@cd math-c/c/linealg && \
	gcc main.c vector.c -o main -lm && \
	./main && \
	rm -rf main

