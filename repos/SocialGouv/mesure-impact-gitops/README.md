# mesure-impact-gitops

Déploiement de [SocialGouv/mesure-impact](https://github.com/SocialGouv/mesure-impact) sur
Kubernetes. Ce dépôt porte tout ce qui est **spécifique à une instance** ; le chart Helm, lui,
vit dans le dépôt applicatif et ignore où il sera déployé.

## Le partage des responsabilités

| Dépôt applicatif | Ce dépôt |
|---|---|
| le chart Helm, **agnostique** de la plateforme | un dossier par environnement, sous `apps/` |
| ne connaît ni cluster, ni namespace, ni host | cluster, namespace, host, ressources, secrets |
| publie le chart en artefact **OCI** versionné | **épingle** une version de chart |
| déclenche ce dépôt après une livraison | rend les manifests, puis les applique |

## Les deux branches

- **`main`** — les sources. C'est ici qu'on édite un host, du scaling, une cadence.
- **`rendered`** — les manifests rendus, un dossier par environnement, écrits par la CI.
  Elle ne se merge jamais et ne s'édite jamais à la main : c'est un artefact, et le seul
  point de départ d'un `kubectl apply`.

Ce découpage rend un déploiement **auditable** — le diff des manifests se lit en clair — et
**reproductible** : chart OCI plus version épinglée.

## Structure

```
apps/mesure-impact-<env>/
├── Chart.yaml           # dépend du chart OCI, version épinglée par la CI
├── values.deploy.yaml   # host, réplicas, cadence — tout le spécifique-instance
├── env.yaml             # descripteur : cluster, namespace, projet Rancher
└── templates/           # ressources propres à l'instance (SealedSecrets…)
```

Un dossier sans `Chart.yaml` ou sans `env.yaml` est **ignoré** par le rendu, jamais rendu à
moitié.

## Les deux flux

**Livraison** — le dépôt applicatif publie son chart en OCI puis envoie un `repository_dispatch`
portant la version. Le rendu l'épingle dans les `Chart.yaml`, rend, et pousse sur `rendered`.

**Exploitation** — changer une ressource, un host, une cadence : éditer `apps/` sur `main`.
Le rendu part seul. Aucun pipeline applicatif n'est impliqué.

Dans les deux cas, un push sur `rendered` déclenche l'apply.

## Cloisonnement

Chaque environnement a **son propre bot Rancher**, membre d'un projet Rancher distinct, donc
d'un seul namespace. Les deux kubeconfigs sont des secrets **d'environnement** GitHub, pas des
secrets de dépôt : le job `dev` ne peut pas lire celui de `prod`, et son kubeconfig ne
l'autoriserait de toute façon pas à écrire dans le namespace de prod.

| Env | Projet Rancher | Bot | Namespace |
|---|---|---|---|
| dev | `c-m-97jxtvnv:p-mrmrt` | `rancherbot-ci-mesure-impact-dev` (`u-h4dmz`) | `mesure-impact-dev` |
| prod | `c-m-97jxtvnv:p-bxkq6` | `rancherbot-ci-mesure-impact-prod` (`u-7nzxq`) | `mesure-impact-prod` |

Vérifié par `SubjectAccessReview` croisés : chaque bot obtient `yes` sur son namespace et `no`
sur l'autre, pour `deployments`, `cronjobs`, `secrets` et `sealedsecrets`.

## État

Le dépôt est en **rodage** : le rendu tourne, l'apply existe mais le déploiement réel part
encore du dépôt applicatif. La bascule consiste à comparer le `manifests.yaml` produit ici avec
`helm get manifest mesure-impact -n <ns>` — un diff vide est la condition d'entrée — puis à
désarmer le job de déploiement côté applicatif.

Deux points restent à traiter, notés pour ne pas les redécouvrir :

- **Nettoyage des orphelins.** Sans agent en cluster, `kubectl apply` ne supprime rien.
  `kubectl apply --prune` est à éviter : son allowlist de types par défaut ne couvre ni
  `Ingress`, ni `NetworkPolicy`, ni `PodDisruptionBudget`, ni `PrometheusRule`, ni
  `SealedSecret` — tout ce que ce chart rend passerait à travers, en silence. Les deux options
  sérieuses sont de garder Helm comme applicateur, dont le prune est correct et gratuit, ou de
  passer à `kapp`.
- **Le nom de release doit rester `mesure-impact`**, constant, jamais le nom du dossier : le
  `selector` d'un Deployment est immuable et contient `app.kubernetes.io/instance`.

## Vers Atlas v2

La structure est celle qu'attend Atlas : `apps/<app>-<env>/`, branche `rendered`, chart OCI
épinglé, descripteur d'instance, host injecté au rendu, secrets référencés par nom. La
migration consistera à remplacer les SealedSecrets par des `ExternalSecret`, à passer
l'ingress class à `public` avec un `cluster-issuer`, et à confier l'apply à ArgoCD.

⚠️ Une incompatibilité connue : Atlas impose `maxLimitRequestRatio.memory = 2`, alors que les
ressources actuelles sont à un ratio de 4. À ajuster dans les `values.deploy.yaml` avant de
basculer, sinon les pods sont refusés à l'admission.
