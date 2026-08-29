## Changelog : seves (30 derniers jours, au 28/08/2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'améliorations significatives pour la gestion des alertes sanitaires, notamment avec une meilleure visualisation cartographique (affichage des parcelles, vue satellite) et une saisie de données simplifiée grâce au pré-remplissage automatique des informations professionnelles. L'interface a également été affinée pour offrir une navigation plus fluide et une gestion des notifications plus pertinente.

### Évolutions fonctionnelles
- **Gestion des alertes sanitaires (SA) :** création d'une vue détaillée avec accès à l'historique [#2220](https://github.com/betagouv/seves/issues/2220), ajout d'un bloc "détenteur" [#2205](https://github.com/betagouv/seves/issues/2205), intégration de la liste des maladies et mise à jour des icônes de domaine [#2214](https://github.com/betagouv/seves/issues/2214).
- **Cartographie :** affichage des parcelles agricoles sur la carte [#2221](https://github.com/betagouv/seves/issues/2221) et possibilité de définir la vue satellite comme style de carte par défaut [#2213](https://github.com/betagouv/seves/issues/2213).
- **Optimisation de la saisie :** pré-remplissage automatique des champs du détenteur via les API SIRENE et BAN, ajout de modales de confirmation lors du changement de type d'établissement [#2215](https://github.com/betagouv/seves/issues/2215) et réinitialisation automatique des champs lors d'un changement de type.
- **Expérience utilisateur :** ajout d'infobulles sur le statut des animaux [#2211](https://github.com/betagouv/seves/issues/2211), amélioration de la validation des fichiers lors de l'upload et ajout de messages d'absence de résultat dans les sélecteurs.
- **Gestion des contacts :** suppression des notifications d'ajout de contacts et des ajouts automents d'agents dans certains contextes pour éviter les doublons [#2194](https://github.com/betagouv/seves/issues/2194) [#2196](https://github.com/betagouv/seves/issues/2196).

### Évolutions techniques
- **Architecture :** création et intégration du domaine "SA" dans les paramètres et les middlewares du système [#2216](https://github.com/betagouv/seves/issues/2216).
- **Performance :** ajout de nouvelles vues matérialisées pour optimiser l'affichage des tableaux de bord Metabase.
- **Sécurité :** ajout du header `X-XSS-Protection` et suppression du JavaScript des fichiers PDF avant leur analyse pour limiter les risques.
- **Maintenance :** correction de bugs sur le focus des composants de recherche et résolution d'un incident de déploiement.
