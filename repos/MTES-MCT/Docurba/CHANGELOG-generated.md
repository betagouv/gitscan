## Changelog : Docurba (30 derniers jours, au 18 août 2026)

### Résumé
Ce mois-ci, Docurba a connu une phase importante de consolidation technique, marquée par la migration de plusieurs services de données vers le backend pour renforcer la fiabilité du système. L'expérience utilisateur est enrichie par le support du format Markdown pour les descriptions et une meilleure gestion des types d'événements réglementaires.

### Évolutions fonctionnelles
- **Support du format Markdown** : les descriptions de procédures et d'événements acceptent désormais le format Markdown, avec une gestion automatique des liens externes.
- **Nouveaux types d'événements** : intégration des types d'événements liés à la loi Huwart (PP et PPI).
- **Amélioration de l'administration** : possibilité d'archiver ou de désarchiver des événements directement depuis l'interface Django et ajout de nouveaux filtres pour les procédures.
- **Interface utilisateur** : ajout d'une bannière d'information pour signaler les périodes de congés.
- **Fiabilité du partage** : amélioration de la gestion des adresses email lors du partage de procédures pour éviter les erreurs de formatage.

### Évolutions techniques
- **Migration de l'architecture** : transfert majeur de la logique de données (communes, collectivités, intercommunalités, etc.) de l'interface Nuxt vers l'API Django pour centraliser le traitement métier.
- **Optimisation des performances** : correction de problèmes de requêtes N+1 dans l'API interne et amélioration de la vitesse des tests.
- **Refonte du système utilisateur** : renommage du modèle utilisateur (`SupabaseUser`) et intégration d'une gestion par profils.
- **Amélioration du filtrage** : optimisation de la recherche par codes INSEE et SIREN et enrichissement des filtres de recherche sur les collectivités.
- **Gestion des environnements** : renforcement de la configuration des variables d'environnement et suppression des bannières de développement en production.
- **Nettoyage du code** : suppression de composants, de fonctions SQL et de répertoires de tests (E2E) obsolètes.

### Autres changements
- **Documentation** : ajout de nouvelles ressources métier, notamment une fiche technique DGALN-OAP ([#2307](https://github.com/MTES-MCT/Docurba/issues/2307)) et un guide pour la rédaction de cahiers des charges ([#2298](https://github.com/MTES-MCT/Docurba/issues/2298)).
