## Changelog : seves (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'application Sèves, notamment sur la gestion des événements sanitaires (SV et SSA). Des corrections et des améliorations ont été apportées à l'interface utilisateur, aux fonctionnalités d'exportation de données, à la gestion des documents et à la performance globale. L'ajout de nouvelles fonctionnalités comme la cartographie et les éléments infestés renforce les capacités de l'application.

### Évolutions fonctionnelles
- Ajout d'un panneau "éléments infestés" au formulaire SV [#8772c4e](https://github.com/betagouv/seves/commit/8772c4e).
- Affichage des lieux et des prélèvements en bloc complet sur la page de détails SV [#a4f8599](https://github.com/betagouv/seves/commit/a4f8599).
- Ajout d'une carte pour visualiser les lieux lors de la création d'un SV [#29a5a51](https://github.com/betagouv/seves/commit/29a5a51) et lors de l'édition d'un lieu existant [#eaafbf2](https://github.com/betagouv/seves/commit/eaafbf2).
- Amélioration de l'historique des SV [#62b3d87](https://github.com/betagouv/seves/commit/62b3d87).
- Possibilité de télécharger des documents au format DOCX même sans date de publication [#cc771d9](https://github.com/betagouv/seves/commit/cc771d9).
- Ajout de la possibilité de télécharger les documents associés à un événement dans une archive ZIP [#912e1c0](https://github.com/betagouv/seves/commit/912e1c0).
- Ajout d'une nouvelle implémentation de Treeselect pour SSA [#f0246ed](https://github.com/betagouv/seves/commit/f0246ed) et SSA [#9a688f1](https://github.com/betagouv/seves/commit/9a688f1).
- Ajout d'un indicateur pour les fiches de zone délimitée dans le tableau des événements SV [#bb0c0ad](https://github.com/betagouv/seves/commit/bb0c0ad).
- Prévisualisation des images et des fichiers PDF [#3bdeb05](https://github.com/betagouv/seves/commit/3bdeb05).
- Amélioration de la performance de la vue liste SSA [#8e5af29](https://github.com/betagouv/seves/commit/8e5af29).

### Évolutions techniques
- Suppression du *feature flag* pour l'éditeur de texte enrichi [#f8fe6ed](https://github.com/betagouv/seves/commit/f8fe6ed).
- Suppression du *feature flag* pour le téléchargement ZIP [#b9881ab](https://github.com/betagouv/seves/commit/b9881ab).
- Refactoring de l'API de recherche d'espèces SV dans un contrôleur Stimulus dédié [#54c0ede](https://github.com/betagouv/seves/commit/54c0ede).
- Migration du modèle SiteInspection vers un TextChoices [#8386f51](https://github.com/betagouv/seves/commit/8386f51).
- Amélioration de la gestion des erreurs OIDC avec ajout d'un timeout [#0d85baf](https://github.com/betagouv/seves/commit/0d85baf).
- Correction d'un conflit de migration entre 0121_lieu_site_inspection_new et 0121_add_on_phytophthora_kernoviae [#ba0fb8a](https://github.com/betagouv/seves/commit/ba0fb8a).
- Amélioration de la reconnexion de Celery à Redis [#9dab5ba](https://github.com/betagouv/seves/commit/9dab5ba).
- Modification de l'ordre par défaut de TIAC et Alim [#f384cd2](https://github.com/betagouv/seves/commit/f384cd2).

### Autres changements
- Corrections de style et d'accessibilité sur l'interface utilisateur SV [#619bf46](https://github.com/betagouv/seves/commit/619bf46), [#e9b2045](https://github.com/betagouv/seves/commit/e9b2045).
- Amélioration des messages d'erreur et des notices dans SSA [#107ac35](https://github.com/betagouv/seves/commit/107ac35).
- Corrections de bugs et améliorations diverses de l'interface utilisateur et des tests.
- Mise à jour de diverses dépendances (gunicorn, urllib3, django, playwright, sentry-sdk, ruff, pytest, lxml, django-dsfr, django-post-office).
- Suppression de l'utilisation de SSA dans l'application core [#d5e7d58](https://github.com/betagouv/seves/commit/d5e7d58).
- Ajout d'une page d'accessibilité [#50fa32f](https://github.com/betagouv/seves/commit/50fa32f).
- Correction d'un problème de CSP pour Brave/Chromium [#b95c150](https://github.com/betagouv/seves/commit/b95c150).
- Amélioration des marges du bouton de téléchargement ZIP [#62b3d87](https://github.com/betagouv/seves/commit/62b3d87).
- Modification du format d'export CSV pour TIAC [#9185ac3](https://github.com/betagouv/seves/commit/9185ac3).
- Amélioration de l'historique des SV [#f375a8c](https://github.com/betagouv/seves/commit/f375a8c).
- Correction de problèmes d'affichage du texte enrichi [#bec903b](https://github.com/betagouv/seves/commit/bec903b), [#42a13ee](https://github.com/betagouv/seves/commit/42a13ee).
- Correction de problèmes d'affichage de la carte dans SV [#eea3c03](https://github.com/betagouv/seves/commit/eea3c03).
- Correction de problèmes de date dans l'export Docx [#665dee3](https://github.com/betagouv/seves/commit/665dee3).
- Correction de tests pour SV [#a14eb40](https://github.com/betagouv/seves/commit/a14eb40), [#a61017c](https://github.com/betagouv/seves/commit/a61017c), [#205a251](https://github.com/betagouv/seves/commit/205a251).
- Correction d'un bug empêchant le téléchargement de documents sur Chrome [#6c3a2d1](https://github.com/betagouv/seves/commit/6c3a2d1).
- Suppression de l'utilisation de SSA dans core app [#d01d70d](https://github.com/betagouv/seves/commit/d01d70d).
- Amélioration de la lisibilité des logs CI en désactivant les warnings Python [#8ef21fc](https://github.com/betagouv/seves/commit/8ef21fc).
- Correction de l'ellipses tooltip sur TIAC [#6a09d39](https://github.com/betagouv/seves/commit/6a09d39).
- Correction d'une regression avec GEA sur le nouveau Treeselect [#e8f5590](https://github.com/betagouv/seves/commit/e8f5590).
- Uniformisation des liens d'annulation sur les fiches d'objets [#98d3a21](https://github.com/betagouv/seves/commit/98d3a21).
- Modification des placeholders pour les filtres Annee/Numero [#f6b7c47](https://github.com/betagouv/seves/commit/f6b7c47).
- Ajout d'ON pour SV [#6b49448](https://github.com/betagouv/seves/commit/6b49448).
- Correction de l'affichage des sauts de ligne pour les messages existants [#bec903b](https://github.com/betagouv/seves/commit/bec903b).
- Ajout de contraintes pour ne pas autoriser les sources vides [#798038a](https://github.com/betagouv/seves/commit/798038a).
- Correction du test pour les maps en modal SV [#a61017c](https://github.com/betagouv/seves/commit/a61017c).
- Correction du test pour l'historique SV [#205a251](https://github.com/betagouv/seves/commit/205a251).
- Ajout de max pour date_reception dans le front end [#16c371b](https://github.com/betagouv/seves/commit/16c371b).
- Correction de l'accès à l'indicateur 'fiche zone délimitée' dans le tableau des événements SV [#bb0c0ad](https://github.com/betagouv/seves/commit/bb0c0ad).
- Correction de l'affichage des dates dans l'export Docx [#f0246ed](https://github.com/betagouv/seves/commit/f0246ed).
