## Changelog : portail-rse (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'ajout de la fonctionnalité d'exportation des données VSME au format PowerPoint (.pptx).  Cette nouvelle fonctionnalité permettra aux utilisateurs de générer des rapports plus visuels et adaptés à la présentation de leurs données RSE.  Des améliorations et corrections ont également été apportées à l'interface utilisateur et à la gestion des données.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger un rapport VSME au format PowerPoint (.pptx) lorsque le rapport est rempli à 100% [#90c8ef2](https://github.com/betagouv/portail-rse/commit/90c8ef2).
- Amélioration des boutons de téléchargement pour une meilleure expérience utilisateur [#cf327b1](https://github.com/betagouv/portail-rse/commit/cf327b1).
- Affichage des unités pour les indicateurs dans l'export PPTX [#c57864e](https://github.com/betagouv/portail-rse/commit/c57864e).
- Notification de l'utilisateur lors de l'enregistrement d'un indicateur [#7d13033](https://github.com/betagouv/portail-rse/commit/7d13033).
- Correction de l'affichage de la page de connexion après expiration de la session lors du remplissage d'un indicateur [#7b56b54](https://github.com/betagouv/portail-rse/commit/7b56b54).
- Redirection de la vue fragment indicateur vers l'exigence de publication si la requête n'est pas Htmx [#d33324e](https://github.com/betagouv/portail-rse/commit/d33324e).

### Évolutions techniques
- Refactorisation importante du code d'exportation PPTX pour une meilleure organisation et maintenabilité.
- Simplification des signatures de fonctions d'export PPTX [#e3d0331](https://github.com/betagouv/portail-rse/commit/e3d0331).
- Utilisation d'un nouveau modèle PPTX plus complet pour l'exportation [#e69b31e](https://github.com/betagouv/portail-rse/commit/e69b31e).
- Suppression des éléments liés aux modules complets dans l'export PPTX [#fa48dbe](https://github.com/betagouv/portail-rse/commit/fa48dbe).
- Déplacement du fichier modèle XLSX [#b7d1d2a](https://github.com/betagouv/portail-rse/commit/b7d1d2a).
- Renommage de fichiers pour une meilleure clarté [#fabe1c4](https://github.com/betagouv/portail-rse/commit/fabe1c4) et [#acb2381](https://github.com/betagouv/portail-rse/commit/acb2381).

### Autres changements
- Mise à jour de la documentation avec un diagramme overview plus complet [#46d3b7e](https://github.com/betagouv/portail-rse/commit/46d3b7e).
- Correction de typos dans les labels VSME [#de88114](https://github.com/betagouv/portail-rse/commit/de88114).
- Ajout de l'attribut EXT_ID de Brevo [#d5119f5](https://github.com/betagouv/portail-rse/commit/d5119f5).
- Correction d'un bug empêchant l'affichage normal de la page de connexion [#7b56b54](https://github.com/betagouv/portail-rse/commit/7b56b54).
- Mises à jour de dépendances : cryptography, aiohttp, pyjwt.
