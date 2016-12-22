

build:
	docker build -t juniper/ravello-ansible .

test:
	docker run -t -i -v $(shell pwd):/project juniper/ravello-ansible ansible-playbook -i tests/inventory.ini tests/pb.rav.test.yaml --syntax-check
