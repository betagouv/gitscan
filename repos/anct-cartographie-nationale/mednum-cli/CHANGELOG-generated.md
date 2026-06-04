## Changelog : mednum-cli (30 derniers jours, au 02 juin 2024)

### Résumé
Cette version apporte des améliorations significatives à la gestion et à la publication des données de lieux de médiation numérique, notamment concernant la gestion des adresses, la prise en charge de nouvelles sources de données et l'optimisation du processus de géocodage. Des corrections ont également été apportées pour assurer la cohérence et la fiabilité des données publiées.

### Évolutions fonctionnelles
- Ajout de la source de données "Meuse" pour enrichir la base de données des lieux de médiation numérique. [#348](https://github.com/anct-cartographie-nationale/mednum-cli/pulls/348)
- Publication du jeu de données national à partir des données dédupliquées. [#354](https://github.com/anct-cartographie-nationale/mednum-cli/pulls/354)
- Renommage de "di resources" en "national" pour plus de clarté. [#355](https://github.com/anct-cartographie-nationale/mednum-cli/pulls/355)
- Amélioration de la gestion des dates de mise à jour (`date_maj`) pour plusieurs sources de données. [#349](https://github.com/anct-cartographie-nationale/mednum-cli/pulls/349)
- Actualisation des adresses dans les fichiers JSON. [#350](https://github.com/anct-cartographie-nationale/mednum-cli/pulls/350)

### Évolutions techniques
- Migration du géocodage BAN vers l'API batch CSV, améliorant ainsi les performances et la scalabilité. [#347](https://github.com/anct-cartographie-nationale/mednum-cli/pulls/347)
- Mise en cache des adresses pour optimiser les performances. [#353](https://github.com/anct-cartographie-nationale/mednum-cli/pulls/353)

### Autres changements
- Correction d'un bug où les adresses invalides étaient ignorées. [#352](https://github.com/anct-cartographie-nationale/mednum-cli/pulls/352)
- Mise à jour de la configuration. [#351](https://github.com/anct-cartographie-nationale/mednum-cli/pulls/351)
