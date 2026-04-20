## Changelog : hyyypertool (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur en corrigeant des bugs liés aux filtres et à la pagination, et en ajoutant des informations supplémentaires aux données affichées. Une migration importante vers Tailwind CSS a également été amorcée pour moderniser l'interface utilisateur et améliorer sa flexibilité.

### Évolutions fonctionnelles
- Ajout du libellé pour la tranche d'effectifs de l'unité légale, améliorant la clarté des informations affichées. [#1520](https://github.com/proconnect-gouv/hyyypertool/issues/1520)
- Correction d'un bug où le filtre `service:` positif était ignoré dans la liste des modérations, assurant un filtrage correct des données. [#1538](https://github.com/proconnect-gouv/hyyypertool/issues/1538)
- Correction d'un problème avec les boutons de pagination qui causaient une fuite de mémoire liée à `hx-trigger`. [#1519](https://github.com/proconnect-gouv/hyyypertool/issues/1519)
- Amélioration du filtre : suppression automatique des tags `is/type` lors d'une recherche par champ dédié (email, SIRET, modérateur), pour une expérience de filtrage plus intuitive. [#1536](https://github.com/proconnect-gouv/hyyypertool/issues/1536)
- Ajout d'un nouveau type de réponse. [#1509](https://github.com/proconnect-gouv/hyyypertool/issues/1509)

### Évolutions techniques
- Début de la migration des composants DSFR vers Tailwind CSS et `tailwind-variants` pour une interface utilisateur plus moderne et personnalisable. [#1508](https://github.com/proconnect-gouv/hyyypertool/issues/1508)
- Ajout de tests pour les routes de l'équipe. [#1518](https://github.com/proconnect-gouv/hyyypertool/issues/1518)
- Mise à jour de TypeScript vers la version 6.0.2. [#1547](https://github.com/proconnect-gouv/hyyypertool/issues/1547)

### Autres changements
- Diverses mises à jour de dépendances pour assurer la sécurité et la stabilité du projet.
