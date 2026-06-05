## Changelog : maestro (30 derniers jours, au 4 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des prélèvements, des analyses et des laboratoires. Des correctifs ont été apportés pour améliorer la stabilité et la fiabilité de l'application, notamment concernant l'envoi d'emails, la gestion des dates et l'affichage des informations. De nouvelles fonctionnalités ont été ajoutées pour faciliter la configuration des laboratoires et la gestion des RAI (Autorisations de Retrait d'échantillons). Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de modifier les analytes des laboratoires en PPV (Prélèvement, Prescription, Vérification) [#919](https://github.com/betagouv/maestro/issues/919).
- Implémentation d'une interface administrateur pour visualiser toutes les RAI reçues [#870](https://github.com/betagouv/maestro/issues/870).
- Ajout d'un filtre par département pour les administrations centrales lors de la recherche de prélèvements [#937](https://github.com/betagouv/maestro/issues/937).
- Possibilité de synchroniser les modifications d'utilisateurs de Maestro avec Brevo (outil d'emailing) [#840](https://github.com/betagouv/maestro/issues/840).
- Ajout d'un filtre sur les prélèvements avec plusieurs exemplaires [#850](https://github.com/betagouv/maestro/issues/850).
- Amélioration de l'affichage des prélèvements pour les administrateurs [#872](https://github.com/betagouv/maestro/issues/872).
- Ajout d'une interface de configuration des laboratoires [#920](https://github.com/betagouv/maestro/issues/920).
- Possibilité d'imprimer le formulaire vierge d'un DAO (Demande d'Autorisation d'Origine) après la sélection de l'abattoir [#1011](https://github.com/betagouv/maestro/issues/1011).
- Ajout de certaines LMR (Lettre de Mission de Recherche) optionnelles [#1013](https://github.com/betagouv/maestro/issues/1013).

### Évolutions techniques
- Refactor de l'URL builder pour une meilleure typage [#987](https://github.com/betagouv/maestro/issues/987).
- Amélioration du typage des réponses de l'API [#1006](https://github.com/betagouv/maestro/issues/1006).
- Utilisation d'une meilleure méthode pour ajouter des pièces jointes aux emails (nodemailer) [#991](https://github.com/betagouv/maestro/issues/991).
- Passage de la fonction GPG en mode non interactif [#938](https://github.com/betagouv/maestro/issues/938).
- Ajout d'un service OIDC local pour l'authentification [#841](https://github.com/betagouv/maestro/issues/841).
- Correction de la gestion des dates et des coerce pour les DAI et RAI [#948](https://github.com/betagouv/maestro/issues/948).
- Correction de l'affichage des dates dans la dernière étape de création d'un prélèvement [#979](https://github.com/betagouv/maestro/issues/979).

### Autres changements
- Correction de bugs concernant la réinitialisation de la sélection d'abattoir [#1012](https://github.com/betagouv/maestro/issues/1012).
- Correction de l'interprétation de la nouvelle syntaxe LMR d'Inovalys [#1005](https://github.com/betagouv/maestro/issues/1005).
- Prise en compte des corrections apportées par Inovalys [#1004](https://github.com/betagouv/maestro/issues/1004).
- Ajout des types de ressources "réglementation" et "modèle" pour les documents [#988](https://github.com/betagouv/maestro/issues/988).
- Suppression des utilisateurs non actifs de la liste des préleveurs [#990](https://github.com/betagouv/maestro/issues/990).
- Correction de la recherche de la programmation associée à une matrice [#965](https://github.com/betagouv/maestro/issues/965).
- Correction du filtre des prélèvements exportés par année [#964](https://github.com/betagouv/maestro/issues/964).
- Correction du status des analyses lors du passage de "non recevable" à "notification non reçu" [#978](https://github.com/betagouv/maestro/issues/978).
- Correction de la gestion des status suite à l'analyse des échantillons [#947](https://github.com/betagouv/maestro/issues/947).
- Mise à jour de nombreuses dépendances (React, Node.js, PostgreSQL, S3, Browserless, Dex, etc.).
- Diverses corrections de bugs et améliorations de la qualité du code.
