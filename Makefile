DIRECTORIES = $(sort $(dir $(wildcard */test_*.py)))

.PHONY: test $(DIRECTORIES)

$(DIRECTORIES):
	pipenv run pytest $@

test: $(DIRECTORIES) ;
