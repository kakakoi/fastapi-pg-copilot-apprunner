
# ローカル開発環境
```bash
$ export PYTHONDONTWRITEBYTECODE=1 #no cache
$ export FPCASVCCLUSTER_SECURITY_GROUP='{"password":"password","dbname": "dev","port": 5432,"username": "dev_api","host": "localhost"}'
$ poetry install
$ poetry shell
$ cd backend
$ docker-compose up -d # app,db,pgadmin
```
```bash
$ uvicorn main:app --reload --port 5000 # app
```

## tips
clean docker `docker-compose down --rmi all --volumes --remove-orphans`

# copilot - App Runner - Aurora(pg) - ci
## copilot : init
```bash
$ copilot init
# apprunner
# Application name: fpca
# Service name: fpca-svc
# Dockerfile: .
```

失敗してROLLBACKした場合は修正してdeploy
```bash
$ copilot deploy
```
## copilot : storage

```bash
$ copilot storage init
Note: Aurora Serverless storage is launched in private subnets of your environment's VPC. 
To reach the database from your Request-Driven Web Service please enable the HTTP Data API: 
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html. 

You will also need to an IAM policy that allows your Request-Driven Web Service to make Data API calls. 
You can simply create the policy in the Aurora addon template and create an output. The policy will be automatically attached to your Request-Driven Web Service:
https://aws.github.io/copilot-cli/docs/developing/additional-aws-resources/#what-does-an-addon-template-look-like

# Storage resource name: fpca-svc-cluster
# Database engine: PostgreSQL
# Initial database name: dev
# ✔ Wrote CloudFormation template for Database Cluster fpca-svc-cluster at copilot/fpca-svc/addons/fpca-svc-cluster.yml

# Recommended follow-up actions:
#   - Update fpca-svc's code to leverage the injected environment variable FPCASVCCLUSTER_SECRET.
# For example, in JavaScript you can write `const {username, host, dbname, password, port} = JSON.parse(process.env.FPCASVCCLUSTER_SECRET)`.
#   - Run `copilot deploy --name fpca-svc` to deploy your storage resources.
```
### Update fpca-svc's code to leverage the injected environment variable FPCASVCCLUSTER_SECRET.
- 上記に従いコード修正
- deploy
```bash
$ copilot deploy --name fpca-svc
```
## copilot : pipeline

```bash
$ copilot pipeline init
# Which environment would you like to add to your pipeline?: test
# Which repository would you like to use for your pipeline?: [Enter]

$ copilot pipeline update
```

## copilot : クリーンアップ
```bash
$ copilot app delete
```


### copilot fargate aurora serverless pg
```bash
$ copilot init
Application name: fpca
Workload type: Load Balanced Web Service
Service name: fpca-svc
Dockerfile: ./Dockerfile
parse EXPOSE: no EXPOSE statements in Dockerfile ./Dockerfile
Port: 80
Ok great, we'll set up a Load Balanced Web Service named fpca-svc in application fpca listening on port 80.'
- Creating the infrastructure for stack fpca-test-fpca-svc                        [create complete]  [335.0s]
$ copilot storage init
Only found one workload, defaulting to: fpca-svc
Storage type: Aurora Serverless
Storage resource name: fpca-svc-cluster
Database engine: PostgreSQL
Initial database name: dev
✔ Wrote CloudFormation template for Database Cluster fpca-svc-cluster at copilot/fpca-svc/addons/fpca-svc-cluster.yml

Recommended follow-up actions:
  - Update fpca-svc's code to leverage the injected environment variable FPCASVCCLUSTER_SECRET.
For example, in JavaScript you can write `const {username, host, dbname, password, port} = JSON.parse(process.env.FPCASVCCLUSTER_SECRET)`.
  - Run `copilot deploy --name fpca-svc` to deploy your storage resources.'
- Updating the infrastructure for stack fpca-test-fpca-svc                        [update complete]  [1194.7s]
$ copilot deploy --name fpca-svc
```