## Changelog : dahlia (30 derniers jours, au 8 juin 2026)

### Résumé
Cette version marque le lancement initial de l'application DAHLIA, une application web destinée aux agents de l'administration pour la gestion des dossiers DALO, DAHO et DAHU.  Les premières fonctionnalités de recherche et de récupération de dossiers de contentieux sont disponibles, avec des améliorations apportées au scraping et à l'intégration SSO ProConnect.

### Évolutions fonctionnelles
- **Intégration SSO ProConnect:**  L'application s'intègre maintenant avec le système d'authentification unique ProConnect. [#7](https://github.com/MTES-MCT/dahlia/issues/7)
- **Recherche et récupération de dossiers:** Implémentation de la recherche et du scraping de tous les types de dossiers, avec anonymisation des données. [#5](https://github.com/MTES-MCT/dahlia/issues/5) et [#6](https://github.com/MTES-MCT/dahlia/issues/6)
- **Amélioration de la robustesse du scraping:** Ajout d'un mécanisme de ré-essai en cas d'erreurs temporaires lors du scraping des données. [#8](https://github.com/MTES-MCT/dahlia/issues/8)
- **Correction du déconnexion intempestive:** Correction d'un problème où l'utilisateur était déconnecté immédiatement après la connexion. [#10](https://github.com/MTES-MCT/dahlia/issues/10)

### Évolutions techniques
- **Déploiement sur Scalingo:** L'application est maintenant déployée et scalable sur la plateforme Scalingo. [#3](https://github.com/MTES-MCT/dahlia/issues/3)
- **Ajout de `ts-node` en production:**  `ts-node` est maintenant inclus dans l'environnement de production pour permettre l'exécution du scraping. [#9](https://github.com/MTES-MCT/dahlia/issues/9)
- **Amélioration du workflow de déploiement:** Ajout d'une étape de checkout avant le déploiement pour assurer la cohérence des fichiers. [#4](https://github.com/MTES-MCT/dahlia/issues/4)

### Autres changements
- **Initialisation du projet:** Création de la première version de l'application web DAHLIA. [#1](https://github.com/MTES-MCT/dahlia/issues/1)
- **Initialisation du dépôt:** Commit initial du dépôt. [#2](https://github.com/MTES-MCT/dahlia/issues/2)
