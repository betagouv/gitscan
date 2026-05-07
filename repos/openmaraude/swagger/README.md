# swagger

CleverCloud applications need to be linked to a github repository. This repository only contains a Dockerfile to deploy [our swagger documentation](https://swagger.api.taxi).

## Deployment


To deploy to production, setup the following remote and push the master branch.

```
git remote add clever git+ssh://git@push-n2-par-clevercloud-customers.services.clever-cloud.com/app_f7ff98f2-9071-41be-b6be-1e5e170aa119.git
```

To connect to container, install [CleverCloud CLI](https://www.clever-cloud.com/doc/reference/clever-tools/getting_started/) and run the following commands:

```
clever link app_f7ff98f2-9071-41be-b6be-1e5e170aa119

# Outputs "prod-swagger"
clever applications

clever ssh -a prod-swagger
```
