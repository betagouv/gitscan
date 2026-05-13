## Changelog : seves (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Sèves, notamment en se concentrant sur l'expérience utilisateur et la correction de bugs. Des améliorations significatives ont été apportées à la gestion des cartes, à l'exportation de données et à l'interface utilisateur générale, en particulier dans les modules SV (Surveillance Vétérinaire) et SSA. De nouvelles fonctionnalités, comme l'ajout d'ON (Organismes Notifiés) et l'intégration d'un nouveau composant Treeselect, ont également été implémentées.

### Évolutions fonctionnelles
- Amélioration de l'affichage des sauts de ligne dans les messages [#29a5a51](https://github.com/betagouv/seves/commit/29a5a51).
- Ajout d'une carte lors de la création d'un lieu en SV [#29a5a51](https://github.com/betagouv/seves/commit/29a5a51).
- Ajout d'une carte lors de la visualisation d'un lieu en SV [#eaafbf2](https://github.com/betagouv/seves/commit/eaafbf2).
- Correction de l'affichage de la date des fichiers lors du téléchargement d'une archive ZIP [#665dee3](https://github.com/betagouv/seves/commit/665dee3).
- Possibilité de télécharger des documents au format DOCX même sans date de publication [#cc771d9](https://github.com/betagouv/seves/commit/cc771d9).
- Ajout de la possibilité de télécharger des documents dans une archive ZIP [#912e1c0](https://github.com/betagouv/seves/commit/912e1c0).
- Prévisualisation des images et des fichiers PDF [#3bdeb05](https://github.com/betagouv/seves/commit/3bdeb05).
- Ajout d'un indicateur d'accessibilité pour la fiche zone délimitée dans le tableau des événements SV [#bb0c0ad](https://github.com/betagouv/seves/commit/bb0c0ad).
- Ajout de l'ON (Organisme Notifié) pour SV [#6b49448](https://github.com/betagouv/seves/commit/6b49448).
- Ajout d'un nouveau composant Treeselect dans SSA [#8386f51](https://github.com/betagouv/seves/commit/8386f51) et [#912e1c0](https://github.com/betagouv/seves/commit/912e1c0).
- Amélioration de la gestion des filtres Annee et Numero [#f3fc1b2](https://github.com/betagouv/seves/commit/f3fc1b2).
- Ajout d'une page d'accessibilité [#50fa32f](https://github.com/betagouv/seves/commit/50fa32f).
- Correction de l'affichage des TIAC et Alim par défaut [#f384cd2](https://github.com/betagouv/seves/commit/f384cd2).
- Ajout du numéro RASFF des objets TIAC [#b6469bf](https://github.com/betagouv/seves/commit/b6469bf).

### Évolutions techniques
- Migration du modèle SiteInspection vers un TextChoices pour une meilleure gestion des données [#8386f51](https://github.com/betagouv/seves/commit/8386f51).
- Refactorisation de l'API ChoiceJSPage pour la rendre réutilisable [#35de83e](https://github.com/betagouv/seves/commit/35de83e).
- Déplacement de ChoiceJSPage dans core/tests/pages.py [#1117f22](https://github.com/betagouv/seves/commit/1117f22).
- Modification de l'ordre par défaut des TIAC et Alim [#f384cd2](https://github.com/betagouv/seves/commit/f384cd2).
- Implémentation d'un nouveau Treeselect sur EvenementUpdateView (SSA) [#fce56df](https://github.com/betagouv/seves/commit/fce56df).
- Correction d'un conflit de migration entre 0121_lieu_site_inspection_new et 0121_add_on_phytophthora_kernoviae [#ba0fb8a](https://github.com/betagouv/seves/commit/ba0fb8a).
- Amélioration des performances de la vue de liste SSA [#8e5af29](https://github.com/betagouv/seves/commit/8e5af29).
- Ajout d'un timeout sur les requêtes OIDC pour éviter les interruptions de workers en production [#0d85baf](https://github.com/betagouv/seves/commit/0d85baf).
- Suppression de l'utilisation de SSA dans l'application core [#d5e7d58](https://github.com/betagouv/seves/commit/d5e7d58).
- Correction de problèmes liés à l'utilisation de Treeselect dans GEA [#e8f5590](https://github.com/betagouv/seves/commit/e8f5590).
- Désactivation des warnings Python sur CI pour améliorer la lisibilité [#d067195](https://github.com/betagouv/seves/commit/d067195).
- Ajout d'un related name dans SV pour zone infestee [#7f183cd](https://github.com/betagouv/seves/commit/7f183cd).

### Autres changements
- Correction de bugs et améliorations de l'interface utilisateur suite aux tests QA pour les adaptations Europhyt [#619bf46](https://github.com/betagouv/seves/commit/619bf46).
- Correction de problèmes de CSP pour Brave/Chromium [#b95c150](https://github.com/betagouv/seves/commit/b95c150).
- Correction du test pour les cartes SV dans la modale lieu [#a61017c](https://github.com/betagouv/seves/commit/a61017c).
- Correction du test pour l'historique SV [#205a251](https://github.com/betagouv/seves/commit/205a251).
- Amélioration des marges sur le bouton de téléchargement ZIP [#62b3d87](https://github.com/betagouv/seves/commit/62b3d87).
- Modification du format de l'export CSV TIAC [#9185ac3](https://github.com/betagouv/seves/commit/9185ac3).
- Amélioration de l'historique pour SV [#f375a8c](https://github.com/betagouv/seves/commit/f375a8c).
- Correction de l'affichage des caractères spéciaux dans l'éditeur de texte enrichi [#42a13ee](https://github.com/betagouv/seves/commit/42a13ee).
- Correction de la date dans les messages lors de l'export Docx [#a4125dd](https://github.com/betagouv/seves/commit/a4125dd).
- Correction de l'affichage des notices dans SSA [#107ac35](https://github.com/betagouv/seves/commit/107ac35).
- Correction de l'affichage des liens d'annulation sur les fiches objets [#98d3a21](https://github.com/betagouv/seves/commit/98d3a21).
- Correction de l'affichage de PDF preview pour Brave [#5565d54](https://github.com/betagouv/seves/commit/5565d54).
- Correction de l'affichage des caractères spéciaux dans l'éditeur de texte enrichi [#42a13ee](https://github.com/betagouv/seves/commit/42a13ee).
- Ajout de la possibilité de prévisualiser les fichiers PDF [#3bdeb05](https://github.com/betagouv/seves/commit/3bdeb05).
- Correction de l'accès à l'indicateur 'fiche zone délimitée' [#bb0c0ad](https://github.com/betagouv/seves/commit/bb0c0ad).
- Correction de l'affichage des ellipses dans TIAC [#6a09d39](https://github.com/betagouv/seves/commit/6a09d39).
- Correction de la date de publication dans SV [#7aa6e6a](https://github.com/betagouv/seves/commit/7aa6e6a).
- Amélioration de la réactivité de Celery avec Redis [#9dab5ba](https://github.com/betagouv/seves/commit/9dab5ba).
- Correction de l'interdiction des sources vides [#798038a](https://github.com/betagouv/seves/commit/798038a).
