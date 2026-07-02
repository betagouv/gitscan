## Changelog : portail-rse (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation de l'export des données VSME au format PowerPoint (.pptx).  Cette nouvelle fonctionnalité permettra aux utilisateurs de générer des rapports plus visuels et adaptés à la présentation de leurs données RSE. De nombreuses améliorations et corrections ont été apportées pour assurer la qualité et la complétude de ces exports.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité d'export des données VSME au format PowerPoint (.pptx). [#0abfb79](https://github.com/betagouv/portail-rse/commit/0abfb79)
- Implémentation du téléchargement du rapport .pptx une fois rempli à 100%. [#dca04a7](https://github.com/betagouv/portail-rse/commit/dca04a7)
- Amélioration des boutons de téléchargement pour une meilleure expérience utilisateur. [#cf327b1](https://github.com/betagouv/portail-rse/commit/cf327b1)
- Ajout de l'affichage des unités dans les exports. [#c57864e](https://github.com/betagouv/portail-rse/commit/c57864e)
- Gestion de l'affichage des indicateurs non pertinents ou non applicables dans les rapports PowerPoint. [#928fa23](https://github.com/betagouv/portail-rse/commit/928fa23), [#90c8ef2](https://github.com/betagouv/portail-rse/commit/90c8ef2), [#12d2c0c](https://github.com/betagouv/portail-rse/commit/12d2c0c)
- Prise en charge de l'export de différents types d'indicateurs (texte, nombres, choix multiples). [#86028f3](https://github.com/betagouv/portail-rse/commit/86028f3), [#2b4d02d](https://github.com/betagouv/portail-rse/commit/2b4d02d)
- Ajout de l'export d'indicateurs environnementaux. [#2121557](https://github.com/betagouv/portail-rse/commit/2121557)
- Remplissage des informations de l'entreprise sur la couverture du rapport. [#15fa99a](https://github.com/betagouv/portail-rse/commit/15fa99a)

### Évolutions techniques
- Refactoring important du code d'export PowerPoint pour améliorer la structure et la maintenabilité.  De nombreux fichiers et fonctions ont été renommés pour plus de clarté. [#e3d0331](https://github.com/betagouv/portail-rse/commit/e3d0331), [#fabe1c4](https://github.com/betagouv/portail-rse/commit/fabe1c4)
- Utilisation d'un nouveau modèle PowerPoint (.pptx) pour une meilleure mise en page et personnalisation. [#fbb472c](https://github.com/betagouv/portail-rse/commit/fbb472c), [#e69b31e](https://github.com/betagouv/portail-rse/commit/e69b31e)
- Optimisation du traitement des tableaux dans les exports PowerPoint, notamment pour les tableaux à lignes variables. [#dd46777](https://github.com/betagouv/portail-rse/commit/dd46777), [#4cd1bc0](https://github.com/betagouv/portail-rse/commit/4cd1bc0)
- Amélioration de la gestion des styles de cellules dans les tableaux PowerPoint. [#bf2bbf6](https://github.com/betagouv/portail-rse/commit/bf2bbf6), [#e48e662](https://github.com/betagouv/portail-rse/commit/e48e662)
- Correction de bugs liés à l'affichage des données dans les tableaux et les graphiques PowerPoint. [#6824421](https://github.com/betagouv/portail-rse/commit/6824421), [#938ca73](https://github.com/betagouv/portail-rse/commit/938ca73)
- Mise à jour des dépendances : cryptography, aiohttp, pyjwt. [#e73e130](https://github.com/betagouv/portail-rse/commit/e73e130), [#3222589](https://github.com/betagouv/portail-rse/commit/3222589), [#e598ea7](https://github.com/betagouv/portail-rse/commit/e598ea7)

### Autres changements
- Correction de typos dans les labels VSME. [#de88114](https://github.com/betagouv/portail-rse/commit/de88114)
- Documentation : Complétion du diagramme overview. [#46d3b7e](https://github.com/betagouv/portail-rse/commit/46d3b7e)
- Correction d'un bug empêchant l'import si l'ID de la liste Brevo n'était pas fourni. [#d5119f5](https://github.com/betagouv/portail-rse/commit/d5119f5)
- Ajout de l'attribut EXT_ID de Brevo. [#62f7a26](https://github.com/betagouv/portail-rse/commit/62f7a26)
