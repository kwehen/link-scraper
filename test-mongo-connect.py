import pymongo
import sensitive

# MongoDB connection parameters
mongo_uri = f"mongodb://{sensitive.db_auth}@{sensitive.db_addr}"  # Change this to your MongoDB URI
database_name = "devops"  # Change this to your database name
collection_name = "test_skills"  # Change this to your collection (table) name

# List of DevOps skills or buzzwords
devops_skills = [
    "Continuous Integration (CI)",
    "Continuous Deployment (CD)",
    "CI/CD",
    "Infrastructure as Code (IaC)",
    "IaC",
    "Terraform",
    "Docker",
    "Kubernetes",
    "Jenkins",
    "Ansible",
    "GitHub Actions",
    "Automation",
    "Configuration Management",
    "Monitoring and Logging",
    "AWS",
    "Ansible",
    "API",
    "Apache",
    "ALB",
    "Amazon Aurora",
    "Cloud computing",
    "CI/CD",
    "Cluster",
    "Container",
    "Containers",
    "CloudFormation",
    "ARM"
    "Containerization",
    "CloudWatch",
    "Configuration drift",
    "Configuration management",
    "DevOps",
    "Dark launch",
    "Docker",
    "Dockerfile",
    "Docker Swarm",
    "Deployment",
    "Django framework",
    "Datadog",
    "Dynatrace",
    "Environment",
    "Elastic",
    "EC2",
    "EKS",
    "AKS",
    "GKE",
    "Fargate",
    "Git",
    "GitHub",
    "GitLab",
    "Gitlab CI",
    "Helm",
    "Infrastructure",
    "IaC",
    "IaaS",
    "Image",
    "InfluxDB",
    "Ingress controller",
    "Jenkins",
    "Kubernetes",
    "Kibana",
    "Logstash",
    "Microservices",
    "MongoDB",
    "Nginx",
    "Orchestration",
    "Open source",
    "OpenStack",
    "OpenShift",
    "PaaS",
    "Prometheus",
    "Provisioning",
    "Python",
    "Pod",
    "Podman",
    "ProxMox",
    "RDS",
    "RabbitMQ",
    "S3",
    "Snapshot",
    "Staging environment",
    "Test automation",
    "Technical debt",
    "Azure",  # Added Azure
    "Google Cloud Platform (GCP)",
    "Reddis",
    "GCP"
]

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)

# Access the database
db = client[database_name]

# Create a collection (table) if it doesn't exist
collection = db[collection_name]

# Insert the DevOps skills into the collection
for skill in devops_skills:
    collection.insert_one({"skill": skill, "title": "DevOps Test"})

# Close the MongoDB connection
client.close()
