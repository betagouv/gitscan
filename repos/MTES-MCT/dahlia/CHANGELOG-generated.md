## Changelog : dahlia (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci a été marqué par le développement initial et le déploiement de l'application DAHL'ia. Les principales avancées concernent l'intégration du SSO ProConnect, l'automatisation du scraping des dossiers DALO, DAHO et DAHU, ainsi que l'amélioration de la gestion des fichiers et des dossiers. L'application est maintenant déployée en production et bénéficie d'une synchronisation nocturne des données.

### Évolutions fonctionnelles
- Intégration de l'authentification SSO ProConnect [#7](https://github.com/MTES-MCT/dahlia/issues/7).
- Possibilité de télécharger des fichiers et de rafraîchir l'affichage des dossiers [#16](https://github.com/MTES-MCT/dahlia/issues/16).
- Les dossiers supprimés sont maintenant correctement gérés et ne sont plus accessibles [#16](https://github.com/MTES-MCT/dahlia/issues/16).
- Ajout de détails supplémentaires aux dossiers [#13](https://github.com/MTES-MCT/dahlia/issues/13).
- Implémentation d'une recherche et d'un scraping de tous les dossiers, avec gestion des erreurs [#5](https://github.com/MTES-MCT/dahlia/issues/5).
- Scraping de tous les types de dossiers avec anonymisation des données [#6](https://github.com/MTES-MCT/dahlia/issues/6).
- Synchronisation automatique des données chaque nuit [#12](https://github.com/MTES-MCT/dahlia/issues/12).

### Évolutions techniques
- Mise en place d'un script de création de release et de déploiement en production [#17](https://github.com/MTES-MCT/dahlia/issues/17).
- Amélioration de la robustesse du scraping avec un système de ré-essai en cas d'erreurs temporaires [#8](https://github.com/MTES-MCT/dahlia/issues/8).
- Correction d'un problème d'anonymisation incomplète [#11](https://github.com/MTES-MCT/dahlia/issues/11).
- Correction d'un bug de déconnexion intempestive après la connexion [#10](https://github.com/MTES-MCT/dahlia/issues/10).
- Ajout de `ts-node` comme dépendance de production pour le scraping [#9](https://github.com/MTES-MCT/dahlia/issues/9).
- Amélioration de la qualité du code avec l'utilisation de Prettier et d'un linter [#15](https://github.com/MTES-MCT/dahlia/issues/15).
- Anonymisation du scraping en fonction de l'environnement [#14](https://github.com/MTES-MCT/dahlia/issues/14).

### Autres changements
- Correction d'un problème de checkout avant déploiement [#4](https://github.com/MTES-MCT/dahlia/issues/4).
- Déploiement initial de l'application sur Scalingo [#3](https://github.com/MTES-MCT/dahlia/issues/3).
- Initialisation du dépôt et création de la première version de l'application [#1](https://github.com/MTES-MCT/dahlia/issues/1).
