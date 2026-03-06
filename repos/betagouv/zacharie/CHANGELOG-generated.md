## Changelog : zacharie (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à Zacharie au cours du dernier mois. Les utilisateurs bénéficieront d'une meilleure expérience grâce à des corrections de bugs, des améliorations de l'interface utilisateur et de nouvelles fonctionnalités comme la création simplifiée de CCG (Circuit Court Groupement) lors du flux de déclaration de FEI (Fiche d'Examen Initiale). Des optimisations techniques ont également été réalisées pour améliorer la synchronisation des données et la gestion des entités.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la création de partenaires avec une adresse email déjà existante. [#159](https://github.com/betagouv/zacharie/issues/159)
- Amélioration de la gestion des fiches FEI : possibilité de créer un CCG directement pendant le processus. [#147](https://github.com/betagouv/zacharie/issues/147)
- Synchronisation des contacts des circuits courts avec Brevo (outil de communication). [#144](https://github.com/betagouv/zacharie/issues/144)
- Correction de l'export des colonnes SVI. [#206](https://github.com/betagouv/zacharie/issues/206)
- Clôture automatique des fiches circuit court lors de la transmission. [#200](https://github.com/betagouv/zacharie/issues/200)
- Amélioration du wording du destinataire. [#205](https://github.com/betagouv/zacharie/issues/205)
- Ajout d'une page FAQ avec des guides et des liens de navigation. [#201](https://github.com/betagouv/zacharie/issues/201)
- Ajout d'un placeholder pour les vues vides. [#167](https://github.com/betagouv/zacharie/issues/167)
- Amélioration de la table et de la barre de recherche. [#164](https://github.com/betagouv/zacharie/issues/164)
- Correction de l'affichage du champ `feisAssigned` pour les SVI.
- Amélioration de l'interface utilisateur pour l'onboarding. [#195](https://github.com/betagouv/zacharie/issues/195)
- Ajout d'une nouvelle fonctionnalité pour la création de fiches. [#197](https://github.com/betagouv/zacharie/issues/197)
- Correction de l'affichage dynamique de la FAQ.
- Correction du menu responsive.
- Suppression d'un lien dupliqué.
- Correction d'un warning lors de la création d'un nouveau partenaire. [#192](https://github.com/betagouv/zacharie/issues/192)
- Correction de l'affichage des champs sur les carcasses.
- Correction de la pagination.
- Amélioration du chargement des entités et des utilisateurs.
- Correction de la transmission des carcasses.

### Évolutions techniques
- Refactorisation de la synchronisation des données hors ligne avec une nouvelle approche utilisant une requête POST en masse pour améliorer les performances.
- Extraction de la logique de sauvegarde des FEIs et des carcasses dans des fonctions distinctes pour une meilleure organisation du code.
- Optimisation du chargement des FEIs.
- Nettoyage du code et suppression de code inutile.
- Mise à jour de la documentation (CLAUD.md et README.md).
- Amélioration de la gestion des tests.
- Correction de problèmes de race condition liés à la transmission des données.
- Suppression des FEIs terminés de l'application.

### Autres changements
- Mise à jour des dépendances : minimatch, @getbrevo/brevo, tar, ajv. [#189](https://github.com/betagouv/zacharie/issues/189), [#187](https://github.com/betagouv/zacharie/issues/187), [#186](https://github.com/betagouv/zacharie/issues/186)
- Correction de la configuration de Brevo.
- Mise à jour du fichier `.gitignore`.
- Amélioration de la gestion du cache administrateur.
- Correction de bugs mineurs et améliorations diverses de l'interface utilisateur.
