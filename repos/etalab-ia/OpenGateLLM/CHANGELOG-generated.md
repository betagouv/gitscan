## Changelog : OpenGateLLM (30 derniers jours, au 04/09/2026)

### Résumé
Ce mois a été marqué par une modernisation profonde de l'architecture du projet vers une structure "Clean Architecture", visant à améliorer la stabilité et la maintenance à long terme. Les utilisateurs bénéficieront d'une interface de test (Playground) plus intuitive, de nouvelles capacités d'authentification via SSO, et d'une gestion plus fine des limites d'utilisation (rate-limiting) pour mieux contrôler les coûts et la consommation des modèles.

### Évolutions fonctionnelles
- **Amélioration du Playground** : Refonte visuelle de l'interface [#1094](https://github.com/etalab-ia/OpenGateLLM/issues/1094), correction des liens URL et de la documentation Swagger [#1096](https://github.com/etalab-ia/OpenGateLLM/issues/1096), et ajout de la pagination complète pour une navigation plus fluide [#983](https://github.com/etalab-ia/OpenGateLLM/issues/983).
- **Authentification et Sécurité** : Support du login/logout via SSO avec `oauth2-proxy` [#986](https://github.com/etalab-ia/OpenGateLLM/issues/986) et gestion améliorée des accès refusés dans le Playground [#1006](https://github.com/etalab-ia/OpenGateLLM/issues/1006).
- **Gestion des limites (Rate-limiting)** : Renforcement du contrôle de consommation en incluant le comptage des tokens de sortie (TPM/TPD) [#1077](https://github.com/etalab-ia/OpenGateLLM/issues/1077) et rejet automatique des requêtes de prompts trop volumineuses avant l'appel aux fournisseurs [#1088](https://github.com/etalab-ia/OpenGateLLM/issues/1088).
- **Simplification de l'API** : Renommage et simplification de certains endpoints utilisateurs pour une utilisation plus intuitive (ex: `/v1/me/info` devient `/v1/me`) [#1033](https://github.com/etalab-ia/OpenGateLLM/issues/1033).
- **Observabilité** : Ajout de nouveaux templates Grafana pour le suivi du trafic et des performances d'inférence [#903](https://github.com/etalab-ia/OpenGateLLM/issues/903).

### Évolutions techniques
- **Migration vers la Clean Architecture** : Refactorisation massive de nombreux modules (organisations, gestion des clés, usage, audio, etc.) pour isoler la logique métier et améliorer la robustesse du code [#1080](https://github.com/etalab-ia/OpenGateLLM/issues/1080), [#1057](https://github.com/etalab-ia/OpenGateLLM/issues/1057), [#1045](https://github.com/etalab-ia/OpenGateLLM/issues/1045), [#1039](https://github.com/etalab-ia/OpenGateLLM/issues/1039), [#1021](https://github.com/etalab-ia/OpenGateLLM/issues/1021), [#1008](https://github.com/etalab-ia/OpenGateLLM/issues/1008).
- **Optimisation de la base de données** : Amélioration des performances PostgreSQL (libération des connexions lors des appels fournisseurs [#1005](https://github.com/etalab-ia/OpenGateLLM/issues/1005), standardisation des types de retour [#1072](https://github.com/etalab-ia/OpenGateLLM/issues/1072)) et suppression des tables liées au RAG pour alléger le schéma [#1007](https://github.com/etalab-ia/OpenGateLLM/issues/1007).
- **Standardisation et Typage** : Uniformisation de la gestion des dates (`datetime`) sur l'ensemble du système [#1062](https://github.com/etalab-ia/OpenGateLLM/issues/1062) et adoption de la syntaxe annotée de Pydantic v3 [#1070](https://github.com/etalab-ia/OpenGateLLM/issues/1070).
- **CI/CD et Infrastructure** : Optimisation des tests en CI/CD (exécution sélective sur les PR prêtes) [#1025](https://github.com/etalab-ia/OpenGateLLM/issues/1025) et mise à jour des outils de scan de sécurité [#1078](https://github.com/etalab-ia/OpenGateLLM/issues/1078).

### Autres changements
- **Documentation** : Mise à jour régulière de la documentation générée et des versions de release [#1082](https://github.com/etalab-ia/OpenGateLLM/issues/1082), [#1055](https://github.com/etalab-ia/OpenGateLLM/issues/1055).
- **Documentation des agents** : Ajout du fichier `AGENTS.md` pour documenter les agents disponibles [#1079](https://github.com/etalab-ia/OpenGateLLM/issues/1079), [#1017](https://github.com/etalab-ia/OpenGateLLM/issues/1017).
