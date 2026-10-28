## Changelog : pitchou (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois-ci, Pitchou renforce ses capacités de gestion et de communication. Les utilisateurs bénéficient de nouveaux outils d'export de données, d'une gestion administrative améliorée des instructeurs et de l'introduction des notifications par email. L'interface a également été affinée pour offrir une navigation plus fluide et une saisie de données plus intuitive.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
  - Export des dossiers filtrés aux formats CSV et ODS [#710]
  - Gestion des personnes impliquées dans un dossier
  - Administration des groupes d'instructeurs et gestion de l'usage ProConnect [#708]
  - Ajout de la date DDEP dans les dossiers [#732]
  - Nouvelles options de décision, UICN et suppression de pièces jointes [#705]
  - Mise en place des notifications par email [#727]
- **Améliorations et corrections** :
  - Amélioration de la gestion des envois d'emails (suivi des échecs et gestion des fichiers volumineux) [#735]
  - Optimisation de l'interface utilisateur (pagination, onglets, boutons d'action et réactivité des formulaires) [#734, #707, #706]
  - Clarification des imports de prescriptions et des conversions de surfaces [#714]
  - Corrections diverses de l'interface (typos et messages d'erreur) [#713, #711]

### Évolutions techniques
- **Architecture et données** :
  - Fiabilisation de la synchronisation complète avec la Démarche Numérique [#733]
  - Mise en place de l'upload direct vers S3 [#704]
  - Restructuration de la base de données pour les porteurs de projet [#709]
- **Maintenance et outils** :
  - Montée de version majeure des frameworks et langages (SvelteKit 3 [#724], TypeScript 6 [#721], Vitest 5 [#723], pnpm 12 [#730])
  - Optimisation de la chaîne de qualité et de CI/CD (audit pipeline [#731], nouveaux outils de linting Oxlint et Oxfmt [#726, #717], mise à jour GitHub Actions [#725])
  - Ajout d'un mode de capture d'emails local pour le développement [#715]

### Autres changements
- Nettoyage du projet (suppression de la page "Tableau de suivi" devenue obsolète [#729] et retrait de dépendances mineures [#719])
