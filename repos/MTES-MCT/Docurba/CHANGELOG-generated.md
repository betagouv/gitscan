## Changelog : Docurba (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois a été marqué par une consolidation importante de l'architecture, notamment par le transfert de plusieurs services de données du frontend vers le backend pour gagner en fiabilité. L'expérience utilisateur a été enrichie par l'adoption du format Markdown pour les descriptions et par l'ajout de nouveaux outils de gestion dans l'interface d'administration.

### Évolutions fonctionnelles
- **Amélioration de l'édition de contenu** : Support du format Markdown pour les descriptions de procédures et d'événements, incluant la gestion des liens externes.
- **Gestion des événements** : 
    - Possibilité d'archiver ou de désarchiver des événements directement depuis l'interface d'administration.
    - Prise en compte des nouveaux types d'événements liés à la loi Huwart (PP et PPI).
- **Interface et ergonomie** :
    - Ajout d'une bannière d'information pour signaler les périodes de congés.
    - Amélioration de la recherche de collaborateurs (recherche insensible à la casse).
    - Correction de la gestion des emails lors du partage de procédures.
- **Administration** : Amélioration des filtres de recherche pour les procédures dans le back-office.

### Évolutions techniques
- **Migration d'architecture** : Migration massive d'endpoints API (collectivités, communes, intercommunalités, Slack) du frontend Nuxt vers le backend Django pour centraliser la logique métier.
- **Optimisation des performances** : 
    - Résolution de problèmes de requêtes N+1 sur l'API interne.
    - Optimisation globale des performances de l'API Django.
- **Refonte du modèle de données** :
    - Renommage et restructuration du modèle utilisateur (`SupabaseUser`).
    - Séparation des codes INSEE et SIREN pour les collectivités.
    - Amélioration de la traçabilité via l'ajout de relations pour l'historique des snapshots d'événements.
- **Qualité et tests** : 
    - Renforcement de la suite de tests (utilisation de snapshots et de `freezegun` pour la gestion du temps).
    - Nettoyage du code : suppression de composants Nuxt, de fonctions SQL et de migrations inutilisées.

### Autres changements
- **Documentation** : Ajout de nouvelles ressources documentaires : [Fiche technique DGALN-OAP](#2307) et [Guide de rédaction de cahier des charges](#2298).
- **Configuration** : Mise en place d'une variable d'environnement pour activer ou désactiver les migrations de base de données.
