## Changelog : acces-cible (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de performances, la maintenance technique et la préparation de futures évolutions. Des corrections de requêtes SQL inefficaces ont été apportées, ainsi que des ajustements pour la gestion des URLs et des migrations de données. L'interface utilisateur a également bénéficié de l'intégration d'un composant DSFR.

### Évolutions fonctionnelles
- Ajout du BOM UTF-8 aux exports CSV pour une meilleure compatibilité avec les logiciels de tableur. [#520](https://github.com/betagouv/acces-cible/issues/520)

### Évolutions techniques
- Correction de requêtes SQL N+1 pour améliorer les performances. [#538](https://github.com/betagouv/acces-cible/issues/538)
- Utilisation du composant DSFR Side Menu pour standardiser l'interface utilisateur. [#571](https://github.com/betagouv/acces-cible/issues/571)
- Mise à jour de Puma vers la version 8.0.1. [#540](https://github.com/betagouv/acces-cible/issues/540)
- Mise à jour de plusieurs dépendances mineures. [#549](https://github.com/betagouv/acces-cible/issues/549), [#546](https://github.com/betagouv/acces-cible/issues/546)
- Sécurisation du rendu des URLs externes et suppression d'une exception Brakeman liée à une potentielle vulnérabilité XSS. [#508](https://github.com/betagouv/acces-cible/issues/508)
- Remplacement de `client_max_limit` par `max_limit` dans la gem `pagy` pour corriger une dépréciation. [#533](https://github.com/betagouv/acces-cible/issues/533)

### Autres changements
- Nettoyage du code mort et des dépendances inutilisées. [#542](https://github.com/betagouv/acces-cible/issues/542)
- Ajout et annulation de plusieurs migrations pour le backfill des URLs des sites, en raison de problèmes rencontrés lors de l'application. [#558](https://github.com/betagouv/acces-cible/issues/558), [#557](https://github.com/betagouv/acces-cible/issues/557), [#556](https://github.com/betagouv/acces-cible/issues/556), [#555](https://github.com/betagouv/acces-cible/issues/555), [#554](https://github.com/betagouv/acces-cible/issues/554), [#553](https://github.com/betagouv/acces-cible/issues/553), [#551](https://github.com/betagouv/acces-cible/issues/551), [#530](https://github.com/betagouv/acces-cible/issues/530)
- Correction d'une faute de frappe dans le fichier `queue.yml`. [#567](https://github.com/betagouv/acces-cible/issues/567)
