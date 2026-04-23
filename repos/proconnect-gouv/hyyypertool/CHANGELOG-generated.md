## Changelog : hyyypertool (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment en remplaçant le framework DSFR par un thème Tailwind CSS personnalisé. Des corrections de bugs ont été apportées pour améliorer la fiabilité de la recherche et de la pagination, et des informations supplémentaires ont été ajoutées pour faciliter la gestion des organisations.

### Évolutions fonctionnelles
- Ajout du libellé pour la tranche d'effectifs d'une unité légale, améliorant la clarté des informations affichées. [#1520](https://github.com/proconnect-gouv/hyyypertool/issues/1520)
- Amélioration de l'interface utilisateur suite à la suppression du framework DSFR, pour une expérience plus cohérente. [#1560](https://github.com/proconnect-gouv/hyyypertool/issues/1560)
- Correction du menu à trois points, qui s'ouvrait incorrectement par le haut. [#1561](https://github.com/proconnect-gouv/hyyypertool/issues/1561)
- Suppression automatique des tags `is/type` lors d'une recherche par champ dédié (email, SIRET, modérateur), simplifiant l'utilisation des filtres. [#1536](https://github.com/proconnect-gouv/hyyypertool/issues/1536)
- Correction d'un bug où un token API expiré affichait silencieusement une liste vide de responsables. [#1548](https://github.com/proconnect-gouv/hyyypertool/issues/1548)

### Évolutions techniques
- Remplacement du framework DSFR par un thème Tailwind CSS personnalisé, offrant plus de flexibilité et de contrôle sur l'apparence de l'application. [#1508](https://github.com/proconnect-gouv/hyyypertool/issues/1508)
- Correction d'une fuite de `hx-trigger` qui cassait les boutons de pagination. [#1519](https://github.com/proconnect-gouv/hyyypertool/issues/1519)
- Ajout de tests pour les routes de l'équipe. [#1518](https://github.com/proconnect-gouv/hyyypertool/issues/1518)
- Mise à jour de plusieurs dépendances, incluant `hono`, `drizzle-kit`, `@proconnect-gouv/proconnect.identite`, `jose`, `actions/upload-artifact`, `drizzle-orm`, `cypress`, `typescript`, `@types/pg`, `@types/bun`, `sentry`, `tailwindcss`, `preact` et `happy-dom`.

### Autres changements
- Documentation : Ajout d'informations sur l'ajout du libellé pour la tranche d'effectifs.
- Diverses mises à jour de dépendances pour maintenir la sécurité et la stabilité du projet.
