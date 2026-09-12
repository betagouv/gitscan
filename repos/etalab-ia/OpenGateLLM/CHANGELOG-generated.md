## Changelog : OpenGateLLM (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois a été marqué par une refonte architecturale majeure visant à améliorer la maintenabilité et la robustesse du système via l'adoption de la "Clean Architecture". Parallèlement, l'expérience utilisateur a été enrichie par de nouvelles capacités de suivi de consommation, une amélioration de l'interface "Playground" et l'ajout du support SSO pour l'authentification.

### Évolutions fonctionnelles
- **Gestion de la consommation** : Ajout de la possibilité de récupérer l'usage quotidien via l'endpoint `GET /v1/usage` [#1107].
- **Limitation de débit (Rate Limiting)** : 
    - Prise en compte des tokens de sortie dans les limites de tokens par minute/jour (TPM/TPD) [#1077].
    - Rejet automatique des requêtes dont le prompt est trop volumineux avant l'appel au fournisseur [#1088].
- **Interface Playground** : 
    - Amélioration globale du design [#1094].
    - Correction de la pagination via le champ `total` de l'API [#983].
    - Correction de liens URL et de la documentation Swagger [#1096].
- **Authentification** : Support de la connexion et déconnexion SSO via `oauth2-proxy` [#986].
- **API & Administration** :
    - Renommage des endpoints "me" pour une meilleure clarté (ex: `/v1/me/keys` devient `/v1/keys`) [#1033].
    - Amélioration de la gestion des erreurs lors de la suppression d'organisations ou de rôles [#1048].
    - Renforcement de la validation des champs lors des mises à jour (PATCH) sur les endpoints d'administration [#1053].
- **Observabilité** : Ajout de modèles Grafana pour le suivi du trafic et de l'inférence [#903].

### Évolutions techniques
- **Migration vers la Clean Architecture** : Refonte massive de nombreux endpoints (Organisations, Clés, Audio, Usage, etc.) pour isoler la logique métier et améliorer la structure du code [#1080, #1057, #1050, #1045, #1041, #1039, #1038, #1024, #1023, #1021, #1020, #1022, #1008].
- **Refonte de la QoS (Quality of Service)** : Simplification du système de priorité en supprimant l'usage de Celery workers et des métriques de séries temporelles au profit d'une approche plus légère [#1131, #1123].
- **Optimisations de la base de données** :
    - Optimisation des requêtes PostgreSQL pour la suppression des fournisseurs [#1067].
    - Amélioration de la gestion des connexions (release des pools) lors des appels aux fournisseurs [#1005].
    - Standardisation des types de retour de la couche DB [#1072].
- **Schémas et Validation** :
    - Adoption de la syntaxe `annotated` de Pydantic v3 [#1070].
    - Normalisation des emails utilisateurs en minuscules et renforcement de la validation des types de modèles [#1126].
- **Infrastructure & CI/CD** :
    - Optimisation des pipelines CI pour n'exécuter les tests de couverture et E2E que sur les PR prêtes [#1025].
    - Implémentation de la réinitialisation des clés Redis [#952].
- **Nettoyage** : Suppression des tables PostgreSQL liées au RAG qui n'étaient plus utilisées [#1007].

### Autres changements
- **Documentation** : 
    - Mise à jour du guide de démarrage rapide (Quickstart) incluant le support ARM64 et les dépendances CLI [#1116].
    - Maintenance régulière de la documentation générée et des fichiers de configuration des agents [#1082, #1055, #1079, #1017].
- **Configuration** : Ajout de `jinja2` aux dépendances du projet [#1122].
