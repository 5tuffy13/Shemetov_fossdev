.DEFAULT_GOAL := help # таргет по умолчанию

create-practice:
	ifndef PRACTICE
		$(error must pass val PRACTICE)
	endif
	@mkdir -p $(PRACTICE)
	@echo "Created practice"

remove-practice:
	@rm -rf $(PRACTICE)
	@echo "Removed practice"

help:
	@echo "This makefile for repo-level activity"

# mkdir demo-practice
# mkdir demo-practice/src
# mkdir demo-practice/tests
# mkdir demo-practice/docs
# mkdir demo-practice/README.md