IMAGE=hashicorp/terraform:latest

CONTAINER_NAME=terraform_local

.PHONY: init plan apply destroy clean

init:
	@docker run --rm -it --name $(CONTAINER_NAME) -v $(shell pwd):/workspace -w /workspace $(IMAGE) init
	@echo "Terraform initialized."

plan:
	@docker run --rm -it --name $(CONTAINER_NAME) -v $(shell pwd):/workspace -w /workspace $(IMAGE) plan
	@echo "Review the plan output above."

apply:
	@docker run --rm -it --name $(CONTAINER_NAME) -v $(shell pwd):/workspace -w /workspace $(IMAGE) apply
	@echo "Terraform apply completed."
	@echo "Resources have been created."

destroy:
	@docker run --rm -it --name $(CONTAINER_NAME) -v $(shell pwd):/workspace -w /workspace $(IMAGE) destroy
	@echo "Terraform destroy completed."
	@echo "Resources have been destroyed."

# run using sudo!
clean:
	@docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	@docker rmi $(IMAGE) 2>/dev/null || true
	rm -rf .terraform .terraform.lock.hcl terraform.tfstate* *.txt
	@echo "Terraform workspace cleaned."
	@echo "Clean up completed."