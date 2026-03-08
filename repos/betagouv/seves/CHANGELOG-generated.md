## Changelog : seves (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Sèves au cours des 30 derniers jours. Les évolutions concernent principalement l'interface utilisateur, avec des améliorations de l'expérience utilisateur sur les pages de détail, les listes d'objets et les formulaires. Des corrections de bugs et des optimisations de performance ont également été réalisées, notamment concernant le chargement des pages et la gestion des documents. Enfin, des mises à jour techniques ont été effectuées pour améliorer la sécurité et la qualité du code.

### Évolutions fonctionnelles
- Ajout du numéro de fiche sur la page de création de message [#1733](https://github.com/betagouv/seves/issues/1733).
- Ajout de l'Organisme Nuisible pour les SV.
- Redesign des cartes dans TIAC.
- Possibilité d'ajouter des agents dans la copie des destinataires des DI.
- Affichage des numéros de téléphone des agents dans la signature des emails.
- Ajout d'une option de suivi pour EnregistrementSimple.
- Ajout d'un nouveau bloc de liens libres avec API sur TIAC.
- Amélioration de l'UX pour le composant LienLibre.
- Correction d'une vulnérabilité XSS dans le chargement massif de documents sur fiche.
- Ajout de Saint-Pierre-et-Miquelon dans les départements.
- Possibilité d'activer les nouveaux utilisateurs par défaut sur des environnements spécifiques.
- Amélioration des tests pour les documents.
- Ajout d'une alerte/warning pour l'équipe sur l'environnement de production.

### Évolutions techniques
- Mise à jour de Ruff (0.15.0 -> 0.15.2 -> 0.15.4).
- Mise à jour de Redis (7.1.1 -> 7.2.1).
- Mise à jour de django-environ (0.12.0 -> 0.12.1 -> 0.13.0).
- Mise à jour de django-dsfr (3.3.0 -> 3.3.1).
- Mise à jour de sentry-sdk[django] (2.49.0 -> 2.51.0 -> 2.53.0).
- Mise à jour de urllib3 (2.5.0 -> 2.6.3).
- Mise à jour de django-reversion-compare (0.19.1 -> 0.19.2).
- Mise à jour de pytest-django (4.11.1 -> 4.12.0).
- Mise à jour de playwright (1.57.0 -> 1.58.0).
- Ajout de linting avec Biome.
- Formatage du code JavaScript et CSS avec Biome.
- Utilisation de Ruff pour trier les imports.
- Nettoyage de code ancien lié au chargement massif de documents synchronisés.
- Refactoring pour préparer le backend au chargement massif de documents asynchrones sur les messages.
- Configuration du fichier `.editorconfig` pour les fichiers YAML et formatage de `.pre-commit-config.yaml`.
- Ajout du paramètre `--fix` au hook ruff de pre-commit.
- Correction d'un problème de détection incorrecte des fichiers XLS.
- Amélioration de la gestion des types de documents lors de la modification.

### Autres changements
- Correction de bugs mineurs sur l'interface utilisateur (UX).
- Optimisations de performance pour le chargement des pages et les listes d'objets.
- Suppression de feature flags obsolètes.
- Amélioration des tests unitaires et d'intégration.
- Correction d'une vulnérabilité potentielle dans les liens rappel conso.
- Suppression des doublons dans la recherche de texte libre.
- Amélioration de la recherche dans les champs ChoiceJs.
- Modification de l'ordre des champs de filtre dans TIAC.
- Ajout de préfixes pour les badges de nombre de participants dans TIAC.
- Amélioration de l'affichage des établissements sur SSA.
- Limitation du nombre de caractères dans le nom de fichier des documents.
- Correction d'erreurs JavaScript.
- Amélioration de la cohérence des dates entre TIAC et SSA.
- Suppression d'une vérification redondante dans les contraintes.
