## Changelog : seves (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Sèves, notamment en se concentrant sur la surveillance végétale et animale (SV) et le système d'alerte sanitaire (SSA). Les améliorations incluent des corrections de bugs, des améliorations de l'interface utilisateur, l'ajout de nouvelles fonctionnalités comme l'affichage de cartes et la gestion des documents, ainsi que des optimisations de performance. Des efforts ont également été faits pour améliorer l'accessibilité et la robustesse de l'application.

### Évolutions fonctionnelles
- Ajout d'une carte lors de la création d'un lieu en SV. [#29a5a51](https://github.com/betagouv/seves/commit/29a5a51)
- Ajout d'une carte lors de la visualisation d'un lieu en SV. [#eaafbf2](https://github.com/betagouv/seves/commit/eaafbf2)
- Amélioration de l'historique pour SV. [#f375a8c](https://github.com/betagouv/seves/commit/f375a8c) et [#205a251](https://github.com/betagouv/seves/commit/205a251)
- Possibilité de télécharger des documents au format DOCX même sans date de publication. [#cc771d9](https://github.com/betagouv/seves/commit/cc771d9)
- Ajout d'une page d'accessibilité. [#50fa32f](https://github.com/betagouv/seves/commit/50fa32f)
- Possibilité de télécharger des documents dans une archive ZIP. [#912e1c0](https://github.com/betagouv/seves/commit/912e1c0)
- Ajout d'un indicateur "fiche zone délimitée" accessible dans le tableau des événements SV. [#bb0c0ad](https://github.com/betagouv/seves/commit/bb0c0ad)
- Prévisualisation des images et des fichiers PDF. [#3bdeb05](https://github.com/betagouv/seves/commit/3bdeb05)
- Amélioration des notices dans SSA. [#107ac35](https://github.com/betagouv/seves/commit/107ac35)
- Ajout de l'ON (Organisme Notifié) pour SV. [#6b49448](https://github.com/betagouv/seves/commit/6b49448)
- Correction de l'affichage des sauts de ligne pour les messages existants. [#bec903b](https://github.com/betagouv/seves/commit/bec903b)
- Correction de l'affichage de la date de réception dans le frontend. [#16c371b](https://github.com/betagouv/seves/commit/16c371b)
- Correction du format CSV pour l'export TIAC. [#9185ac3](https://github.com/betagouv/seves/commit/9185ac3)

### Évolutions techniques
- Implémentation d'un nouveau composant Treeselect dans SSA. [#fce56df](https://github.com/betagouv/seves/commit/fce56df) et [#92046ed](https://github.com/betagouv/seves/commit/92046ed)
- Refactoring du modèle SiteInspection en utilisant TextChoices. [#8386f51](https://github.com/betagouv/seves/commit/8386f51)
- Correction d'un conflit de migration entre les migrations 0121. [#ba0fb8a](https://github.com/betagouv/seves/commit/ba0fb8a)
- Amélioration des performances de la vue de liste SSA. [#8e5af29](https://github.com/betagouv/seves/commit/8e5af29)
- Ajout d'un timeout sur les requêtes OIDC pour éviter les interruptions des workers en production. [#0d85baf](https://github.com/betagouv/seves/commit/0d85baf)
- Suppression de l'utilisation de SSA dans l'application core. [#d5e7d58](https://github.com/betagouv/seves/commit/d5e7d58)
- Correction de problèmes de CSP pour Brave/Chromium. [#b95c150](https://github.com/betagouv/seves/commit/b95c150)
- Correction de problèmes avec le rich text editor. [#42a13ee](https://github.com/betagouv/seves/commit/42a13ee) et [#6a5418e](https://github.com/betagouv/seves/commit/6a5418e)
- Amélioration de la gestion de la reconnexion de Celery à Redis. [#9dab5ba](https://github.com/betagouv/seves/commit/9dab5ba)
- Ajout d'un related name dans SV pour zone infestee. [#7f183cd](https://github.com/betagouv/seves/commit/7f183cd)

### Autres changements
- Déplacement de ChoiceJSPage dans core/tests/pages.py. [#1117f22](https://github.com/betagouv/seves/commit/1117f22)
- Correction de tests pour les cartes SV dans le modal lieu. [#a61017c](https://github.com/betagouv/seves/commit/a61017c)
- Correction de tests pour l'historique SV. [#205a251](https://github.com/betagouv/seves/commit/205a251)
- Amélioration des marges sur le bouton de téléchargement ZIP. [#62b3d87](https://github.com/betagouv/seves/commit/62b3d87)
- Correction de bugs d'interface utilisateur dans le tableau SV. [#e9b2045](https://github.com/betagouv/seves/commit/e9b2045)
- Correction de régressions avec GEA sur le nouveau Treeselect. [#e8f5590](https://github.com/betagouv/seves/commit/e8f5590)
- Désactivation des warnings Python sur CI pour améliorer la lisibilité. [#d067195](https://github.com/betagouv/seves/commit/d067195)
- Uniformisation des liens d'annulation sur les fiches objets. [#98d3a21](https://github.com/betagouv/seves/commit/98d3a21)
- Modification des placeholders pour les filtres d'année et de numéro. [#f3fc1b2](https://github.com/betagouv/seves/commit/f3fc1b2)
- Correction de l'affichage des ellipsis dans TIAC. [#6a09d39](https://github.com/betagouv/seves/commit/6a09d39)
- Correction pour autoriser les lettres dans le numero_agrement d'Etablissement. [#2055cfe](https://github.com/betagouv/seves/commit/2055cfe)
- Correction pour éviter le téléchargement de documents sur Chrome. [#6c3a2d1](https://github.com/betagouv/seves/commit/6c3a2d1)
- Correction pour PDF preview sur Brave. [#5565d54](https://github.com/betagouv/seves/commit/5565d54)
- S'assurer que les sources vides ne sont pas autorisées. [#798038a](https://github.com/betagouv/seves/commit/798038a)
