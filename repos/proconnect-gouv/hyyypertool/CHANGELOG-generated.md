## Changelog : hyyypertool (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, l'équipe a continué à améliorer l'interface utilisateur en remplaçant progressivement les composants DSFR par une nouvelle thématique Tailwind CSS personnalisée. Des corrections de bugs ont été apportées, notamment concernant le filtre de recherche et le menu à trois points, améliorant ainsi l'expérience utilisateur. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct de la liste des dirigeants en cas de token API expiré. [#1548](https://github.com/proconnect-gouv/hyyypertool/issues/1548)
- Ajout du libellé pour la tranche d'effectifs de l'unité légale, améliorant la clarté des informations affichées. [#1520](https://github.com/proconnect-gouv/hyyypertool/issues/1520)
- Correction du filtre `service:` qui était ignoré lors de la recherche, permettant désormais de filtrer correctement les modérations par service. [#1538](https://github.com/proconnect-gouv/hyyypertool/issues/1538)
- Correction du bug lié à l'ouverture du menu à trois points, qui s'ouvrait désormais depuis le haut de l'écran. [#1561](https://github.com/proconnect-gouv/hyyypertool/issues/1561)
- Amélioration de l'interface utilisateur suite à la suppression du DSFR, rendant l'application plus cohérente visuellement. [#1560](https://github.com/proconnect-gouv/hyyypertool/issues/1560)
- Suppression automatique des filtres `is/type` lors de l'utilisation des champs de recherche dédiés (email, SIRET, modérateur). [#1536](https://github.com/proconnect-gouv/hyyypertool/issues/1536)

### Évolutions techniques
- Remplacement progressif des composants DSFR par une nouvelle thématique Tailwind CSS personnalisée. [#1508](https://github.com/proconnect-gouv/hyyypertool/issues/1508)
- Mise à jour de plusieurs dépendances, notamment `hono`, `drizzle-kit`, `@proconnect-gouv/proconnect.identite`, `jose`, `actions/upload-artifact`, `drizzle-orm`, `cypress`, `@types/pg` et `@types/bun`.
- Ajout de tests pour les routes de l'équipe. [#1518](https://github.com/proconnect-gouv/hyyypertool/issues/1518)

### Autres changements
- Publication des versions 2026.4.0, 2026.4.1, 2026.4.2, 2026.4.3 et 2026.4.4.
- Correction d'une fuite de `hx-trigger` qui cassait les boutons de pagination. [#1519](https://github.com/proconnect-gouv/hyyypertool/issues/1519)
