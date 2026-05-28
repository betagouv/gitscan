## Changelog : a-just (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la couverture des tests automatisés (E2E), notamment dans le cockpit et les extracteurs de données. Des corrections ont été apportées à la gestion des congés (ASA), au simulateur et à l'affichage des données dans le cockpit. Des améliorations de sécurité ont également été implémentées concernant la validation des URLs des iframes.

### Évolutions fonctionnelles
- Correction de la migration des décharges syndicales. [#556](https://github.com/betagouv/a-just/pull/556)
- Amélioration du simulateur : correction du calcul et de l'URL de retour.
- Ajout d'indicateurs d'erreur et d'alertes dans le cockpit pour faciliter l'identification des problèmes.
- Correction de l'affichage des agents dans les colonnes "Arrivées" et "Départs" du module "Changement dans les effectifs".
- Ajout de tooltips pour les outils EPT dans le calculateur.
- Correction de l'affichage des données à compléter dans le panorama.
- Amélioration de la gestion des dates de début pour les réaffectations.
- Correction d'un bug lié à un jour incorrect au milieu des indisponibilités.

### Évolutions techniques
- Ajout de tests E2E pour le panorama, notamment pour vérifier l'affichage des données à compléter et la complétion des données de contentieux.
- Mise à jour des dépendances `@emnapi` et suppression des entrées obsolètes d'esbuild.
- Adaptation des tests E2E à la nouvelle version de Cypress (version 15).
- Amélioration de la configuration de Cypress et correction de l'accès aux variables d'environnement.
- Refactorisation du code pour supprimer les duplications.
- Validation des URLs des iframes pour renforcer la sécurité.
- Mise à jour de la configuration de toastr.

### Autres changements
- Ajout d'un fichier `.env.example` pour les tests E2E.
- Ajout de logs pour faciliter le débogage dans le cockpit.
- Amélioration du tri dans le cockpit.
- Correction de fautes de grammaire dans les logs.
- Mise à jour de la version du projet.
- Suppression du lockfile pnpm du front-admin.
- Correction de l'affichage des libellés "contentieux" dans les tests E2E.
- Ajout de règles ASA.
- Migration ASA vers absenteisme.
- Correction de la configuration de Quill JS.
- Amélioration du calcul du nombre de jours pour la simulation de projection.
- Ajout de messages d'erreur dans le cockpit.
- Réorganisation de l'équipe OT et EPT.
- Correction de l'affichage des messages d'erreur dans le cockpit.
