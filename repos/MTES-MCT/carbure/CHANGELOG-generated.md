## Changelog : carbure (30 derniers jours)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant la gestion des intrants et des matières premières pour le biométhane, avec l'ajout de nouveaux modèles, d'une nouvelle API et d'un script d'importation Excel. Des corrections et des améliorations ont également été apportées à la gestion des certificats d'électricité, à la traçabilité des SAF et à l'interface utilisateur pour les DREAL. Enfin, des optimisations et des refactorings ont été réalisés pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- Possibilité d'annuler un certificat de transfert d'électricité rejeté. [#1234](https://github.com/MTES-MCT/carbure/issues/1234)
- Ajout d'un bouton d'aide lorsque les paramètres ne sont pas renseignés pour faciliter la configuration.
- Envoi d'emails aux producteurs de biométhane.
- Amélioration de l'affichage du solde des certificats d'électricité pour une meilleure clarté.
- Ajout de la possibilité pour les DREAL d'accepter ou de refuser des utilisateurs.
- Ajout de champs pour le type de CIVE, les détails de la culture et le type de collecte pour les intrants.
- Simplification de la page de mise à jour du plan d'approvisionnement.
- Ajout de la possibilité de filtrer les entreprises pour les DREAL.
- Amélioration de la gestion des erreurs lors de l'importation Excel pour les plans d'approvisionnement.
- Ajout de la possibilité d'importer des producteurs de biométhane via un fichier Excel.
- Ajout d'un formulaire de satisfaction pour les utilisateurs.
- Ajout de la gestion des entités DREAL.
- Possibilité de visualiser le prénom des utilisateurs.
- Amélioration de la gestion des validations logistiques SAF avec un indicateur de fonctionnalité.

### Évolutions techniques
- Refactor de code pour améliorer la réutilisabilité et la lisibilité.
- Mise à jour des migrations pour la gestion des sites et des biométhanes.
- Utilisation de nouvelles structures de données pour la gestion des matières premières et des intrants.
- Optimisation des requêtes en base de données pour améliorer les performances.
- Suppression de code obsolète et nettoyage du code.
- Amélioration de la gestion des erreurs et des validations.
- Refactor de la gestion des certificats d'électricité pour simplifier le code et améliorer la performance.
- Mise en place de tests unitaires pour garantir la qualité du code.
- Utilisation de variables d'environnement pour la configuration.
- Amélioration de la gestion des migrations pour éviter les conflits.
- Refactor de la gestion des modèles de sites pour utiliser l'héritage.
- Ajout de commentaires pour faciliter la compréhension du code.

### Autres changements
- Correction de bugs mineurs dans l'interface utilisateur.
- Mise à jour de la documentation.
- Amélioration des messages d'erreur.
- Correction de problèmes de performance.
- Corrections de migrations.
- Suppression de dépendances inutiles.
- Mise à jour des dépendances.
