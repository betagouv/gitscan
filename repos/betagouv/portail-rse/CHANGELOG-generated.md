## Changelog : portail-rse (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, les évolutions du portail RSE se sont concentrées sur l'amélioration de la gestion des entreprises, notamment l'ajout du code postal, la correction de bugs liés à la recherche d'entreprises et la simplification des processus d'habilitation et d'invitation. Des améliorations ont également été apportées à l'export des données VSME et à l'accès aux fonctionnalités pour les entreprises non qualifiées. Enfin, des refactorings techniques ont été effectués pour améliorer la maintenabilité du code.

### Évolutions fonctionnelles
- **Entreprises :** Ajout du code postal du siège social lors de la création d'une entreprise et possibilité de l'exporter vers Metabase. Correction d'un bug empêchant la recherche d'entreprises avec des codes postaux incorrects. Affichage du code postal dans le tableau de bord pour faciliter le diagnostic des problèmes.
- **Rapports VSME :** Pré-remplissage des rapports VSME à partir de rapports précédents. Amélioration du template Excel pour l'export des indicateurs VSME.
- **Accès et habilitations :** Simplification du processus d'habilitation des utilisateurs Proconnect. Les utilisateurs Proconnect deviennent automatiquement éditeurs sur une entreprise existante. Suppression du concept de confirmation d'habilitation.
- **Tableau de bord :** Amélioration de l'accessibilité du résumé du tableau de bord. Restriction de l'accès à la gestion des réglementations du tableau de bord aux entreprises qualifiées.
- **Ajout d'entreprise :** Possibilité d'ajouter une entreprise sans être connecté.
- **Analyses IA et indicateurs VSME :** Autorisation d'accès aux analyses IA et à l'espace indicateurs VSME pour les entreprises non qualifiées.

### Évolutions techniques
- **Refactoring :** Plusieurs refactorings ont été effectués pour améliorer la structure du code, notamment au niveau de la gestion des propriétaires, des invitations et des acceptations.
- **Dépendances :** Mise à jour de plusieurs dépendances : `pillow`, `pytest`, `cryptography`, `pygments`, `requests`, `picomatch`, `aiohttp`, `pyjwt`.
- **Outils :** Remplacement de `pipenv` par `uv` pour la gestion des dépendances.
- **Documentation :** Complétion du fichier README.

### Autres changements
- Suppression de fichiers inutiles et de code obsolète.
- Ajout du fichier `.python-version` pour faciliter le déploiement.
- Correction de typos et amélioration de la lisibilité du code.
