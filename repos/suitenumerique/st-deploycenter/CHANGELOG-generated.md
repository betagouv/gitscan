## Changelog : st-deploycenter (30 derniers jours)

### Résumé
Les dernières mises à jour de st-deploycenter se concentrent sur l'amélioration de la gestion des comptes et des organisations, notamment avec l'ajout d'interfaces utilisateur pour la gestion des comptes et l'importation massive de SIRET. Des améliorations ont également été apportées à la gestion des droits et des services, ainsi qu'à l'infrastructure et à la robustesse du système.

### Évolutions fonctionnelles
- Ajout d'une interface utilisateur pour la suppression de comptes via l'UI et l'API (#38).
- Possibilité d'importer en masse des SIRET pour les abonnements via l'interface d'administration.
- Ajout de filtres supplémentaires dans l'interface d'administration pour faciliter la gestion des organisations.
- Affichage correct des services ayant une priorité d'affichage inférieure à 0.
- Ajout d'une carte "Messages" et amélioration de la gestion des droits (#36).
- Ajout de la possibilité de filtrer les organisations par type et corrections d'affichage (#25).
- Ajout d'une interface utilisateur pour la gestion des comptes et de filtres pour les organisations (#28).
- Amélioration de la gestion des droits avec un résolveur étendu et une jointure automatique pour les organisations (#33).
- L'API des comptes accepte désormais les requêtes POST dupliquées (#20).

### Évolutions techniques
- Refactorisation des résolveurs de droits et amélioration de la logique d'accès aux droits (#29).
- Mise à jour des routes et des sérialiseurs pour la gestion des comptes.
- Ajout du modèle Account et de l'entitlement admin associé.
- Amélioration de l'intégration avec Keycloak avec l'ajout de vérifications de santé.
- Mise à jour du scraping des métriques pour les comptes.
- Optimisation de l'autorisation des opérateurs.
- Mise à jour des étapes du workflow GitHub Actions pour utiliser les dernières versions (#39).

### Autres changements
- Mise à jour de la terminologie dans la documentation (readme).
- Correction de quelques traductions dans l'interface utilisateur.
- L'import DPNT est maintenant planifié à 8h du matin.
