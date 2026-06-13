## Changelog : dahlia (30 derniers jours, au 2026-06-11)

### Résumé
Ce mois-ci, le projet Dahlia a connu une progression significative, passant d'une première version initiale à une application fonctionnelle capable de scraper, d'anonymiser et de gérer différents types de dossiers DALO, DAHO et DAHU. L'intégration du SSO ProConnect et l'amélioration de la robustesse du scraping sont des avancées majeures pour les agents de l'administration qui utiliseront l'application.

### Évolutions fonctionnelles
- Intégration du Single Sign-On (SSO) ProConnect pour l'authentification des utilisateurs. [#7](https://github.com/MTES-MCT/dahlia/issues/7)
- Ajout de la synchronisation automatique des données via un scraping nocturne. [#12](https://github.com/MTES-MCT/dahlia/issues/12)
- Possibilité de scraper tous les types de dossiers (DALO, DAHO, DAHU) et anonymisation des données. [#6](https://github.com/MTES-MCT/dahlia/issues/6)
- Amélioration de la recherche et du scrapping des dossiers, corrigeant les erreurs précédentes. [#5](https://github.com/MTES-MCT/dahlia/issues/5)
- Ajout de détails supplémentaires aux dossiers pour une meilleure information. [#13](https://github.com/MTES-MCT/dahlia/issues/13)

### Évolutions techniques
- Mise en place d'un mécanisme de ré-essai lors du scraping pour gérer les erreurs temporaires. [#8](https://github.com/MTES-MCT/dahlia/issues/8)
- Correction d'un problème d'anonymisation incomplète. [#11](https://github.com/MTES-MCT/dahlia/issues/11)
- Correction d'un bug empêchant le préchargement des liens de déconnexion, ce qui provoquait une déconnexion immédiate après la connexion. [#10](https://github.com/MTES-MCT/dahlia/issues/10)
- Ajout de `ts-node` en production pour permettre l'exécution du scraping. [#9](https://github.com/MTES-MCT/dahlia/issues/9)
- Amélioration du pipeline de déploiement avec un checkout explicite avant le déploiement sur Scalingo. [#4](https://github.com/MTES-MCT/dahlia/issues/4)
- Déploiement de l'application sur Scalingo. [#3](https://github.com/MTES-MCT/dahlia/issues/3)

### Autres changements
- Initialisation du projet et création de la première version de l'application web Dahlia. [#1](https://github.com/MTES-MCT/dahlia/issues/1)
- Initial commit du projet. [#1](https://github.com/MTES-MCT/dahlia/issues/1)
- Mise à jour de la configuration du gestionnaire de paquets utilisé par Dependabot. [#2](https://github.com/MTES-MCT/dahlia/issues/2)
