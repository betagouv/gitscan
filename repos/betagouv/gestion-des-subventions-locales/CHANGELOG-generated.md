## Changelog : gestion-des-subventions-locales (30 derniers jours, au 18 août 2026)

### Résumé
Ce mois-ci, l'outil a bénéficié d'une refonte majeure de son système de notifications et d'une amélioration significative de la gestion documentaire. Les utilisateurs peuvent désormais gérer plus facilement les documents (téléchargement groupé, mise à jour, génération de lettres de refus) et suivre plus précisément l'état de notification de chaque projet directement depuis les listes.

### Évolutions fonctionnelles
- **Gestion documentaire**
  - Possibilité de télécharger l'ensemble des documents générés via un nouveau bouton dédié [#802](https://github.com/betagouv/gestion-des-subventions-locales/pull/802).
  - Tous les documents générés sont désormais téléchargeables individuellement [#742](https://github.com/betagouv/gestion-des-subventions-locales/pull/742).
  - Les fichiers générés peuvent désormais être mis à jour.
  - Ajout de la fonctionnalité de génération de lettres de refus ou de classement sans suite [#793](https://github.com/betagouv/gestion-des-subventions-locales/pull/793).
- **Système de notifications**
  - Refonte complète de l'onglet des notifications pour une meilleure lisibilité [#783](https://github.com/betagouv/gestion-des-subventions-locales/pull/783).
  - Ajout de badges de notification dans l'onglet dédié [#788](https://github.com/betagouv/gestion-des-subventions-locales/pull/788).
  - Affichage du statut de notification directement dans les listes de projets [#789](https://github.com/betagouv/gestion-des-subventions-locales/pull/789).
  - Sécurisation du processus : la génération et l'import de documents sont désormais bloqués lorsqu'un projet est notifié [#790](https://github.com/betagouv/gestion-des-subventions-locales/pull/790).

### Évolutions techniques
- **Architecture et outils**
  - Migration de la gestion des dépendances de `pip-tools` vers `uv` [#786](https://github.com/betagouv/gestion-des-subventions-locales/pull/786).
  - Intégration de `HTMX` pour améliorer l'interactivité des formulaires (assiette de dotation, notifications, génération de documents) [#787](https://github.com/betagouv/gestion-des-subventions-locales/pull/787).
  - Mise en place de la nouvelle structure de données pour le système de notifications.
  - Ajustements techniques pour garantir la compatibilité du Design System (DSFR) avec l'utilisation de `uv` [#794](https://github.com/betagouv/gestion-des-subventions-locales/pull/794).
- **Optimisations et corrections**
  - Optimisation des propriétés de statut de notification et refactorisation du code pour limiter la duplication.
  - Correction de l'affichage des erreurs HTMX [#798](https://github.com/betagouv/gestion-des-subventions-locales/pull/798).

### Autres changements
- Ajout d'une commande permettant l'importation des données du COG [#782](https://github.com/betagouv/gestion-des-subventions-locales/pull/782).
- Mise en place de `dependabot.yml` pour automatiser la maintenance des dépendances [#797](https://github.com/betagouv/gestion-des-subventions-locales/pull/797).
- Nettoyage et maintenance de scripts internes (`generate_dump.py`).
