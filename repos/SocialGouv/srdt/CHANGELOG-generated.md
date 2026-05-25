## Changelog : srdt (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'assistant virtuel SRDT a bénéficié d'améliorations significatives en termes d'expérience utilisateur, notamment une refonte de l'affichage du statut de la convention collective, l'ajout d'un lien vers un questionnaire d'évaluation et la possibilité de changer de modèle d'IA via une configuration Kubernetes. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la précision du système, notamment concernant l'anonymisation des données de localisation et la permissivité du prompt. Enfin, des métriques de performance ont été ajoutées pour le suivi du temps de génération des réponses.

### Évolutions fonctionnelles
- Ajout d'un lien vers un questionnaire d'évaluation sur la page d'accueil. [#372](https://github.com/SocialGouv/srdt/issues/372)
- Refonte de l'affichage du badge de statut de la convention collective. [#374](https://github.com/SocialGouv/srdt/issues/374)
- Le badge de convention collective est désormais toujours affiché. [#365](https://github.com/SocialGouv/srdt/issues/365)
- Correction de l'affichage des labels et des textes d'aide pour l'IDCC. [#364](https://github.com/SocialGouv/srdt/issues/364)
- Possibilité de changer de modèle d'IA depuis une configuration Kubernetes. [#366](https://github.com/SocialGouv/srdt/issues/366)

### Évolutions techniques
- Ajout du suivi du temps de génération des réponses pour Metabase. [#348](https://github.com/SocialGouv/srdt/issues/348)
- Correction concernant l'utilisation du modèle ChatGPT en production.
- Correction de bugs liés aux contributions et autres éléments. [#351](https://github.com/SocialGouv/srdt/issues/351) [#352](https://github.com/SocialGouv/srdt/issues/352) [#357](https://github.com/SocialGouv/srdt/issues/357) [#359](https://github.com/SocialGouv/srdt/issues/359)
- Suppression de l'anonymisation des localisations. [#370](https://github.com/SocialGouv/srdt/issues/370)
- Amélioration de la permissivité du prompt. [#363](https://github.com/SocialGouv/srdt/issues/363)

### Autres changements
- Suppression du "tally". [#376](https://github.com/SocialGouv/srdt/issues/376)
- Publication des versions : 1.43.0, 1.42.1, 1.42.0, 1.41.0, 1.40.3, 1.40.2, 1.40.1, 1.40.0, 1.39.7, 1.39.6, 1.39.5.
