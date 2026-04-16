## Changelog : hyyypertool (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, Hyyypertool a bénéficié d'améliorations significatives de l'expérience utilisateur, notamment une meilleure gestion des filtres de recherche et l'ajout d'informations sur les tranches d'effectifs des entités légales. Des corrections de bugs ont également été apportées pour améliorer la fiabilité de l'application. L'interface utilisateur a été modernisée en remplaçant les composants DSFR par un thème Tailwind CSS personnalisé.

### Évolutions fonctionnelles
- Ajout du libellé pour la tranche d'effectifs d'une unité légale, améliorant la clarté des informations affichées. [#1520](https://github.com/proconnect-gouv/hyyypertool/issues/1520)
- Amélioration de la barre de recherche Hyyyper avec une suppression automatique des filtres `is/type` lors de l'utilisation des champs de recherche dédiés (email, SIRET, modérateur), pour une expérience plus intuitive. [#1536](https://github.com/proconnect-gouv/hyyypertool/issues/1536)
- Correction d'un bug où le filtre `service:` positif était ignoré dans la liste des modérations, assurant un affichage correct des résultats filtrés. [#1538](https://github.com/proconnect-gouv/hyyypertool/issues/1538)
- Ajout d'un nouveau type de réponse. [#1509](https://github.com/proconnect-gouv/hyyypertool/issues/1509)

### Évolutions techniques
- Migration de l'interface utilisateur de DSFR vers un thème Tailwind CSS personnalisé, offrant plus de flexibilité et de contrôle sur le style de l'application. [#1508](https://github.com/proconnect-gouv/hyyypertool/issues/1508)
- Ajout de tests pour les routes de l'équipe, améliorant la couverture de test du projet. [#1518](https://github.com/proconnect-gouv/hyyypertool/issues/1518)
- Correction d'une fuite de mémoire causée par `hx-trigger` sur les boutons de pagination. [#1519](https://github.com/proconnect-gouv/hyyypertool/issues/1519)

### Autres changements
- Mises à jour de dépendances pour TypeScript, les types de PostgreSQL, Bun, et divers autres paquets.
- Mises à jour des paquets Sentry pour la surveillance des erreurs.
- Mises à jour de Cypress et des actions GitHub pour l'intégration continue.
