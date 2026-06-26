## Changelog : gestion-des-subventions-locales (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment la gestion des projets, des notifications et des importations de données. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de l'application. Des optimisations techniques ont également été réalisées pour améliorer les performances, en particulier concernant la synchronisation avec le DS et la génération de documents.

### Évolutions fonctionnelles
- Possibilité de définir le nom du fichier PDF lors de l'envoi d'une notification d'acceptation. [#736](https://github.com/betagouv/gestion-des-subventions-locales/issues/736)
- Unification de la page de détail d'un projet, pilotée par son état, simplifiant ainsi l'accès aux informations clés. [#753](https://github.com/betagouv/gestion-des-subventions-locales/issues/753)
- Ajout d'une entrée de menu dédiée pour les modèles de publipostage, facilitant leur accès. [#750](https://github.com/betagouv/gestion-des-subventions-locales/issues/750)
- Import des dossiers de tous les territoires gérés. [#749](https://github.com/betagouv/gestion-des-subventions-locales/issues/749)
- Affichage du périmètre, des dates Turgot et du report dans l'interface d'administration. [#748](https://github.com/betagouv/gestion-des-subventions-locales/issues/748)
- Correction de la sélection de projets sur plusieurs pages, améliorant la navigation et la gestion des projets. [#766](https://github.com/betagouv/gestion-des-subventions-locales/issues/766)
- Correction du formulaire d'avis de la commission DETR. [#774](https://github.com/betagouv/gestion-des-subventions-locales/issues/774)
- Correction du décochage silencieux des filtres de type ModelMultipleChoiceFilter. [#737](https://github.com/betagouv/gestion-des-subventions-locales/issues/737)
- Correction de la perte du curseur des dossiers supprimés sur les pages vides. [#742](https://github.com/betagouv/gestion-des-subventions-locales/issues/742)

### Évolutions techniques
- Limitation de chaque token du proxy DS à une seule requête simultanée pour améliorer la robustesse. [#758](https://github.com/betagouv/gestion-des-subventions-locales/issues/758)
- Ajout d'un verrou anti-concurrence sur la synchronisation des dossiers DS pour éviter les conflits. [#740](https://github.com/betagouv/gestion-des-subventions-locales/issues/740)
- Augmentation du timeout Gunicorn à 120s pour la génération de documents, résolvant les problèmes de timeout. [#763](https://github.com/betagouv/gestion-des-subventions-locales/issues/763)
- Activation de la compression WhiteNoise (gzip + Brotli) des fichiers statiques pour améliorer les performances de chargement. [#757](https://github.com/betagouv/gestion-des-subventions-locales/issues/757)
- Priorisation des tâches Celery selon le contexte d'appel pour une meilleure gestion des ressources. [#751](https://github.com/betagouv/gestion-des-subventions-locales/issues/751)
- Refactoring de plusieurs composants (projets, notifications, DS) pour améliorer la maintenabilité et la lisibilité du code.
- Utilisation de Class-Based Views (CBV) à la place de Function-Based Views (FBV) pour certaines vues, améliorant la structure et la réutilisabilité du code.
- Ajout d'un mixin SafeRedirectMixin pour gérer les redirections POST de manière sécurisée.
- Amélioration de la gestion des erreurs et ajout de journalisation structurée pour le proxy DS.
- Conversion des largeurs de tableaux TipTap en pourcentages pour l'export PDF, améliorant la compatibilité.

### Autres changements
- Journalisation des modifications des utilisateurs via l'admin Django pour l'audit. [#741](https://github.com/betagouv/gestion-des-subventions-locales/issues/741)
- Correction d'un test flaky lié à la création de collègues. [#738](https://github.com/betagouv/gestion-des-subventions-locales/issues/738)
- Suppression des rafraîchissements DS bloquants à l'ouverture des modales. [#743](https://github.com/betagouv/gestion-des-subventions-locales/issues/743)
- Rendre le champ enveloppe readonly dans l'admin ProjetAction. [#762](https://github.com/betagouv/gestion-des-subventions-locales/issues/762)
- Initialiser l'assiette d'un DotationProjet à finance_cout_total par défaut. [#765](https://github.com/betagouv/gestion-des-subventions-locales/issues/765)
- Correction de l'initialisation de l'assiette d'un DotationProjet.
- Amélioration de l'affichage du tableau des enveloppes. [#752](https://github.com/betagouv/gestion-des-subventions-locales/issues/752)
- Correction de l'affichage du formulaire avis detr.
