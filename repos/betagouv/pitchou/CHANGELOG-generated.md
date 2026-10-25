## Changelog : pitchou (30 derniers jours, au 24 octobre 2026)

### Résumé
Ce mois-ci, l'application a franchi des étapes importantes pour améliorer l'expérience des agents et la gestion des dossiers. Les utilisateurs bénéficient désormais de notifications par e-mail, de nouvelles capacités d'exportation de données (CSV, ODS) et d'une meilleure gestion des acteurs impliqués dans les dossiers. L'interface a également été affinée pour être plus ergonomique et responsive.

### Évolutions fonctionnelles
- **Gestion des dossiers et données** :
  - Ajout de la gestion des personnes impliquées dans un dossier.
  - Structuration de l'entité "porteur de projet" en base de données [#709](https://github.com/betagouv/pitchou/pull/709).
  - Possibilité de supprimer des pièces jointes [#705](https://github.com/betagouv/pitchou/pull/705).
  - Exportation des dossiers filtrés aux formats CSV et ODS [#710](https://github.com/betagouv/pitchou/pull/710).
- **Administration et notifications** :
  - Mise en place des notifications par e-mail [#727](https://github.com/betagouv/pitchou/pull/727).
  - Gestion des groupes d'instructeurs et utilisation de ProConnect pour l'administration [#708](https://github.com/betagouv/pitchou/pull/708).
- **Améliorations de l'interface (UI/UX) et corrections** :
  - Optimisation de l'affichage des onglets, de la pagination et des boutons d'action dans les dossiers [#707](https://github.com/betagouv/pitchou/pull/707).
  - Mise en conformité responsive du layout de saisie des espèces [#706](https://github.com/betagouv/pitchou/pull/706).
  - Corrections diverses : clarification des imports de prescriptions et des conversions de surfaces [#714](https://github.com/betagouv/pitchou/pull/714), correction de typos [#713](https://github.com/betagouv/pitchou/pull/713) et suppression de notifications de champs obligatoires en double [#711](https://github.com/betagouv/pitchou/pull/711).

### Évolutions techniques
- **Mises à jour majeures du framework** :
  - Passage à SvelteKit 3 [#724](https://github.com/betagouv/pitchou/pull/724) et TypeScript 6 [#721](https://github.com/betagouv/pitchou/pull/721).
- **Infrastructure et stockage** :
  - Implémentation de l'upload direct des fichiers sur S3 [#704](https://github.com/betagouv/pitchou/pull/704).
- **Qualité et outils de développement** :
  - Modernisation de la chaîne de test avec la montée en version de Vitest v5 [#723](https://github.com/betagouv/pitchou/pull/723).
  - Optimisation du linting et du formatage avec l'introduction d'oxfmt [#726](https://github.com/betagouv/pitchou/pull/726) et oxlint [#717](https://github.com/betagouv/pitchou/pull/717).
  - Mise à jour de l'outil de gestion de paquets vers pnpm 12 [#730](https://github.com/betagouv/pitchou/pull/730).
- **CI/CD et maintenance** :
  - Audit du pipeline de CI [#731](https://github.com/betagouv/pitchou/pull/731) et mise à jour des dépendances GitHub Actions [#725](https://github.com/betagouv/pitchou/pull/725).
  - Nettoyage du projet : suppression de la page "Tableau de suivi" devenue obsolète [#729](https://github.com/betagouv/pitchou/pull/729) et réduction du nombre de dépendances [#719](https://github.com/betagouv/pitchou/pull/719).

### Autres changements
- Ajout d'une option de capture d'e-mails locale pour faciliter les tests en environnement de développement [#715](https://github.com/betagouv/pitchou/pull/715).
