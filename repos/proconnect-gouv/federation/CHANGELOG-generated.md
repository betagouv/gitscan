## Changelog : federation (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, notamment la suppression de configurations SSL obsolètes et l'ajout d'une politique de sécurité de contenu plus stricte. Des fonctionnalités ont été ajoutées pour faciliter la gestion des collaborateurs des clients OIDC et pour permettre des tests de l'authentification multi-facteurs (MFA). Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de gérer les collaborateurs des clients OIDC. [#1312](https://github.com/proconnect-gouv/federation/issues/1312)
- Implémentation d'un mécanisme de repli basé sur l'email pour l'authentification multi-facteurs (MFA) pour les fournisseurs d'identité non compatibles. [#4bc2593](https://github.com/proconnect-gouv/federation/commit/4bc2593)
- Possibilité de tester l'authentification multi-facteurs (MFA) avec des alias d'email +mfa. [#5ae2f9e](https://github.com/proconnect-gouv/federation/commit/5ae2f9e)
- Ajout d'un point de terminaison DELETE pour supprimer les clients OIDC. [#73c3167](https://github.com/proconnect-gouv/federation/commit/73c3167)
- Ajout d'un indicateur de conformité MFA aux fournisseurs d'identité. [#6a941e2](https://github.com/proconnect-gouv/federation/commit/6a941e2)

### Évolutions techniques
- Extraction de l'application de fourniture de données de mock vers une application autonome. [#978f84d](https://github.com/proconnect-gouv/federation/commit/978f84d)
- Ajout de healthchecks livez/readyz à l'application admin. [#bd1e7f7](https://github.com/proconnect-gouv/federation/commit/bd1e7f7)
- Refactorisation pour supprimer le champ d'email du propriétaire obsolète. [#c75ab46](https://github.com/proconnect-gouv/federation/commit/c75ab46)
- Amélioration des performances des requêtes MongoDB en utilisant une correspondance de chaînes exacte. [#46a03a5](https://github.com/proconnect-gouv/federation/commit/46a03a5)
- Mise à jour de plusieurs dépendances (FastAPI, PostgreSQL, Uvicorn, etc.).
- Suppression de la configuration SSL MongoDB obsolète. [#2e75757](https://github.com/proconnect-gouv/federation/commit/2e75757)
- Suppression de la politique `unsafe-inline` de la Content Security Policy pour renforcer la sécurité. [#7f6ec77](https://github.com/proconnect-gouv/federation/commit/7f6ec77)
- Downgrade de PostgreSQL à la version 16. [#ee15ae5](https://github.com/proconnect-gouv/federation/commit/ee15ae5)

### Autres changements
- Ajout de documentation pour hyyyperbridge. [#888e759](https://github.com/proconnect-gouv/federation/commit/888e759)
- Suppression du widget de chat Crisp. [#4892f96](https://github.com/proconnect-gouv/federation/commit/4892f96)
- Nettoyage des fixtures Cypress pour Kubernetes. [#f492706](https://github.com/proconnect-gouv/federation/commit/f492706)
- Amélioration de la lisibilité du diagramme cinématique dans la documentation back. [#01a73fc](https://github.com/proconnect-gouv/federation/commit/01a73fc)
- Extraction du script de confirmation de déconnexion vers un fichier externe. [#87a5321](https://github.com/proconnect-gouv/federation/commit/87a5321)
- Correction d'un bug empêchant l'application de la valeur par défaut `isMfaCompliant` lors de la migration. [#3e1e38e](https://github.com/proconnect-gouv/federation/commit/3e1e38e)
- Correction d'un bug dans pcdbapi où l'ID client demandé était ignoré. [#2a5d290](https://github.com/proconnect-gouv/federation/commit/2a5d290)
- Correction d'un bug empêchant l'application de la valeur par défaut `isMfaCompliant` lors de la migration. [#d9ebabb](https://github.com/proconnect-gouv/federation/commit/d9ebabb)
- Correction d'un bug empêchant l'application de la valeur par défaut `isMfaCompliant` lors de la migration. [#3e1e38e](https://github.com/proconnect-gouv/federation/commit/3e1e38e)
