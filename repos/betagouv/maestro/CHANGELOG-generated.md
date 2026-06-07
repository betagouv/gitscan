## Changelog : maestro (30 derniers jours, au 4 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la gestion des prélèvements, des analyses et des laboratoires, notamment avec l'ajout d'interfaces de configuration et de nouvelles fonctionnalités pour les RAI et les laboratoires. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, ainsi que des mises à jour techniques pour maintenir la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'une interface administrateur pour visualiser toutes les RAI [#898](https://github.com/betagouv/maestro/issues/898).
- Possibilité de modifier les analytes des laboratoires en PPV [#919](https://github.com/betagouv/maestro/issues/919).
- Amélioration de la gestion des prélèvements pour les administrateurs, avec correction de l'affichage [#897](https://github.com/betagouv/maestro/issues/897).
- Ajout de filtres par département pour les administrations centrales dans la gestion des prélèvements [#930](https://github.com/betagouv/maestro/issues/930).
- Possibilité d'imprimer le formulaire vierge pour les DAO après sélection de l'abattoir [#1011](https://github.com/betagouv/maestro/issues/1011).
- Amélioration de la gestion des conformités des prélèvements, avec affichage d'un message d'alerte avant envoi (revert puis réintégration) [#902](https://github.com/betagouv/maestro/issues/902).
- Ajout de la gestion des non quantifiables pour Cereco [#945](https://github.com/betagouv/maestro/issues/945).
- Ajout de certaines LMR optionnelles [#1013](https://github.com/betagouv/maestro/issues/1013).
- Correction de la réinitialisation de la sélection d'un abattoir lors de la création d'un prélèvement [#1012](https://github.com/betagouv/maestro/issues/1012).

### Évolutions techniques
- Amélioration du typage des réponses de l'API pour une meilleure robustesse [#1006](https://github.com/betagouv/maestro/issues/1006).
- Refactorisation de l'URL avec l'ajout d'un builder typé [#987](https://github.com/betagouv/maestro/issues/987).
- Utilisation d'une meilleure méthode pour ajouter les pièces jointes avec Nodemailer [#991](https://github.com/betagouv/maestro/issues/991).
- Passage de GPG en mode non interactif [#937](https://github.com/betagouv/maestro/issues/937).
- Ajout d'une table pour stocker toutes les RAI reçues [#870](https://github.com/betagouv/maestro/issues/870).
- Ajout d'une interface au S3 local [#889](https://github.com/betagouv/maestro/issues/889).
- Correction de la syntaxe de parsing des LMR Inovalys [#1005](https://github.com/betagouv/maestro/issues/1005) et prise en compte des corrections apportées par Inovalys [#1004](https://github.com/betagouv/maestro/issues/1004).
- Correction pour prendre en compte l'email du destinataire lors de l'envoi d'email par les laboratoires [#1002](https://github.com/betagouv/maestro/issues/1002).

### Autres changements
- Ajout des types de ressources "réglementation" et "modèle" pour les documents [#988](https://github.com/betagouv/maestro/issues/988).
- Suppression des utilisateurs non actifs de la liste des préleveurs [#990](https://github.com/betagouv/maestro/issues/990).
- Mise à jour de plusieurs dépendances (voir les commits dependabot).
- Correction de bugs mineurs et améliorations de la qualité du code.
