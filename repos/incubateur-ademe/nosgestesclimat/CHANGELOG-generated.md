## Changelog : nosgestesclimat (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment en simplifiant les options de chauffage et en affinant les traductions. Des corrections ont été apportées aux données utilisées pour le calcul de l'empreinte carbone, en particulier concernant l'eau et les réglementations. Des fonctionnalités expérimentales, comme l'éditeur de règles et le partage de situations, ont également été ajoutées et améliorées.

### Évolutions fonctionnelles
- Simplification des options de chauffage pour une meilleure expérience utilisateur. [#2766](https://github.com/incubateur-ademe/nosgestesclimat/pull/2766)
- Suppression de la question relative au biogaz pour le chauffage. [#2766](https://github.com/incubateur-ademe/nosgestesclimat/pull/2766)
- Suppression des options VAE (Validation des Acquis de l'Expérience) dans la question relative aux transports.
- Mise à jour des chiffres relatifs à la consommation d'eau avec les données réglementaires les plus récentes. [#2738](https://github.com/incubateur-ademe/nosgestesclimat/pull/2738)
- Ajout d'une commande "save" dans l'éditeur de règles. [#2766](https://github.com/incubateur-ademe/nosgestesclimat/pull/2766)
- Ajout d'une fonctionnalité de partage de situations.
- Suppression de l'action "café mode scolaire". [#2738](https://github.com/incubateur-ademe/nosgestesclimat/pull/2738)
- Amélioration de la documentation rapide (quick doc). [#2758](https://github.com/incubateur-ademe/nosgestesclimat/pull/2758)

### Évolutions techniques
- Split de la partie frontend "scooter électrique". [#2772](https://github.com/incubateur-ademe/nosgestesclimat/pull/2772)
- Mise à jour de la bibliothèque `ED-fr.publicodes` pour intégrer les dernières données. [#2759](https://github.com/incubateur-ademe/nosgestesclimat/pull/2759)
- Utilisation d'un modèle hébergé sur Scaleway pour certaines fonctionnalités.
- Ajout d'un éditeur de règles avec vérification des erreurs et complétion automatique.
- Corrections de traductions et améliorations de la qualité des traductions. [#2771](https://github.com/incubateur-ademe/nosgestesclimat/pull/2771)

### Autres changements
- Suppression du support de la langue espagnole (es). [#2759](https://github.com/incubateur-ademe/nosgestesclimat/pull/2759)
- Suppression d'un message de débogage dans la console. [#2758](https://github.com/incubateur-ademe/nosgestesclimat/pull/2758)
- Corrections de wording et améliorations de la clarté du texte.
- Mise à jour des personas.
- Intégration de la branche `preprod` dans les branches `test-poc-scolaire` et `update-ecobalyse-reglementaire`.
- Versioning : 4.12.2, 4.12.1, 4.12.0, 4.11.0.
